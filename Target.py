import pymunk
import random
all_boxes = []

x_value = 0
y_value = 450

for i in range(1, 20):
    exec("body%s = pymunk.Body(1, 100, pymunk.Body.KINEMATIC)" % i)
    exec("all_boxes.append(body%s)" % i)
    box_size = random.randint(50, 100)
    if x_value < 1160:
        exec("box%s = pymunk.Poly.create_box(body%s, size = (box_size, 50))" %(i, i))
        x_value += 5
        x_value += box_size/2
        exec("body%s.position = x_value, y_value" % i)
        x_value += box_size/2
        exec("body%s.elasticity, box%s.elasticity = 0.99, 0.99" % (i, i))
        exec("body%s.friction, box%s.friction = 0, 0" % (i, i))
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
        break



