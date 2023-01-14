
import random
import pygame
from util import *


class Snake :
    def __init__(self) :
        self.movDirection = DIRECTIONS[random.randint(0, 3)]
        self.positions = [[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]]
    
    def draw(self, window) :
        for pos in self.positions :
            pygame.draw.rect(window, SNAKE_COLOR, pygame.Rect(pos[0] * TILE, pos[1] * TILE, SNAKE_LENGTH, SNAKE_LENGTH))

    def update(self) :
        pos_len = len(self.positions)
        if (pos_len == 1) :
            self.positions[0][0] = self.positions[0][0] + self.movDirection[0]
            self.positions[0][1] = self.positions[0][1] + self.movDirection[1]
            return

        for i in range(0, pos_len - 1) :
            self.positions[i][0] = self.positions[i + 1][0]
            self.positions[i][1] = self.positions[i + 1][1]

        self.positions[pos_len - 1][0] = self.positions[pos_len - 1][0] + self.movDirection[0]
        self.positions[pos_len - 1][1] = self.positions[pos_len - 1][1] + self.movDirection[1]


class Food :
    def __init__(self) :
        self.position = [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]

    def draw(self, window) :
        pygame.draw.rect(window, FOOD_COLOR, pygame.Rect(self.position[0] * TILE, self.position[1] * TILE, FOOD_LENGTH, FOOD_LENGTH))

    def update(self) :
        self.position = [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]
  

            
class SnakeGame :
    def __init__(self) :
        self.screen = pygame.display.set_mode((SCREEN_WIDTH * TILE, SCREEN_HEIGHT * TILE))
        pygame.display.set_caption("Snake Game")

        self.food = Food()
        self.snake = Snake()
        self.running = True

    def runloop(self) :
        while self.running :
            self.screen.fill(BACKGROUND_COLOR)
            self.food.draw(self.screen)
            self.snake.draw(self.screen)
            self.snake.update()
            self.checkCollison()

            pygame.display.flip()
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    self.running = False
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_LEFT :
                        self.snake.movDirection = LEFT
                    elif event.key == pygame.K_RIGHT :
                        self.snake.movDirection = RIGHT
                    elif event.key == pygame.K_UP :
                        self.snake.movDirection = UP
                    elif event.key == pygame.K_DOWN :
                        self.snake.movDirection = DOWN

            pygame.time.delay(DELAY)
        
    def checkCollison(self) :
        for pos in self.snake.positions :
            if pos == self.food.position :
                self.snake.positions.append([self.food.position[0] + self.snake.movDirection[0], self.food.position[1] + self.snake.movDirection[1]])
                self.food.update()

        pos_len = len(self.snake.positions)
        if   (self.snake.positions[pos_len - 1][0] < 0 or self.snake.positions[pos_len - 1][0] > (SCREEN_WIDTH  - 1)) : self.running = False
        elif (self.snake.positions[pos_len - 1][1] < 0 or self.snake.positions[pos_len - 1][1] > (SCREEN_HEIGHT - 1)) : self.running = False
        


if __name__ == "__main__" :
    pygame.init()
    
    snakeGame = SnakeGame()
    snakeGame.runloop()

    pygame.quit()
    quit()
