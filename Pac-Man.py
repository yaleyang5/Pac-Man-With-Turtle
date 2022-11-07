import turtle
import random

#_______________________ 1. DRAWING AND PREPARATION ______________________
#black screen + register Pac-Man shapes
screen = turtle.Screen()
screen.bgcolor("black")
screen.register_shape("Pac-Man", ((-9,-2), (-8,-4), (-7,-5), (-6.5,-6.5), (-5,-7), (-4,-8), (-2,-9), (0,-9.5), (2,-9), (4,-8), (5,-7),  (6.5,-6.5), (7,-5), (8,-4), (9,-2), (9.5,0), (9,2), (8,4), (7,5), (6.5,6.5), (0,-2.5), (-6.5,6.5), (-7,5), (-8,4), (-9,2), (-9.5,0)))
screen.register_shape("Pac-Man2", ((-9,-2), (-8,-4), (-7,-5), (-6.5,-6.5), (-5,-7), (-4,-8), (-2,-9), (0,-9.5), (2,-9), (4,-8), (5,-7),  (6.5,-6.5), (7,-5), (8,-4), (9,-2), (9.5,0), (9,2), (8,4), (7,5), (6.5,6.5), (5,7), (0,-2.5), (-5,7), (-6.5,6.5), (-7,5), (-8,4), (-9,2), (-9.5,0)))
screen.register_shape("Pac-Man3", ((-9,-2), (-8,-4), (-7,-5), (-6.5,-6.5), (-5,-7), (-4,-8), (-2,-9), (0,-9.5), (2,-9), (4,-8), (5,-7),  (6.5,-6.5), (7,-5), (8,-4), (9,-2), (9.5,0), (9,2), (8,4), (7,5), (6.5,6.5), (5,7),(4,8), (0,-2.5), (-4,8), (-5,7), (-6.5,6.5), (-7,5), (-8,4), (-9,2), (-9.5,0)))
screen.register_shape("Cyrcle", ((-9,-2), (-8,-4), (-7,-5), (-6.5,-6.5), (-5,-7), (-4,-8), (-2,-9), (0,-9.5), (2,-9), (4,-8), (5,-7),  (6.5,-6.5), (7,-5), (8,-4), (9,-2), (9.5,0), (9,2), (8,4), (7,5), (6.5,6.5), (5,7),(4,8), (2,9), (0,9.5), (-2,9), (-4,8), (-5,7), (-6.5,6.5), (-7,5), (-8,4), (-9,2), (-9.5,0)))

screen.tracer(0)  # this disables animation
playing = True
vulnerable = False
winnum = 30
amountpellets = winnum
timer = 800

#create Pac-Man
pacman = turtle.Turtle()
pacman.penup()
pacman.goto(0,0)
pacman.speed(0)
pacman.shape("Pac-Man")
pacman.color("yellow")

#create boundary
t = turtle.Turtle()
t.color("blue")
t.ht()
t.penup()
t.goto(-230,250)
t.pendown()
for i in range(2):
  t.forward(460)
  t.right(90)
  t.forward(500)
  t.right(90)

#create ghosts (list)
ghosts = []
colors = 0
for i in range(4):
  ghost = turtle.Turtle()
  ghost.shape('turtle')
  ghost.penup()
  ghost.setheading(270)
  if colors == 0:
    ghost.color('red')
  elif colors == 1:
    ghost.color('pink')
  elif colors == 2:
    ghost.color('cyan')
  elif colors == 3:
    ghost.color('orange')
  ghost.speed(0)
  ghost.goto(random.randint(-210,210),240)
  colors += 1
  ghosts.append(ghost)

#create pellets (list)
pellets = []

for i in range(amountpellets - 1):
  pellet = turtle.Turtle()
  pellet.color('white')
  pellet.shape('circle')
  pellet.speed(0)
  pellet.penup()
  pellet.goto(random.randint(-220,220), random.randint(-240,240))
  pellets.append(pellet)

powerpellet = turtle.Turtle()
powerpellet.color('yellow')
powerpellet.shape('circle')
powerpellet.speed(0)
powerpellet.penup()
powerpellet.goto(random.randint(-220,220), random.randint(-240,240))
#create scoreturtle (remaining pellets)

scoreturtle = turtle.Turtle()
scoreturtle.ht()
scoreturtle.color('white')
scoreturtle.penup()
scoreturtle.goto(-50,260)
scoreturtle.write('Score: 0/' + str(winnum))

score = 0

# create timeturtle (remaining time)
timeturtle = turtle.Turtle()
timeturtle.ht()
timeturtle.color('white')
timeturtle.penup()
timeturtle.goto(10,260)
timeturtle.write('Time: ' + str(timer))

# this updates the canvas with what has been drawn
screen.update()

#__________________________ 2. TECHNICALITIES ___________________________
#function definitions
def faceright():
  pacman.setheading(0)
def faceleft():
  pacman.setheading(180)
def faceup():
  pacman.setheading(90)
def facedown():
  pacman.setheading(270)
def abort():
  global playing
  global vulnerable
  screen.tracer(0)
  lose = turtle.Turtle()
  lose.goto(-30,0)
  lose.color('red')
  lose.ht()
  lose.write('GAME ABORTED')
  screen.update()
  screen.tracer(1)
  playing = False
  vulnerable = False

#button mapping
screen.onkey(faceright, "Right")
screen.onkey(faceleft, "Left")
screen.onkey(faceup, "Up")
screen.onkey(facedown, "Down")
screen.onkey(abort, "Space")
screen.listen()

screen.tracer(1) #enables animation again

#_________________________ 3. PLAYING THE GAME ___________________________

phase = 0
while playing: #!!!if spacebar is pressed, game will abort
  #move pacman and ghosts, move time forward
  screen.tracer(0)
  pacman.forward(4)
  far = 0
  for ghost in ghosts:
    if abs(ghost.ycor()) < 270 and abs(ghost.xcor()) < 270:
      if abs(ghost.ycor() + 250) < 9:
        ghost.goto(random.randint(-210,210),240)
      if far == 0:
        ghost.forward(13)
      elif far == 1:
        ghost.forward(10)
      elif far == 2:
        ghost.forward(9)
      elif far == 3:
        ghost.forward(7)
    far += 1
  timer -= 1
  timeturtle.clear()
  timeturtle.write('Time: ' + str(timer))
  if abs(timer) < 2:
    playing = False #!!!end condition: if time is over
  screen.update()
  screen.tracer(1)
  
  #pacman's eating movements
  if phase == 0:
    pacman.shape("Cyrcle")
    phase = 1
  elif phase == 1:
    pacman.shape("Pac-Man3")
    phase = 2
  elif phase == 2:
    pacman.shape("Pac-Man2")
    phase = 3
  elif phase == 3:
    pacman.shape("Pac-Man")
    phase = 4
  elif phase == 4:
    pacman.shape("Pac-Man2")
    phase = 5
  elif phase == 5:
    pacman.shape("Pac-Man3")
    phase = 0
  else:
    phase = 0
  
  #check for power pellet (ghosts now vulnerable for a ceratin amount of time)
  if pacman.distance(powerpellet) < 15:
    screen.tracer(0)
    powerpellet.ht()
    powerpellet.goto(-300,300)
    score += 1
    scoreturtle.clear()
    scoreturtle.write('Score: ' + str(score) + '/' + str(winnum))
    screen.update()
    screen.tracer(1)
    #!!!end condition: if all pellets are eaten
    if score == winnum:
      screen.tracer(0)
      win = turtle.Turtle()
      win.goto(-20,0)
      win.color('white')
      win.ht()
      win.write('YOU WIN!!!')
      screen.update()
      screen.tracer(1)
      playing = False
    if abs(pacman.xcor() - 230) < 4:
      pacman.goto(-225, pacman.ycor())
      pacman.setheading(0)
    elif abs(pacman.xcor() + 230) < 4:
      pacman.goto(225, pacman.ycor())
      pacman.setheading(180)
    elif abs(pacman.ycor() - 250) < 4:
      pacman.goto(pacman.xcor(), -245)
      pacman.setheading(90)
    elif abs(pacman.ycor() + 250) < 4:
      pacman.goto(pacman.xcor(), 245)
      pacman.setheading(270)
    #___________________________ SUBGAME HERE ____________________________
    vulnerable = True
    timeup = 0
    if timer > 100:
      timeup = timer - 100
    else:
      timeup = 0
    while(vulnerable & playing):
      screen.tracer(0)
      pacman.forward(7)
      for ghost in ghosts:
        if abs(ghost.ycor()) < 270 and abs(ghost.xcor()) < 270:
          ghost.color('blue')
          if abs(ghost.ycor() + 250) < 9:
            ghost.goto(random.randint(-210,210),240)
          ghost.forward(4)
          if pacman.distance(ghost) < 15:
            ghost.ht()
            ghost.goto(-300,300)
            timer += 25
      timer -= 1
      timeturtle.clear()
      timeturtle.write('Time: ' + str(timer))
      if abs(timer) < 2:
        playing = False
        vulnerable = False #!!!end condition: if time is over
      screen.update()
      screen.tracer(1)
      
      #pacman's eating movements
      if phase == 0:
        pacman.shape("Cyrcle")
        phase = 1
      elif phase == 1:
        pacman.shape("Pac-Man3")
        phase = 2
      elif phase == 2:
        pacman.shape("Pac-Man2")
        phase = 3
      elif phase == 3:
        pacman.shape("Pac-Man")
        phase = 4
      elif phase == 4:
        pacman.shape("Pac-Man2")
        phase = 5
      elif phase == 5:
        pacman.shape("Pac-Man3")
        phase = 0
      else:
        phase = 0
      if playing & vulnerable:
        for pellet in pellets:
          if pacman.distance(pellet) < 15:
            screen.tracer(0)
            pellet.ht()
            pellet.goto(-300,300)
            score += 1
            scoreturtle.clear()
            scoreturtle.write('Score: ' + str(score) + '/' + str(winnum))
            screen.update()
            screen.tracer(1)
            #!!!end condition: if all pellets are eaten
            if score == winnum:
              screen.tracer(0)
              win = turtle.Turtle()
              win.goto(-20,0)
              win.color('white')
              win.ht()
              win.write('YOU WIN!!!')
              screen.update()
              screen.tracer(1)
              vulnerable = False
              playing = False
      if abs(pacman.xcor() - 230) < 4:
        pacman.goto(-225, pacman.ycor())
        pacman.setheading(0)
      elif abs(pacman.xcor() + 230) < 4:
        pacman.goto(225, pacman.ycor())
        pacman.setheading(180)
      elif abs(pacman.ycor() - 250) < 4:
        pacman.goto(pacman.xcor(), -245)
        pacman.setheading(90)
      elif abs(pacman.ycor() + 250) < 4:
        pacman.goto(pacman.xcor(), 245)
        pacman.setheading(270)
      if abs(timer - timeup) < 5:
        colors = 0
        for i in range(4):
          if colors == 0:
            ghosts[i].color('red')
          elif colors == 1:
            ghosts[i].color('pink')
          elif colors == 2:
            ghosts[i].color('cyan')
          elif colors == 3:
            ghosts[i].color('orange')
          ghost.speed(0)
          if abs(ghosts[i].ycor()) < 270 and abs(ghosts[i].xcor()) < 270:
            ghosts[i].goto(random.randint(-210,210),240)
          colors += 1
        break

  #checking for pellets
  if playing:
    for pellet in pellets:
      if pacman.distance(pellet) < 15:
        screen.tracer(0)
        pellet.ht()
        pellet.goto(-300,300)
        score += 1
        scoreturtle.clear()
        scoreturtle.write('Score: ' + str(score) + '/' + str(winnum))
        screen.update()
        screen.tracer(1)
        #!!!end condition: if all pellets are eaten
        if score == winnum:
          screen.tracer(0)
          win = turtle.Turtle()
          win.goto(-20,0)
          win.color('white')
          win.ht()
          win.write('YOU WIN!!!')
          screen.update()
          screen.tracer(1)
          playing = False
  
  #!!!checking if it is touching the ghosts (end the game) - must be invulnerable
  for ghost in ghosts:
    if abs(ghost.ycor()) < 270 and abs(ghost.xcor()) < 270 and pacman.distance(ghost) < 15:
      screen.tracer(0)
      lose = turtle.Turtle()
      lose.goto(-25,0)
      lose.color('red')
      lose.ht()
      lose.write('GAME OVER')
      screen.update()
      screen.tracer(1)
      playing = False
  
  #checking boundaries (teleport to other side)
  if abs(pacman.xcor() - 230) < 4:
    pacman.goto(-225, pacman.ycor())
    pacman.setheading(0)
  elif abs(pacman.xcor() + 230) < 4:
    pacman.goto(225, pacman.ycor())
    pacman.setheading(180)
  elif abs(pacman.ycor() - 250) < 4:
    pacman.goto(pacman.xcor(), -245)
    pacman.setheading(90)
  elif abs(pacman.ycor() + 250) < 4:
    pacman.goto(pacman.xcor(), 245)
    pacman.setheading(270)



#you only get here if you reach the end of the game
if abs(timer) < 2:
  screen.tracer(0)
  lose = turtle.Turtle()
  lose.goto(-25,0)
  lose.color('red')
  lose.ht()
  lose.write('GAME OVER')
  screen.update()
  screen.tracer(1)
#GAME OVER or no message
  
  
  

  
  
# idea:
# have everything stop: spin when dying from ghost