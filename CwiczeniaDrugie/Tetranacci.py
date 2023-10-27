class Tetranacci:
    def __init__(self, steps):
        self.steps = steps
        self.current_step = 0
        self.a, self.b, self.c, self.d = 0, 0, 0, 1

    def __next__(self):
        if self.current_step >= self.steps:
            raise StopIteration('Iterator reached the final step')
        elif self.current_step < 3:
            self.current_step += 1
            return 0
        elif self.current_step == 3:
            self.current_step += 1
            return 1
        else:
            next_value = self.a + self.b + self.c + self.d
            self.a, self.b, self.c, self.d = self.b, self.c, self.d, next_value
            self.current_step += 1
            return next_value

    def __iter__(self):
        return self
