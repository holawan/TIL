# python 함수 앞 '_'는 언제 사용할까?

가끔, python 파일을 확인하면 함수 앞에 _가 있는 경우가 있다. 이는 언제, 사용하고 언제 사용하지 않는걸까 ?

결론적으로, 해당 함수를 작성된 파이썬 파일에서만 사용하고 싶다면, *를 붙이고 아니라면* 를 붙이지 않는다.

예로 살펴보자

### 예

- underbar_test.py

```python
def not_under_bar() :
    print('not underbar import')

def _under_bar() :

    print('underbar import')

not_under_bar()

_under_bar()
```

해당 방식으로 2개의 함수를 작성했다. teminal에서 해당 python file을 실행하면, 둘다 정상적으로 출력된다.

```bash
$ python underbar_test.py 
not underbar import
underbar import
```

그렇다면, 이를 다른 file에서 import 해서 사용해보자

- underbar_import_test.py

```python
from underbar_test import *

not_under_bar()

_under_bar()
```

- 해당 파일은 underbar_test에서 모든 모듈을 import해서 실행하고자 한다.
- 실행 전, 이전 underbar_test에서 실행시킨 `not_under_bar()`와, `_under_bar`는 주석처리 해주도록 하자
    \- import 하는 것만으로 실행되기 때문

```bash
$ python underbar_import_test.py 
not underbar import
Traceback (most recent call last):
  File "C:\Users\multicampus\Desktop\TIL\Python Intro\함수\함수연
습\underbar_import_test.py", line 5, in <module>
    _under_bar()
NameError: name '_under_bar' is not defined
```

- 위 결과처럼 `_under_bar` 모듈을 찾지 못한다.
- 그 이유는 앞에 _를 선언해주면, 그 파일을 해당 파일 안에서만 사용한다는 의미이기 때문이다.
- 따라서, 이를 가져올 수 없고 에러가 발생했다.

- 그렇다면, 이 경우 절대 해당 모듈을 불러올 수 없을까?
- 이는 명시적으로 선언을 해주면 가져올 수 있다 .

```python
from underbar_test import *

from underbar_test import _under_bar
not_under_bar()

_under_bar()
```

- 위 파일처럼 _under_bar라는 모듈을 직접 선언해서 imoprt 해주면 정상적으로 출력된다.

```bash
$ python underbar_import_test.py 
not underbar import
underbar import
```

#### 정리

- 함수 앞에 언더바('_')를 붙여주면, 해당 함수는 그 모듈 내부에서만 사용한다는 의미이다.
- 개인적으로 프로그래밍 중 naming이 어렵기 때문에, 가독성 있게 해당 모듈안에서만 사용할 때 유용할 것 같다.
- 하지만, 이 또한 명시적으로 가져온다고 선언해주면 import해서 사용 가능하다 !
