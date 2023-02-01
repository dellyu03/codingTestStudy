import turtle

# Initialize screen and bird
screen = turtle.Screen()
bird = turtle.Turtle()

# Draw the bird
bird.shape("circle")
bird.color("red")
bird.penup()

# Set bird's starting position
bird.goto(0, 0)
bird.dy = 0

# Define flap function to move the bird upward
def flap():
    bird.dy = 5

# Listen for user input to flap
screen.onkeypress(flap, "space")
screen.listen()

# Game loop
while True:
    # Apply gravity
    bird.dy -= 0.1
    bird.sety(bird.ycor() + bird.dy)

    # Check for collision with the ground
    if bird.ycor() < -200:
        break

# End the game
screen.bye()