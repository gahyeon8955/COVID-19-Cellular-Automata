import os
#os 모듈 가져오기

def calcu_MN(MN,MC) :
   #calcu_MN(MN,MC)함수 정의, MN은 다음세대의 상태를, MC는 이전세대의 상태를 나타냄. 
   for x in range(1, SIZE+1) :
      #range는 정수범위 표현, 즉 x의 범위는 1부터 SIZE+1까지 
      for y in range(1, SIZE+1) :
         #y의 범위는 1부터 SIZE+1까지

         C = MC[x-1][y+1] + MC[x][y+1] + MC[x+1][y+1] + MC[x-1][y] + MC[x+1][y] + MC[x-1][y-1] + MC[x][y-1] + MC[x+1][y-1]
         #C는 이웃들임.(8개 이웃, 즉 무어이웃)

         if   C == 3 :         MN[x][y] = 1
         #이웃이 3명 살아있다면(C==3) 다음세대 세포 새로 살아남(MN=1)
         elif C == 2 : 
            #이웃 2명 살아있다면(C == 2)
            if MC[x][y] == 1 :    MN[x][y] = 1
            #이웃이 2명 살아있는 중에서 이전세대에 살아있는 애가 있다면(MC[x][y] == 1) 다음세대 세포가 계속 살아있음(MN[x][y] = 1)
            else :              MN[x][y] = 0
            #이웃이 2명 살아있는 중에서 그밖의 것들은(이전세대가 죽어있다면) 다음세대 세포는 계속 죽어 있음(MN[x][y] = 0)
         else :            MN[x][y] = 0
         #이웃이 3명 살아있지 않은 그 밖의 것들(이웃이 1명 이하 또는 4명 이상 있는경우)은 다음세대 세포가 죽음(MN[x][y] = 0)
      

def print_MN(MN,MC) :
   #calcu_MN(MN,MC)함수 정의
   os.system('clear')
 #콘솔 화면 지움
   print("\n\n")
 #문자열 줄바꿈
   for x in range(1, SIZE+1) :
      #아까 위에서 했던 거, x의 범위는 1부터 SIZE+1까지
      print("\t\t", end=' ')
   #문자열 줄바꿈, end=' '는 다음번 출력이 한줄로 이어짐.
      for y in range(1, SIZE+1) :
         #아까 위에서 했던 거, y의 범위는 1부터 SIZE+1까지

         if MN[x][y] == 1 :    
            #다음세대 세포가 살아있다면(MN[x][y] == 1)
            if MC[x][y] == 1 : print("O",end=' ') 
      #다음세대 세포가 살아있는 중에서 이전세대 세포가 살아있다면(MC[x][y] == 1) 문자 0 출력(0은 살아있음), 다음번 출력이 한줄로 이어짐
            else :          print("*",end=' ') 
      #다음세대 세포가 살아있는 중에서 그밖의 것들은(이전세대 죽어있다면) 문자 * 출력(*은 새로 살아난 상태), 다음번 출력이 한줄로 이어짐
         else :
            #그밖의 것들은(다음 세포가 죽어있다면)
            if MC[x][y] == 1 : print("X",end=' ') 
      #다음세대 세포가 죽어있는 중에서 이전세대 세포가 살아있다면(MC[x][y] == 1) 문자 X출력(X는 죽은상태), 다음번 출력이 한줄로 이어짐
            else :             print(" ",end=' ') 
      #다음세대 세포가 죽어있는 중에서 그밖의 것들은(이전세포가 죽어있다면) 아무것도 출력 안함. 다음번 출력 한줄로 이어짐.
      
      print(" ") 

   print("\n\nSTEP :  ", STEP) 
 #화면에 "STEP:" 출력. 변수명은 STEP

def init_MC() :                                    #init_MC()함수 정의
	global MC, MI, STEP                            #MC, MI, STEP 전역변수 설정
	MC = MI                                       
	STEP = 0
	print_MN(MC,MC)                                #print_MN 함수 실행
	NEXT = input()                                 #input()함수로 사용자에게 값을 입력받고 변수NEXT에 저장

SIZE = 10
STEP = 0

MI = [[0]*(SIZE+2) for i in range(SIZE+2)]
# 2차원 리스트를 만드는 반복문

MI[0] =  [0,0,0,0,0,0,0,0,0,0,0,0]
MI[1] =  [0,0,0,0,0,0,0,0,0,0,0,0]
MI[2] =  [0,0,0,0,0,0,0,0,0,0,0,0]
MI[3] =  [0,0,0,0,0,0,0,0,0,0,0,0]
MI[4] =  [0,0,0,0,0,1,0,0,0,0,0,0]
MI[5] =  [0,0,0,0,1,1,1,0,0,0,0,0]
MI[6] =  [0,0,0,0,0,1,0,0,0,0,0,0]
MI[7] =  [0,0,0,0,0,0,0,0,0,0,0,0]
MI[8] =  [0,0,0,0,0,0,0,0,0,0,0,0]
MI[9] =  [0,0,0,0,0,0,0,0,0,0,0,0]
MI[10] = [0,0,0,0,0,0,0,0,0,0,0,0]
MI[11] = [0,0,0,0,0,0,0,0,0,0,0,0]

#MI 리스트(12*11)를 만든 뒤 각 열의 내용을 지정
#MI는 2차원 리스트이며 지정해 준 열의 내용이 초기조건을 의미하게 됨

MC = [[0]*(SIZE+2) for i in range(SIZE+2)]
#같은 방법으로 MC리스트도 생성

init_MC()                                         #init_MC()함수 작동

while 1 :                                         #while문으로 아래 코드 반복 수행(1은 조건)

	MN = [[0]*(SIZE+2) for i in range(SIZE+2)]   

	STEP += 1                                     #STEP변수에 +1하고 저장
	calcu_MN(MN,MC)                               #calcu_MN(MN,MC) 함수 작동
	print_MN(MN,MC)                               #print_MN(MN,MC) 함수 작동

	NEXT = input()                                #input()함수로 사용자에게 값을 입력받고 변수NEXT에 저장

	if NEXT == 'q' : break                        #NEXT변수를 'q'로 입력받으면 break로 반복문 끝냄
	elif NEXT == 'c' : init_MC()                  #NEXT변수를 'c'로 입력받으면 init_MC()함수 실행
	else : MC = MN                                #else if와 elif조건 둘 다 해당 안 하면 MC = MN

	del MN                                        #MN변수 삭제

print ("END OF GAME")                             #"END OF GAME" 출력