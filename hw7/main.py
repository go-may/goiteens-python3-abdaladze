from datetime import datetime

def checks_element_of_list(name_list, value_element):
    for element_of_list in name_list:
        if element_of_list == value_element: # value_element - есть ли такой элемент (мы этот элемент указали в функции мы просто его проверяем на существование)
            return "Да " + value_element + " есть" # value_element - если есть такой элемент то выводим
# 1
def menu():
    print ("Привет, я программа!")

# 2
def add_element_of_list(list, what):
    list.append(what)

# 4
def add_element_of_list_of_date(list, what):
    list.append(what)
    return datetime.now().day

list = []

print(add_element_of_list_of_date(list, "Text"))

# 5
def event(event):
    return event