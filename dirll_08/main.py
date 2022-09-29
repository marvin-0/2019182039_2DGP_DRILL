from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def handle_events():
    global standing
    global On
    global x_dir, y_dir
    global stand_dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
           On = False
        elif event.type == SDL_KEYDOWN:
            standing = False
            if event.key == SDLK_ESCAPE:
                On = False
            elif event.key == SDLK_RIGHT:
                x_dir += 1
                stand_dir = 1
            elif event.key == SDLK_LEFT:
                x_dir -= 1
                stand_dir = -1
            elif event.key == SDLK_UP:
                y_dir += 1
            elif event.key == SDLK_DOWN:
                y_dir -= 1

        elif event.type == SDL_KEYUP:
            standing = True
            if event.key == SDLK_RIGHT:
                x_dir -= 1
            elif event.key == SDLK_LEFT:
                x_dir += 1
            elif event.key == SDLK_UP:
                y_dir -= 1
            elif event.key == SDLK_DOWN:
                y_dir += 1
    pass

def map_in():
    global x, y
    global x_dir, y_dir
    global TUK_WIDTH, TUK_HEIGHT

    if x < 0:
        x -= x_dir * 5
    elif x > TUK_WIDTH:
        x -= x_dir * 5
    if y < 0:
        y -= y_dir * 5
    elif y > TUK_HEIGHT:
        y -= y_dir * 5
    pass

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

standing = True
On = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
x_dir, y_dir = 0, 0
stand_dir = 1
stand_frame = 0
run_frame = 0


while On:
    if standing:
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        if stand_dir == 1:
            character.clip_draw(stand_frame * 100, 100 * 3, 100, 100, x, y)
        elif stand_dir == -1:
            character.clip_draw(stand_frame * 100, 100 * 2, 100, 100, x, y)

        update_canvas()
        stand_frame = (stand_frame + 1) % 8
        delay(0.1)

    else:
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        if(stand_dir == 1):
            character.clip_draw(run_frame * 100, 100 * 1, 100, 100, x, y)
        elif(stand_dir == -1):
            character.clip_draw(run_frame * 100, 0, 100, 100, x, y)

        x += x_dir * 5
        y += y_dir * 5
        map_in()

        update_canvas()
        run_frame = (run_frame + 1) % 8
        delay(0.01)

    handle_events()

close_canvas()




