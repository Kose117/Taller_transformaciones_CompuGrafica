from OpenGL.GL import *


class Mesh(object):
    def __init__(self, filename: str):
        self.vertices = []
        self.faces = []
        self.load_mesh(filename)

    def load_mesh(self, filename: str):
        with open(filename) as f:
            line = f.readline()
            while line:
                line_tokens = line.split()
                if line_tokens[0] == "v":
                    self.vertices.append([float(x) for x in line_tokens[1:]])
                elif line_tokens[0] == "f":
                    self.faces.append([
                        int(x.split('/')[0]) - 1 for x in line_tokens[1:]
                    ])
                line = f.readline()

    def draw_mesh(self):
        for face in self.faces:
            glBegin(GL_LINE_LOOP)
            glVertex3fv(self.vertices[face[0]])
            glVertex3fv(self.vertices[face[1]])
            glVertex3fv(self.vertices[face[2]])
            glEnd()
