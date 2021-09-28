class Item:
  def __init__(self, category = None, condition = None):
    
    if not category:
        category = ""
    elif not condition:
        condition = 0.0

    self.category = category
    self.condition = condition

  def __str__(self):
    return "Hello World!"

  def condition_description(self):
      if self.condition == 5:
          return "Fantastic"
      if 4 < self.condition < 5:
          return "Great"
      if 3 < self.condition <= 4:
          return "Good"
      if 2 < self.condition <= 3:
          return "Meh"
      if 1 < self.condition <= 2:
          return "Poor"
      if 0 < self.condition <= 1:
          return "Bad"
      else:
          return "Not even if you paid me."



