import pymunk
import random
all_boxes = []

RED = (220,20,30)
GREEN = (0,205,0)
YELLOW = (238,238,0)

x_value = 0
y_value = 450

for i in range(1, 60):
    exec("body%s = pymunk.Body(1, 100, pymunk.Body.KINEMATIC)" % i)
    exec("all_boxes.append(body%s)" % i)
    box_size = random.randint(50, 100)
    if y_value == 450:
        color = GREEN
    elif y_value == 505:
        color = YELLOW
    else:
        color = RED
    if x_value < 1160:
        exec("box%s = pymunk.Poly.create_box(body%s, size = (box_size, 50))" %(i, i))
        x_value += 5
        x_value += box_size/2
        exec("body%s.position = x_value, y_value" % i)
        x_value += box_size/2
        exec("body%s.elasticity, box%s.elasticity = 0.99, 0.99" % (i, i))
        exec("body%s.friction, box%s.friction = 0, 0" % (i, i))
        exec("box%s.color = color" % i)
        exec("all_boxes.append(box%s)" % i)
    else:
        box_size = 1280 - 10 - x_value
        x_value += 5
        x_value += box_size/2
        exec("box%s = pymunk.Poly.create_box(body%s, size = (box_size, 50))" %(i, i))
        exec("body%s.position = x_value, y_value" % i)
        exec("body%s.elasticity, box%s.elasticity = 0.99, 0.99" % (i, i))
        exec("body%s.friction, box%s.friction = 0, 0" % (i, i))
        exec("all_boxes.append(box%s)" % i)
        exec("box%s.color = color" % i)
        x_value = 0
        y_value += 55
    if y_value > 560:
        break



