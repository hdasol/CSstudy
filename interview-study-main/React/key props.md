# key props

## 동현

### 리액트에서 사용하는 Key에 대해 설명해주세요

key를 이용하면 React가 Data를 가지고 있는 List에서 반환하는 element 각각을 식별하는데 도움을 줍니다. 이를 통해, 어떤 항목들이 추가되었고, 변했는지, 삭제되었는지를 파악하기 쉽습니다.

이는 리액트가 렌더링하는 방식과 관련이 있는데, 리액트에서는 가상돔을 만들어 이전돔과 비교해 바뀐 부분을 내부 알고리즘을 통해 연산하고 반영하는 방식으로 렌더링을 수행합니다. list의 중간지점에 새로운 데이터가 들어와서 새로운 element 렌더링을 발생시켜야 한다고 가정했을 때, key가 없다면 전체 list를 순회하고 변화를 줍니다. 하지만, key가 있다면 리액트는 빠르게 값의 변화를 파악하고, 변화가 필요없는 부분은 건너뛸 수 있습니다. 즉, 비효율적인 렌더링을 방지할 수 있습니다.

### 참고 자료

- [Understand the Importance of React’s “Key” Prop](https://meganslo.medium.com/why-is-reacts-key-prop-important-b6bd51124270#8977)
