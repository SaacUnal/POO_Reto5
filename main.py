from rectangle import Rectangle, Square
from triangle import Equilateral, Isosceles, Scalene

if __name__ == "__main__":
  square = Square()
  print(square.compute_area())
  print(square.compute_perimeter())
  #print(square.compute_inner_angle())

  print("#-------------------------------------------------------------------")

  rectangle = Rectangle()
  print(rectangle.compute_area())
  print(rectangle.compute_perimeter())
  #print(rectangle.compute_inner_angle())

  print("#-------------------------------------------------------------------")

  equilateral = Equilateral()
  print(equilateral.compute_area())
  print(equilateral.compute_perimeter())
  #print(equilateral.compute_inner_angle())

  print("#-------------------------------------------------------------------")

  isosceles = Isosceles()
  print(isosceles.compute_area())
  print(isosceles.compute_perimeter())
  #print(isosceles.compute_inner_angle())

  print("#-------------------------------------------------------------------")

  scalene = Scalene()
  print(scalene.compute_area())
  print(scalene.compute_perimeter())
  #print(scalene.compute_inner_angle())
