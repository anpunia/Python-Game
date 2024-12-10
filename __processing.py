from rendering import *
from collision import *
from velocity import *
from settings import *
import time

dt = 0
lt = time.time()


def start():
    screen.reset()
    player.append(Player(0, Vector2(70, 225)))
    player.append(Player(1, Vector2(90, 225)))
    player.append(Player(2, Vector2(110, 225)))
    player.append(Player(3, Vector2(130, 225)))
    add_settings(tk, screen)

    screen.root.bind("<a>", lambda e: player[0].set_direction(e, "left", True))
    screen.root.bind("<KeyRelease-a>", lambda e: player[0].set_direction(e, "left", False))
    screen.root.bind("<d>", lambda e: player[0].set_direction(e, "right", True))
    screen.root.bind("<KeyRelease-d>", lambda e: player[0].set_direction(e, "right", False))
    screen.root.bind("<w>", lambda e: player[0].jump(e))

    screen.root.bind("<Left>", lambda e: player[1].set_direction(e, "left", True))
    screen.root.bind("<KeyRelease-Left>", lambda e: player[1].set_direction(e, "left", False))
    screen.root.bind("<Right>", lambda e: player[1].set_direction(e, "right", True))
    screen.root.bind("<KeyRelease-Right>", lambda e: player[1].set_direction(e, "right", False))
    screen.root.bind("<Up>", lambda e: player[1].jump(e))

    screen.root.bind("<f>", lambda e: player[2].set_direction(e, "left", True))
    screen.root.bind("<KeyRelease-f>", lambda e: player[2].set_direction(e, "left", False))
    screen.root.bind("<h>", lambda e: player[2].set_direction(e, "right", True))
    screen.root.bind("<KeyRelease-h>", lambda e: player[2].set_direction(e, "right", False))
    screen.root.bind("<t>", lambda e: player[2].jump(e))

    screen.root.bind("<j>", lambda e: player[3].set_direction(e, "left", True))
    screen.root.bind("<KeyRelease-j>", lambda e: player[3].set_direction(e, "left", False))
    screen.root.bind("<l>", lambda e: player[3].set_direction(e, "right", True))
    screen.root.bind("<KeyRelease-l>", lambda e: player[3].set_direction(e, "right", False))
    screen.root.bind("<i>", lambda e: player[3].jump(e))

    x = Object(Vector2(220, 220), Vector2(50, 5), Vector2(0, -250))
    x.moving = True
    x.colour = "dim gray"
    objects.append(x)
    x = Object(Vector2(-110, 50 ), Vector2(50, 5), Vector2(-250, 0))
    x.direction = Vector2(-250, 0)
    x.moving = True
    x.colour = "dim gray"
    objects.append(x)

    x = Object(Vector2(-550, 50), Vector2(100, 5))
    objects.append(x)
    x = Object(Vector2(150, 400), Vector2(900, 5))
    objects.append(x)
    x = Object(Vector2(100, 350), Vector2(45, 5))
    objects.append(x)
    x = Object(Vector2(210, 375), Vector2(10, 5))
    x.restrict = [1, 0, 0, 0]
    x.colour = "darkgreen"
    objects.append(x)
    x = Object(Vector2(230, 325), Vector2(10, 5))
    x.restrict = [1, 0, 0, 0]
    x.colour = "darkgreen"
    objects.append(x)
    x = Object(Vector2(250, 275), Vector2(10, 5))
    x.restrict = [1, 0, 0, 0]
    x.colour = "darkgreen"
    objects.append(x)
    x = Object(Vector2(370, 250), Vector2(75, 5))
    objects.append(x)
    x = Object(Vector2(50, 50), Vector2(100, 5))
    objects.append(x)

    for i in range(10):
        x = Object(Vector2(550, (375 - (i*40))), Vector2(25, 5))
        x.restrict = [1, 0, 0, 0]
        x.colour = "darkgreen"
        objects.append(x)


def update(lt, player):
    ct = time.time()
    dt = (ct - lt) * 15000
    lt = ct

    ft = 1000 / 60
    at = 0

    at += dt

    while at >= ft:
        for i in range(len(player)):
            player[i].prev_pos.x, player[i].prev_pos.y, = player[i].pos.x, player[i].pos.y,
            player[i].gravity()
            player[i].move()
            calculate_velocity(player[i])
            check_collision(player[i])

        for obj in objects:
            if obj.moving:
                obj.move()
        at -= ft

    draw_objects(screen)
    coord_label.config(text = f"{int(player[0].pos.x)}, {int(player[0].pos.y)}")
    coord_label.lift()
    screen.root.after(16, lambda: update(lt, player))


start()
update(lt, player)
screen.root.mainloop()
