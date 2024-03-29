# Virtual DOM

## 동현

### 가상돔이란 무엇인가요?

웹 브라우저 단에서의 DOM 내부 변화로 인해 reflow와 repaint 등의 동작이 발생하고 그에 따른 연산 비용이 들게 됩니다. 문제는, DOM의 변화가 `동시에 여러 번` 발생할 수 있다는 것인데, 이렇게 되면 연산 비용이 많이 들고 성능 이슈까지 이어집니다. 리액트에서는 가상돔을 이용해 여러번의 DOM 갱신을 내부적으로 처리하고, 최종 처리된 가상DOM 객체를 실제 DOM에 전달하는 방식으로 성능을 향상시킵니다.

### 가상돔의 동작 원리를 설명해주세요.

현재 DOM의 상태를 항상 메모리에 저장합니다. DOM의 변화가 발생하면, 메모리에 저장된 DOM과 변경 이후의 DOM을 비교해 변경된 부분만 실제 DOM에 반영해 성능을 향상시킵니다.

데이터가 업데이트 되면, 새로운 UI를 가상DOM에 만듭니다. 이전 가상DOM과 새로운 가상 DOM을 비교해 바뀐 부분만 실제 DOM에 적용합니다. 따라서, 컴포넌트가 업데이트 될 때 연산 과정을 한 번만 거치게 됩니다. 작은 규모의 reflow/repaint가 여러 번 발생하는 것 보다 큰 규모의 그것이 한 번 발생하는게 성능적으로 크게 좋아진다는 것을 이용한 방식입니다.

### 참고 자료

- [가상돔이 나오게 된 이유](https://dev-cini.tistory.com/10#:~:text=Virtual%20DOM)%20%EC%9D%B4%EB%9E%80%3F-,Virtual%20DOM%EC%9D%84%20%EC%82%AC%EC%9A%A9%ED%95%98%EB%A9%B4%20%EC%8B%A4%EC%A0%9C%20DOM%EC%97%90%20%EC%A0%91%EA%B7%BC%ED%95%98%EC%97%AC,%EC%84%B1%EB%8A%A5%20%ED%96%A5%EC%83%81%20%EA%B0%80%EC%83%81%20DOM%EC%9D%80)
