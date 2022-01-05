import random
import numpy as np
import matplotlib.pyplot as pl
import pygame

#pygame으로 사각형을 그려주는 함수 생성. pygame.draw.rect는 pygame에서 사각형을 그려주는 메소드임. 사각형의 [x축, y축, 가로, 세로]의 형태
def drawSquare(screen, currentColor, currentColumn, cellSize, currentRow):
    pygame.draw.rect(screen, currentColor, [currentColumn * cellSize, currentRow * cellSize, (currentColumn + 1)
                                             * cellSize, (currentRow + 1) * cellSize])

def seirpygame(cellCountX, cellCountY, universeTimeSeries):
    pygame.init()     #게임 엔진 초기화

    #색깔(RGB)로 Color변수 설정
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 150, 100)
    YELLOW = (255, 255, 0)
    RED = (200, 30, 0)
    ORANGE = (255, 165, 0)

    screenHeight = 800
    screenWidth = 800

    cellSize = screenHeight / cellCountX

    #pygame에서 사용할 전역변수 선언
    size = [screenHeight, screenWidth]
    screen = pygame.display.set_mode(size) 
    #화면 전체를 설정하기 위한 값이 들어있는 screen변수
    screen.fill(WHITE)
    clock = pygame.time.Clock()


    mainloop = True
    FPS = 60              #초당 화면 출력
    playtime = 0
    cycletime = 0
    interval = .15  #단일 영상을 몇 초 만에 표시해야하는 시간,간격

    currentTimeStep = 0

    while mainloop:
        milliseconds = clock.tick(FPS)  # 마지막 프레임 이후 경과된 밀리초
        seconds = milliseconds / 1000.0  # 마지막 프레임 이후 경과한 시간(초)
        playtime += seconds
        cycletime += seconds
        if cycletime > interval:             #if cycletime값이 interval값보다 클 때

            if currentTimeStep >= simulationIterations:   #if currentTimeStep값이 simulationIterations값보다 크거나 동일하면
                currentTimeStep = 0                       #currentTimeStep = 0이다
            else:                                         #else 위의 경우가 아니면
                currentTimeStep += 1                      #currentTimeStep에 1을 더해주고 저장한다
            pygame.display.set_caption("TimeStep %3i:  " % currentTimeStep)  #타이틀 바의 텍스트 설정

            currentColor = BLACK
            for currentRow in range(
                    cellCountY):  # Y축cellCount에 할당된 값을 range함수에 넣고 이 값의 범위 안의 값들을 하나하나 꺼내 currentRow에 넣어 for문 실행
                for currentColumn in range(
                        cellCountX):  # X축cellCount에 할당된 값을 range함수에 넣고 이 값의 범위 안의 값들을 하나하나 꺼내 currentColumn에 넣어 for문 실행
                    if currentTimeStep > 0 and currentTimeStep < simulationIterations:  # if currentTimeStep과 0이 currentTimeStep보다 작고 simulationIterations보다
                        # 크면(시뮬레이션이 구동되는 동안)
                        if universeTimeSeries[currentTimeStep][currentRow][currentColumn] == '0':  # 그중 만약 상태가 '0'이면
                            currentColor = BLUE  # 상태의 색상은 파란색
                        if universeTimeSeries[currentTimeStep][currentRow][currentColumn] == '1':  # 그중 만약 상태가 '1'이면
                            currentColor = YELLOW  # 상태의 색상은 노란색
                        if universeTimeSeries[currentTimeStep][currentRow][currentColumn] == '2':  # 그중 만약 상태가 '2'이면
                            currentColor = RED  # 상태의 색상은 빨간색
                        if universeTimeSeries[currentTimeStep][currentRow][currentColumn] == '3':  # 그중 만약 상태가 '3'이면
                            currentColor = GREEN  # 상태의 색상은 초록색
                        if universeTimeSeries[currentTimeStep][currentRow][currentColumn] == '4':
                            currentColor = WHITE

                        drawSquare(screen, currentColor, currentColumn, cellSize, currentRow)           #drawSquare함수 실행

        pygame.display.flip()                                                                           #화면 전체를 업데이트

#균등 분포의 형상을 갖는 난수 생성
def getRandomNumber(distribution):
    RandomNumber = np.random.uniform()  # 균등분포
    return RandomNumber

#무어 이웃을 기반으로 세포의 새로운 상태를 계산하는 함수
def getNewState2D(currentRowNeighbours, upperRowNeighbours, lowerRowNeighbours): #2D의 새로운 상태를 얻는 함수(상부행, 중간행, 하부행 인자를 받아옴)
    selfCharacter = currentRowNeighbours[1]                                      #중간행에서 값 1에 해당하는 인덱스를 추출하고 selfCharacter에 넣어줌
    newState = selfCharacter                                                     #자신의 특징,기질을 새로운 상태에 넣어줌

    if selfCharacter == '0':                                                    #만약 selfCharacter이 '0'이면
        if currentRowNeighbours.count('2') > 0 or upperRowNeighbours.count('2') > 0 or lowerRowNeighbours.count(  
                '2') > 0:                                                                    #만약 0보다 하부행의 문자열에서 '2'를 센 수 또는 0이 크고, 상부행의 문자열에서 '2'를
                                                                                             #센 수 또는 0이 크며 중간행의 문자열에서 '2'를 센 수가 크면
            betaChance = getRandomNumber(0)                                                  #0을 인자로 받아온 getRandomNumber함수를 betachance에 넣어줌
            if betaChance < beta and betaChance > 0:                                           #만약 beta와 betachance(둘 다 참이여야 참)가 betachance보다 크고 0보다 크면
                newState = '1'
            else:
                deltaChance=getRandomNumber(0)
                if deltaChance<delta and deltaChance>0:
                    newState='4'
                    global fourCount
                    fourCount += 1
            '''deltaChance = getRandomNumber(0)
            if deltaChance < delta and deltaChance > 0:
                newState = '4' '''

    elif selfCharacter == '1':                                                             #selfCharacter가 '1'이면
        sigmaChance = getRandomNumber(0)                                                   #0을 인자로 받아온 getRandomNumber함수를 sigmachance에 할당함
        if sigmaChance > 0 and sigmaChance < sigma:                                          #만약 0과 sigmaChance가 sigma보다 작고 sigmaChance보다 작으면
            newState = '2'
        else:                                                                                #else
            if currentRowNeighbours.count('2') > 0 or upperRowNeighbours.count('2') > 0 or lowerRowNeighbours.count(
                    '2') > 0:                                                                  #만약 중간행의 문자열에서 '2'를 센 수 보다 0또는 하부행에서 '2'를 센 수가 작고 이보다
                                                                                               #0 또는 하부행에서 '2'를 센 수가 작으며 이것이 0보다 크면
                newState = '1'                                                                 #'1'이 newstate에 할당됨
            else:                                                                              #else
                newState = '0'                                                                 #'0'이 newstate에 할당됨

    elif selfCharacter == '2':
        gammaChance = getRandomNumber(0)                                                   #0을 인자로 받아온 getRandomNumber함수를 gammachance에 넣어줌
        if gammaChance < gamma and gammaChance > 0:                                          #만약 gammaChance와 gamma가 0보다 크고 gammaChance보다 크면
            newState = '3'                                                                   #'3'을 newState에 할당함
    elif selfCharacter == '3':                                                             #selfCharacter가 '3'이면
        alphaChance = getRandomNumber(0)                                                   #0을 인자로 받아온 getRandomNumber함수를 alphachance에 넣어줌
        if alphaChance < alpha and alphaChance > 0:                                          #alpha와 alphaChance가 0보다 크고 alphaChance보다 크면  
            newState = '0'                                                                   #'0'을 newState 할당함

    return newState                                                                        #newState를 반환해줌


def VaccinedNeighbors(cellCountX, cellCountY):
    UpperRowNeighbours='000'
    LowerRowNeighbours='000'
    for currentRow in range(cellCountY):
        for currentColumn in range(cellCountX):
            CurrentRowNeighbours = oldUniverseList[currentRow][currentColumn - 1:currentColumn + 1]
            if (currentRow - 1) >= 0 and (currentRow+1) < cellCountY:
                UpperRowNeighbours = oldUniverseList[currentRow - 1][currentColumn - 1:currentColumn + 1]
                LowerRowNeighbours = oldUniverseList[currentRow+1][currentColumn-1:currentColumn + 1]
                if oldUniverseList[currentRow][currentColumn]=='1':
                    UpperRowNeighbours=UpperRowNeighbours.replace('0','4')
                    LowerRowNeighbours=LowerRowNeighbours.replace('0','4')
                    CurrentRowNeighbours=CurrentRowNeighbours.replace('0','4')

mu = 0                                          #사망률
muStart = 0                                     #출생률

simulationIterations = 300                      #300만큼 시뮬레이션 반복
cellCountX = 100                                #100을 X축cellCount에 할당
cellCountY = 100                                #100을 Y축cellCount에 할당

# 기본값 설정
extremeEndValue = '0' 
timeStart = 0.0                                #시간의 시작은 0.0으로 함
timeEnd = simulationIterations                 #시간의 끝은 위에서 설정해준 시뮬레이션 반복 값인 70이 끝날 때
timeStep = 1                                   #시간단계는 1
timeRange = np.arange(timeStart, timeEnd + timeStart, timeStep) #시간 범위에 numpy arange함수에서 시간의 단계 크기만큼 떨어져 있는 값을 array 형태로 반환해준 것을 할당
universeList = []

#첫 번째 상태 랜덤화
for currentColumn in range(cellCountY):      #Y축cellCount에 할당된 값을 range함수에 넣고 이 값의 범위 안의 값들을 하나하나 꺼내 currentRow에 넣어 for문 실행
    universe = ''.join(random.choice('00000000000000000000002') for universeColumn in range(cellCountX)) #Y축cellCount에 할당된 값을 range함수에 넣고 이 값의 범위 안의 
    #값들을 하나하나 꺼내 universeColumn으로 넣어 실행되는 for문과 '00000000000000000000002'에서 랜덤으로 선택된 리스트에 ''문자열이 들어간 것을 universe변수에 할당
    universeList.append(universe)            #universelist에 universe리스트 추가

#초기 상태 변수 고정
InitSusceptibles = 0.0                                                              #처음에 S가 몇 명 있었나?       
InitInfected = 0.0
InitRecovered = 0.0
InitVaccined = 0.0
InitVariables = [InitSusceptibles, InitInfected, 0.0, 0.0, InitVaccined, 0.0]                     #초기 상태 변수

RES = [InitVariables]                                                               #RES에 초기상태변수 저장

universeTimeSeries = []                                                             #UniverseTimeSeries라는 공백 리스트 생성(후에 시간에 따른 각 셀의 상태를 시각적으로 나타낼 리스트)


zeroCount = 0                                                                   #각 상태(0,1,2,3)의 수를 세어 저장할 변수들을 선언
oneCount = 0
twoCount = 0
threeCount = 0
fourCount = 0



for currentTimeStep in range(simulationIterations):
    #시간에 따른 파라미터값 변화

    #2월 18일 최초감염자 발생~3월 8일
    sigma = 0.95
    alpha = 0.5
    gamma = 0.434
    delta = 0.1

    #2월 18일~2월 26일
    if currentTimeStep < 8:
        R0 = 0.005
        beta = R0*gamma
    
    #2월 26일~3월 12일
    elif 8 < currentTimeStep <= 23:
        R0 = 2.5
        beta = R0*gamma
    
    #3월 12일~8월 14일
    elif 23 < currentTimeStep <= 181:
        R0 = 0.215
        beta = R0*gamma

    #8월 14일~9월 2일
    elif 181 < currentTimeStep <= 200:
        R0 = 2.0
        beta = R0*gamma

    #9월 2일~11월 15일
    elif 200 < currentTimeStep <= 274:
        R0 = 0.215
        beta = R0*gamma

    #11월 15일~11월 29일
    elif 274 < currentTimeStep <= 300:
        R0 = 2.0
        beta = R0*gamma
    
    for currentRow in range(cellCountY):
        zeroCount += universeList[currentRow].count('0')                            #universeList 속 0의 수를 세어 zeroCount 변수에 추가(universeList[i]는 i번째 행 전체를
                                                                                    #문자열로 만든 것: 전체 셀 중 0인 셀의 수를 저장)
        oneCount += universeList[currentRow].count('1')
        twoCount += universeList[currentRow].count('2')
        threeCount += universeList[currentRow].count('3')
    RES.append([zeroCount, oneCount, twoCount, threeCount, fourCount, currentTimeStep])        #RES에 각 상태의 셀 수와 currentTimeStep(전체 시간)을 저장

    #경계조건
    oldUniverseList = []
    toCopyUniverseList = []
    for currentRow in range(cellCountY):
        oldUniverseList.append(extremeEndValue + universeList[currentRow] + extremeEndValue)                 #셀의 양 옆에 0을 붙여 oldUniverseList에 추가(행에 대해서는
                                                                                                             #현 셀의 이웃이 모두 0인 상태)
        toCopyUniverseList.append(universeList[currentRow])                                                  #toCopyUniverseList에 현 셀을 추가

    universeTimeSeries.append(toCopyUniverseList)                                                            #universeTimeseries에 toCopyUniverseList 추가

    for currentRow in range(cellCountY):                                                                     #oldUniverseList에 대한 계산-맨 위와 아래 행은 제외하고
        newUniverseRow = ''
        for currentColumn in range(cellCountX):
                upperRowNeighbours = '000'                                                                   #무어 이웃에서 위의 행
                lowerRowNeighbours = '000'                                                                   #무어 이웃에서 아래의 행
                currentRowNeighbours = oldUniverseList[currentRow][currentColumn:currentColumn + 3]          #무어 이웃에서 가운데 행의 상태를 저장(기준 셀 포함)
                if (currentRow - 1) >= 0:                                                                    #맨 위에서 한 칸 아래 줄부터
                    upperRowNeighbours = oldUniverseList[currentRow - 1][currentColumn:currentColumn + 3]    #무어 이웃에서 위의 행의 상태를 저장
                if (currentRow + 1) < cellCountY:                                                            #맨 아래에서 한 칸 윗 줄까지
                    lowerRowNeighbours = oldUniverseList[currentRow + 1][currentColumn:currentColumn + 3]    #무어 이웃에서 아래의 행의 상태를 저장

                newUniverseRow += getNewState2D(currentRowNeighbours, upperRowNeighbours, lowerRowNeighbours)#newUniverseRow에 getNewState2D에 각 셀의 이웃들 상태를 넣고
                                                                                                             #실행시킨 결과(새로운 상태)를 추가
                universeList[currentRow] = newUniverseRow                                                    #universeList에 새로운 상태를 저장(각 셀들을 새로운 상태로 교체)


#RES 그래프 그리기
RES = np.array(RES)                                                                                          #RES를 행렬로 만든다. np.array()는 행렬 계산이 가능하게 하는 함수.


pl.subplot(2, 1, 1)
pl.plot(RES[:, 5], RES[:, 2], '-r', label='Infected')                                                        #RES[:,4]를 x축, RES[:,2]가 y축으로 갖는 solid line style의 붉은 색 그래프를 그리고 label(범례)에 Infected 저장
pl.plot(RES[:, 5], RES[:, 1], '-y', label='Exposed')                                                         #RES[:,4]를 x축, RES[:,1]가 y축으로 갖는 solid line style의 붉은 색 그래프를 그리고 label(범례)에 Exposed 저장
pl.plot(RES[:, 5], RES[:, 3], '-g', label='Recovered')                                                       #RES[:,4]를 x축, RES[:,3]가 y축으로 갖는 solid line style의 붉은 색 그래프를 그리고 label(범례)에 Recovered 저장
pl.plot(RES[:, 5], RES[:, 4], '-b', label='vaccined')                                                         #RES[:,4]를 x축, RES[:,3]가 y축으로 갖는 solid line style의 붉은 색 그래프를 그리고 label(범례)에 Recovered 저장
pl.legend(loc=0)                                                                                             #범례 표기. loc=0은 범례를 표시할 위치를 설정하는 부분(위치를 0~10의 숫자로 나타냄)
pl.title('COVID19 SEIR model')                                                                                       #제목 표기: SEIR model
pl.xlabel('Time')                                                                                            #x축 표기: Time
pl.ylabel('Count')                                                                                           #y축 표기: Count


pl.subplot(2, 1, 2)
pl.plot(RES[:, 5], RES[:, 2], '-r', label='Infected')
pl.plot(RES[:, 5], RES[:, 3], '-g', label='Recovered')
pl.legend(loc=0)
pl.title('')
pl.xlabel('Time')
pl.ylabel('Count')

pl.show()                                                                                                    #그래프 띄우기

seirpygame(cellCountX, cellCountY, universeTimeSeries)                                                       #세포자동자 시뮬레이션 실행