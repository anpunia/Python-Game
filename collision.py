from _vars import *


def check_bounds(obj, position, area):
    if not obj.pos.y - obj.scale.y - area < position.y:
        return False
    if not obj.pos.y + obj.scale.y + area > position.y:
        return False
    if not obj.pos.x - obj.scale.x - area < position.x:
        return False
    if not obj.pos.x + obj.scale.x + area > position.x:
        return False
    return True


def check_collision(player):
    player.block("all", False)

    player.can_jump = False

    for obj in objects:
        player_pos = Vector2(player.pos.x, player.pos.y)
        if check_bounds(obj, player_pos, player.scale + 50):
            cut = False
            ray_pos = Vector2(player.prev_pos.x, player.prev_pos.y)
            direction = Vector2(player.pos.x - player.prev_pos.x, player.pos.y - player.prev_pos.y)

            factor = int(max(abs(direction.x), abs(direction.y))) + 1

            for _ in range(factor):
                if cut:
                    continue
                ray_pos.x += direction.x / factor
                ray_pos.y += direction.y / factor
                if check_bounds(obj, ray_pos, player.scale):
                    cut = True
                    prev_pos = Vector2(player.prev_pos.x, player.prev_pos.y)
                    if not check_bounds(obj, prev_pos, player.scale):
                        player.pos.x = ray_pos.x
                        player.pos.y = ray_pos.y
                    obj.blocked["down"] = (abs(player.pos.y - (obj.pos.y - obj.scale.y - player.scale)) <= obj.restrict[0])
                    obj.blocked["up"] = (abs(player.pos.y - (obj.pos.y + obj.scale.y + player.scale)) <= obj.restrict[1])
                    obj.blocked["left"] = (abs(player.pos.x - (obj.pos.x + obj.scale.x + player.scale)) <= obj.restrict[2])
                    obj.blocked["right"] = (abs(player.pos.x - (obj.pos.x - obj.scale.x - player.scale)) <= obj.restrict[3])
                else:
                    obj.blocked["down"] = obj.blocked["up"] = obj.blocked["left"] = obj.blocked["right"] = False
            if obj.blocked["down"]:
                player.pos.y = obj.pos.y - obj.scale.y - player.scale + 0.0001
                player.block("down", True, obj)
                player.can_jump = True
            else:
                obj.player_on = False
            if obj.blocked["up"]:
                player.pos.y = obj.pos.y + obj.scale.y + player.scale
                player.block("up", True, obj)
            if obj.blocked["left"]:
                player.pos.x = obj.pos.x + obj.scale.x + player.scale
                player.block("left", True, obj)
            if obj.blocked["right"]:
                player.pos.x = obj.pos.x - obj.scale.x - player.scale
                player.block("right", True, obj)