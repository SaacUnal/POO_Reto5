from shape.shape import Point, Line
from rectangle import Rectangle, Square
from triangle import Equilateral, Isosceles, Scalene

if __name__ == "__main__":
  origen = Point(0,0)

  vertices = [origen, Point(), Point(), Point()]
  square = Square(vertices)
  print(square.compute_area())
  print(square.compute_perimeter())
  #print(square.compute_inner_angle())

  print("#-------------------------------------------------------------------")

  vertices = [origen, Point(), Point(), Point()]
  rectangle = Rectangle(False)
  print(rectangle.compute_area())
  print(rectangle.compute_perimeter())
  #print(rectangle.compute_inner_angle())

  print("#-------------------------------------------------------------------")

  vertices = [Point(5, 5), origen, Point(4, 0)]
  equilateral = Equilateral(vertices)
  print(equilateral.compute_area())
  print(equilateral.compute_perimeter())
  #print(equilateral.compute_inner_angle())

  print("#-------------------------------------------------------------------")

  vertices = [Point(3, 5), origen, Point(0, 5)]
  isosceles = Isosceles(vertices)
  print(isosceles.compute_area())
  print(isosceles.compute_perimeter())
  #print(isosceles.compute_inner_angle())

  print("#-------------------------------------------------------------------")

  vertices = [Point(2.5, 5), origen, Point(0, 5)]
  scalene = Scalene(vertices)
  print(scalene.compute_area())
  print(scalene.compute_perimeter())
  #print(scalene.compute_inner_angle())
