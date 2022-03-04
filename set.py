my_set = {"Jan", "Feb", "Mar"}
#item in a set do not have a defined order
#item connot be reffrec to by index!
#item connot by changed , only read/remove

for element in my_set:
    print(element)

my_set.add("ahmed")
print(my_set)

my_set.remove("Jan")
print(my_set)