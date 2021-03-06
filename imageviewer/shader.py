from OpenGL.GL import *
import OpenGL.GL.shaders as shaders


class LocationType(object):

    ATTRIB = 0
    UNIFORM = 1


class ShaderProgram(object):

    def __init__(self, vertex_shader_file, fragment_shader_file):
        self.vertex_shader_file = vertex_shader_file
        self.fragment_shader_file = fragment_shader_file
        self.program = None

    def load(self, shader_file):
        shader_source = ""
        with open(shader_file) as fid:
            shader_source = fid.read()
        return str.encode(shader_source)

    def compile(self):
        vertex_shader_code = self.load(self.vertex_shader_file)
        fragment_shader_code = self.load(self.fragment_shader_file)
        vertex_shader = shaders.compileShader(vertex_shader_code, GL_VERTEX_SHADER)
        fragment_shader = shaders.compileShader(fragment_shader_code, GL_FRAGMENT_SHADER)
        self.program = shaders.compileProgram(vertex_shader, fragment_shader)

    def get_location(self, name, type=LocationType.ATTRIB):
        if type == LocationType.ATTRIB:
            return glGetAttribLocation(self.program, name)
        elif type == LocationType.UNIFORM:
            return glGetUniformLocation(self.program, name)

    def use(self):
        glUseProgram(self.program)
