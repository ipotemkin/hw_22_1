class Unit:
    def __init__(self, x, y, state='fly', speed=1):
        self.coord = [x, y]
        self.state = state
        self.speed = speed

    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Wrong quality')

    def move(self, direction):
        speed = self._get_speed()
        if direction == 'UP':
            self.coord[1] += speed
        elif direction == 'DOWN':
            self.coord[1] -= speed
        elif direction == 'LEFT':
            self.coord[0] -= speed
        elif direction == 'RIGTH':
            self.coord[0] += speed
