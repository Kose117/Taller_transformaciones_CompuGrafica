import numpy as np
from OpenGL.GL import *

colors = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1]
]


def plot_parametric_mesh(points_matrix):
    glPointSize(3)
    n_rows = len(points_matrix)
    n_cols = len(points_matrix[0])
    for i in range(n_rows):
        for j in range(n_cols):
            if (j + 1) < n_cols and (i + 1) < n_rows:
                glBegin(GL_LINES)
                glColor3fv(colors[0])
                glVertex3fv(points_matrix[i][j])
                glColor3fv(colors[1])
                glVertex3fv(points_matrix[i][(j + 1) % n_cols])
                glColor3fv(colors[2])
                glVertex3fv(points_matrix[(i + 1) % n_rows][(j + 1) % n_cols])
                glColor3fv(colors[0])
                glVertex3fv(points_matrix[i][j])
                glEnd()
                glBegin(GL_LINES)
                glColor3fv(colors[3])
                glVertex3fv(points_matrix[i][j])
                glColor3fv(colors[4])
                glVertex3fv(points_matrix[(i + 1) % n_rows][(j + 1) % n_cols])
                glColor3fv(colors[5])
                glVertex3fv(points_matrix[(i + 1) % n_rows][j])
                glColor3fv(colors[0])
                glVertex3fv(points_matrix[i][j])
                glEnd()


def generate_sphere_points(
        radius=3,
        alpha_samples=20,
        beta_samples=10
):
    point_matrix = []
    for alpha in np.linspace(0, 2 * np.pi, alpha_samples):
        point_array = []
        for beta in np.linspace(0, np.pi, beta_samples):
            point_array.append(
                (
                    radius * np.cos(alpha) * np.sin(beta),
                    radius * np.sin(alpha) * np.sin(beta),
                    radius * np.cos(beta)
                )
            )
        point_matrix.append(point_array)
    return point_matrix


def generate_klein_bottle_points(
        alpha_samples=20,
        beta_samples=20
):
    point_matrix = []
    for alpha in np.linspace(0, np.pi, alpha_samples):
        point_array = []
        for beta in np.linspace(0, 2 * np.pi, beta_samples):
            point_array.append(
                (
                    (-2 / 15) * np.cos(alpha) * (
                            3 * np.cos(beta)
                            - 30 * np.sin(alpha)
                            + 90 * (np.cos(alpha) ** 4) * np.sin(alpha)
                            - 60 * (np.cos(alpha) ** 6) * np.sin(alpha)
                            + 5 * np.cos(alpha) * np.cos(beta) * np.sin(alpha)
                    ),
                    (-1 / 15) * np.sin(alpha) * (
                            3 * np.cos(beta)
                            - 3 * (np.cos(alpha) ** 2) * np.cos(beta)
                            - 48 * (np.cos(alpha) ** 4) * np.cos(beta)
                            + 48 * (np.cos(alpha) ** 6) * np.cos(beta)
                            - 60 * np.sin(alpha)
                            + 5 * np.cos(alpha) * np.cos(beta) * np.sin(alpha)
                            - 5 * (np.cos(alpha) ** 3) * np.cos(beta) * np.sin(alpha)
                            - 80 * (np.cos(alpha) ** 5) * np.cos(beta) * np.sin(alpha)
                            + 80 * (np.cos(alpha) ** 7) * np.cos(beta) * np.sin(alpha)
                    ),
                    (2 / 15) * (3 + 5 * np.cos(alpha) * np.sin(alpha)) * np.sin(beta)
                )
            )
        point_matrix.append(point_array)
    return point_matrix


def generate_toroid_points(
        radius_1=4,
        radius_2=1,
        alpha_samples=20,
        beta_samples=20
):
    point_matrix = []
    for alpha in np.linspace(0, 2 * np.pi, alpha_samples):
        point_array = []
        for beta in np.linspace(0, 2 * np.pi, beta_samples):
            point_array.append(
                (
                    (radius_1 + radius_2 * np.cos(beta)) * np.sin(alpha),
                    (radius_1 + radius_2 * np.cos(beta)) * np.cos(alpha),
                    radius_2 * np.sin(beta)
                )
            )
        point_matrix.append(point_array)
    return point_matrix
