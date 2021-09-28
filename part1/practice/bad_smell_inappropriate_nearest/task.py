class Cube:
    x: int
    y: int
    z: int

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube):
        return cube.x * cube.y * cube.y
