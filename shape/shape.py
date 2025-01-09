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
