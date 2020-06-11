class MyParser:
  def __init__(self):
    self.error = None
  def processLine(self, line):
    if (line == 'quit' or line == 'exit'):
      exit()
    elif (self.isNumber(line) == False or float(line) < 0) :
      return -1
    return line
  def isNumber(self, token):
    try:
      float(token)
      return True
    except ValueError:
      return False