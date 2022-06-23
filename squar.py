from abstract.area import Area
from abstract.shape import Shape
from utils.profiler import Profiler

class Square(Shape,Area):
    
    @Profiler
    def draw(self):
        print("Draw square")
    
    @Profiler
    def calculate_area(self):
        print("Calcualte Area")