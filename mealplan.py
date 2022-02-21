#Data are from myfitnesspal
#I be updating this program often to include more items in the future and location prompts to allow better identification of meals nearby
#For now do enjoy this little program, where the max amount of food is 4 for each category.

import random
import warnings

warnings.filterwarnings("ignore")
Calorieamount = input("How much do you aim for your daily calorie intake:" )
intcalorieamount = int(Calorieamount)
breakfast = (
    "Hashbrowns",
    "Hotcakes",
    "Kaya Toast",
    "Peanut Butter Bread")
breakfastmp = random.sample(set(breakfast), 1)
lunch = (
    "Chicken Rice",
    "Bak Kut Teh with Rice",
    "Sliced Fish Soup with Rice",
    "Wanton Noodles")
lunchmp = random.sample(set(lunch), 1)
dinner = (
    "Chicken Chop with Rice",
    "Steak & Fries",
    "Garden Salad with dressing",
    "Maggi Goreng")
dinnermp = random.sample(set(dinner), 1)
p = (breakfastmp, lunchmp, dinnermp)
print(f"\nYour mealplan for today is: {p}")
breakfastcalories = (153, 600, 318, 446)
breakfastprotein = (1, 9, 5, 24)
breakfastcarbs = (14, 102, 45, 14)
breakfastfats = (9, 17, 16, 42)
lunchcalories = (607, 502, 450, 411)
lunchprotein = (25, 32, 23, 19)
lunchcarbs = (75, 36, 39, 55)
lunchfats = (23, 25, 4, 12)
dinnercalories = (550, 360, 123, 461)
dinnerprotein = (44, 30, 1, 23)
dinnercarbs = (42, 23, 9, 84)
dinnerfats = (22, 17, 8, 14)

mealprepcalories = 0
mealprotein = 0
mealcarbs = 0
mealfat = 0
for i in breakfastmp:
    if i  == "Hashbrowns":

     mealprepcalories += breakfastcalories[0]
     mealprotein += breakfastprotein[0]
     mealcarbs += breakfastcarbs[0]
     mealfat += breakfastfats[0]
    elif i  == "Hotcakes":

     mealprepcalories += breakfastcalories[1]
     mealprotein += breakfastprotein[1]
     mealcarbs += breakfastcarbs[1]
     mealfat += breakfastfats[1]

    elif i == "Toast":

     mealprepcalories += breakfastcalories[2]
     mealprotein += breakfastprotein[2]
     mealcarbs += breakfastcarbs[2]
     mealfat += breakfastfats[2]

    elif i == "Peanut Butter Bread":

     mealprepcalories += breakfastcalories[3]
     mealprotein += breakfastprotein[3]
     mealcarbs += breakfastcarbs[3]
     mealfat += breakfastfats[3]

    else:
     quit()

for i in lunchmp:
    if i  == "Chicken Rice":

     mealprepcalories += lunchcalories[0]
     mealprotein += lunchprotein[0]
     mealcarbs += lunchcarbs[0]
     mealfat += lunchfats[0]

    elif i  == "Bak Kut Teh with Rice":

     mealprepcalories += lunchcalories[1]
     mealprotein += lunchprotein[1]
     mealcarbs += lunchcarbs[1]
     mealfat += lunchfats[1]

    elif i == "Sliced Fish Soup with Rice":

     mealprepcalories += lunchcalories[2]
     mealprotein += lunchprotein[2]
     mealcarbs += lunchcarbs[2]
     mealfat += lunchfats[2]

    elif i == "Wanton Noodles":

     mealprepcalories += lunchcalories[3]
     mealprotein += lunchprotein[3]
     mealcarbs += lunchcarbs[3]
     mealfat += lunchfats[3]

    else:
     quit()

for i in dinnermp:
    if i  == "Chicken Chop with Rice":

     mealprepcalories += dinnercalories[0]
     mealprotein += dinnerprotein[0]
     mealcarbs += dinnercarbs[0]
     mealfat += dinnerfats[0]

    elif i  == "Steak & Fries":

     mealprepcalories += dinnercalories[1]
     mealprotein += dinnerprotein[1]
     mealcarbs += dinnercarbs[1]
     mealfat += dinnerfats[1]

    elif i == "Garden Salad with dressing":

     mealprepcalories += dinnercalories[2]
     mealprotein += dinnerprotein[2]
     mealcarbs += dinnercarbs[2]
     mealfat += dinnerfats[2]

    elif i == "Maggi Goreng":

     mealprepcalories += dinnercalories[3]
     mealprotein += dinnerprotein[3]
     mealcarbs += dinnercarbs[3]
     mealfat += dinnerfats[3]
    else:
     quit()

print(f"\nYour total kcal for this mealplan is: {mealprepcalories} kcal")
print(f"\nTotal Protein is: {mealprotein}g,  \nTotal Carbs is: {mealcarbs}g,  \nTotal Fat is: {mealfat}g")

if intcalorieamount < mealprepcalories:
  print(f"\nYou are in calorie excess")
elif intcalorieamount > mealprepcalories:
  print(f"\nYou are in calorie deficit")

