import play

print("Airplane")

play.new_image("background.png")

airplane = play.new_image("airplane.png", x=-350, y=-250, size=20)
airplane.score = 0
airplane.game_over = False

message = play.new_text("0", x=-325, y=275, color='yellow')

rocks = []
for k in range(10):
    rock = play.new_image("rocks.png", size=20)
    rock.go_to(play.random_position())
    rocks.append(rock)

scissors = []
for k in range(3):
    scissor = play.new_image("scissors.png", size=20)
    scissor.go_to(play.random_position())
    scissor.y = scissor.y + 300
    scissors.append(scissor)

@play.repeat_forever
def forever_loop():
    if airplane.game_over:
        message.words = "You Win!"
        return
    airplane.point_towards(play.mouse)
    airplane.move(5)

    for rock in rocks:
        if rock.is_touching(airplane):
            airplane.score = airplane.score + 1
            if airplane.score == 10:
                airplane.game_over = True
            rock.x = 2000
            rock.hide()
            message.words = airplane.score

    for scissor in scissors:
        scissor.point_towards(airplane)
        scissor.move(1)
        if scissor.is_touching(airplane):
            airplane.go_to(-400, -300)
            message.words = "Gotcha!"

play.start_program()
