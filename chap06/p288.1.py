class Triangle:
  num_tri = 0

  def __init__(self, base = 0, height = 0):
    self.base = base
    self.height = height
    Triangle.num_tri += 1

  def find_area(self):
    b = self.base
    h = self.height
    return 0.5 * b * h
  
# Create instances of the Triangle class
t1 = Triangle(1, 1)
print(t1.find_area())

print(Triangle.num_tri)

t2 = Triangle(2, 2)
print(Triangle.num_tri)

t3 = Triangle(3, 5)
print(Triangle.num_tri)

print(t1.num_tri, t2.num_tri, t3.num_tri, Triangle.num_tri)

t1.num_tri = 5
print(t1.num_tri, t2.num_tri, t3.num_tri, Triangle.num_tri)

Triangle.num_tri = 6
print(t1.num_tri, t2.num_tri, t3.num_tri, Triangle.num_tri)

