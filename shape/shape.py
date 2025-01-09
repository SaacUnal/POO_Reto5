class Point:
  def __init__(self, x:int, y:int):
    self.x = x
    self.y = y

  def compute_distance(self, point):
    distance = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
    return distance

class Line:
  def __init__(self, start_point:Point, end_point:Point, length:float):
    self.start_point = start_point
    self.end_point = end_point
    self.length = length

##############################################################################

class Shape:
  def __init__(self, is_regular:bool, vertices:list[Point], edges:list[Line], inner_angles:list[float]):
    self.is_regular = is_regular
    self.vertices = vertices
    self.edges = edges
    self.inner_angles = inner_angles

  def compute_area(self):
    raise NotImplementedError("Subclases has to implement compute_area() ")

  def compute_perimeter(self):
    raise NotImplementedError("Subclases has to implement compute_perimeter() ")

  def compute_inner_angles(self):
    raise NotImplementedError("Subclases has to implement compute_inner_angles() ")

##############################################################################

class Rectangle(Shape):
  def __init__(self, vertices:list[Point]):
    super().__init__(is_regular=False)

  def compute_area(self):
    area = self.edges[0].length * self.edges[1].length
    return area

  def compute_perimeter(self):
    perimeter = (self.edges[0].length*2) + (self.edges[1].length*2)
    return perimeter

  def compute_inner_angle(self):
    inner_angle = 0
    return inner_angle

class Square(Rectangle):
  def __init__(self, vertices:list[Point]):
    super().__init__(is_regular=True)

  def compute_area(self):
    area = self.edges[0].length ** 2
    return area

  def compute_perimeter(self):
    perimeter = self.edges[0].length * 4
    return perimeter

##############################################################################

class Triangle(Shape):
  def __init__(self, vertices:list[Point]):
    super().__init__(is_regular=False)

  def compute_height(self):
    height = ((self.edges[0].length**2) - ((self.edges[1].length/2)**2))**0.5
    return height

  def compute_area(self):
    height = self.compute_height()
    area = (self.edges[0].length*height)/2
    return area

class Equilateral(Triangle):
  def __init__(self, vertices:list[Point]):
    super().__init__(is_regular=True)

  def compute_perimeter(self):
    perimeter = self.edges[0].length * 3
    return perimeter

class Isosceles(Triangle):
  def __init__(self, vertices:list[Point]):
    super().__init__(is_regular=False)

  def compute_perimeter(self):
    perimeter = (self.edges[0].length * 2) + self.edges[1].length
    return perimeter

class Scalene(Triangle):
  def __init__(self, vertices:list[Point]):
    super().__init__(is_regular=False)

  def compute_height(self):
    point_height = Point(self.vertices[0].x, self.vertices[1].y)
    height = self.edges[0].compute_distance(point_height)
    return height

  def compute_perimeter(self):
    perimeter = self.edges[0].length + self.edges[1].length + self.edges[2].length
    return perimeter

##############################################################################
