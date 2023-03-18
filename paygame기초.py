import pygame

White = (255,255,255) #색상정의 
blue = (0,0,255)


size = (300,200)#윈도 크기 정의

pygame.init() #윈도 초기화 - 파이게임 초기화

screen = pygame.display.set_mode(size)#화면 크기 지정해 스크린을 생성

pygame.display.set_caption('첫 게임 파이윈도')#제목인 캡션 지정


done = False #윈도 종료 플래그로 사용되는 변수 초기값 지정

#폰트 생성과 출력할 문자열 지정
font = pygame.font.SysFont('Arial',20)
outstr = 'Hello, pygame!'

while not done: #메인루프
    for event in pygame.event.get(): #이벤트를 받아 처리
        if event.type == pygame.QUIT: #윈도 종료 버튼을 누르면
            done = True #프로그램 종료를 위해 true지정

    screen.fill(White) #스크린 색상을 휜색으로 지정

    text = font.render(outstr,True,blue) #지정된 문자열 글씨를 그린 화면을 반환해 text에 저장

    screen.blit(text,[100,80]) #글씨가 그려진 화면인 text를 윈도 스크린 위치 [x,y]에 그리기




    pygame.display.update() #화면의 필요한 부분만을 수정

pygame.quit() #메인루프를 빠져나오면 프로그램 종료

