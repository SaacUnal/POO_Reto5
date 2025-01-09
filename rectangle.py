from shape.shape import shape

class Rectangle(shape.Shape):
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
