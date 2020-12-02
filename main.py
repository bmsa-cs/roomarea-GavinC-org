"""
RoomArea
Author:

Original assignment by: Edhesive Intro to CS

Find the area of an irregularly shaped room with the shape as shown in room.png.

Ask the user to enter the values for sides A, B, C, D, and E and print out the total room area.

"""
import os
import importlib.util

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v tests.py"
  print(command)
  os.system(command)

def right_triangle_area(base, height):
  """
  Given the base and height of a right triangle, returns the area.

  Parameters:
  base, height (float) - the base and height of the triangle

  Returns:
  float: the product of the base and height divided by two
  """
  area = base * height * 0.5
  return area


def rectangle_area(length, width):
  """
  Given the length and width of a rectangle, returns the area.

  Parameters:
  length, height (int) - the length and width of the rectangle
  Returns:
  int: the product of the length and width
  """
  return float(length * width)


def room_area(a, b, c, d, e):
  """
  Given five measurements, this function calculates and returns the area of the room.

  Parameters:
  a, b, c, d, e (int): the variables used to calculate the area

  Returns:
  float: the sum of the area of each shape
  """
  rectangle1 = rectangle_area(d-e, a-c)
  rectangle2 = rectangle_area(b, c)
  triangle = right_triangle_area(e, a-c)
  return float(rectangle1 + rectangle2 + triangle)


if __name__ == "__main__":
  os.system("clear") # clears the console each time you run

  a = float(input("A: "))
  b = float(input("B: "))
  c = float(input("C: "))
  d = float(input("D: "))
  e = float(input("E: "))

  final_area = room_area(a, b, c, d, e)
  print("Room area: " + str(final_area))

  tests = input("Run tests? (y/n)")
  if tests.lower() == 'y':
    run_tests()