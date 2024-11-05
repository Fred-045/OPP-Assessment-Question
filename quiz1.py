# class keyword
class car():
    def __init__(self,make,model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"car.make:{self.make}")
        print(f"car.model:{self.model}")
        print(f"car.year:{self.year}")
mycar = car("Lexus", "cz2000", "2020")
mycar. display_info()