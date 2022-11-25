import pygame

BlACK = (0, 0, 0)
dis_width = 600
dis_height = 503
char_width = 80
char_height = 75

#이미지 나타내기
def drawObject(obj, x, y):
    global gameDisplay
    gameDisplay.blit(obj, (x,y))
#게임 실행
def runGame():
    global gameDisplay, clock, map, character

    onGame = False
    dis_x = 0
    dis_y = 0
    dis_move = False
    dis_x_move = 0
    dis_y_move = 0
    x_move = 0
    y_move = 0
    x = int(dis_width*0.45)
    y = int(dis_height*0.9)

    
    while not onGame:
        #버튼 이벤트
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if dis_move:
                        dis_x_move += 5
                    x_move -= 5
                elif event.key == pygame.K_RIGHT:
                    if dis_move:
                        dis_x_move -= 5
                    x_move += 5
                elif event.key == pygame.K_UP:
                    y_move -= 5
                elif event.key == pygame.K_DOWN:
                    y_move += 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0

        #캐릭 움직임 조절
        x += x_move
        if x < 0:
            x = 0
        elif x > dis_width - char_width:
            x = dis_width - char_width
            dis_move = True
        elif x < dis_width - char_width:
            dis_move = False

        y += y_move
        if y < 0:
            y = 0
        elif y > dis_height - char_height:
            y = dis_height - char_height

        #배경 움직임 조절
        dis_x += dis_x_move
        if dis_x > 0:
            dis_x = 0
        elif dis_x < -585:
            dis_x = -585

        if dis_y > 0:
            dis_y = 0
        elif dis_y < -500:
            dis_y = -500

        #그리는 함수에 이동
        drawObject(map,dis_x, dis_y)
        drawObject(character,x,y)


        pygame.display.update()
        clock.tick(60)

def initGame():
    global gameDisplay, clock, map, character

    pygame.init()
    gameDisplay = pygame.display.set_mode((dis_width,dis_height))
    pygame.display.set_caption('今ここに')
    clock = pygame.time.Clock()
    map = pygame.image.load('map.jpg')
    character = pygame.image.load('character.png')

initGame()
runGame()