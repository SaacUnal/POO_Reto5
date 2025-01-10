from shape.shape import Shape, Point, Line

class Triangle(Shape):
  def __init__(self, vertices:list[Point], is_regular:bool):
    super().__init__(vertices, is_regular)

  def compute_height(self):
    height = ((self.edges[0].length**2) - ((self.edges[1].length/2)**2))**0.5
    return height

  def compute_area(self):
    height = self.compute_height()
    area = (self.edges[0].length*height)/2
    return area

class Equilateral(Triangle):
  def __init__(self, vertices:list[Point]):
    super().__init__(vertices, is_regular=True)

  def compute_perimeter(self):
    perimeter = self.edges[0].length * 3
    return perimeter

class Isosceles(Triangle):
  def __init__(self, vertices:list[Point]):
    super().__init__(vertices, is_regular=False)

  def compute_perimeter(self):
    perimeter = (self.edges[0].length * 2) + self.edges[1].length
    return perimeter

class Scalene(Triangle):
  def __init__(self, vertices:list[Point]):
    super().__init__(vertices, is_regular=False)

  def compute_height(self):
    point_height = Point(self.vertices[0].x, self.vertices[1].y)
    height = self.edges[0].compute_distance(point_height)
    return height

  def compute_perimeter(self):
    perimeter = self.edges[0].length + self.edges[1].length + self.edges[2].length
    return perimeter
