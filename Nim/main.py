import play
import random


play.new_image("christmas_background.png")

# 1/11: we just created a randomized player button - it has no functionality yet
# @player_button.when_clicked

if random.randint(1,2) == 1:
    player_button = play.new_image("P1Button.png", size=80, x=-275, y=-240)
else:
    player_button = play.new_image("P2Button.png", size=80, x=275, y=-240)

PENGUIN = 0
POLARBEAR = 1
SEAL = 2

images = [[], [], []]


def place_image(obj_type, x_location, y_location):
    if obj_type == PENGUIN:
        obj = play.new_image("penguin.png", size=18, x=x_location, y=y_location)
    if obj_type == POLARBEAR:
        obj = play.new_image("polarbear.png", size=16, x=x_location, y=y_location)
    if obj_type == SEAL:
        obj = play.new_image("seal.png", size=13, x=x_location, y=y_location)
    obj.has_x = False
    images[obj_type].append(obj)


def place_row_of_images(obj_type, y_location, quantity):
    spacing = 100
    x = -spacing * ((quantity - 1) / 2)
    for _ in range(quantity):
        place_image(obj_type, x, y_location)
        x += spacing


place_row_of_images(PENGUIN, -100, random.randint(3,8))
place_row_of_images(POLARBEAR, 0, random.randint(3,8))
place_row_of_images(SEAL, 100, random.randint(3,8))


def update_images():
    for sprite in images[PENGUIN]:
        if sprite.has_x:
            sprite.image = "penguinX.png"
        else:
            sprite.image = "penguin.png"
    for sprite in images[POLARBEAR]:
        if sprite.has_x:
            sprite.image = "polarbearX.png"
        else:
            sprite.image = "polarbear.png"
    for sprite in images[SEAL]:
        if sprite.has_x:
            sprite.image = "sealX.png"
        else:
            sprite.image = "seal.png"



@play.repeat_forever
def forever_loop():
    if play.mouse.is_clicked:
        for k in range(3):
            for sprite in images[k]:
                if sprite.is_clicked:
                    sprite.has_x = not sprite.has_x
        update_images()


play.start_program()
