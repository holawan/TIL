## M:N 관계

### INTRO : 병원 진료 기록 시스템으로 다대다 관계 이해해보기

- 환자와 의사가 사용하는 병원 진료 기록 시스템 구축
  - 병원 시스템에서 가장 핵심이 되는 객체는 무엇일까? -> 환자와 의사
  - 이 둘의 관계를 어떻게 표현할 수 있을까?
- 시작하기 전
  - 모델링은 현실세계를 최대한 유사하게 반영하기 위한 것
  - 우리 일상에 가까운 예시를 통해 DB를 모델링하고, 그 내부에서 일어나는 데이터의 흐름을 어떻게 제어할 수 있을지 고민해보기.

#### 연습 모델

```python
#models.py
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

```python
doctor1 = Doctor.objects.create(name='justin')
doctor2 = Doctor.objects.create(name='eric')
patient1 = Patient.objects.create(name='tony', doctor=doctor1)
patient2 = Patient.objects.create(name='harry', doctor=doctor2)
```

##### hospital_doctor

|  id  |  name  |
| :--: | :----: |
|  1   | justin |
|  2   |  eric  |

##### hospitals_patient

|  id  | name  | doctor_id |
| :--: | :---: | :-------: |
|  1   | tony  |     1     |
|  2   | harry |     2     |
|  3   | tony  |     2     |

```python
patient3 = Patient.objects.create(name='tony', doctor=doctor2)
```

### 1:N의 한계

- 1번 환자(tony)가 1번 의사의 진료를 마치고 2번 의사에게도 방문하려 한다면, 새로운 예약을 생성해야한다.
  - 기존의 예약을 유지한 상태로 새로운 예약을 생성
  - 새로 생성한 3번환자는 1번환자와 다름 
  - 예약하고자 하는 사람은 동일하지만 인스턴스가 다른 것이 문제.

```python
patient4 = Patient.objects.create(name='harry', doctor=doctor1, doctor2)
```

- 한번에 두 의사에게 진료를 받고자 함
  - 하나의 외래 키에 2개의 의사 데이터를 넣을 수 없음 
- 새로운 예약을 생성하는 것이 불가능
  - 새로운 객체를 생성해야함
- 여러 의사에게 진료받은 기록을 환자 한 명에 저장할 수 없음 
  - 외래 키에 '1,2' 형식의 데이터를 사용할 수 없기 때문



### 중개 모델

1. 중개 모델(Associative table) 작성

|  id  | doctor_id | patient_id |
| :--: | :-------: | :--------: |
|  .   |     .     |     .      |

2. 기존 마이그레이션 초기화를 위해 migration 내 파일과 db지우기 

3. 새로운 모델 적용

```python
from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


# 외래키 삭제
class Patient(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# 중개모델 작성
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

![중계모델과관계](Relation(M-N).assets/중계모델과관계.PNG)



4. 예약 만들기

```shell
In [1]: doctor1 = Doctor.objects.create(name='justin')

In [2]: patient1 = Patient.objects.create(name='tony')

In [3]: Reservation.objects.create(doctor=doctor1, patient=patient1)
Out[3]: <Reservation: 1번 의사의 1번 환자>
```

5. 의사와 환자가 진료 조회를 할 때 역참조를 이용한다.

```shell
#의사의 예약환자 조회
In [4]: doctor1.reservation_set.all()
Out[4]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>
#환자의 진료의사 조회
In [5]: patient1.reservation_set.all()
Out[5]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>
```

6. 환자 1명 추가 생성 및 1번 의사에게 예약 생성

```shell
In [7]: Reservation.objects.create(doctor=doctor1, patient=patient2)
Out[7]: <Reservation: 1번 의사의 2번 환자>
```

7. 의사의 예약 환자 조회

```shell
In [9]: doctor1.reservation_set.all()
Out[9]: <QuerySet [<Reservation: 1번 의사의 1번 환자>, <Reservation: 1번 의사의 2번 
환자>]>
```

##### 한 명의 의사는 여러 환자를 진료할 수 있고, 한 명의 환자는 여러 의사에게 진료를 받을 수 있는 다대다 관계 형성



### ManyToManyField

1. ManyToManyField ?

   - 다대다 관계 설정 시 사용하는 모델 필드

   - 하나의 필수 위치인자(M:N 관계로 설정할 모델 클래스)가 필요 

2. ManyToManyField 작성 (중개모델 삭제)
   - 필드 작성 위치는 Doctor 또는 Patient 모두 작성 가능 
   - DB 삭제 후 마이그레이션 초기화
3. ManyToManyField 적용

```python
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    # ManyToManyField 작성
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

4. 중개모델과 같은 테이블이 생성됨
   - 1:N에서는 외래키가 무조건 종속관계가 있었지만, M:N은 대등한 관계이기 때문에 MTM필드를 둘 중 하나의 클래스에 두면 된다.
   - 다만 ManyToManyField를 어디에 기입하는지에 따라 참조와 역참조 관계가 바뀐다.
   - 위의 경우에는 Doctor가 Patient를 역참조, Patient가 Doctor를 참조하는 관계이다. 

![mtom](Relation(M-N).assets/mtom-16502460882031.PNG)

5. 의사 1명과 환자 2명 생성

```shell
doctor1 = Doctor.objects.create(name='justin')
patient1 = Patient.objects.create(name='tony')
patient2 = Patient.objects.create(name='harry')
```

6. 예약 생성(환자 입장에서 참조)

```shell
#환자1이 의사1에게 예약 진행 
patient1.doctors.add(doctor1)
#patient1이 예약한 의사 목록 확인
patient1.doctors.all()
Out[6]: <QuerySet [<Doctor: 1번 의사 justin>]>
#doctor1에게 예약된 환자 목록 확인 
doctor1.patient_set.all()
Out[7]: <QuerySet [<Patient: 1번 환자 tony>]>
```

7. 예약 생성 (의사 입장에서 역참조)

```shell
#의사 1에게 환자2 추가 
doctor1.patient_set.add(patient2)
#의사가 맡은 환자들조회 
doctor1.patient_set.all()
Out[9]: <QuerySet [<Patient: 1번 환자 tony>, <Patient: 2번 환자 harry>]>
patient2.doctors.all()
Out[10]: <QuerySet [<Doctor: 1번 의사 justin>]>
patient1.doctors.all()
Out[11]: <QuerySet [<Doctor: 1번 의사 justin>]>
```

8. 예약 취소

```shell
#1번 환자 삭제 
doctor1.patient_set.remove(patient1)
#2번 환자만 남음 
doctor1.patient_set.all()
Out[13]: <QuerySet [<Patient: 2번 환자 harry>]>
#1번 환자의 예약정보는 사라짐 
patient1.doctors.all()
Out[14]: <QuerySet []>
```

9. 예약 취소2

```shell
#2번 환자의 예약 중 1번 의사 삭제 
patient2.doctors.remove(doctor1)
#2번 환자의 예약정보 사라짐 
patient2.doctors.all()
Out[19]: <QuerySet []>
#1번 의사의 예약 정보 사라짐 
doctor1.patient_set.all()
Out[20]: <QuerySet []>
```

#### related_name

- 1:N에서는 related_name을 사용하지 않고 targetmodel_set을 사용하고 M:N에서는 related_name을 사용해서 둘을 구분해보자 ! 

##### 새로운 모델

```python
from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    # ManyToManyField - related_name 작성
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

- 새로운 모델을 생성함으로써 둘다 역참조 참조를 신경쓰지 않고, 같은 형식으로 참조할 수 있다.

```python
#환자 1의 모든 예약 조회 
patient1.doctors.all()
#의사 1의 모든 예약 조회
doctor1.patients.all()
```



#### 중개모델 in Django

- django는 ManyToManyField를 통해 중개 테이블을 자동으로 생성
- 그렇다면 중개 테이블을 직접 작성하는 경우는 없을까?
  - 중개 테이블을 수동으로 지정하려는 경우 through 옵션을 사용하여, 중개 테이블을 나타내는 Django 모델을 지정할 수 있음
  - 가장 일반적인 용도는 중개 테이블에 추가 데이터를 사용해 다대다 관계로 연결하려 하는 경우에 사용 

### 요약

- 실제 Doctor와 Patient 테이블이 변하는 것은 없다.
- 1:N관계는 완전한 종속의 관계이지만, M:N 관계는 의사에게 진찰받는 환자, 환자를 진찰하는 의사의 두가지 형태로 모두 표현이 가능하다. 
