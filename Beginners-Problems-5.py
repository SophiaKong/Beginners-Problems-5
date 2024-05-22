numsList = [7, 6, 23, 8.18, 18, 8, 7.2, 85, 915, 12]

# Finding the biggest number and its position
biggest_number = max(numsList)
biggest_position = numsList.index(biggest_number)

# Finding the smallest number and its position
smallest_number = min(numsList)
smallest_position = numsList.index(smallest_number)

# Calculating the average
average_number = sum(numsList) / len(numsList)

print(f"The biggest number is {biggest_number} at position {biggest_position}")
print(f"The smallest number is {smallest_number} at position {smallest_position}")
print(f"The average of the numbers is {average_number:.2f}")

stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]


count_same_start_end = 0

for string in stringsList:
    if string[0].lower() == string[-1].lower():
        count_same_start_end += 1

print(f"The number of strings that have the same start and end character is {count_same_start_end}")

iLikePesto = []
otherFoods = []

for _ in range(8):
    food = input("What's your favourite food? ").strip().lower()
    if food == "pesto":
        iLikePesto.append(food)
    else:
        otherFoods.append(food)

print(f"Pesto is loved by {len(iLikePesto)} people!")
for _ in range(len(iLikePesto)):
    print("I like pesto")

print("\nOther Foods:")
for food in otherFoods:
    print(food)

cerealList = []

while True:
    cereal = input("Enter Cereal: ").strip().lower()
    if cereal in ["sultana and bran", "weetbix"]:
        break
    cerealList.append(cereal)

print(cerealList)
