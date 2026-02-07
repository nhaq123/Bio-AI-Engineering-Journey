def turn_right():
    move_left()
    move_left()
    move_left()


while front is clear:
    move()
turn_left()


while not at_goal():
    if front is clear:
        move()
    elif right is clear:
        turn_right()
        move()
    else:
        turn_left()
        move()


