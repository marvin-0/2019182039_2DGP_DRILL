from pico2d import *

open_canvas()

run_ani = load_image('run_sprite.png')
sword_attack_ani = load_image('sword_atk_sprite.png')
punch_attack_ani = load_image('punch_atk_sprite.png')

def run_anime(run_frame, run_x):
    run_frame = run_frame % 10 + 1
    run_ani.clip_draw(run_frame * 34, 0, 34, 35, run_x, 300, 100, 100)
    pass

def sword_attack_anime(sword_frame):
    sword_frame = sword_frame % 11
    sword_attack_ani.clip_draw(sword_frame * 71, 0, 71, 60, 150, 120, 200, 200)
    pass

def punch_attack_anime(punch_frame):
    punch_frame = punch_frame % 9
    punch_attack_ani.clip_draw(punch_frame * 43, 0, 43, 40, 600, 120, 120, 120)
    pass


x = 50
frame = 0

while(x < 700):
    clear_canvas()
    run_anime(frame, x)
    sword_attack_anime(frame)
    punch_attack_anime(frame)
    update_canvas()
    delay(0.1)
    frame += 1
    x += 5
    get_events()


close_canvas()
