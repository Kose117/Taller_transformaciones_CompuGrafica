import numpy as np
import pygame
from OpenGL.GLU import *


class Camera:
    def __init__(self, offset_x, offset_y, offset_z):
        # Offset de la cámara desde la nave
        self.offset = pygame.math.Vector3(offset_x, offset_y, offset_z)
        self.eye = pygame.math.Vector3(0, 0, 0)  # Se actualizará basado en la posición de la nave
        self.up = pygame.math.Vector3(0, 1, 0)
        self.forward = pygame.math.Vector3(0, 0, 1)
        self.right = pygame.math.Vector3(1, 0, 0)
        self.look = pygame.math.Vector3(0, 0, 0)  # Se actualizará basado en la orientación de la nave
        self.yaw = 0.0
        self.pitch = 0.0

    def rotate(self, yaw, pitch):
        # Actualiza yaw y pitch basado en el movimiento del ratón
        self.yaw += yaw
        self.pitch = max(-89.0, min(89.0, self.pitch + pitch))  # Limita el pitch para evitar el bloqueo del gimbal

    def update(self, ship_position, ship_forward, ship_up):
        # Primeramente, actualiza forward basado en yaw y pitch.
        # Esto determina la dirección en la que la cámara está mirando.
        rad_yaw = np.radians(self.yaw)
        rad_pitch = np.radians(self.pitch)
        forward = pygame.math.Vector3(
            np.cos(rad_pitch) * np.sin(rad_yaw),
            np.sin(rad_pitch),
            np.cos(rad_pitch) * np.cos(rad_yaw)
        ).normalize()

        # Calcula la posición de la cámara basada en el offset y la rotación.
        # Este enfoque mantiene la cámara orbitando alrededor de la nave.
        self.eye = ship_position + forward * (-self.offset.z) + ship_up * self.offset.y

        # Actualiza look para que la cámara siempre mire hacia la nave.
        self.look = ship_position

        # Actualiza la vista de la cámara.
        gluLookAt(self.eye.x, self.eye.y, self.eye.z,
                  self.look.x, self.look.y, self.look.z,
                  ship_up.x, ship_up.y, ship_up.z)

