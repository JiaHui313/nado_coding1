import pygame

pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("나도 게임") # 게임이름

# 배경이미지 불러오기
background = pygame.image.load("C:\\Users\\rkgpt\\OneDrive\\Desktop\\혼공파\\pygame_basic\\background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:\\Users\\rkgpt\\OneDrive\\Desktop\\혼공파\\pygame_basic\\character.png")
character_size = character.get_rect().size #캐릭터 크기 가져오기
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = (screen_width / 2 ) - (character_width/2) #좌우 위치 설정: 화면가로 사이즈의 절반
character_y_pos = screen_height - character_height # 세로크기 가장 아래에 위치(640)

#이벤트 루프
running = True # 게임이 진행중인가를 확인하는 문장
while running:
  for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
    if event.type == pygame.QUIT: #창닫는 이벤트가 발생한 경우에
      running = False # 게임이 진행중이 아님

  screen.blit(background, (0,0)) # 배경 그리기

  screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
 
  pygame.display.update() # 반드시 게임화면을 다시 그리기!!!


# pygame 종료
pygame.quit()
