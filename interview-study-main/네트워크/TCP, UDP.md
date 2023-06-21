# TCP / UDP

## 동현

### TCP와 UDP

송신자와 수신자를 연결하고 데이터를 보내기 위해 사용하는 프로토콜입니다.

TCP는 3-way handshaking을 이용해 송신자와 수신자가 가상적으로 연결되었는지를 확인하기 때문에 `연결 지향적`이며 `신뢰도`가 높습니다. 또한, 흐름 제어와 혼잡 제어등이 가능하며, 패킷 추적 및 관리가 가능합니다. 하지만, 여러 검증 절차 때문에 UDP보다 속도가 느린 프로토콜입니다.

UDP는 검증 절차 없이 단순 목적지로 데이터를 넘기기만 하는 `비연결성` 프로토콜입니다. `속도`가 매우 빠르지만, 데이터가 올바르게 도착했는지에 대한 보장이 안됩니다. 따라서, 신뢰성보다는 연속성이 중요한 서비스에서 많이 사용합니다.

### TCP의 흐름제어와 혼잡제어

흐름제어란, 수신측의 설정 수신량보다 송신측의 전송량이 더 클 경우 전송된 패킷이 손실될 수 있기 때문에 송신 측의 `전송량`을 제어하는 성질입니다. 데이터 처리 속도를 조절하여 수신자의 버퍼 오버플로우를 방지합니다.

혼잡제어란, 네트워크 데이터 처리 속도가 송신측의 데이터 전달 속도를 못따라는 경우를 대비하기 위해 송신측에서 보내는 데이터의 `전송 속도`를 제어하는 방식입니다.

## 참고자료

- [TCP와 UDP의 차이를 자세히 알아보자](https://velog.io/@hidaehyunlee/TCP-%EC%99%80-UDP-%EC%9D%98-%EC%B0%A8%EC%9D%B4)
- (나중에 읽어보기)[TCP 흐름제어/혼잡제어/오류제어](https://velog.io/@jsj3282/TCP-%ED%9D%90%EB%A6%84%EC%A0%9C%EC%96%B4%ED%98%BC%EC%9E%A1%EC%A0%9C%EC%96%B4-%EC%98%A4%EB%A5%98%EC%A0%9C%EC%96%B4)



## 기태

### TCP와 UDP에 대해서 설명해주세요

- TCP와 UDP는 OSI 7계층 중 Transport Layer에서 이루어지는 데이터 전송 프로토콜입니다.
- 우선 Transport Layer는 End Point 간 신뢰성있는 데이터 전송을 담당하는 계층입니다.

- TCP는 신뢰성있는 데이터 통신을 가능하게 해주는 프로토콜입니다.
- 3 way handshake로 Connection 연결을 하고 양방향 통신을 가능하게 합니다.
- 데이터의 순차전송을 보장하고, flow control, congestion control, error detection이 이루어집니다.

- 반대로 UDP는 TCP보다는 신뢰성이 떨어지지만 전송 속도가 빠른 프로토콜입니다.
- TCP처럼 flow control, congestion control 을 하지 않습니다. 물론 연결을 위한 3-way handshake도 이루어지지 않습니다. Error detection만 합니다.
- UDP는 비교적 데이터의 중요도가 낮거나 빠른 전송 속도를 요구하는 경우 사용합니다.

### 3-way handshake에 대해서 설명해주세요

- 3-way handshake는 두 end point간 데이터 전송을 하기 전 서로를 연결하는 과정입니다.
- 서로 보내는 패킷의 Header에는 flag bit들이 있는데요, 그 중에는 SYN, ACK, FIN bit들이 있습니다.
- SYN은 패킷을 보낼때 보낸다는 의미로 1을 설정하고, 마찬가지로 ACK도 패킷을 보낼때 잘 받았다는 의미로 1을 설정합니다.
- 우선 A endpoint에서 SYN를 1로하여 B endpoint로 보냅니다.
- 다음 B에서 그 SYN을 잘 받았다는 ACK 1과, 양방향 통신을 위해 B도 A에게 SYN을 1로 설정하여 보냅니다.
- 다음 A에서 잘 받았다는 ACK 1을 B에게 보내고, 이제 Connection이 Established됩니다.
- 이렇게 세번 패킷을 주고받는다는 의미로 3-way handshake라고 부릅니다.

- 추가로 4-way handshake 과정은 방금 3-way handshake로 연결한 것을 끊는 과정인데요.
- A에서 B로 FIN bit를 1로 설정하고 전송하고, ACK를 1로하여 보냅니다.
- 마찬가지로 B도 A에게 FIN bit를 1로 설정해 전송하고, A가 ACK를 1로 설정하여 또 보냅니다.
- 각 End Point가 FIN 패킷을 받으면 연결이 CLOSED 됩니다.

## 참고자료
- [테코톡](https://www.youtube.com/watch?v=ikDVGYp5dhg) <- 지림. 개추요!!