class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.min_value = min_value
        self.max_value = max_value

        if self.min_value > self.max_value:
            raise ValueError("min_value не може бути більшим за max_value")
        if not (self.min_value <= current <= self.max_value):
            raise ValueError("Початкове значення current поза межами min_value, max_value")
        self.current = current

    def set_current(self, start):
        if not (self.min_value <= start <= self.max_value):
            raise ValueError("current поза межами min_value, max_value")

        self.current = start

    def set_max(self, max_max):
        if max_max < self.min_value:
            raise ValueError("max_value не може бути меншим за min_value")
        if self.current > max_max:
            raise ValueError("max_value не може бути меншим за поточне значення current")

        self.max_value = max_max

    def set_min(self, min_min):
        if min_min > self.max_value:
            raise ValueError("min_value не може бути більшим за max_value")
        if self.current < min_min:
            raise ValueError("min_value не може бути меншим за поточне значення current")

        self.min_value = min_min

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Досягнуто максимуму")

        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Досягнуто мінімум")

        self.current -= 1

    def get_current(self):
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()

assert counter.get_current() == 10
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум
assert counter.get_current() == 10

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()

assert counter.get_current() == 7
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнут минимум
assert counter.get_current() == 7
