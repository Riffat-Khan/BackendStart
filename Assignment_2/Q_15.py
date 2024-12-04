# Write a program that take 10-time, name (string) and marks (integer) as an input from the
# user. Populate a list such that all even indices have name and odd indices with the
# corresponding marks. e.g. [‘Ahmad’, 29, ‘Asad’, 15, ‘Zainab’, 20]. At the end print the list.
# Hint: You can use append function of list data type.


def data(name , marks):
    list = []
    for i in range(10):
        name = input("Enter student's name: ")
        marks = input ("Enter student's marks: ")
        list.append(name)
        list.append(int(marks))

    print(list)

data(name="" , marks=0)
