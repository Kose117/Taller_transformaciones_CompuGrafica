import numpy as np
import pygame
from OpenGL.GLU import *


class Camera:
    def __init__(
            self,
            initial_pos_x,
            initial_pos_y,
            initial_pos_z,
    ):
        self.eye = pygame.math.Vector3(initial_pos_x, initial_pos_y, initial_pos_z)
        self.up = pygame.math.Vector3(0, 1, 0)
        self.right = pygame.math.Vector3(1, 0, 0)
        self.forward = pygame.math.Vector3(0, 0, 1)
        self.look = self.eye + self.forward
        self.yaw = -90
        self.pitch = 0
        self.last_mouse = pygame.math.Vector2(0, 0)

    def rotate(self, yaw, pitch):
        self.yaw += yaw
        self.pitch += pitch
        if self.pitch > 89.0:
            self.pitch = 89.0
        if self.pitch < -89.0:
            self.pitch = -89.0
        self.forward.x = np.cos(self.yaw) * np.cos(self.pitch)
        self.forward.y = np.sin(self.pitch)
        self.forward.z = np.sin(self.yaw) * np.cos(self.pitch)
        self.forward = self.forward.normalize()
        self.right = self.forward.cross(pygame.math.Vector3(0, 1, 0)).normalize()
        self.up = self.right.cross(self.forward).normalize()

    def update(self, screen_width, screen_height):
        mouse_pos = pygame.mouse.get_pos()
        mouse_change = self.last_mouse - pygame.math.Vector2(mouse_pos)
        pygame.mouse.set_pos((screen_width / 2, screen_height / 2))
        self.last_mouse = pygame.mouse.get_pos()
        self.rotate(-mouse_change.x * 0.001, mouse_change.y * 0.001)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.eye -= self.forward * 0.1
        if keys[pygame.K_UP]:
            self.eye += self.forward * 0.1
        if keys[pygame.K_RIGHT]:
            self.eye += self.right * 0.1
        if keys[pygame.K_LEFT]:
            self.eye -= self.right * 0.1

        self.look = self.eye + self.forward
        gluLookAt(self.eye.x, self.eye.y, self.eye.z,
                  self.look.x, self.look.y, self.look.z,
                  self.up.x, self.up.y, self.up.z)
