import matplotlib.pyplot as plt


class HertzsprungRussell:
    def __init__(self, temperature: float, luminosity:float):
        self.temperature = temperature
        self.luminosity = luminosity

    def plot_HR_diagram(self):
        plt.figure(figsize=(8, 8))
        plt.scatter(self.temperature, self.luminosity, c='black', s=5, alpha=0.5)
        plt.gca().invert_xaxis()
        plt.xlabel('Temperature (K)')
        plt.ylabel('Luminosity (Solar Units)')
        plt.title('Hertzsprung-Russell Diagram')
        plt.show()


def start_hr_diagram():
    temperature = [5000, 6000, 7000, 8000, 9000, 10000]
    luminosity = [0.1, 0.5, 1, 3, 10, 30]

    hr_diagram = HertzsprungRussell(temperature, luminosity)
    hr_diagram.plot_HR_diagram()