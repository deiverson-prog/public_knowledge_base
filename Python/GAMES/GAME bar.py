import pygame

pygame.init()
pygame.font.init()

display = pygame.display.set_mode((1280,720))

player1 = pygame.Rect(0,0,30,130)
player1_score = 0
player1_speed = 1

player2 = pygame.Rect(1250,0,30,130)
player2_score = 0
player2_speed = 1

ball = pygame.Rect(740,360,20,20)
ball_dir_x = 1
ball_dir_y = 1

font = pygame.font.Font(None, 50)
placar_player1 = font.render(str(player1_score), True, "yellow")
placar_player2 = font.render(str(player2_score), True, "yellow")

cena = "menu"

loop = True
while loop:

    if cena == "jogo":

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    player1_speed = -1
                elif event.key == pygame.K_a:
                    player1_speed = 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    player2_speed = -1
                elif event.key == pygame.K_l:
                    player2_speed = 1

        if player2_score >=7:
            cena = "gameover2"

        if player1_score >=7:
            cena = "gameover1"

        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_dir_x *= -1
            hit = pygame.mixer.Sound('BallHitWall.wav')
            hit.play()

        if player1.y <=0:
            player1.y = 0
        elif player1.y >= 720 - 130:
            player1.y = 720 - 130
        
        player1.y += player1_speed

        if ball.x <= 0:
            player2_score += 1
            placar_player2= font.render(str(player2_score), True, "yellow")
            ball.x = 500
            ball_dir_x *= -1
        elif ball.x >= 1280:
            player1_score += 1
            placar_player1 = font.render(str(player1_score), True, "yellow")
            ball.x = 500
            ball_dir_x *= -1

        if ball.y <= 0:
            ball_dir_y *= -1
        elif ball.y >= 720 - 15:
            ball_dir_y *= -1

        ball.x += ball_dir_x
        ball.y += ball_dir_y

        #player2.y = ball.y - 75
        player2.y += player2_speed

        if player2.y <= 0:
            player2.y = 0
        elif player2.y >= 720 - 130:
            player2.y = 720 - 130

        display.fill((0,0,0))
        pygame.draw.rect(display,"yellow", player1)
        pygame.draw.rect(display,"purple", player2)
        pygame.draw.circle(display,"gray", ball.center,10)
        display.blit(placar_player1, (500,50))
        display.blit(placar_player2, (780,50))

    elif cena == "gameover1":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = "menu"

        display.fill((0,0,0))
        text_win = font.render("Game over", True, "yellow")
        tex_win1 = font.render("O Player1 venceu!", True, "yellow")
        display.blit(text_win, [(565), 360])
        display.blit(tex_win1, [(500), 400])

    elif cena == "gameover2":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = "menu"

        display.fill((0,0,0))
        text_win = font.render("Game over", True, "purple")
        tex_win1 = font.render("O Player2 venceu!", True, "purple")
        display.blit(text_win, [(565), 360])
        display.blit(tex_win1, [(500), 400])

    elif cena == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player1_score = 0
                    placar_player1 = font.render(str(player1_score), True, "yellow")
                    player2_score = 0
                    placar_player2 = font.render(str(player2_score), True, "yellow")
                    player1.y = 0
                    player2.y = 0
                    ball.x = 640
                    ball.y = 320
                    cena = "jogo"

        display.fill((0,0,0))
        title = font.render("My game", True, "green")
        text = font.render("press start to play", True, "green")
        display.blit(title, [(565), 160])
        display.blit(text, [(492), 460])

    pygame.display.flip()