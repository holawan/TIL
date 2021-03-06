## DFS

- 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함
- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게되면, 가장 마지막에 만났던 가림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입 선출 구조의 스택 사용 

### 알고리즘

- 시작 정점 v를 결정하여 방문한다.

- 정범 v에 인접한 정점 중에서

  - 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문한다.

    그리고 w를 v로 하여 다시 두번째를 반복한다.

  - 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 두번째를 반복한다. 

- 스택이 공백이 될 때까지 2)를 반복한다. 



## 계산기

- 문자열로 된 계산식이 주어질 때 스택을 이용하여 이 계산식의 값을 계산할 수 있다.
- 문자열 수식 계산의 일반적 방법
  - 중위표기법의 수식을 후위표기법으로 변경한다.
  - 후위 표기법의 수식을 스택으로 이용하여 계산한다.

- step1
  - 입력 받은 중위 표기식에서 토큰을 읽는다.
  - 토큰이 피연산자이면 토큰을 출력한다.
  - 토큰이 연산자일때 , 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고, 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push한다. 만약 top에 연산자가 없으면 push한다. 
  - 토큰이 오른쪽 괄호')' 이면 스택 top에 왼쪽 괄호'('가 올 때까지 스택에 pop 연산을 수행하고 pop한 연산자를 출력한다. 왼족 괄호를 만나면 pop하고 출력하지는 않는다.
  - 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복한다.
  - 스택에 남아있는 연산자를 모두 pop 하여 출력한다.
    - 스택 밖의 왼쪽 괄호는 우선순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮다. 
- step2
  - 피연산자를 만나면 스택에 push한다.
  - 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여, 연산하고, 연산결과를 다시 스택에 push한다.
  - 수식이 끝나면, 마지막으로 스택을 pop하여 출력한다. .