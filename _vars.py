import tkinter as tk


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Screen:
    def __init__(self):
        self.root = tk.Tk()
        self.size = Vector2(500, 500)
        self.zoom = 1
        self.canvas = tk.Canvas(self.root, width=self.size.x, height=self.size.y, bg="lightblue")

    def reset(self):
        self.root.geometry(str(self.size.x) + "x" + str(self.size.y))
        self.canvas.destroy()
        self.canvas = tk.Canvas(self.root, width=self.size.x, height=self.size.y, bg="lightblue")
        self.canvas.place(x=-1.5, y=0, anchor="nw")

def get_player_colour(index):
    if index == 0:
        return "red"
    if index == 1:
        return "blue"
    if index == 2:
        return "orange"
    if index == 3:
        return "magenta"
    if index == 4:
        return "cyan"
    if index == 5:
        return "white"

class Player:
    def __init__(self, index = 0, pos = Vector2(150, 225)):
        self.index = index
        self.colour = get_player_colour(index)
        self.pos = pos
        self.scale = 10
        self.jump_power = 0.5
        self.gravity_power = 0.002
        self.move_speed = 0.15
        self.friction = 0.1
        self.infinite_jumps = False
        self.can_jump = False
        self.velocity = Vector2(0, 0)
        self.prev_pos = Vector2(150, 225)
        self.moving = {"right": False, "left": False, "down": False, "up": False}
        self.blocked = {"right": False, "left": False, "down": False, "up": False}
        self.blocking_object = {"right": None, "left": None, "down": None, "up": None}
        self.eye_offset = 4

    def block(self, direction, state, obj = None):
        if direction != "all":
            self.blocked[direction] = state
            if state:
                self.blocking_object[direction] = obj
            else:
                self.blocking_object[direction] = None
        else:
            self.blocked = {"right": state, "left": state, "down": state, "up": state}
            if state:
                self.blocking_object = {"right": obj, "left": obj, "down": obj, "up": obj}
            else:
                self.blocking_object = {"right": None, "left": None, "down": None, "up": None}

    def set_direction(self, e, direction, state):
        if direction == "left":
            self.moving["left"] = state
        elif direction == "right":
            self.moving["right"] = state
    def jump(self, e):
        if self.can_jump or self.infinite_jumps:
            self.velocity.y = 0
            self.velocity.y -= self.jump_power
            self.can_jump = False
    def gravity(self):
        if not self.blocked["down"]:
            self.velocity.y += self.gravity_power
    def move(self):
        friction = 0
        if self.blocked["down"]:
            friction = self.friction
        if self.moving["left"] and not self.blocked["left"]:
            self.pos.x -= self.move_speed - (self.move_speed * friction)
        if self.moving["right"] and not self.blocked["right"]:
            self.pos.x += self.move_speed - (self.move_speed * friction)

class Object:
    def __init__(self, size, scale, direction = Vector2(0,0)):
        self.pos = size
        self.scale = scale
        self.friction = 1
        self.stickiness = 0
        self.colour = "green"
        self.solid = True
        self.restrict = [1,1,1,1]
        self.blocked = {"right": False, "left": False, "down": False, "up": False}
        self.moving = False
        self.direction = direction
        self.speed = 1
        self.point1 = Vector2(self.pos.x, self.pos.y)
        self.point2 = Vector2(self.pos.x + self.direction.x, self.pos.y + self.direction.y)
        self.point = 1

    def move(self):
        factor = int(max(abs(self.direction.x), abs(self.direction.y))) * 8
        step = Vector2(self.direction.x / factor, self.direction.y / factor)
        self.pos.x += step.x
        self.pos.y += step.y

        for i in range(len(player)):
            if player[i].blocking_object["down"] == self:
                player[i].pos.x += step.x
                player[i].pos.y += step.y

        if self.point == 1:
            if self.pos.x >= self.point1.x:
                self.direction.x = -self.direction.x
                self.point = 2
            if self.pos.y >= self.point1.y:
                self.direction.y = -self.direction.y
                self.point = 2
        if self.point == 2:
            if self.pos.x <= self.point2.x:
                self.direction.x = -self.direction.x
                self.point = 1
            if self.pos.y <= self.point2.y:
                self.direction.y = -self.direction.y
                self.point = 1

objects = []
screen = Screen()
player = []
