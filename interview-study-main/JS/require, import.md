# require / import

## 동현

### commonjs vs es6

CommonJS란, 자바스크립트를 브라우저뿐 아니라 Server Side / Desktop Application 등의 개발을 위해서도 사용할 수 있는 `범용 언어`로 만들기 위한 그룹(팀)이면서 모듈 방식입니다. Node에서 현재 사용하는 방식입니다.

ES6란 2015년에 발행된 자바스크립트 언어의 표준 규격입니다. ES6에서는 Promise, 블록 단위 스코프, 화살표 함수, 모듈화, 템플릿 리터럴, 클래스 등이 추가되었습니다.

### require vs import

CommonJS에서는 모듈화를 위해 module.exports 객체를 이용해 정의하고, require 함수를 이용해 사용합니다. exports는 moudle.exports를 참조하기 때문에 같은 값을 바라봅니다. require()은 module.exports를 리턴합니다.

import / export 문법은 ES6에서 사용하는 모듈 문법입니다. 모듈을 내보내기 위해 export 및 export default를 사용하며, 가져오기 위해 import 키워드를 사용합니다. 아직 모든 브라우저들이 ES6를 완벽히 지원하지 못하므로, webpack과 babel bundler등을 이용하는게 좋습니다.  
한 모듈에서 export를 사용해 여러 객체를 내보낼 수 있습니다. 내보낸 객체는 중괄호를 이용해 import 해야합니다. 이를 `named export`라고 합니다.  
반면, export default를 이용해 단 하나의 객체만 내보낼 수 있는데, 이 때는 중괄호를 사용하지 않고 import 합니다. 이를 `default export`라고 합니다.

### 참고 자료

- [ECMAScript, ES6이란](https://m.blog.naver.com/rhkrehduq/221379338730)



## 기태
- require와 import는 외부 파일이나 라이브러리를 불러올 때 사용합니다.
- require은 CommonJS 키워드, import는 ES2015에서 도입된 키워드입니다.
- 다른 파일의 코드를 불러온다는 목적은 같지만, 문법이 다릅니다.
- Babel과 같은 ES6 코드를 변환(transpile)해주는 도구를 사용할 수 없는 경우에는 require 키워드를 사용해야 합니다.