# Engine class
class Engine:
    def start(self):
        print(" you have started the Engine.")
    
    def stop(self):
        print("You have stopped the Engine.")

# Car class
class Car:
    def __init__(self):
    
        self.engine = Engine()

    def start_engine(self):
    
        self.engine.start()
    
    def stop_engine(self):
    
        self.engine.stop()

my_car = Car()
my_car.start_engine()  
my_car.stop_engine()   
