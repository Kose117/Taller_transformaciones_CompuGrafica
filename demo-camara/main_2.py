import os

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from mesh_renderer import plot_parametric_mesh, generate_sphere_points, generate_toroid_points, \
    generate_klein_bottle_points

os.environ["SDL_VIDEO_CENTERED"] = '1'
display = [1000, 1080]
pygame.init()
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)


def initialize():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (display[0] / display[1]), 0.1, 500)


def init_camera():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    gluLookAt(0, 0, 1, 0, 0, 0, 0, 1, 0)


def display_world(points_matrix):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    init_camera()
    glMatrixMode(GL_MODELVIEW)
    draw_world_axes()
    glLineWidth(1)
    glPushMatrix()
    glTranslatef(0, -1, 0)
    plot_parametric_mesh(points_matrix)
    glPopMatrix()


def draw_world_axes():
    glLineWidth(4)
    glBegin(GL_LINES)
    glColor(1, 0, 0)
    glVertex3d(-1000, 0, 0)
    glVertex3d(1000, 0, 0)
    glColor(0, 1, 0)
    glVertex3d(0, -1000, 0)
    glVertex3d(0, 1000, 0)
    glColor(0, 0, 1)
    glVertex3d(0, 0, -1000)
    glVertex3d(0, 0, 1000)
    glEnd()


def main():
    initialize()

    run = True
    points_matrix = generate_klein_bottle_points()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        display_world(points_matrix)
        pygame.display.flip()
        pygame.time.wait(10)
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
