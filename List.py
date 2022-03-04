my_list = ["jan", "Feb", "Mar"]
print(my_list[2])
my_list.append("Apr")
print(my_list)
print (set(my_list))
print(type(my_list))
print(type(set(my_list)))

for element in my_list:
    print(element)

my_list.remove("Mar")
print(my_list)

