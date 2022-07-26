from re import A, X
from tkinter import Y


a=[1,2,3]
b=[4,5,6]
print(zip(a,b))
#<zip object at 0x00000249E34AE5C0>
print(list(zip(a,b)))
#[(1, 4), (2, 5), (3, 6)]

c=[1,2,3,4]
d=[1,2]
print(list(zip(c,d)))
#짝이 없으면 버리고 있는 것만 반환
#[(1, 1), (2, 2)]

print(list(zip(a,b,c)))
#[(1, 4, 1), (2, 5, 2), (3, 6, 3)]

#e={1:0,2:0,3:0} 는 어떻게 만들까?
b=dict(zip(range(1,4),[0]*3))
print(b)
#{1: 0, 2: 0, 3: 0}

#전치에서 zip을 많이 씀
# m=[[0]*3]*3 으로 쓰면 안됨?->안됨
#얕은복사
n=[[0]*3]*3
n[0][0]=99
print(n)
#[[99, 0, 0], [99, 0, 0], [99, 0, 0]]가 되어버림.
matrix = []
for _ in range(3):
    matrix.append([0]*3)
matrix[0][0]=99
print(matrix)
#[[99, 0, 0], [0, 0, 0], [0, 0, 0]]=>해결됨
n=[[0]*3 for _ in range(3)]
#이러한 형태로 표현할 수 있음-중요!


#########

#전치

a=[[3,1,2],[4,7,9],[6,8,5]]

for r in range(3):
    for c in range(3):
        a[r][c],a[c][r]=a[c][r],a[r][c]
print(a)
#[[3, 1, 2], [4, 7, 9], [6, 8, 5]]그대로 남음.두번 전환하게 되므로
for r in range(3):
    for c in range(r+1,3):
        a[r][c],a[c][r]=a[c][r],a[r][c]
print(a)
#[[3, 4, 6], [1, 7, 8], [2, 9, 5]]
#여기서는 정사각형의 모양만 전치가 가능

#zip으로 전치하기
#예를 들어 3X4의 경우
a=[[3,1,2],[4,7,9],[6,8,5]]
transpose_matrix=list(zip(*a))
print(transpose_matrix)
#[(3, 4, 6), (1, 7, 8), (2, 9, 5)]
#원소를 튜플에서 리스트로 바꾸는 법?
transpose_matrix = list(map(list,zip(*a)))
print(transpose_matrix)
#[[3, 4, 6], [1, 7, 8], [2, 9, 5]]
#필요에 따라 변환 가능



################################################################

#함수 안에서 되는 것, 안되는 것?
#nonlocal, global?
#Local 과 Global의 관계?

#1.함수에 리턴값이 없는 경우
nums=[1,2,3,4,5]
def a():
    print("싸피 어서오고")

print(a()) 
#싸피 어서오고
#None

def a():
    nums=[9,10,11,12,13]
    print(nums[4])
a()
print(nums[4])
#13
#5

def a():
    #nums=[9,10,11,12,13]
    print(nums[4])
a()
print(nums[4])
#5
#5

def a():
    #nums=[9,10,11,12,13]
    num = nums[4]
    print(num)
a()
#참조가 가능


def a():
    #nums=[9,10,11,12,13]
    nums[2] = 99

a()
print(nums)
#[1, 2, 99, 4, 5]
#변경이 가능
#for문은 global임 헷갈리면 안됨 따로 로컬 공간이 생성되는 게 아님 2중 for문도 마찬가지임
#함수 내부에서도 참조도 가능하고, 참조값을 할당도 가능함
#변경까지도 가능함
#다만, 재할당은 불가능함

nums = [1,2,3,4,5]
def a():
    nums="이제 다른거로 갈아끼자"
a()

print(nums)
#"nums" is not accessed ->재할당이 불가능함


#############################################################

nums = [1,2,3,4,5]
def a():
    global nums
    nums = '왜이렇게 죽상이야'

a()
print(nums)
#이제 다른걸로 갈아끼자



################################################################

a=3
print('(1) 맨처음 a의 id: ', id(a))

def first():
    global a
    global x
    x = 'global은 이런게 된다!!!'
    #재할당을 위해서global 사용.
    print('(2-1) first 안에서의 a의 id', id(a))
    b=4
    print('(2-2) first 안에서의 b의 id', id(b))

    def second():
        nonlocal b
        # nonlocal y
        #No binding for nonlocal "y" found
        #global만 됨
        y = 'nonlocal은 그러면 되는거야?'
        print('(3-1) second 안에서의 b의 id', id(b))
        c=6
        print('(3-2) second 안에서의 c의 id', id(c))
    
    #여기서 second를 쓰면 정의되지 않은 곳에 쓰는 것이 되어버림(third까지가 second 정의되는 곳)

        def third():
            nonlocal c
            #nonlocal c가 없으면
            #UnboundLocalError: local variable 'c' referenced before assignment
            #위에 분명히 c있는데 안됨?
            #가장 가까운 것 부터 찾기 때문=>c=7을 먼저 찾기 때문에

            print('(4-1) third 안에서의 c의 id', id(c))
            c=7
            print('(4-2) third 안에서의 c의 id', id(c))
        
        third()
    second()
first()

print('진짜 됨?',x)
#진짜 됨? global은 이런게 된다!!!


#(1) 맨처음 a의 id:  2464670640496
#(2-1) first 안에서의 a의 id 2464670640496
#(2-2) first 안에서의 b의 id 2464670640528
#(3-1) second 안에서의 b의 id 2464670640528
#(3-2) second 안에서의 c의 id 2464670640592
#(4-1) third 안에서의 c의 id 2464670640592
#(4-2) third 안에서의 c의 id 2464670640624

######
#a()
#name 'a' is not defined
#name이라는게 중요! 함수도 값이기 때문에 define 되지 않은 상태에서는 쓸 수 없음. 함수가 정의된 이후 써야함


def a():
    print("hi")

a()

#################################
a={
'name':'alex',
'age' : 3,
'address':'대전'
}



#dic에서 key값 지우는 법
#for문에서 del을 쓸수는 없음. 정해진 size에서 실행되므로

a={
'name':'alex',
'age' : 3,
'address':'대전'
}
for key,val in a.items():
    #RuntimeError: dictionary changed size during iteration0
    del a[key]




#########
#객체의 주소를 다르게?
a={1,2,3,4,5}
print(id(a))
b = set(a)
id(b)
id(a)
#둘의 주소가 다름
