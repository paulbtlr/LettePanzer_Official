import math
import random

class Boden:
    def __init__(self):
        """
        Initialisierungsmethode für die Klasse Boden.
        Diese Methode definiert die Parameter für mehrere Wellen, die zur Simulation des Bodens verwendet werden.
        """
        # Anzahl der Wellen definieren
        num_waves = 3
        self.waves = []  # Liste, um die Wellenparameter zu speichern

        # Definieren der Fenstergröße (Breite, Höhe)
        self.window_size = (1920, 1020)

        # Generieren von Wellen mit zufälligen Parametern
        for _ in range(num_waves):
            # Wellenlänge zufällig zwischen A und B auswählen
            wave_length = random.randint(100, 400)
            # Amplitude zufällig zwischen A und B auswählen
            amplitude = random.randint(10, 20)
            # Phasenverschiebung zufällig zwischen A und Bπ auswählen
            phase_shift = random.uniform(0, 2 * math.pi)
            # Füge die Welle zur Liste der Wellen hinzu
            self.waves.append((wave_length, amplitude, phase_shift))

    def get_ground_height(self, x):
        """
        Berechnet die Höhe des Bodens an einer bestimmten x-Position.
        Parameter:
        x (float): Die x-Position, an der die Bodenhöhe berechnet werden soll.
        Rückgabewert:
        int: Die berechnete Bodenhöhe an der x-Position.
        """
        y = 0  # Anfangshöhe
        for wave in self.waves:
            wave_length, amplitude, phase_shift = wave
            # Addiere die Sinuskomponente der aktuellen Welle zur Gesamthöhe
            y += amplitude * math.sin(x / wave_length * 2 * math.pi + phase_shift)
        # Füge die mittlere Höhe des Fensters hinzu und runde auf eine Ganzzahl
        return int(self.window_size[1] / 1.5 + y)

    def get_ground_slope(self, x):
        """
        Berechnet die Steigung des Bodens an einer bestimmten x-Position.
        
        Parameter:
        x (float): Die x-Position, an der die Bodensteigung berechnet werden soll.

        Rückgabewert:
        float: Die berechnete Bodensteigung an der x-Position.
        """
        dy = 0  # Anfangssteigung ist 0
        for wave in self.waves:
            wave_length, amplitude, phase_shift = wave
            # Addiere die Ableitung der Sinuskomponente der aktuellen Welle zur Gesamtsteigung
            dy += (amplitude * 2 * math.pi / wave_length) * math.cos(x / wave_length * 2 * math.pi + phase_shift)
        return dy  # Rückgabe der berechneten Steigung