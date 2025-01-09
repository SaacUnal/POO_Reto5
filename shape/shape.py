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
