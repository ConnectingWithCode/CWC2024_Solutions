import play
import random

game = play.new_image("background.png", size=84)
game.counter = 0
game.game_over = False

play.new_text("Linear Lights Out",
              y=200,
              font_size=100,
              color='yellow')

### Reminder for 11/16 - change yellow, maybe update start game to be random presses

message = play.new_text("Turn all of the lights off!",
                        y=100,
                        font_size=50,
                        color='yellow')

light_list = []
light_images = ["light_off.png", "light_on.png"]

# Creates the seven light sprites
for k in range(7):
    light = play.new_image(light_images[0],
                           x=-300 + k * 100,
                           y=0,
                           size=50)
    light.is_on = False
    light.num = k
    light_list.append(light)


def reset_game():
    game.counter = 0
    game.game_over = False
    message.words = "Turn all of the lights off!"
    for k in range(7):
        if random.random() < 0.5:
            light_list[k].image = light_images[0]
            light_list[k].is_on = False
        else:
            light_list[k].image = light_images[1]
            light_list[k].is_on = True

reset_game()

@play.repeat_forever
async def control_lights():
    if game.game_over:
        message.words = f"You won in {game.counter} moves!"
        if game.counter == 1:
            message.words = f"You won in {game.counter} move!"
        message.show()
        await play.timer(seconds=5)
        reset_game()
        return
    for light in light_list:
        if play.mouse.is_clicked:
            if play.mouse.is_touching(light):
                if light.num == 0:
                    toggle_light(light_list[light.num])
                    toggle_light(light_list[light.num + 1])
                    game.counter += 1
                elif light.num == 6:
                    toggle_light(light_list[light.num - 1])
                    toggle_light(light_list[light.num])
                    game.counter += 1
                else:
                    toggle_light(light_list[light.num - 1])
                    toggle_light(light_list[light.num])
                    toggle_light(light_list[light.num + 1])
                    game.counter += 1
                message.words = f"Moves: {game.counter}"
                await play.timer(seconds=0.25)


    off_counter = 0
    for light in light_list:
        if not light.is_on:
            off_counter += 1

    if off_counter == len(light_list):
        game.game_over = True


def toggle_light(light):
    if light.is_on:
        light.image = light_images[0]
        light.is_on = False
    else:
        light.image = light_images[1]
        light.is_on = True


play.start_program()

