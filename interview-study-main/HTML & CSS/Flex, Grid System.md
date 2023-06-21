# Flex, Grid System

## 동현

### Flex Layout

레이아웃 배치 전용으로 고안된 스타일입니다. 부모 요소인 Flex Container 내부에 자식 요소인 Flex Item을 넣어줍니다. 설정한 `속성`에 따라 Flex Item의 배치 형태가 결정되는 레이아웃입니다.

### Flex Layout의 속성

(기본값은 []로 표시해뒀음)

1. Container 속성

- display : flex;
  - Item들이 가로 방향으로 배치됩니다. 너비는 Item의 width 만큼, 높이는 Container의 height만큼 차지하게 됩니다.
  - (display: inline-flex 설정은 Container를 inline-block처럼 동작하게 만듭니다.)
- flex-direction
  - [row], row-reverse, column, column-reverse
  - 메인축의 방향을 결정합니다. row가 가로로.. column이 세로로 배치됩니다.
  - 모바일에서는 column, 웹에서는 row를 사용하는 식으로 반응형 구성을 할 수 있습니다.
- flex-wrap
  - [nowrap], wrap, wrap-reverse
  - 컨테이너가 더 이상 아이템을 한 줄에 담을 공간이 없을 때, 아이템 줄바꿈을 어떻게 할지 결정합니다.
  - nowrap은 컨테이너 밖으로 튀어나가고, wrap은 다음 줄로 넘깁니다.
- justify-content
  - [flex-start], flex-end, center, space-between, space-around, space-evenly
  - 메인축 방향으로 정렬하는 방식을 결정합니다.
  - space-between, space-around, space-evenly는 각각 간격을 만드는 방식이 다릅니다.
- align-items
  - [stretch], flex-start, flex-end, center, baseline
  - 수직축 방향으로 정렬하는 방식을 결정합니다.
  - stretch를 사용하면 아이템들을 컨테이너 높이만큼 쭉 늘립니다. 즉, 아이템의 높이가 컨테이너의 높이만큼이 됩니다.

2. Item 속성

- flex-basis
  - 아이템의 크키 (row면 width column이면 height)를 결정합니다. 기본값은 auto입니다.
  - 만약, 설정한 크기보다 content 영역의 너비가 더 크다면 아이템의 최소 너비로 동작합니다.
- flex-grow
  - 아이템이 flex-basis의 값보다 커질 수 있는지를 결정하는 속성입니다.
  - 0을 적용하면 늘어나지 않고, 1 이상을 적용하면 `여백`에 한해서만 비율이 적용되는 방식으로 쭉 늘어나게 됩니다.
- flex-shrink
  - 아이템이 flex-basis의 값보다 작아질 수 있는지를 결정하는 속성입니다.
  - 기본값은 1이기 때문에 작아질 수 있으며, 0을 설정하면 flex-basis보다 작아지지 않기 때문에 크기가 고정인 컬럼을 만들 때 사용할 수 있습니다.
