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
        self.forward = pygame.math.Vector3(0, 0, -1)
        self.up = pygame.math.Vector3(0, 1, 0)
        self.right = pygame.math.Vector3(1, 0, 0)
        self.camera = Camera(0, 5, 10)  # Asigna la cámara aquí si es necesario

    def draw(self, screen_width, screen_height):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)
        glViewport(0, 0, screen_width, screen_height)

        camera_position = self.position - self.forward * 10 + self.up * 5

        gluLookAt(camera_position.x, camera_position.y, camera_position.z,
                  self.position.x, self.position.y, self.position.z,
                  self.up.x, self.up.y, self.up.z)

        glPushMatrix()
        glTranslate(self.position.x, self.position.y, self.position.z)
        glScale(0.25, 0.25, 0.25)
        print(f'x: {self.position.x:.1f}, y: {self.position.y:.1f}, z: {self.position.z:.1f}')
        self.mesh.draw_mesh()
        glPopMatrix()

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        movement_speed = 5.0  # velocidad de la nave

        if keys[pygame.K_w]:
            self.position += self.forward * movement_speed * delta_time
        if keys[pygame.K_s]:
            self.position -= self.forward * movement_speed * delta_time
        if keys[pygame.K_a]:
            self.position -= self.right * movement_speed * delta_time
        if keys[pygame.K_d]:
            self.position += self.right * movement_speed * delta_time

            # Actualización de la rotación de la cámara basada en el movimiento del ratón
        mouse_movement = pygame.mouse.get_rel()
        self.camera.rotate(mouse_movement[0], mouse_movement[1])

        # Actualizar la posición de la cámara para seguir a la nave
        # Esto permite que la cámara mantenga su orientación mientras sigue a la nave
        #self.camera.update(self.position, self.camera.forward, self.camera.up)

