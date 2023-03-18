import pygame, random

pygame.init()#게임 엔진 초기화

White = (255,255,255) #색상정의 
black = [0,0,0]

size = [500,350]
snow_cnt = 90 #눈의 개수

screen = pygame.display.set_mode(size)
pygame.display.set_caption("눈 오는 밤")

#눈이 오는 좌표 리스트
snow_list = []

#snow_list에 snow_cnt 수만큼의 좌표 저장
for i in range(snow_cnt):
    x = random.randrange(0,size[0]) #x좌표 저장
    y= random.randrange(0,size[1]) #y좌표 저장
    snow_list.append([x,y]) #좌표를 리스트에 추가

clock = pygame.time.Clock() #화면 수정에 사용될 시계 저장

#메인 루프
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(black) #배경 검정

    #눈 내리는 모습그리기
    for i in range(len(snow_list)): 

        #radius = 1
        #밑은 주석처리 해도 됨, 단 이때 는 위의 주석을 풀어야 함
        radius = random.randint(1,3)
        pygame.draw.circle(screen,White,snow_list[i],radius)

        #눈 snow_list[i]의 y좌표를 1 증가시켜 눈이 내리도록 수정
        snow_list[i][1]+=1
        #밑은 주석처리 해도됨
        snow_list[i][1] += random.randint(1,3)
        #눈 snow_list[i]의 x좌표를 (-1,0,1) 중 하나에서 선택, 이전 값에 더해 대입
        snow_list[i][0] += random.randint(-1,1)

        #sonw_list[i]가 윈도 바닥으로 내려서가서 보이지 않게 되면
        if snow_list[i][1] > size[1]: #snow_list[i][1]는 snow_list[i]의 y좌표
            #y좌표를 위(음수)로 다시 지정
            snow_list[i][1] = random.randrange(-5,0)
            #x좌표도 다시 지정, snow_list[i][0]은 snow_list[i] 눈의 x좌표
            snow_list[i][0] = random.randrange(0,size[0])

    pygame.display.update()
        #초당 수정될 프레임 수 지정, 초당 20 프레임 화면이 수정됨
    clock.tick(20)


pygame.quit()










