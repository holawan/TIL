# Django 실행

## 1. 가상환경 설치 안했을 때

### 1. 가상환경 설치

```
python -m venv venv	
```

### 2. 가상환경 실행

```
source venv/scripts/activate
```

### 3. 패키지 설치

```
pip install -r requirements.txt
```

### 4. 마이그레이션

```
python manage.py migrate
```

### 5. 실행

```
python manage.py runserver
```

## 2. 가상환경 이미 설치되었을 때

### 1. 가상환경 실행

```
source venv/scripts/activate
```

### 2. 실행

```
python manage.py
```