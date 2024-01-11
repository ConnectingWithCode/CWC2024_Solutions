import play

play.new_image("christmas_background.png")

PENGUIN = 0
POLARBEAR = 1
SEAL = 2

row0 = []
row1 = []
row2 = []


def stamp(obj_type, x_location, y_location):
    if obj_type == PENGUIN:
        obj = play.new_image("penguin.png", size=18, x=x_location, y=y_location)
        obj.has_x = False
        row0.append(obj)
    if obj_type == POLARBEAR:
        obj = play.new_image("polarbear.png", size=16, x=x_location, y=y_location)
        obj.has_x = False
        row1.append(obj)
    if obj_type == SEAL:
        obj = play.new_image("seal.png", size=13, x=x_location, y=y_location)
        obj.has_x = False
        row2.append(obj)
    obj.is_clicked


def stamp_row(obj_type, y_location, quantity):
    spacing = 100
    x = -spacing * ((quantity - 1) / 2)
    for _ in range(quantity):
        stamp(obj_type, x, y_location)
        x += spacing



stamp_row(PENGUIN, -100, 3)
stamp_row(POLARBEAR, 0, 4)
stamp_row(SEAL, 100, 5)


def update_images():
    for sprite in row0:
        if sprite.has_x:
            sprite.image = "penguinX.png"
        else:
            sprite.image = "penguin.png"
    for sprite in row1:
        if sprite.has_x:
            sprite.image = "polarbearX.png"
        else:
            sprite.image = "polarbear.png"
    for sprite in row2:
        if sprite.has_x:
            sprite.image = "sealX.png"
        else:
            sprite.image = "seal.png"

# Testing
row0[0].has_x = True
row1[1].has_x = True
row2[2].has_x = True

# Testing
update_images()


@play.repeat_forever
def forever_loop():
    if play.mouse.is_clicked:
        for penguin in row0:
            if penguin.is_clicked:
                penguin.has_x = not penguin.has_x

        for penguin in row1:
            if penguin.is_clicked:
                penguin.has_x = not penguin.has_x

        for penguin in row2:
            if penguin.is_clicked:
                penguin.has_x = not penguin.has_x

    update_images()


play.start_program()
