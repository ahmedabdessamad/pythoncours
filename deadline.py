import datetime as date

user_input = input("enter your goal with a deadline separated by colon \n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
print(input_list)
print(goal)
print(deadline)

date_python = date.datetime.strptime(deadline, "%d.%m.%Y")
print(date_python)
print(type(date_python))

# calcul number of day wen you learn python.

to_day = date.datetime.today()
day_till = to_day - date_python
print(day_till.days)
