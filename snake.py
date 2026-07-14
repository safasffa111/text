import random
import sys
import pygame

# 游戏参数
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
FPS = 10

# 颜色
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


def random_food_position(snake):
    """生成不与蛇身重叠的食物坐标"""
    while True:
        x = random.randrange(0, WIDTH, GRID_SIZE)
        y = random.randrange(0, HEIGHT, GRID_SIZE)
        if (x, y) not in snake:
            return x, y


def draw_grid(screen):
    """可选：绘制网格线，方便观察"""
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("贪吃蛇")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("SimHei", 24)

    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (GRID_SIZE, 0)  # 初始向右
    food = random_food_position(snake)
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                    direction = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                    direction = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                    direction = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                    direction = (GRID_SIZE, 0)
                elif event.key == pygame.K_ESCAPE:
                    running = False

        # 移动蛇
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)

        # 撞墙或撞自己 -> 游戏结束
        if (
            new_head[0] < 0
            or new_head[0] >= WIDTH
            or new_head[1] < 0
            or new_head[1] >= HEIGHT
            or new_head in snake
        ):
            break

        snake.insert(0, new_head)

        # 吃到食物
        if new_head == food:
            score += 1
            food = random_food_position(snake)
        else:
            snake.pop()

        # 绘制
        screen.fill(BLACK)
        draw_grid(screen)

        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

        pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))

        score_text = font.render(f"分数: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    # 游戏结束画面
    game_over = font.render(f"游戏结束！最终分数: {score}", True, WHITE)
    screen.fill(BLACK)
    screen.blit(game_over, (WIDTH // 2 - game_over.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
