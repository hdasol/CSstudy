# CPU 스케줄링


## 기태

### CPU 스케줄링
- 컨텍스트 스위칭 내용 빼기

- 프로세스가 CPU를 점유해서 작업하는 도중에 인터럽트가 발생하면 일시적으로 CPU는 일을 하지 않지만 프로세스는 계속 CPU을 점유하고있는 경우가 있습니다. 
- 이러한 상황을 줄이고 CPU를 효율적으로 사용하기 위해 여러 CPU 스케줄링 방식이 있습니다.

- 크게 선점 스케줄링, 비선점 스케줄링으로 나뉩니다.
- 선점 스케줄링은 어떤 프로세스가 CPU를 점유중일 때, 다른 프로세스가 CPU의 점유를 뺏어올 수 있고, 비선점은 그럴 수 없는 방식입니다.
- 선점 스케줄링에는 Round Robin 방식이 있습니다.
- 프로세스들이 적당한 크기의 CPU 시간을 할당받고 선입선출되는 방식입니다.
- 비선점 스케줄링에는 Shortest Job First 방식이 있습니다.
- 큐에 들어있는 프로세스증 시간이 제일 짧은 것부터 먼저 CPU를 점유하도록 하여 평균 대기 시간을 작은 장점이 있습니다.
## 동현

### CPU 스케줄링이란?

다수의 프로세스가 Ready 상태에 있을 때, 어떤 프로세스를 CPU(프로세서)가 먼저 처리하도록 할 것인가를 결정하는 방법을 의미합니다.

사용자 관점에서는 응답 시간, 대기 시간을 줄이는 목적으로 사용하며, 시스템 관점에서는 CPU 이용률과 처리량을 높이기 위한 전략을 제시합니다.

### CPU 스케줄링의 발생 시기

1. 프로세스가 입/출력을 요구할 때
- 운영체제에게 입출력 시스템 콜을 요청하면, 입출력이 완료될 때 까지 프로세스는 CPU를 할당받지 못하고 CPU는 다른 프로세스에게 넘어갑니다.

2. 프로세스가 종료를 요구할 때
- 프로그램의 모든 라인이 읽히고 수행 되었을 경우나 명시적으로 종료를 요구하는 시스템콜이 발생했을 경우 새로운 프로세스를 찾기 위한 CPU 스케줄링이 발생합니다.

3. 높은 우선순위의 프로세스가 나타났을 때
- 특정 프로세스의 입출력 완료 인터럽트에 의해 Ready Queue에 들어가게 되면, CPU는 실행 중이던 프로세스의 우선순위와 새로운 프로세스의 우선순위를 비교합니다. 기존 프로세스의 우선순위가 더 높다면 CPU 할당을 즉시 교체할 수 있습니다.

4. 주어진 CPU 실행 시간을 초과했을 때
- 프로세스가 연속해서 사용할 수 있는 최대 시간을 설정하고, 해당 시간이 초과한 경우 CPU 스케줄링이 발생할 수 있습니다.

### CPU 스케줄링 전략

CPU 스케줄링 전략에는 실행 중인 프로세스가 자발적으로 CPU를 반납할 때 까지 계속 점유하는 `비선점형 전략`과 프로세스가 직접 CPU를 반납하지 않더라도 언제든 교체가 가능한 `선점형 전략`이 존재합니다.

- (비선점) FCFS (First-Come-First-Served): 프로세스들이 레디큐에 도착하는 순서대로 CPU에 할당됩니다. 중요도나 응답시간에 상관없이 먼저 들어온 프로세스의 작업이 끝날 때 까지 기다리기 때문에 CPU 이용률이 저하되는 등 효율적이지 못한 경우가 많습니다.

- (비선점) SJF (Shortest Job First): CPU 버스트가 짧은 순서대로 CPU에 할당되는 전략입니다. 상대적으로 응답 시간이 긴 프로세스들이 늦게 실행되는데, 해당 작업이 중요도가 높은 작업이라면 작업이 지연되므로 사용성이 좋지 않을 수 있습니다. 

- (선점) SRT (Shortest Remaining Time): SJF와 비슷하지만 처리 시간이 더 짧은 프로세스가 새로 레디큐에 들어오면 바로 선점되는 전략입니다. 오래 걸리는 작업은 계속해서 뒤로 밀리는 단점이 있습니다.

- (선점, 비선점) HRN (Highest Response-ratio Next): 작업의 수행 시간과 대기 시간을 모두 고려해 최적의 응답률을 계산하는 알고리즘을 통해, 응답률이 가장 높은 작업을 먼저 처리하는 방식입니다.

- (선점) 라운드로빈 (Round Robin): 시분할 전략입니다. 최대 CPU 점유 시간을 정해놓고, 해당 시간이 지나면 다른 프로세스로 CPU 할당을 넘깁니다. 할당시간을 너무 크게 설정하면 선입선출(FCFS)와 달라질게 없고, 너무 짧게 설정하면 Context Switching이 너무 빈번하게 발생하기 때문에 오버헤드가 발생합니다. (오히려 처리율이 감소)


### 용어 관련 내용 (참고)

- CPU 스케줄러: 프로세스들에게 CPU를 배분하는 역할을 담당하므로 `Dispatcher`라고 부르기도 한다.  
- 응답 시간: 사용자 데이터 입력 후, 출력이 이루어질 때 까지의 소요 시간  
- 대기 시간: 프로세스들이 준비 상태로 대기열에서 기다린 시간의 총합  
- CPU 이용률: 총 경과 시간 대비 CPU가 순수하게 사용자 프로세스를 수행한 시간의 비  
- 처리량: 단위 시간당 처리된 프로세스의 수

### 참고 자료

- [훑어보는 CPU 스케줄링 (내용 좋음)](https://boycoding.tistory.com/258)
- [CPU 스케줄링 기법](https://preamtree.tistory.com/19)
- [공룡책 5장 CPU 스케줄링](https://imbf.github.io/computer-science(cs)/2020/10/18/CPU-Scheduling.html)
