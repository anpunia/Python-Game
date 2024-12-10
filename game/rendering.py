from _vars import *

coord_label = tk.Label(screen.root, text=f"")
coord_label.pack(side=tk.TOP)

def draw_player(player, offset):
    screen.canvas.create_rectangle(
        (player.pos.x * screen.zoom) + offset.x - (player.scale * screen.zoom),
        (player.pos.y * screen.zoom) + offset.y - (player.scale * screen.zoom),
        (player.pos.x * screen.zoom) + offset.x + (player.scale * screen.zoom),
        (player.pos.y * screen.zoom) + offset.y + (player.scale * screen.zoom),
        fill=player.colour,
        width=0,
    )

    if player.moving["right"] and not player.moving["left"]:
        player.eye_offset = abs(player.eye_offset)
    elif player.moving["left"] and not player.moving["right"]:
        player.eye_offset = -abs(player.eye_offset)

    x = (player.scale / 10) * screen.zoom
    screen.canvas.create_rectangle(
        (player.pos.x * screen.zoom) + offset.x + (1.5 * x) + (player.eye_offset * x),
        (player.pos.y * screen.zoom) + offset.y - (6 * x),
        (player.pos.x * screen.zoom) + offset.x + (4.5 * x) + (player.eye_offset * x),
        (player.pos.y * screen.zoom) + offset.y + (0 * x),
        fill="black",
        width=0,
    )
    screen.canvas.create_rectangle(
        (player.pos.x * screen.zoom) + offset.x - (4.5 * x) + (player.eye_offset * x),
        (player.pos.y * screen.zoom) + offset.y  - (6 * x),
        (player.pos.x * screen.zoom) + offset.x  - (1.5 * x) + (player.eye_offset * x),
        (player.pos.y * screen.zoom) + offset.y  + (0 * x),
        fill="black",
        width=0,
    )

def draw_objects(screen):
    global player, player2

    offset = Vector2((screen.size.x / 2) - (player[0].pos.x * screen.zoom),
                     (screen.size.y / 2) - (player[0].pos.y * screen.zoom))
    screen.canvas.delete("all")

    for obj in objects:
        screen.canvas.create_rectangle(
            (obj.pos.x * screen.zoom) + offset.x - (obj.scale.x * screen.zoom),
            (obj.pos.y * screen.zoom) + offset.y - (obj.scale.y * screen.zoom),
            (obj.pos.x * screen.zoom) + offset.x + (obj.scale.x * screen.zoom),
            (obj.pos.y * screen.zoom) + offset.y + (obj.scale.y * screen.zoom),
            fill=obj.colour,
            width=0,
        )

    for i in range(len(player)):
        draw_player(player[i], offset)