from shape.shape import Point, Line
from rectangle import Rectangle, Square
from triangle import Equilateral, Isosceles, Scalene

if __name__ == "__main__":
  origen = Point(0,0)

  vertices = [origen, Point(5,0), Point(5,5), Point(0,5)]
  square = Square(vertices)
  print(square.compute_area())
  print(square.compute_perimeter())
  #print(square.compute_inner_angle())

  print("#-------------------------------------------------------------------")

  vertices = [origen, Point(10, 0), Point(10, 5), Point(0,5)]
  rectangle = Rectangle(vertices, False)
  print(rectangle.compute_area())
  print(rectangle.compute_perimeter())
  #print(rectangle.compute_inner_angle())

  print("#-------------------------------------------------------------------")

  vertices = [Point(2.5, 4.33), origen, Point(5, 0)]
  equilateral = Equilateral(vertices)
  print(equilateral.compute_area())
  print(equilateral.compute_perimeter())
  #print(equilateral.compute_inner_angle())

  print("#-------------------------------------------------------------------")

  vertices = [Point(0.5, 1), Point(-5, -5), Point(-1,-7)] # https://www.youtube.com/watch?v=0eyUYbB45fo
  isosceles = Isosceles(vertices)
  print(isosceles.compute_area())
  print(isosceles.compute_perimeter())
  #print(isosceles.compute_inner_angle())

  print("#-------------------------------------------------------------------")

  vertices = [Point(3, 3), Point(-2, 1), Point(7, -4)] # https://www.youtube.com/watch?v=7ZQgjbhyxFk
  scalene = Scalene(vertices)
  print(scalene.compute_area())
  print(scalene.compute_perimeter())
  #print(scalene.compute_inner_angle())
