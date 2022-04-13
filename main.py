import pygame

pygame.font.init()
pygame.display.set_caption("PONG")
SCORE_FONT = pygame.font.SysFont('comicsans', 40)
WIDTH = 900
HEIGHT = 600
P_WIDTH = 20
P_HEIGHT = 120
VEL = 9
FPS = 60
B_WIDTH = 20
B_HEIGHT = 20


def score(ball, p1_score, p2_score):
    if ball.x + B_WIDTH == WIDTH:
        p1_score += 1
        ball.x = WIDTH // 2 - B_WIDTH // 2
        ball.y = HEIGHT // 2 - B_HEIGHT // 2
    if ball.x == 0:
        p2_score += 1
        ball.x = WIDTH // 2 - B_WIDTH // 2
        ball.y = HEIGHT // 2 - B_HEIGHT // 2


def ball_movement(ball, B_VELx, B_VELy):
    ball.x += B_VELx * VEL
    ball.y += B_VELy * VEL


def movement(keys_pressed, player1, player2):
    if keys_pressed[pygame.K_w] and player1.y - VEL > 0:  # Up
        player1.y -= VEL
    if keys_pressed[pygame.K_s] and player1.y + VEL < HEIGHT - player1.height:  # Down
        player1.y += VEL

    if keys_pressed[pygame.K_UP] and player2.y - VEL > 0:  # Up
        player2.y -= VEL
    if keys_pressed[pygame.K_DOWN] and player2.y + VEL < HEIGHT - player2.height:  # Down
        player2.y += VEL


def draw(player1, player2, ball, p1_score, p2_score):
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (160, 160, 160), (player1.x, player1.y, P_WIDTH, P_HEIGHT))
    pygame.draw.rect(window, (160, 160, 160), (player2.x, player2.y, P_WIDTH, P_HEIGHT))
    pygame.draw.rect(window, (160, 160, 160), (ball.x, ball.y, B_WIDTH, B_HEIGHT))
    pygame.draw.line(window, (160, 160, 160), (WIDTH // 2 - 3 / 2, 0), (WIDTH // 2 - 3 / 2, HEIGHT), 3)
    p1score = SCORE_FONT.render("SCORE: " + str(p1_score), True, (160, 160, 160))
    p2score = SCORE_FONT.render("SCORE: " + str(p2_score), True, (160, 160, 160))
    window.blit(p2score, (WIDTH - p2score.get_width() - 10, 10))
    window.blit(p1score, (10, 10))

    pygame.display.update()


def main():
    player1 = pygame.Rect(0, HEIGHT // 2 - P_HEIGHT // 2, P_WIDTH, P_HEIGHT)
    player2 = pygame.Rect(WIDTH - P_WIDTH, HEIGHT // 2 - P_HEIGHT // 2, P_WIDTH, P_HEIGHT)
    ball = pygame.Rect(WIDTH // 2 - B_WIDTH // 2, HEIGHT // 2 - B_HEIGHT // 2, B_WIDTH, B_HEIGHT)
    b_vel_x = 1
    b_vel_y = 0
    p1_score = 0
    p2_score = 0

    run = True
    clock = pygame.time.Clock()
    while run:
        pygame.init()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        draw(player1, player2, ball, p1_score, p2_score)
        keys_pressed = pygame.key.get_pressed()
        movement(keys_pressed, player1, player2)
        ball_movement(ball, b_vel_x, b_vel_y)
        if (ball.x + B_WIDTH >= player2.x) and not (
                (ball.y + B_HEIGHT // 2 >= player2.y + P_HEIGHT) or (ball.y + B_HEIGHT // 2 <= player2.y)):
            b_vel_x = -1

        if (ball.x <= player1.x + P_WIDTH) and not (
                (ball.y + B_HEIGHT // 2 >= player1.y + P_HEIGHT) or (ball.y + B_HEIGHT // 2 <= player1.y)):
            b_vel_x = 1

        if (ball.x + B_WIDTH >= player2.x) and not (
                (ball.y + B_HEIGHT // 2 >= player2.y + P_HEIGHT) or (ball.y + B_HEIGHT // 2 <= player2.y)):
            y = ((ball.y + B_HEIGHT // 2) - player2.y) / P_HEIGHT
            if y == 0.5:
                b_vel_y = 0
            elif y > 0.5:
                b_vel_y = (y - 0.5) * 2
            else:
                b_vel_y = ((y * 2) - 1)
                
        if (ball.x <= player1.x + P_WIDTH) and not (
                (ball.y + B_HEIGHT // 2 >= player1.y + P_HEIGHT) or (ball.y + B_HEIGHT // 2 <= player1.y)):
            y = ((ball.y + B_HEIGHT // 2) - player1.y) / P_HEIGHT
            if y == 0.5:
                b_vel_y = 0
            elif y > 0.5:
                b_vel_y = (y - 0.5) * 2
            else:
                b_vel_y = ((y * 2) - 1)

        if ball.y <= 0:
            b_vel_y = -b_vel_y

        if ball.y + B_HEIGHT >= HEIGHT:
            b_vel_y = -b_vel_y

        if ball.x + B_WIDTH >= WIDTH:
            p1_score += 1
            ball.x = WIDTH // 2 - B_WIDTH // 2
            ball.y = HEIGHT // 2 - B_HEIGHT // 2
            b_vel_x = 1
            b_vel_y = 0

        if ball.x <= 0:
            p2_score += 1
            ball.x = WIDTH // 2 - B_WIDTH // 2
            ball.y = HEIGHT // 2 - B_HEIGHT // 2
            b_vel_x = -1
            b_vel_y = 0


if __name__ == "__main__":
    main()
