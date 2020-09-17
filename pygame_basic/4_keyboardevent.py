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

#이동할 좌표
to_x = 0
to_y = 0

#이벤트 루프
running = True # 게임이 진행중인가를 확인하는 문장
while running:
  for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
    if event.type == pygame.QUIT: #창닫는 이벤트가 발생한 경우에
      running = False # 게임이 진행중이 아님

    if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
      if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
        to_x -= 5 # to_x = to_x - 5
      elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
        to_x += 5
      elif event.key == pygame.K_UP: #캐릭터를 위로
        to_y -= 5
      elif event.key == pygame.K_DOWN: #캐릭터를 아래로
        to_y += 5

    if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        to_x = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        to_y = 0
  
  character_x_pos += to_x # 캐릭터 좌표에 대입
  character_y_pos += to_y
  
  #캐릭터를 화면 가로 경계값 안으로 조정
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > (screen_width - character_width):
    character_x_pos = screen_width - character_width

  #캐릭터를 화면 세로 경계값 안으로 조정
  if character_y_pos < 0:
    character_y_pos = 0
  elif character_y_pos > screen_height - character_height:
    character_y_pos = screen_height - character_height
    

  screen.blit(background, (0,0)) # 배경 그리기

  screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
 
  pygame.display.update() # 반드시 게임화면을 다시 그리기!!!


# pygame 종료
pygame.quit()
