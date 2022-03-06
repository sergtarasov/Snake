# подключение модулей
import pygame
from random import randrange
# константы
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGTH = (300, 300)
OBJECT_SIZE = 10
# переменные и инициализация
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
x = randrange(0, WINDOW_WIDTH, OBJECT_SIZE)
y = randrange(0, WINDOW_HEIGTH, OBJECT_SIZE)
body_snake = [(x, y)]
length_snake = 1
# цикл программы
while True:
  # показ экрана и закрска его в черный цвет
  screen.fill(pygame.Color('black'))
  # Отрисовка змеки
  for i, j in body_snake:
    pygame.draw.rect(screen, pygame.Color('green'), (i, j, OBJECT_SIZE, OBJECT_SIZE))
    if x < 0 or x > WINDOW_WIDTH or y < 0 or y > WINDOW_HEIGTH:
      break
  
  # условие закрытия программы
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
      # обновление экрана
  pygame.display.flip()
 
