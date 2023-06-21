# position

## 동현

### position이 무엇이며, 어떤 값들을 가지고 있나요?

position이란, 요소들의 위치를 결정하는데 사용되는 css 속성입니다.  
위치의 기준을 정하거나, 행동 정의를 위해 static, relative, absolute, fixed, sticky 등의 값을 사용할 수 있습니다. 부가적인 속성으로 top bottom left right 등의 속성을 이용해 위치를 잡을 수 있습니다. (+ position 속성은 상속되지 않습니다~)

### static

기본값이며, 위치를 지정하지 않고 요소의 특성에 맞도록 왼쪽에서 오른쪽, 위에서 아래로 배치됩니다. top, right, bottom, left, z-index 속성들이 아무런 효과를 주지 못합니다.

### relative

자기 자신의 원래 위치(static)를 기준으로 합니다. top, right, bottom, left등의 속성을 이용해 위치를 변경할 수 있으며, 해당 속성을 주지 않는다면 static이랑 같은 위치에 존재합니다.

### absolute

자기 자신의 가장 가까운 static이 아닌 조상 요소를 기준으로 위치를 잡습니다. 만약 그러한 조상 요소가 없다면 body를 기준으로 합니다. (스크롤되면 위치가 변함)

### fixed

뷰포트를 기준으로 위치를 정합니다. 따라서, 스크롤을 움직여도 위치가 변하지 않고 절대적인 위치에 고정됩니다.

### sticky

가장 가까운 부모 요소를 기준으로 위치를 잡을 수 있습니다. 평소에는 relative처럼 동작하다가 부모 요소의 스크롤 액션에 의해 화면에서 사라져야 할 경우라도 컨테이너에 딱 붙게되는 특징이 있습니다.

### 참고 자료

- [css position 설명](https://medium.com/@su_bak/css-css-position-%EC%84%A4%EB%AA%85-f2c0a0b26556)


## 기태

### CSS position?
- css position 속성은 요소를 배치하는 방법을 말합니다.
- default 값은 static입니다.

- relative
    - 요소 자기 자신의 원래 위치(static일 때의 위치)를 기준으로 배치한다.
    - 원래 위치를 기준으로 위쪽(top), 아래쪽(bottom), 왼쪽(left), 오른쪽(right)에서 얼마만큼 떨어질 지 결정한다.
    - 위치를 이동하면서 다른 요소에 영향을 주지 않는다.
    - 문서 상 원래 위치가 그대로 유지된다.

- absolute
    - 가장 가까운 위치에 있는 조상 요소를 기준으로 배치한다.
    - 조상 요소 위치를 기준으로 위쪽(top), 아래쪽(bottom), 왼쪽(left), 오른쪽(right)에서 얼마만큼 떨어질 지 결정한다.
    - 조상 중 Position을 가진 요소가 없다면 초기 컨테이닝 블록(<body>요소)를 기준으로 삼는다. (static을 제외한 값)
    - 문서 상 원래 위치를 잃어버린다. (아래에 있는 div가 해당 자리를 차지한다)