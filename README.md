# turtle01
## 무인 이동체 알고리즘 수업

이 프로젝트는 Python의 turtle 모듈을 활용하여, 무인 이동체가 장애물을 회피하며 목적지에 도착하는 과정을 시각적으로 표현한 시뮬레이터입니다.
## 코드 동작 순서
1. 거북이가 출발점과 도착점을 만든다.
2. 거북이가 출발지에서 목적지로 이동을 시작한다.
3. 이동 중 장애물 범위를 감지하여 회피 알고리즘을 실행한다.
4. 회피 후 다시 목적지를 향해 직진한다.
5. 목적지에 도착하면 "도착" 메시지를 팝업으로 띄운다.
### 사용한 알고리즘
#### 1. 장애물 회피 알고리즘
   
 장애물의 좌표 영역을 사전에 정의해두고, 해당 영역에 접근할 경우 회피 함
회피 시, 거북이는 일정한 각도로 우측 혹은 좌측으로 회피 후 다시 셋팅
회피가 끝난 후 다시 목적지를 향해 이동

#### 2. 거리 계산 알고리즘

현재 위치와 목적지 좌표 간의 유클리드 거리(√((x2-x1)² + (y2-y1)²))를 계산

#### 실행 방법

`turtle01.py` 파일을 실행합니다.

   ```bash
   python turtle01.py



