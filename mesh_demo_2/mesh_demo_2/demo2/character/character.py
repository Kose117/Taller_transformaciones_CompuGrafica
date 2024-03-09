from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import numpy as np
from demo2.character.camera import Camera
from demo2.mesh_loading.Mesh import Mesh

class Character(object):
    def __init__(self, mesh_file: str, initial_pos_x, initial_pos_y, initial_pos_z):
        self.mesh = Mesh(mesh_file)
        self.position = pygame.math.Vector3(initial_pos_x, initial_pos_y, initial_pos_z)
        self.forward = pygame.math.Vector3(0, 0, 1)
        self.up = pygame.math.Vector3(0, 1, 0)
        self.right = pygame.math.Vector3(-1, 0, 0)
        self.yaw_angle = 0  # Ángulo de giro de la nave sobre el eje Y
        self.camera = Camera(0, 0, 0)  # Asigna la cámara aquí si es necesario

    def draw(self, screen_width, screen_height):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)
        glViewport(0, 0, screen_width, screen_height)

        camera_position = self.position - self.forward * 8 + self.up * 4

        gluLookAt(camera_position.x, camera_position.y, camera_position.z,
                  self.position.x, self.position.y, self.position.z,
                  self.up.x, self.up.y, self.up.z)
        self.camera.update(screen_width, screen_height)

        glPushMatrix()
        glTranslate(self.position.x, self.position.y, self.position.z)
        glRotate(self.yaw_angle, 0, 1, 0)
        glScale(0.25, 0.25, 0.25)
        print(f'x: {self.position.x:.1f}, y: {self.position.y:.1f}, z: {self.position.z:.1f}')
        self.mesh.draw_mesh()
        glPopMatrix()

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        movement_speed = 3.0

        if keys[pygame.K_w]:
            self.position += self.forward * movement_speed * delta_time
        if keys[pygame.K_s]:
            self.position -= self.forward * movement_speed * delta_time
        if keys[pygame.K_a]:
            self.position -= self.right * movement_speed * delta_time
        if keys[pygame.K_d]:
            self.position += self.right * movement_speed * delta_time

        if keys[pygame.K_q]:
            self.yaw_angle += 3  # velocidad de giro
        if keys[pygame.K_e]:
            self.yaw_angle -= 3  # velocidad de giro


        if keys[pygame.K_SPACE]:
            self.position += self.up * movement_speed * delta_time
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.position -= self.up * movement_speed * delta_time
