from shape.shape import Shape, Point

# Teniendo en cuenta que el primer vertice es el apice y los otros dos las bases
class Triangle(Shape):
  def __init__(self, vertices:list[Point], is_regular:bool):
    super().__init__(vertices, is_regular)
    Shape.compute_edges(self)

  def compute_height(self):
    point_height = Point(((self.vertices[1].x+self.vertices[2].x)/2), ((self.vertices[1].y+self.vertices[2].y)/2))
    height = self.vertices[0].compute_distance(point_height)
    return height

  def compute_area(self): 
    height = self.compute_height()
    area = (self.edges[1].length*height)/2
    return area

class Equilateral(Triangle): # Done
  def __init__(self, vertices:list[Point]):
    super().__init__(vertices, is_regular=True)

  def compute_perimeter(self):
    perimeter = self.edges[0].length * 3
    return perimeter

class Isosceles(Triangle): # Done
  def __init__(self, vertices:list[Point]):
    super().__init__(vertices, is_regular=False)
  
  def compute_perimeter(self):
    perimeter = (self.edges[0].length * 2) + self.edges[1].length
    return perimeter

class Scalene(Triangle):
  def __init__(self, vertices:list[Point]):
    super().__init__(vertices, is_regular=False)

  def compute_perimeter(self):
    perimeter = self.edges[0].length + self.edges[1].length + self.edges[2].length
    return perimeter
