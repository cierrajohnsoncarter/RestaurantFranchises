#Menu class with constructor with 5 parameters
class Menu():
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return self.name + ' menu available from ' + str(self.start_time) + ' to ' + str(self.end_time)

#Method for calculating the bill
  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill

#Brunch Menu
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu('Brunch', brunch_items, 1100, 1600)

#Early Bird Menu
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu('Early Bird', early_bird_items, 1500, 1800)

#Dinner Menu
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu('Dinner', dinner_items, 1700, 2300)

#Kids Menu
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu('Kids', kids_items, 1100, 2100)

#Menu.calculate bill test
brunch_order_1 = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
early_bird_order_1 = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])

print(brunch_order_1)
print(early_bird_order_1)

#List of menus
menus = [brunch, early_bird, dinner, kids]

#Franchise class for multiple stores
class Franchise():
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

#New franchises
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

#available_menus test
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))

#New business
class Busniness():
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_restaurant = Menu('Arepas', arepas_menu, 1000, 2000)

#New business address
arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)
