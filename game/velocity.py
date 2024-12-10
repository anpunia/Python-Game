def calculate_velocity(player):
    if player.velocity.y > 0:
        player.velocity.y -= 0.0001
        if player.blocked["down"]:
            player.velocity.y = 0
    if player.velocity.y < 0:
        player.velocity.y += 0.0001
        if player.blocked["up"]:
            player.velocity.y = 0
    if player.velocity.x < 0:
        player.velocity.x += 0.0001
        if player.blocked["right"]:
            player.velocity.x = 0
    if player.velocity.x > 0:
        player.velocity.x -= 0.0001
        if player.blocked["left"]:
            player.velocity.x = 0

    player.pos.x += player.velocity.x
    player.pos.y += player.velocity.y