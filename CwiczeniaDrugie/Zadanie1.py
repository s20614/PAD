def cache(func):
    cache_val = {}

    def wrapper(self, steps):
        if steps not in cache_val:
            result = func(self, steps)
            cache_val[steps] = result
        return cache_val[steps]

    return wrapper


class Tetranacci:
    def __init__(self, steps):
        self.steps = steps
        self.counter = 0
        self.values = [0, 0, 0, 1]

    def __iter__(self):
        return self

    @cache
    def __next__(self):
        if self.counter < self.steps:
            self.counter += 1
            if self.counter <= 4:
                return self.values[self.counter - 1]
            else:
                next_value = sum(self.values)
                self.values = self.values[1:] + [next_value]
                return next_value
        else:
            raise StopIteration


def main():
    steps = 10
    tet = Tetranacci(steps)
    for value in tet:
        print(value)


if __name__ == "__main__":
    main()
