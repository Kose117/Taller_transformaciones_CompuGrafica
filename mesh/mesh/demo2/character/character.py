import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from mesh.demo2.character.camera import Camera
from mesh.demo2.mesh_loading.Mesh import Mesh
import pygame


class Character(object):
    def __init__(self, asset_path: str):
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = -1
        self.camera = Camera(self.pos_x, self.pos_y, self.pos_z)
        self.mesh = Mesh(asset_path)

    def display(self, screen_width, screen_height):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glLineWidth(1)
        glViewport(0, 0, screen_width, screen_height)
        glEnable(GL_DEPTH_TEST)
        self.camera.update(screen_width, screen_height)
        yaw_rot_vector = pygame.math.Vector3(0, 0, 1).project(
            pygame.math.Vector3(self.camera.forward.x, 0, self.camera.forward.z)
        )
        angle_yaw = np.arccos(yaw_rot_vector.magnitude()) * 180.0 / np.pi
        angle_pitch = abs(np.arctan(self.camera.forward.y / self.camera.forward.z)) * 180.0 / np.pi
        if self.camera.forward.x < 0 <= self.camera.forward.z:
            angle_yaw = -angle_yaw
        elif self.camera.forward.x < 0 and self.camera.forward.z < 0:
            angle_yaw = -90 - (90 - angle_yaw)
        elif self.camera.forward.x >= 0 > self.camera.forward.z:
            angle_yaw = 90 + (90 - angle_yaw)
        if self.camera.forward.y > 0:
            angle_pitch = - angle_pitch
        else:
            angle_pitch = angle_pitch
        print(f'angle {angle_yaw} Pitch: {angle_pitch}')
        new_pos = self.camera.eye - self.camera.up * 0.25 + self.camera.forward * 1
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glTranslated(new_pos.x, new_pos.y, new_pos.z)
        glRotate(angle_yaw, 0, 1, 0)
        glRotate(angle_pitch, 1, 0, 0)
        glScale(0.1, 0.1, 0.1)
        self.mesh.draw_mesh()
        glPopMatrix()
