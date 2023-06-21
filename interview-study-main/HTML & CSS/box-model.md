# box model

## 동현

### Box Model이란?

HTML 요소들은 박스 모양으로 구성되어 있습니다. 박스의 외곽부터 내부까지 margin, border, padding, content 로 구성됩니다.

### box-sizing

박스의 크기 기준을 정하기 위해 사용하는 속성입니다. default 값으로 content-box이며, 또 다른 값으로 border-box를 많이 사용합니다.

content-box는 content를 기준으로 크기를 정합니다. width와 height 속성값이 content 부분에만 영향을 주기 때문에 직관적이지 못하다는 느낌을 받을 때가 많았습니다. 또한, 반응형 레이아웃을 구현하기 위해 길이의 단위를 %로 잡으면 계산 문제는 더욱 복잡해집니다.

border-box는 border를 기준으로 크기를 정합니다. padding이나 border의 크기에 따라 content 영역의 너비나 높이가 동적으로 바뀌게 됩니다. 개인적으로는 이 방식이 편해서 css reset 파일에 border-box를 기본 설정해놓고, content-box가 필요한 별도의 요소에는 따로 설정하는 방식을 사용합니다.
