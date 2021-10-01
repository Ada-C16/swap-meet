class Item:
  def __init__(self, condition = 0.0, age = None, category = ""):
    self.condition = condition
    self.age = age
    self.category = category

  def __str__(self):
    return "Hello World!"

  def condition_description(self):
 
      condition_description = [
          "Not even if you paid me.",
          "Poor",
          "Meh.",
          "Good",
          "Great!",
          "Fantastic!"
      ]

      return "I will give you my first born" if self.condition == 5 else condition_description[round(self.condition)]