def turn_right():
  turn_left()
  turn_left()
  turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
       
#THIS CODE IS VALID IN THE WEBSITE "REEBORG'S WORLD" AND DIFFICULTY LEVEL IS "MAZE"
