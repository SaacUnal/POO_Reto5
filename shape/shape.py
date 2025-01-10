class Point:
  def __init__(self, x:float, y:float): # Saliendome un poco del UML
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
  def __init__(self, vertices:list[Point], is_regular:bool, ):
    self.vertices = vertices
    self.is_regular = is_regular
  
  def compute_edges(self):
    edges = []
    for i in range(len(self.vertices)):
      x = self.vertices[i] 
      y = self.vertices[(i+1) % len(self.vertices)]
      edges.append(Line(x, y, Point.compute_distance(x, y)))
    self.edges = edges
  
  def compute_area(self):
    raise NotImplementedError("Subclases has to implement compute_area() ")

  def compute_perimeter(self):
    raise NotImplementedError("Subclases has to implement compute_perimeter() ")

  def compute_inner_angles(self):
    raise NotImplementedError("Subclases has to implement compute_inner_angles() ")
