class XP():
  def __init__(self, xp_per_level:int, total_levels:int, starting_xp:int, starting_level:int, points_awarded_per_level:int, starting_points:int):
    self.xp_per_level = xp_per_level
    self.total_levels = total_levels
    
    self.xp = starting_xp
    self.level = starting_level
    
    
    self.points_per_level = points_awarded_per_level
    self.points = starting_points
    if self.xp >= self.xp_per_level: raise TypeError("Starting XP must be less than XP per level!")
    if self.level >= self.total_levels: raise TypeError("Starting level must be less than total levels!")

    
    
  def award_xp(self, amount:int):
    self.xp = self.xp + amount
    if self.xp_per_level < self.xp:
      xptemp = self.xp
      ltemp = self.level
      while xptemp > self.xp_per_level:
        ltemp += 1
        xptemp = xptemp - self.xp_per_level
      
      print(f"You got {str(amount)} XP, enough to level up to level {ltemp}!")
    else: print(f"You got {str(amount)} XP! Only {self.xp_per_level - self.xp} XP to Level {self.level +1}. You currently have {self.xp} XP")
    while self.xp_per_level < self.xp:
      if self.level == self.total_levels:
        break
      # self.level += 1
      
      while self.xp > self.xp_per_level:
        self.level += 1
        self.xp  = self.xp - self.xp_per_level
      self.points += self.points_per_level
      
      print(f"You leveled up! You are now at level {self.level} with {self.xp} XP. You also now have {self.points} points available.")
  def revoke_xp(self, amount:int):
    amount_og = amount
    from time import sleep
    if amount > self.xp:
      xptemp = self.xp_per_level
      while amount >= xptemp:
        self.level -= 1
        print("level -1")
        amount = amount - self.xp
        self.xp = self.xp_per_level
        
        while amount > self.xp_per_level:
          self.level -=1
          amount = amount - self.xp_per_level
        self.xp = self.xp - amount
        
      if self.xp - amount_og <= 0: print(f"You just lost {amount_og} XP! Unfortunately, you have no XP to lose, so you are still at level {self.level}")
      else: print(f"You just lost {amount_og} XP and have been demoted to level {self.level}! You currently have {self.xp} XP!")
    else:
      self.xp = self.xp - amount
      print(f"You just lost {amount_og} XP! You currently have {self.xp} XP.")
    

