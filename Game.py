import pymunk
import pyglet
from pymunk.pyglet_util import DrawOptions
from pyglet.window import key, mouse

options = DrawOptions()

window = pyglet.window.Window(1280, 720, "Game", resizable = False)

space = pymunk.Space()
body = pymunk.Body(1, 100)
ball_body = pymunk.Body(1, 100)
ball_body.position = 640, 360
ball = pymunk.Circle(ball_body, 10, offset = (0, 0))
ball.position = 640, 360
body.elasticity = 0.99
ball.elasticity = 0.99

player = pymunk.Poly.create_box(body, size=(250, 5))
player.elasticity = 0.99
player.position = 640, 15
body.position = 640, 15

space.add(player, body, ball)

left_pressed = False
right_pressed = False

@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)

def refresh(time):
    global left_pressed, right_pressed
    space.step(time)
    if left_pressed == True and right_pressed == False:
        x, y = player.position
        if x > 125:
            player.position = x - 5, y
            x,y = body.position
            body.position = x - 5, y
    elif right_pressed == True and left_pressed == False:
        x, y = player.position
        if x < 1155:
            player.position = x + 5, y
            x,y = body.position
            body.position = x + 5, y

@window.event
def on_key_press(symbol, modifiers):
    global left_pressed, right_pressed
    if symbol == key.A or symbol == key.LEFT:
        left_pressed = True
        right_pressed = False
        x, y = player.position
        if x > 125:
            player.position = x - 5, y
            x,y = body.position
            body.position = x - 5, y
    elif symbol == key.D or symbol == key.RIGHT:
        left_pressed = False
        right_pressed = True
        x, y = player.position
        if x < 1155:
            player.position = x + 5, y
            x,y = body.position
            body.position = x + 5, y

@window.event
def on_key_release(symbol, modifiers):
    global left_pressed, right_pressed
    if symbol == key.A or symbol == key.LEFT:
        left_pressed = False
    if symbol == key.D or symbol == key.RIGHT:
        right_pressed = False
    
if __name__ == "__main__":
    pyglet.clock.schedule_interval(refresh, 1.0/60.0)
    pyglet.app.run()