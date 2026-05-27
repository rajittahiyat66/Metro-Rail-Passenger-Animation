from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *


# GLOBAL VARIABLES


train_x = -1000
train_speed = 3

train_stop = False
stop_timer = 0

door_offset = 0

# Passenger movement
outside_passenger_x = -40
outside_passenger_y = 120

inside_passenger_x = 170
inside_passenger_y = 120

# Passenger visibility
show_inside_passenger = True
show_outside_passenger = True


# TEXT


def draw_text(x, y, text):

    glRasterPos2f(x, y)

    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))



# CIRCLE


def draw_circle(cx, cy, r):

    glBegin(GL_POLYGON)

    for i in range(100):

        theta = 2 * pi * i / 100

        x = r * cos(theta)
        y = r * sin(theta)

        glVertex2f(cx + x, cy + y)

    glEnd()



# PASSENGER


def draw_passenger(x, y, r, g, b):

    # Head
    glColor3f(1, 0.8, 0.6)
    draw_circle(x, y + 18, 7)

    # Body
    glColor3f(r, g, b)

    glBegin(GL_POLYGON)

    glVertex2f(x - 7, y + 10)
    glVertex2f(x + 7, y + 10)
    glVertex2f(x + 7, y - 12)
    glVertex2f(x - 7, y - 12)

    glEnd()

    # Legs
    glColor3f(0, 0, 0)

    glBegin(GL_LINES)

    glVertex2f(x - 4, y - 12)
    glVertex2f(x - 4, y - 22)

    glVertex2f(x + 4, y - 12)
    glVertex2f(x + 4, y - 22)

    glEnd()


# STATION


def draw_station():

    # Platform
    glColor3f(0.55, 0.55, 0.55)

    glBegin(GL_POLYGON)

    glVertex2f(-300, 80)
    glVertex2f(400, 80)
    glVertex2f(400, 160)
    glVertex2f(-300, 160)

    glEnd()

    # Roof
    glColor3f(0.25, 0.25, 0.25)

    glBegin(GL_POLYGON)

    glVertex2f(-340, 250)
    glVertex2f(450, 250)
    glVertex2f(400, 310)
    glVertex2f(-300, 310)

    glEnd()

    # Pillars
    for i in range(-250, 380, 120):

        glColor3f(0.4, 0.4, 0.4)

        glBegin(GL_POLYGON)

        glVertex2f(i, 80)
        glVertex2f(i + 15, 80)
        glVertex2f(i + 15, 250)
        glVertex2f(i, 250)

        glEnd()

    glColor3f(1, 1, 1)

    draw_text(20, 270, "METRO RAIL STATION")


# TRACK


def draw_track():

    glColor3f(0.2, 0.2, 0.2)

    glLineWidth(6)

    glBegin(GL_LINES)

    glVertex2f(-1600, 40)
    glVertex2f(1600, 40)

    glVertex2f(-1600, 10)
    glVertex2f(1600, 10)

    glEnd()



# TRAIN


def draw_train(x):

    # Main body
    glColor3f(0.1, 0.35, 0.95)

    glBegin(GL_POLYGON)

    glVertex2f(x, 80)
    glVertex2f(x + 500, 80)
    glVertex2f(x + 500, 220)
    glVertex2f(x, 220)

    glEnd()

    # Front cabin
    glColor3f(0.2, 0.5, 1)

    glBegin(GL_POLYGON)

    glVertex2f(x + 500, 80)
    glVertex2f(x + 600, 80)
    glVertex2f(x + 600, 180)
    glVertex2f(x + 500, 220)

    glEnd()

    # Windows
    glColor3f(0.85, 0.95, 1)

    for i in range(7):

        wx = x + 30 + i * 65

        glBegin(GL_POLYGON)

        glVertex2f(wx, 160)
        glVertex2f(wx + 40, 160)
        glVertex2f(wx + 40, 195)
        glVertex2f(wx, 195)

        glEnd()

    # Door
    door_x = x + 230

    glColor3f(0.95, 0.95, 0.95)

    # Left Door
    glBegin(GL_POLYGON)

    glVertex2f(door_x - door_offset, 80)
    glVertex2f(door_x + 25 - door_offset, 80)
    glVertex2f(door_x + 25 - door_offset, 160)
    glVertex2f(door_x - door_offset, 160)

    glEnd()

    # Right Door
    glBegin(GL_POLYGON)

    glVertex2f(door_x + 25 + door_offset, 80)
    glVertex2f(door_x + 50 + door_offset, 80)
    glVertex2f(door_x + 50 + door_offset, 160)
    glVertex2f(door_x + 25 + door_offset, 160)

    glEnd()

    # Wheels
    glColor3f(0, 0, 0)

    draw_circle(x + 100, 55, 20)
    draw_circle(x + 380, 55, 20)

    # Passenger INSIDE train
    if show_inside_passenger:

        draw_passenger(
            inside_passenger_x,
            inside_passenger_y,
            1,
            0,
            0
        )


# DISPLAY


def display():

    glClear(GL_COLOR_BUFFER_BIT)

    # Sky
    glColor3f(0.6, 0.9, 1)

    glBegin(GL_POLYGON)

    glVertex2f(-1800, -800)
    glVertex2f(1800, -800)
    glVertex2f(1800, 800)
    glVertex2f(-1800, 800)

    glEnd()

    # Ground
    glColor3f(0.3, 0.8, 0.3)

    glBegin(GL_POLYGON)

    glVertex2f(-1800, -800)
    glVertex2f(1800, -800)
    glVertex2f(1800, 0)
    glVertex2f(-1800, 0)

    glEnd()

    draw_station()
    draw_track()
    draw_train(train_x)

    # Waiting passengers
    draw_passenger(-120, 120, 0, 1, 0)
    draw_passenger(-70, 120, 1, 0.5, 0)

    # Outside passenger enters train
    if show_outside_passenger:

        draw_passenger(
            outside_passenger_x,
            outside_passenger_y,
            1,
            0,
            1
        )

    # Title
    glColor3f(0, 0, 0)

    draw_text(
        -250,
        500,
        "METRO RAIL ENTRY & EXIT PASSENGER ANIMATION"
    )

    glutSwapBuffers()




# UPDATE


def update(v):

    global train_x
    global train_stop
    global stop_timer
    global door_offset

    global outside_passenger_x
    global outside_passenger_y

    global inside_passenger_x
    global inside_passenger_y

    global show_inside_passenger
    global show_outside_passenger



    # TRAIN MOVEMENT
    

    if not train_stop:
        train_x += train_speed

    # Stop train at station
    if train_x >= -200 and train_x <= -195:
        train_stop = True



    # TRAIN STOPPED
   

    if train_stop:

        stop_timer += 1


        # OPEN DOOR
        

        if stop_timer < 70:

            if door_offset < 25:
                door_offset += 0.5


        # INSIDE PASSENGER COMES OUT
        

        elif stop_timer < 220:

            if inside_passenger_x > 80:

                inside_passenger_x -= 1

            else:

                inside_passenger_y -= 0.5

                if inside_passenger_y < 110:
                    show_inside_passenger = False

        # OUTSIDE PASSENGER ENTERS TRAIN
        
        elif stop_timer < 380:

            if outside_passenger_x < 180:

                outside_passenger_x += 1

            else:

                outside_passenger_y += 0.5

                if outside_passenger_y > 190:
                    show_outside_passenger = False

        

        # CLOSE DOOR
        

        elif stop_timer < 470:

            if door_offset > 0:
                door_offset -= 0.5

       


        # TRAIN STARTS AGAIN
       

        else:

            train_stop = False
            stop_timer = 0

            # Reset passengers
            outside_passenger_x = -40
            outside_passenger_y = 120

            inside_passenger_x = 170
            inside_passenger_y = 120

            show_inside_passenger = True
            show_outside_passenger = True


    # RESET TRAIN
   

    if train_x > 1800:
        train_x = -1000

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

# INIT


def init():

    glClearColor(1, 1, 1, 1)

    glMatrixMode(GL_PROJECTION)

    gluOrtho2D(-1800, 1800, -800, 800)

# MAIN


glutInit()

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

glutInitWindowSize(1600, 900)

glutCreateWindow(
    b"Metro Rail Passenger Animation"
)

init()

glutDisplayFunc(display)

glutTimerFunc(0, update, 0)

glutMainLoop()