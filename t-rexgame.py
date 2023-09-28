# import các thứ
import pygame as pg
import sys
pg.init()

screen = pg.display.set_mode((960, 540))
pg.display.set_caption("T-REX")
screen.fill(pg.Color("white"))
bg = pg.image.load("images/background.jpg")
bg = pg.transform.scale(bg, (960, 540))
player = pg.image.load("images/playerR.png")
player = pg.transform.scale(player, (70, 170))
tree = pg.image.load("images/pipe-green.png")
tree = pg.transform.scale(tree, (50, 85))

clock = pg.time.Clock()
bg2 = pg.image.load("images/floor.png")
bg2 = pg.transform.scale(bg2, (960, 120))
bg2_x_pos = 0

bg_x, bg_y = 0, 0
bg_x2, bg_y2 = 0, 423
tree_x, tree_y = 900, 340
dino_x, dino_y = 50, 270
x_def = 5
y_def = 6
jump = False
gameplay = True
running = True
#ham check diem so
score=0
hscore=0
game_font=pg.font.Font('04B_19.TTF',20)
def score_view():
    global hscore
    if gameplay:
        score_txt=game_font.render(f'Score: {int(score)}',True,(255,0,0))
        screen.blit(score_txt,(250, 50))
        if hscore>=score:
            hscore=hscore
        else:
            hscore=score
        score_txt=game_font.render(f'hscore: {int(hscore)}',True,(255,0,0))
        screen.blit(score_txt,(450, 50))
    else:
        score_txt=game_font.render(f'Score: {int(score)}',True,(255,0,0))
        screen.blit(score_txt,(250, 50))

#xu ly va cham
def checkvc():
    if dino_hcn.colliderect(tree_hcn):
        return False
    return True
# nhan doi background


def draw_bg2():
    screen.blit(bg2, (bg2_x_pos, bg_y2))
    screen.blit(bg2, (bg2_x_pos+960, bg_y2))

# vong lap


while running:
    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and gameplay:
                if dino_y == 270:
                    jump = True
            if event.key == pg.K_SPACE and gameplay == False:
                gameplay = True
    


    if gameplay:
        # bg
        bg_hcn = screen.blit(bg, (bg_x, bg_y))
        # player
        dino_hcn = screen.blit(player, (dino_x, dino_y))
        # tree
        tree_hcn = screen.blit(tree, (tree_x, tree_y))
        tree_x -= x_def
        if tree_x == -20:
            tree_x = 900
        if dino_y >= 60 and jump:
            dino_y -= y_def
        else:
            jump = False
        if dino_y < 270 and jump == False:
            dino_y += y_def
        score+=0.01
        if hscore<score: hsocre=score
        gameplay=checkvc()
        score_view()

    else:
        bg_x, bg_y = 0, 0
        bg_x2, bg_y2 = 0, 423
        tree_x, tree_y = 900, 340
        dino_x, dino_y = 50, 270
        bg_hcn = screen.blit(bg, (bg_x, bg_y))
        dino_hcn = screen.blit(player, (dino_x, dino_y))
        tree_hcn = screen.blit(tree, (tree_x, tree_y))
        score=0

        f="baka :))"
        text=f.encode("utf-8").decode("utf-8")
        font=pg.font.Font(None,100)
        txt=font.render(text,True,(255,20,20))
        screen.blit(txt,(150, 250))
        score_view()
    #nen di chuyen
    bg2_x_pos -= 1
    draw_bg2()
    if bg2_x_pos <= -432:
        bg2_x_pos = 0
    
        # Cập nhật màn hình
    pg.display.update()
    clock.tick(80)
