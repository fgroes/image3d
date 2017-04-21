#import OpenGL.GLUT as glut
#import OpenGL.GLU as glu
#import OpenGL.GL as gl
import sys
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import OpenGL.GL.shaders as shaders
import numpy as np
import ctypes


WIDTH = 800
HEIGHT = 600
NAME = "My OpenGL window"


# position, color
vertices = [
    -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
    0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
    0.5, 0.5, 0.0, 0.0, 0.0, 1.0,
    -0.5, 0.5, 0.0, 1.0, 1.0, 1.0
]
vertices = np.array(vertices, dtype=np.float32)

indices = [
    0, 1, 2,
    2, 3, 0
]
indices = np.array(indices, dtype=np.uint32)


vertex_shader_code = \
"""
#version 330

in vec3 position;
in vec3 color;
out vec3 new_color;

void main()
{
    gl_Position = vec4(position, 1.0f);
    new_color = color;
}
"""


fragment_shader_code = \
"""
#version 330

in vec3 new_color;
out vec4 out_color;

void main()
{
    out_color = vec4(new_color, 1.0f);
}
"""


def initialize():
    vertex_shader = shaders.compileShader(vertex_shader_code, GL_VERTEX_SHADER)
    fragment_shader = shaders.compileShader(fragment_shader_code, GL_FRAGMENT_SHADER)
    program = shaders.compileProgram(vertex_shader, fragment_shader)

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    ebo = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

    position = glGetAttribLocation(program, "position")
    dim = 3
    stride = 24
    offset = ctypes.c_void_p(0)
    glVertexAttribPointer(position, dim, GL_FLOAT, GL_FALSE, stride, offset)
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(program, "color")
    byte_size = np.dtype(np.float32).itemsize
    offset = ctypes.c_void_p(3 * byte_size)
    glVertexAttribPointer(color, dim, GL_FLOAT, GL_FALSE, stride, offset)
    glEnableVertexAttribArray(color)

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

    #glDrawArrays(GL_TRIANGLES, num_skip, num_vertices)
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)

    glutSwapBuffers()


if __name__ == "__main__":
    main()