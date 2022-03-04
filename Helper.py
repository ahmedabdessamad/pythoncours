def get_your_age(birth_day):
    try:
        # birth_day = input("enter your birthday\n")
        if birth_day.isdigit():  # bech nét2akdou ennou number
            birth_day_number = int(birth_day)

            if birth_day_number < 1990:
                print("generation 3al 7éééééééééééééét ")
                age = 2022 - birth_day_number
                print(str(age))
                age_dictionary = {"age": age, "unit": "year"}
                print(age_dictionary["age"])

                print(age_dictionary)
            elif birth_day_number > 2000:
                print("generation yar7ém 3ammi")
                age = 2022 - birth_day_number
                print(str(age))
                age_dictionary = {"age": age, "unit": "year"}
                print(age_dictionary)
                print(age_dictionary["age"])
            elif birth_day_number == 1994:
                print("3id milad lem3alééééééém")
                age = 2022 - birth_day_number
                print(str(age))
                age_dictionary = {"age": age, "unit": "year"}
                print(age_dictionary)
                print(age_dictionary["age"])
            else:
                print("generation el 7oooooooooooob")
                age = 2022 - birth_day_number
                print(str(age))
                age_dictionary = {"age": age, "unit": "year"}
                print(age_dictionary)
                print(age_dictionary["age"])
        else:
            print("enter a number")
    except ValueError:
        print("famma mochkol fi code !!")
