while True:
    print("================================")
    print("         BMI CALCULATOR")
    print("================================")
    print("1. Calculate BMI")
    print("2. View BMI Categories")
    print("3. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("\nEnter your name: ")
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"

        print("\n================================")
        print("           BMI RESULT")
        print("================================")
        print("Name:", name)
        print("Weight:", weight, "kg")
        print("Height:", height, "m")
        print("BMI:", round(bmi, 2))
        print("Category:", category)
        print("================================\n")

    elif choice == "2":
        print("\nBMI CATEGORIES")
        print("Below 18.5       : Underweight")
        print("18.5 to below 25 : Normal weight")
        print("25 to below 30   : Overweight")
        print("30 and above     : Obesity\n")

    elif choice == "3":
        print("\nThank you for using the BMI Calculator!")
        break

    else:
        print("\nInvalid choice. Please enter 1, 2, or 3.\n")