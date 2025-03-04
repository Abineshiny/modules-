def write1(filename, data):
  with open(filename, "w") as file:
    file.write(data)

def append2(filename, data):
  with open(filename, "a") as file:
    file.write(data)

def read3(filename):
  with open(filename, "r") as file:
    return file.read()