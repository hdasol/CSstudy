# OSI 7계층

## 기태

### OSI 7계층에 대해서 알고계신가요?
- OSI는 Open System Interconnection의 약자로, 통신이 일어나는 과정을 단계별로 나눈 모델입니다.
- 이렇게 계층별로 나눈 이유는, 특정한 곳에서 이상이 생기면 그 단계만 수정하면 되기 때문입니다.
- 이에 대한 예시를 들어보겠습니다.
- PC방에서 메이플스토리를 하다가 연결이 끊긴 상황입니다.
- 만약 모든 PC에서 연결이 끊겼다면 라우터에 문제가 생겼을 수 있고 이 경우에는 3계층을 조사해 원인을 찾을 수 있습니다.
- 또 한 PC에서만 연결이 끊겼고 메이플스토리 소프트웨어에 문제가 없다면 스위치에 문제가 생겼다는 것을 판단하여 2계층을 조사해 원인을 찾을수도 있을 것입니다.
- 이렇게 어디서 문제가 생겼는지를 판단해서 원인을 찾을수 있게 계층별로 나눴다고 할 수 있습니다.

### 그럼 계층별로 간단히 설명 부탁드립니다.
- 1계층부터 7계층까지 올라가보겠습니다.
- 1계층부터 7계층까지, Physical, Data Link, Network, Transport, Session, Presentation, Application 레이어가 존재합니다.
- 1계층은 Physical Layer 입니다.
- 만약 두 대의 컴퓨터를 전선 하나로 연결하고, 서로 통신을 해야한다고 해보겠습니다.
- 컴퓨터의 모든 파일과 프로그램은 0과 1로 이루어져 있습니다.
- 두 대의 컴퓨터가 통신을 한다는 것은 결국 이 전선을 통해 0과 1의 데이터를 주고받는 과정입니다.
- 이렇게 데이터를 주고받는 과정은 전기신호, 즉 전자기파로 전송이 됩니다.
- 일반적으로 전기신호를 전송하고 받을 때, 전선의 매질에 따라 통과시킬수 있는 주파수의 영역대가 다릅니다.
- 그래서 어떤 주파수는 통과하고, 어떤 주파수는 통과하지 못해 데이터 송수신에 에러가 있을 수 있습니다.
- 저희는 0과 1의 데이터를 주고 받아야하는데 이 전기신호들은 수평선, 수직선의 그래프로 되어있기 때문에 0~무한대의 주파수를 가지고 있습니다.
- 그래서 저희는 데이터 자체를 전선을 통해 통과시키는 것이 불가능합니다.
- 이를 가능하게 하려면, 아날로그 신호로 변조해서 보내야합니다.
- 이 말은 무한대의 주파수를 가지는 데이터를, 전선이 통과시킬수 있는 주파수에 맞춰 바꾸어 보내야 한다는 뜻입니다.
- 0과 1의 데이터를 아날로그 신호로 바꾸어 보내고, 수신하는 부분에서 이 아날로그 신호를 원래 데이터로 복조하여 이해하는 과정이 이 계층에서 이루어집니다. (하드웨어)

- 2계층은 Data Link Layer 입니다.
- 여기서는 우선 여러대의 컴퓨터가 통신한다는 설정을 하겠습니다.
- 1계층에서는 두 대의 컴퓨터에 전선을 연결했죠.
- 하지만 여러개의 컴퓨터끼리 전선을 연결하는 것은 불가능합니다. 비용 면에서도 그렇구요.
- 그래서 여기서는 스위치라는 장비가 사용이 됩니다.
- 스위치는 여러대의 컴퓨터가 연결되어 네트워크를 이루게하는 장치입니다.
- 이렇게 네트워크가 모이고 모여서 전 세계의 컴퓨터들을 연결한 것을 인터넷이라고 하구요.
- 실제로 규모가 엄청나게 큰 케이블이 바다밑에 깔려있어서 전세계의 컴퓨터끼리 통신이 가능합니다.
- 그럼 이제 여러대의 컴퓨터가 한 컴퓨터로 데이터를 전송한다고 하겠습니다.
- 1계층처럼 데이터를 0과 1로 보내는데, 수신하는 측에서는 이 0과 1을 끊어 읽지 않으면 올바른 데이터를 이해하기가 힘듭니다.
- 그래서 데이터를 끊어 읽기 위해서 2계층에서는 데이터의 앞뒤에 특정한 비트열을 붙여 데이터를 보냅니다. 이것을 Framing 한다고 합니다.
- 따라서 이러한 작업이 이루어지는 계층이 Data Link Layer 입니다. (하드웨어 랜카드)

- 3계층은 Network Layer 입니다.
- Network Layer 에서 사용되는 대표적인 장치는 라우터입니다.
- 라우터는 한 컴퓨터에서 다른 컴퓨터로 데이터를 전송할 때 그 길을 찾게 도와주는 장치라고 할 수 있습니다.
- 3계층이 없다면 2계층에서 데이터를 전송할 때 스위치에 연결된 모든 컴퓨터에 데이터가 전송될 수 있는데, 어떻게 보면 이런 문제가 일어나지 않기 위해 존재한다고도 볼 수가 있습니다.
- 3계층에서는 데이터에 상대방의 IP주소를 붙여 전송하고, 라우터는 그 IP주소로 잘 찾아갈 수 있도록 도와줍니다.
- 이 IP주소가 붙은 데이터를 패킷 이라고하고 이 작업들이 Network Layer에서 이루어집니다. (운영체제 커널에 소프트웨어적으로 구현되어 있음)

- 4계층은 Transport Layer 입니다.
- Transport Layer는 End to End 사용자들이 신뢰성있는 데이터를 주고받을 수 있도록 하는 계층입니다.
- 데이터의 유효성을 검사하기 위한 프로토콜로 TCP와 UDP가 있습니다.
- 여기서는 포트번호를 사용해서 수신하는 컴퓨터의 최종 도착지인 프로세스에 데이터가 도달하게 하는 Layer입니다.
- 즉 포트번호를 통해 어떤 프로세스가 데이터를 받아야 하는지 알 수 있습니다.


## 참고자료
- [테코톡](https://www.youtube.com/watch?v=1pfTxp25MA8&t=1192s)


## 동현

### OSI 7계층이란?

네트워크에서 통신이 일어나는 과정을 7개의 계층으로 나눈 것을 의미합니다. 네트워크 구조의 호환성을 증가시키기 위해 규정된 모델입니다. 상위 계층은 하위 계층의 기능을 포함하며, 하위 계층에 오류가 있다면 상위 계층이 정상적으로 동작하지 않는다는 특징이 있습니다. 즉, 문제가 발생 시 하위 계층부터 차근차근 확인해 문제의 시작점을 확인할 수 있습니다.

### 7계층 (응용 계층, Application Layer)

응용 프로그램과 통신 프로그램간의 인터페이스를 제공하는 계층입니다. 대표적으로 HTTP, FTP, SMTP 등의 프로토콜이 브라우저나 메일 프로그램 등의 인터페이스를 통해 제공됩니다. (응용계층의 서비스들은 고유의 포트번호를 가지고 있으며 절대적이지는 않음)

### 6계층 (표현 계층, Presentation Layer)

데이터를 어떻게 표현할지 정하는 역할을 합니다. 송신할 데이터를 암호화하거나 수신할 데이터를 복호화하며, 혹은 데이터를 압축하거나 압축해제도 할 수 있습니다. (추가적으로, 해당 데이터가 text인지, gif/jpg인지 등의 구분도 해당 계층에서 할 수 있다.)

### 5계층 (세션 계층, Session Layer)

응용 프로그램간의 `대화를 유지`하기 위한 구조를 제공합니다. 네트워크 상에서 통신을 할 경우, 양쪽 호스트간에 최초 연결을 담당하고 연결이 끊어지지 않도록 동기화 및 유지시켜주는 역할을 합니다. (접속 설정 및 해제) 또한 오류 복구 명령도 관리합니다. SSH, TLS 프로토콜이 유명하며, 흔히 사용하는 Socket 라이브러리가 5계층을 관리하기 위해 사용될 수 있습니다.  

+) 연결이 전이중(Full duplex)인지 반이중(Half Duplex)인지 확인하고 결정한다고 하는데 뭔말인지 모르겠으니깐 공부하기

### 4계층 (전송 계층, Transport Layer)

포트를 이용해 END POINT간의 신뢰성 있고 정확한 `데이터 전송`을 담당합니다. TCP / UDP 프로토콜이 존재하는 계층입니다. 흐름제어나 오류제어 및 복구등을 하는 물리적인 계층입니다. 하위 계층으로 패킷을 생성하고 전송합니다. 혹은 패킷을 받아 데이터를 합쳐 상위 계층에 던져주는 역할을 합니다.

### 3계층 (네트워크 계층, Network Layer)

데이터를 목적지까지 안전하게 `전달`하는 계층입니다. 목적지를 정해 최적의 경로를 결정하고, 경로를 따라 패킷을 전달하는 라우팅 기능을 제공합니다. IP라는 논리적인 주소를 부여합니다.

+) 대표적인 라우팅 장비가 라우터의 NAT 기능을 활성화 한 공유기!

### 2계층 (데이터링크 계층, DataLink Layer)

Point-to-Point 방식의 물리적인 연결을 통해 두 장치간의 신뢰성 있는 정보 전송을 담당합니다. 물리적인 장치를 식별하는데 사용할 수 있는 MAC 주소를 통해 통신합니다. (브리지, 스위치, 이더넷 등)

### 1계층 (물리 계층, Physical Layer)

데이터가 전송되는 물리적인 매체입니다. 케이블, 허브 등의 물리적 장치를 이용해 전기신호로 통신합니다. 디지털에서 아날로그로 혹은 그 반대로 신호를 변환하는 역할을 합니다. 해당 계층에서는 데이터를 단순 전송만 할 뿐, 어떤 데이터인지 어떤 에러가 있는지는 신경쓰지 않습니다.


### 참고 자료

- [OSI 7계층이란?, OSI 7계층을 나눈 이유](https://shlee0882.tistory.com/110)