import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
FOOD_SIZE = SNAKE_SIZE = 20

# Цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Настройки экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Змейка')


# Функция для создания еды
def draw_food(x, y):
    pygame.draw.rect(screen, RED, [x, y, FOOD_SIZE, FOOD_SIZE])


# Класс змейки
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice(
            [(0, -1), (0, 1), (-1, 0), (1, 0)])  # Исправлено: теперь выбирается случайное направление
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * SNAKE_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * SNAKE_SIZE)) % SCREEN_HEIGHT)
        if new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice(
            [(0, -1), (0, 1), (-1, 0), (1, 0)])  # Повторное исправление для корректного старта

    def draw(self):
        for p in self.positions:
            pygame.draw.rect(screen, self.color, (p[0], p[1], SNAKE_SIZE, SNAKE_SIZE))

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.turn((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.turn((1, 0))


def main():
    clock = pygame.time.Clock()

    snake = Snake()
    food = (random.randint(0, (SCREEN_WIDTH - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE,
            random.randint(0, (SCREEN_HEIGHT - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE)

    while True:
        snake.handle_keys()
        snake.move()

        if snake.get_head_position() == food:
            snake.length += 1
            food = (random.randint(0, (SCREEN_WIDTH - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE,
                    random.randint(0, (SCREEN_HEIGHT - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE)

        screen.fill(BLACK)
        snake.draw()
        draw_food(food[0], food[1])

        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()