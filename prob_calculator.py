import random


class Hat:

  def __init__(self, **colors_inside):
    contents = []
    self.contents = contents
    for color, inside in colors_inside.items():
      for i in range(inside):
        contents.append(color)

    return None

  def draw(self, draws):

    result = []
    if int(draws) > len(self.contents):
      return self.contents
    for x in range(draws):

      drawn = random.choice(self.contents)
      self.contents.remove(drawn)
      result.append(drawn)

    return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  hat = hat
  sample = expected_balls.copy()
  m = 0
  n = 0

  while True:
    sample = expected_balls.copy()

    n += 1
    result = hat.draw(num_balls_drawn)

    for i in result:
      try:
        value = sample.get(f'{i}')
        if value > 1:
          sample[f'{i}'] -= 1
        if value == 1:
          del sample[f'{i}']
      except:
        pass
    if len(sample) == 0:
      m += 1

    if n == num_experiments:
      break

  probability = m / num_experiments
  return probability
