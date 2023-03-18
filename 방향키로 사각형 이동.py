import pygame
from pygame.locals import QUIT, KEYUP, KEYDOWN,\
K_LEFT,K_RIGHT,K_UP,K_DOWN


white = (255,255,255)
green = [0,255,0]

#화면에 사각형 그리고 초당 화면 프레임 수정
def paint(surface,x,y):
    #사각형그리기
    def drawrect(surface,x,y):
        sizex,sizey = 30,30
        pygame.draw.rect(surface,green,[x,y,sizex,sizey])
    
    surface.fill(white)
    drawrect(surface,x,y)
    pygame.display.update()
    #초당 화면 수정 프레임 수 지정
    clock.tick(60)

#시작: 초기화
pygame.init()
surface = pygame.display.set_mode([600,400])
pygame.display.set_caption("키보드 이벤트 처리")

#화면 수정 시간에 사용
clock = pygame.time.Clock()

#방향키에 따른 이동거 리와 첨자 관리
inc = (-2, 0, 2) #방향키에 따른 이동 거리
posx = 1 #위 값 중 하나의 첨자
posy = 1 #위 값 중 하나의 첨자

#사각형의 처음 위치
x,y = 270,170

#메인 루프
done = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        #키를 누르면
        elif event.type == KEYDOWN:
            key = event.key
            if key == K_LEFT:
                posx = 0
            elif key == K_RIGHT:
                posx = 2
            elif key == K_DOWN:
                posy = 2
            elif key == K_UP:
                posy = 0

        elif event.type == KEYUP:
            key = event.key
            #왼쪽 오른쪽 키면 x증가를 0으로
            if key ==K_LEFT or key == K_RIGHT:
                posx=1
            elif key == K_UP or key == K_DOWN:
                posy = 1

    x,y = x + inc[posx], y + inc[posy]           
    paint(surface,x,y)


pygame.quit()




