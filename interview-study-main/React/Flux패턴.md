# Flux 패턴

## 동현

### FLUX 패턴이란?

데이터를 단방향으로 흐르도록 만들어, 각 시스템간의 의존성을 줄여 프로그램의 복잡도를 낮춘 패턴입니다. Action, Dispatcher, Store, View로 구성되어 있습니다.

View에서 Action이 발생하든, 어떤 이벤트가 동작해서 Action이 발생하든.. type과 payload를 가진 Action 객체가 Dispatcher로 전달됩니다. Dispatcher에서는 등록된 모든 store로 액션을 전달할 수 있습니다. store는 처리할 액션을 type으로 분별합니다. 처리가 필요한 액션이라면 payload값을 이용해 변경하고 싶은 데이터를 바꿔줍니다. 데이터 변경이 완료되면 View에게 이를 알리고 View는 새로운 상태를 이용해 원하는 동작을 수행합니다.

### 참고 자료

- [Flux로의 카툰 안내서](https://bestalign.github.io/translation/cartoon-guide-to-flux/)
