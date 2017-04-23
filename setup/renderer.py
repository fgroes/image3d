import OpenGL.GL as gl


class Renderer(object):

    def __init__(self, vertex_loc):
        self._vertex_loc = vertex_loc

    def prepare(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glClearColor(0.2, 0.3, 0.2, 1.0)
        #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    def render(self, model):
        gl.glBindVertexArray(model.vao_id)
        #gl.glEnableVertexAttribArray(self._vertex_loc)
        #gl.glDrawArrays(gl.GL_TRIANGLES, 0, model.vertex_count)
        gl.glDrawElements(gl.GL_TRIANGLES, model.index_count, gl.GL_UNSIGNED_INT, None)
        gl.glDisableVertexAttribArray(self._vertex_loc)
        gl.glBindVertexArray(0)
