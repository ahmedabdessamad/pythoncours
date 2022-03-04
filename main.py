from Helper import  get_your_age



print("hello Ahmed Abdessamad your age is " + str(27) + "years")
print(f"hello Ahmed Abdessamad your age is {27 * 365 * 24 * 60 * 60} sec")

to_sec = 27 * 365 * 24 * 60 * 60
print(f"hello Ahmed Abdessamad your age is " + str(to_sec) + " sec")
print("hello Ahmed Abdessamad your age is " + str(to_sec / 60) + " minutes")
print(f"hello Ahmed Abdessamad your age is {to_sec} sec")


def birth_day_to_days():
    print(f"hello Ahmed Abdessamad your age is " + str(to_sec / 60 / 60) + " hours")


birth_day_to_days()


def get_number_of_day(age):
    print(f"hello Ahmed Abdessamad your age is " + str(age * 365) + " days")


get_number_of_day(35)

Name = "Ayoub"


def message(age, costum_message):
    print("your age is " + str(age) + " good luck " + str(costum_message) + "")


message(27, "Ahmed")
message(27, Name)



    # print(type(age))


def while_function():
    test = ""
    while test != "exit":
        test = input("hey, enter your birdhdaay\n")
        get_your_age(test)


def get_ower_age():
    birdh_days = input("hey, the 5 number of birdhdaay\n")
    for birdh in birdh_days.split(","):
        get_your_age(birdh)


get_ower_age()
# while_function()
