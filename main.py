import datetime
import random

class Company:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age

class Co_Founder(Company):

  def __init__(self, job, pay):
    self.job = job
    self.pay = pay
  
class Workers(Company):
  pass

class Sources:
  def __init__(self, name, pay, link):
    self.name = name
    self.pay = pay
    self.link = link
    Income = []
    pass

Co_Host1 = Company("Michael Palma", 16, "Male")
Co_Host1 = Co_Founder("Co_Host", .25)

