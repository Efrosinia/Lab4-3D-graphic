import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges_QUADS = (
    (0, 1, 2, 3),  # front
    (3, 2, 7, 6),  # left
    (6, 7, 5, 4),  # back
    (4, 5, 1, 0),  # right
    (1, 5, 7, 2),  # top
    (4, 0, 3, 6)   # bottom
)

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

colors = (
    (1, 0, 0),  # Червоний
    (0, 1, 0),  # Зелений
    (0, 0, 1),  # Синій
    (1, 1, 0),  # Жовтий
    (1, 0, 1),  # Фіолетовий
    (0, 1, 1),  # Блакитний
)

def Cube():
    glBegin(GL_QUADS)
    for surface in edges_QUADS:
        glColor3fv(colors[2])
        for vertex in surface:
            glVertex3fv(verticies[vertex])
    glEnd()



def set_material_and_lighting():
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    glEnable(GL_LIGHTING)
    
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 0])


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Білий колір фону


    glTranslatef(0.0,0.0, -5)
    set_material_and_lighting()

    n =1 
    i =3 
    j = 1
    t = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    n =0
                    i =0
                    j =0
                    t =0
                if event.button == 3:
                    n =1 
                    i =3 
                    j = 1
                    t = 1

        glRotatef(n, i, j, t)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()