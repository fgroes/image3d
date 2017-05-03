from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import OpenGL.GL.shaders as shaders
import numpy as np
import ctypes
import pyrr
from PIL import Image
from shader import *


class OpenGlProgram(object):

    WIDTH = 800
    HEIGHT = 600
    NAME = "My OpenGL window"

    def __init__(self, vertices, indices, shader_program):
        self.vertices = vertices
        self.indices = indices
        self.program = shader_program

    def initialize(self):
        dim_vertex = 3
        dim_color = 3

        self.program.compile()

        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)

        position = self.program.get_location("position")
        stride = (dim_vertex + dim_color) * self.vertices.itemsize
        offset = ctypes.c_void_p(0)
        glVertexAttribPointer(position, dim_vertex, GL_FLOAT, GL_FALSE, stride, offset)
        glEnableVertexAttribArray(position)

        color = self.program.get_location("color")
        offset = ctypes.c_void_p(dim_vertex * self.vertices.itemsize)
        glVertexAttribPointer(color, dim_color, GL_FLOAT, GL_FALSE, stride, offset)
        glEnableVertexAttribArray(color)

        self.program.use()


    def main(self):

        glutInit(sys.argv)

        glutInitContextVersion(3, 3)
        glutInitContextFlags(GLUT_FORWARD_COMPATIBLE)
        glutInitContextProfile(GLUT_CORE_PROFILE)

        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(self.WIDTH, self.HEIGHT)
        glutCreateWindow(self.NAME)

        self.initialize()

        glClearColor(0.2, 0.3, 0.2, 1.0)
        glEnable(GL_DEPTH_TEST)
        #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

        model = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, 0.0]))
        view = pyrr.matrix44.create_from_translation(pyrr.Vector3([0.0, 0.0, -3.0]))
        projection = pyrr.matrix44.create_perspective_projection_matrix(45.0, self.WIDTH / self.HEIGHT, 0.1, 100.0)

        model_loc = self.program.get_location("model", LocationType.UNIFORM)
        view_loc = self.program.get_location("view", LocationType.UNIFORM)
        proj_loc = self.program.get_location("projection", LocationType.UNIFORM)

        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)
        glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

        glutDisplayFunc(self.display)
        glutTimerFunc(10, self.timer, 10)

        glutMainLoop()


    def timer(self, value):
        time = 1.0 * glutGet(GLUT_ELAPSED_TIME) / 10000

        ax = 0.0
        ay = 0.0
        az = 0.0

        rot_x = pyrr.Matrix44.from_x_rotation(ax)
        rot_y = pyrr.Matrix44.from_y_rotation(ax)
        rot_z = pyrr.Matrix44.from_z_rotation(az)

        #rot_x = pyrr.Matrix44.from_x_rotation(np.pi * time)
        #rot_y = pyrr.Matrix44.from_y_rotation(np.pi * time)
        #rot_z = pyrr.Matrix44.from_z_rotation(np.pi * time)

        transform_loc = self.program.get_location("transform", LocationType.UNIFORM)
        glUniformMatrix4fv(transform_loc, 1, GL_FALSE, rot_x * rot_y * rot_z)
        glutPostRedisplay()
        glutTimerFunc(value, self.timer, value)


    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)
        glutSwapBuffers()


if __name__ == "__main__":
    from crate_data import vertices, indices
    vertex_shader_filename = "vertex_shader.sdr"
    fragment_shader_filename = "fragment_shader.sdr"
    shader_program = ShaderProgram(vertex_shader_filename, fragment_shader_filename)
    program = OpenGlProgram(vertices, indices, shader_program)
    program.main()
