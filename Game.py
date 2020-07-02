import pymunk
import pyglet
from pymunk.pyglet_util import DrawOptions
from pyglet.window import key, mouse
import math
import random
import Wall
import Target

speed = 10

options = DrawOptions()

window = pyglet.window.Window(1280, 720, "Game", resizable = False)

space = pymunk.Space()
space.gravity = 0, 0
body = pymunk.Body(1, 100, pymunk.Body.KINEMATIC)
ball_body = pymunk.Body(1, 100)
ball_body.position = 640, 360
ball = pymunk.Circle(ball_body, 10, offset = (0, 0))
body.position = 640, 360
ball.position = 640, 360
body.elasticity = 0.99
ball.elasticity = 0.99

width = 125

player = pymunk.Poly.create_box(body, size=(width, 5))
player.elasticity = 0.99
player.position = 640, 15
body.position = 640, 15

space.add(player, body, ball, ball_body)
space.add(Wall.wall1_body, Wall.right_wall, Wall.wall2_body, Wall.left_wall, Wall.wall3_body, Wall.top_wall)
for i in Target.all_boxes:
    space.add(i)

left_pressed = False
right_pressed = False
ball_body.position = player.position
power = 4.5
ball_body.angle = 0.0
ball_body.angle = random.uniform(math.pi/4, (math.pi * 3)/4)
ball_body.apply_force_at_local_point((1000 * power, 720), (1000 * power, 720))
count = 1

player.friction = 0
body.friction = 0
ball.friction = 0
ball_body.friction = 0

damp_level = 1

def zero_gravity(body, gravity, damping, dt):
    pymunk.Body.update_velocity(body, (0,0), damp_level, dt)

ball_body.velocity_func = zero_gravity

player.color = 0, 100, 200 

@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)

def refresh(time):
    global left_pressed, right_pressed, count, energy, damp_level
    space.step(time)
    if pymunk.SegmentQueryInfo != None:
        # print(ball.shapes_collide(Wall.top_wall).points) #length of the list returned will be 0 if there's no collision
        pass
    if count == 1:
        energy = ball_body.kinetic_energy
    damp_level = energy/ball_body.kinetic_energy
    count += 1
    if left_pressed == True and right_pressed == False:
        x, y = player.position
        if x > width/2:
            player.position = x - speed, y
            x,y = body.position
            body.position = x - speed, y
    elif right_pressed == True and left_pressed == False:
        x, y = player.position
        if x < 1280 - width/2:
            player.position = x + speed, y
            x,y = body.position
            body.position = x + speed, y

@window.event
def on_key_press(symbol, modifiers):
    global left_pressed, right_pressed
    if symbol == key.A or symbol == key.LEFT:
        left_pressed = True
        right_pressed = False
        x, y = player.position
        if x > width/2:
            player.position = x - speed, y
            x,y = body.position
            body.position = x - speed, y
    elif symbol == key.D or symbol == key.RIGHT:
        left_pressed = False
        right_pressed = True
        x, y = player.position
        if x < 1280 - width/2:
            player.position = x + speed, y
            x,y = body.position
            body.position = x + speed, y

@window.event
def on_key_release(symbol, modifiers):
    global left_pressed, right_pressed
    if symbol == key.A or symbol == key.LEFT:
        left_pressed = False
    if symbol == key.D or symbol == key.RIGHT:
        right_pressed = False
    
if __name__ == "__main__":
    pyglet.clock.schedule_interval(refresh, 1.0/120.0)
    pyglet.app.run()