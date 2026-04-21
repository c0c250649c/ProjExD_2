import os
import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1100, 650
DELTA = {pg.K_UP: (0, -5),  # 練習問題01 / キーと移動量の辞書を作成
         pg.K_DOWN: (0, +5),
         pg.K_LEFT: (-5, 0),
         pg.K_RIGHT: (+5, 0)}
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def check_bound(rct: pg.Rect) -> tuple[bool, bool]:   # 練習問題03 / 画面内or画面外を判定
    """
    引数：Rect
    戻り値：真偽値タプル（横方向、縦方向）
    """
    x, y = True, True
    if rct.left < 0 or WIDTH < rct.right:
        x =  False
    if rct.top < 0 or HEIGHT < rct.bottom:
        y = False
    return (x, y)

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200

    bb_img = pg.Surface((20, 20))   # 練習問題02 / 爆弾を描画
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)
    bb_img.set_colorkey((0, 0, 0))
    bb_rct = bb_img.get_rect()
    bb_rct.center = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    vx, vy = +5, +5

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]

        for k, mv in DELTA.items(): # 練習問題01 / 移動量を加算
            if key_lst[k]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]

        kk_rct.move_ip(sum_mv)
        screen.blit(kk_img, kk_rct)

        if check_bound(kk_rct) != (True, True):   # 練習問題03 / 画面外に出たら元に戻す
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        
        screen.blit(bb_img, bb_rct) # 練習問題02 / 爆弾表示
        bb_rct.move_ip(vx, vy) 
        yoko , tate = check_bound(bb_rct)   # 練習問題03 / 爆弾が画面外に出たら跳ね返る
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1

        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
