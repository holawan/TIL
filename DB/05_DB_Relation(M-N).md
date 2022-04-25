## M:N 관계

### ManyToManyField's  개념 및 특징 

- 다대다 관계 설정 시 사용하는 모델 필드
- 하나의 필수 위치인자(M:N 관계로 설정할 모델 클래스)가 필요
- 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 생성할 수 있음
  - add(), remove(), create(), clear...
- RelatedManager
  - 일대다 또는 다대다 관련 컨텍스트에서 사용되는 manager

### ManyToManyField's  Arguments

#### related_name

- target model(관계 필드를 가지지 않은 모델)이 source model(관계 필드를 가진 모델)을 참조할 때 (역참조 시) 사용할 manager의 이름을 설정
- ForeignKey의 related_name과 동일

#### through

- 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정할 수 있음
- 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우에 주로 사용됨 

#### symmetrical

- ManyToManyField가 동일한 모델(on self)를 가리키는 정의에서만 사용
- symmetrical=True(기본값)일 경우 Django는 person_set 매니저를 추가하지 않음
- source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면, target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함 
  - 즉, 내가 너의 친구면 너도 나의 친구
  - 대칭을 원하지 않을 경우 False
  - Follo 기능 구현시 활용

### Related Manager

- 1:N 또는 M:N 관련 컨텍스트에서 사용되는 매니저
- 같은 이름의 메서드여도 각 관계(1:N, M:N)에 따라 다르게 사용 및 동작
  - 1:N에서는 target 모델 인스턴스만 사용 가능
  - M:N 관계에서는 관련된 두 객체에서 모두 사용 가능 

#### add

- 지정된 객체를 관련 객체 집합에 추가
- 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
- 모델 인스턴스, 필드 값(PK)를 인자로 허용 

##### 추가

- 만약 doctor_id와 patient_id를 동일하게 병명을 갱신하고 싶다면??
  - 이미 관계가 있기 때문에 일단 add 매니저로는 이용할 수 없다.
  - 만약 update를 하고 싶다면 해당 reservation을 가져오고, 갱신하면 된다.

```python
reservation = Reservation.objects.get(pk=1)

reservation.symptom = 'x'
reservation.save()
```

- 만약 같은 환자가 같은 의사에게 다른 병으로 온다면 ? 
  - 직접 reservation을 만들어서 일일이 추가해준다..?

```shell
reservation = Reservation()
reservation.symptom='a'
reservation.patient_id=1
reservation.doctor_id=1
reservation.save()
```

![update&add](Relation(M-N).assets/update&add.PNG)

#### remove

- 관련 객체 집합에서 지정된 모델 객체를 제거
- 내부적으로 QuerySet.delete()를 사용하여 관계가 삭제된
- 모델 인스턴스, 필드 값(PK)를 인자로 허용 



### Through 예시

1. 모델 관계 설정

```python
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    #증상
    symptom = models.TextField()
    #예약일자
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
```

2. 의사 1명과 환자 2명 생성

```shell
doctor1 = Doctor.objects.create(name='justin')
patient1 = Patient.objects.create(name='tony')
patient2 = Patient.objects.create(name='harry')
```

3. 예약을 만들기

```shell
#예약 만들기(증상을 담아서)
reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
#예약 저장
reservation1.save()
#의사의 예약 
doctor1.patient_set.all()
patient1.doctors.all()

#환자의 입장에서 예약 만들기
patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})
doctor1.patient_set.all()
patient2.doctors.all()
```

4. 테이블 확인

![table](Relation(M-N).assets/table.PNG)

5. 예약 삭제

```shell
doctor1.patient_set.remove(patient1)
patient2.doctors.remove(doctor1)
```



#### 데이터베이스에서의 표현

- Django는 다대다 관계를 나타내는 중개 테이블을 만듬
- 테이블 이름은 다대다 필드의 이름과 이를 포함하는 모델의 테이블 이름을 조합하여 생성됨



### 중개 테이블 필드 생성의 규칙

1. source model 및 target model이 다른 경우
   - id 
   - <containig_model>_id
   - <other_model>_id
2. ManyToManyField가 동일한 모델을 가리키는 경우 (재귀적으로 자기 자신을 가리킴)
   - id
   - `from <model>_id`
   - `to_<model>_id`
