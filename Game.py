import pymunk
import pyglet
from pymunk.pyglet_util import DrawOptions
from pyglet.window import key, mouse
import math
import random
import Wall
import Target
speed = 0
options = DrawOptions()

window = pyglet.window.Window(1280, 720, "Game", resizable = False)
window.set_mouse_visible(False)

space = pymunk.Space()
space.gravity = 0, 0
body = pymunk.Body(1, 100, pymunk.Body.KINEMATIC)
ball_body = pymunk.Body(1, 100)
ball = pymunk.Circle(ball_body, 10, offset = (0, 0))
body.position = 640, 360
ball.position = 640, -100
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

for i in Target.all_bodies:
    space.add(i)

left_pressed = False
right_pressed = False
ball_body.position = -100, 10
power = 35
ball_body.angle = 0.0

started = False
count = 1

player.friction = 0
body.friction = 0
ball.friction = 0
ball_body.friction = 0

damp_level = 1

label = pyglet.text.Label('Press Space to Begin', font_name='Times New Roman', font_size=36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')

def zero_gravity(body, gravity, damping, dt):
    pymunk.Body.update_velocity(body, (0,0), damp_level, dt)

ball_body.velocity_func = zero_gravity

player.color = 0, 100, 200 #dark blue

dead = False

has_won = False

target_velocity = 0, 0

@window.event
def on_draw():
    global label, speed
    window.clear()
    space.debug_draw(options)
    if started == False:
        label.draw()
    if dead == True:
        label = pyglet.text.Label('Game Over', font_name='Times New Roman', font_size=36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
        label.draw()
    if has_won == True:
        label = pyglet.text.Label('You Win!', font_name='Times New Roman', font_size=36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')
        label.draw()
        speed = 0

def refresh(time):
    global left_pressed, right_pressed, count, energy, damp_level, dead, speed, has_won, target_velocity, target_x, target_y
    space.step(time)
    if len(Target.all_boxes) == 0:
        ball_body.position = -1000, 150
        ball_body.velocity = 0, 0
        has_won = True
    ball_x, ball_y = ball_body.position
    if ball_y < 0:
        dead = True
        left_pressed = False
        right_pressed = False
        speed = 0
    if pymunk.SegmentQueryInfo != None:
        new_list = []
        for i in Target.all_boxes:
            if len(ball.shapes_collide(i).points) > 0: #length of the list returned will be 0 if there's no collision
                i.position = -1000, 0
                space.remove(i)
            else:
                new_list.append(i)
        Target.all_boxes = new_list
    if count == 1 and started == True:
        # energy = ball_body.kinetic_energy
        target_velocity = ball_body.velocity
        target_x, target_y = target_velocity
        count += 1
    if ball_body.kinetic_energy == 0:
        damp_level = 1
    else:
        # damp_level = energy/ball_body.kinetic_energy
        target_x, target_y = target_velocity
        current_x, current_y = ball_body.velocity
        current_velocity = math.sqrt(current_x ** 2 + current_y ** 2)
        damp_level = (math.sqrt(target_x ** 2 + target_y ** 2))/current_velocity
    
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
    global left_pressed, right_pressed, started, speed
    if dead == False:
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
        elif symbol == key.SPACE and started == False:
            ball_body.position = player.position
            ball_body.angle = random.uniform(math.pi/4, (math.pi * 3)/4)
            ball_body.apply_force_at_local_point((1000 * power, 1000), (1000 * power, 1000))
            started = True
            speed = 12

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