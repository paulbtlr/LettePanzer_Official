import pygame
import math
import random

class Boden:
    # Define colors
    def __init__(self):
        LIGHT_BLUE = (50, 100, 255)
        PERU = (205, 133, 63)

        # Define parameters for multiple waves
        num_waves = 3
        self.waves = []

        self.window_size = (1920, 1020)

        for _ in range(num_waves):
            wave_length = random.randint(100, 400)
            amplitude = random.randint(10, 40)
            phase_shift = random.uniform(0, 2 * math.pi)
            self.waves.append((wave_length, amplitude, phase_shift))

    def get_ground_height(self, x):
        y = 0
        for wave in self.waves:
            wave_length, amplitude, phase_shift = wave
            y += amplitude * math.sin(x / wave_length * 2 * math.pi + phase_shift)
        return int(self.window_size[1] / 1.5 + y)

    def get_ground_slope(self, x):
        dy = 0
        for wave in self.waves:
            wave_length, amplitude, phase_shift = wave
            dy += (amplitude * 2 * math.pi / wave_length) * math.cos(x / wave_length * 2 * math.pi + phase_shift)
        return dy