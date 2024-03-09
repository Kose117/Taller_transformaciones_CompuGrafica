from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import numpy as np
from demo2.character.camera import Camera
from demo2.mesh_loading.Mesh import Mesh


class Character(object):
    def __init__(self, mesh_file: str):
        self.camera = Camera(0, 0, 0)
        self.mesh = Mesh(mesh_file)

    def draw(self, screen_width, screen_height):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glViewport(0, 0, screen_width, screen_height)
        glEnable(GL_DEPTH_TEST)
        self.camera.update(screen_width, screen_height)
        new_pos = self.camera.eye - 0.5 * self.camera.up + 2 * self.camera.forward

        yaw_angle = np.arctan2(self.camera.forward.x, self.camera.forward.z) * 180 / np.pi
        pitch_angle = np.arctan2(self.camera.forward.y,
                                 np.sqrt(self.camera.forward.x ** 2 + self.camera.forward.z ** 2)) * 180 / np.pi
        print(f'angle: {yaw_angle}')
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glTranslate(new_pos.x, new_pos.y, new_pos.z)
        glRotate(yaw_angle, 0, 1, 0)
        glRotate(pitch_angle, 1, 0, 0)
        glScale(0.25, 0.25, 0.25)
        self.mesh.draw_mesh()
        glPopMatrix()


