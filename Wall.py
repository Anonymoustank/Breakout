import pymunk

wall1_body = pymunk.Body(1, 100, pymunk.Body.KINEMATIC)
wall1_body.position = 1285, 360
right_wall = pymunk.Poly.create_box(wall1_body, size = (10, 720))
wall1_body.elasticity = 0.99
right_wall.elasticity = 0.99
wall1_body.friction = 0
right_wall.friction = 0

wall2_body = pymunk.Body(1, 100, pymunk.Body.KINEMATIC)
wall2_body.position = -5, 360
left_wall = pymunk.Poly.create_box(wall2_body, size = (10, 720))
wall2_body.elasticity = 0.99
left_wall.elasticity = 0.99
wall2_body.friction = 0
left_wall.friction = 0


wall3_body = pymunk.Body(1, 100, pymunk.Body.KINEMATIC)
wall3_body.position = 640, 725
top_wall = pymunk.Poly.create_box(wall3_body, size = (1280, 10))
wall3_body.elasticity = 0.99
top_wall.elasticity = 0.99
wall3_body.friction = 0
top_wall.friction = 0


