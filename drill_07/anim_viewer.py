from pico2d import *

open_canvas()

run_ani = load_image('run_sprite.png')
sword_attack_ani = load_image('sword_atk_sprite.png')
punch_attack_ani = load_image('punch_atk_sprite.png')
exit_ani = load_image('exit_sprite.png')

def run_anime():
    x = 50
    frame = 0
    while(x < 401):
        clear_canvas()
        run_ani.clip_draw(frame * 34, 0, 34, 35, x, 300, 100, 100)
        frame = frame % 10 + 1
        x += 10
        update_canvas()
        delay(0.05)
    pass

def sword_attack_anime():
    for frame in range(0, 11):
        clear_canvas()
        sword_attack_ani.clip_draw(frame * 71, 0, 71, 60, 420, 340, 200, 190)
        update_canvas()
        delay(0.1)
    pass

def punch_attack_anime():
    for frame in range(0, 9):
        clear_canvas()
        punch_attack_ani.clip_draw(frame * 43, 0, 43, 40, 410, 310, 130, 130)
        update_canvas()
        delay(0.1)
    pass

def exit_anime():
    for frame in range(0, 12):
        clear_canvas()
        exit_ani.clip_draw(frame * 30, 0, 30, 48, 395, 320, 100, 150)
        update_canvas()
        delay(0.1)
    pass


run_anime()
sword_attack_anime()
punch_attack_anime()
exit_anime()





close_canvas()
