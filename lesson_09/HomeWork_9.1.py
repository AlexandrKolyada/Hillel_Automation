class Diamond:
    def __init__(self, side_a, angle_a, angle_b=None):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle = angle_b

    def __setattr__(self, key, value):
        if key == 'side_a':
            if value <= 0:
                raise ValueError ("Wrong side")
            else:
                super().__setattr__('side_a', value)

        elif key == 'angle_a':
            if not (0 < value < 180):
                raise ValueError ("Wrong angle")
            else:
                super().__setattr__('angle_a', value)
                super().__setattr__('angle_b', 180 - value)

        elif key == 'angle_b':
            raise ValueError("Calculated automatically")

d = Diamond(5, 60)