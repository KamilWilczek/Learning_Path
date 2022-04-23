class Animal:
    noise = "Rrrr"
    color = "Red"

    def make_noise(self):
        print(f"{self.noise}")

    def set_noise(self, new_noise):
        self.noise = new_noise

    # getter
    def get_color(self):
        return self.color

    # setter
    def set_color(self, new_color):
        self.color = new_color
        return self.color


# inheritance
class Wolf(Animal):
    noise = "grrrr"


# 2nd layer of inheritance, 2nd layer of abstraction
class BabyWolf(Wolf):
    color = "yellow"
