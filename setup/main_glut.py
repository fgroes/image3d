#import OpenGL.GLUT as glut
#import OpenGL.GLU as glu
#import OpenGL.GL as gl
import sys
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import OpenGL.GL.shaders as shaders
import numpy as np


WIDTH = 800
HEIGHT = 600
NAME = "My OpenGL window"


triangle = [
    -0.5, -0.5, 0.0,
    0.5, -0.5, 0.0,
    0.0, 0.5, 0.0
]
triangle = np.array(triangle, dtype=np.float32)


vertex_shader_code = \
"""
#version 330

layout (location=0) in vec4 position;

void main()
{
    gl_Position = position;
}
"""


fragment_shader_code = \
"""
#version 330

out vec4 output_color;

void main()
{
    output_color = vec4(1.0f, 0.0f, 0.0f, 1.0f);
}
"""


num_skip = 0
num_vertices = 3


def initialize():
    vertex_shader = shaders.compileShader(vertex_shader_code, GL_VERTEX_SHADER)
    fragment_shader = shaders.compileShader(fragment_shader_code, GL_FRAGMENT_SHADER)
    program = shaders.compileProgram(vertex_shader, fragment_shader)

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)

    byte_per_float = 4
    glBufferData(GL_ARRAY_BUFFER, triangle.nbytes, triangle, GL_STATIC_DRAW)

    position = glGetAttribLocation(program, "position")

    dim = 3
    bytes_betw_data = 0
    offset = None
    glVertexAttribPointer(position, dim, GL_FLOAT, GL_FALSE, bytes_betw_data, offset)

    glEnableVertexAttribArray(position)
    glUseProgram(program)


def main():
    glutInit(sys.argv)

    glutInitContextVersion(3, 3)
    #glutInitContextFlags(GLUT_FORWARD_COMPATIBLE)
    #glutInitContextProfile(GLUT_CORE_PROFILE)

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(WIDTH, HEIGHT)
    glutCreateWindow(NAME)

    initialize()

    glutDisplayFunc(display)

    glutMainLoop()


def display():
    glClearColor(0.2, 0.3, 0.2, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glDrawArrays(GL_TRIANGLES, num_skip, num_vertices)
    glutSwapBuffers()


if __name__ == "__main__":
    main()
