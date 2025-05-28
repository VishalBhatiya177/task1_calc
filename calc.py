categories = {
    "cloth" : [0],
    "mobile expenses" : [0],
    "home expenses" : [0],
    "tution fees" : [0]

} 



while True:
    userInput = input("select the categories - cloth/mobile expenses/home expenses/tution fees , to end the function type quit and see the total expenses : - ").lower().rstrip()
    if userInput == "quit":
        break

    elif userInput in categories:
        try:
            expense = float(input("enter the ammount here: "))
            categories[userInput].append(expense)

        except ValueError:
            print("invlid amount has been entered ")
    else:
        print("type the right categories")


totalExpenses = 0

for key , value in categories.items():
    categorieAmount = sum(value)
    print(f" {key} : {categorieAmount} ")
    totalExpenses += categorieAmount

print("total expenditure :" , totalExpenses )
