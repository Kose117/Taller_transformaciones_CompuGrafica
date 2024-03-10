import os
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from demo2.character.character import Character
from demo2.mesh_loading.Mesh import Mesh
from demo2.character.camera import Camera

os.environ["SDL_VIDEO_CENTERED"] = '1'
pygame.init()

# Obtén las dimensiones de la pantalla
info = pygame.display.Info()
display = [info.current_w, info.current_h]

# Establecer el modo de pantalla completa
screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL | pygame.FULLSCREEN)

camera = Camera(0,0,0)

def initialize():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(60, (display[0] / display[1]), 0.1, 500)

def display_world(character: Character):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    character.draw(screen.get_width(), screen.get_height())
    glMatrixMode(GL_MODELVIEW)
    draw_world_axes()

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
    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)
    run = True
    character = Character('./assets/Fighter_01.obj', 0, 0, 0)
    clock = pygame.time.Clock()

    while run:
        delta_time = clock.tick(144) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        character.update(delta_time)
        display_world(character)
        pygame.display.flip()

        pygame.time.wait(10)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
