# Go to your implementation of the Phonebook application from module 1 or any other comprehensive code, which you have
# done during the course, and annotate this code with type hints, using knowledge from this lesson.
import json

with open("phonebook.json", "r+") as file:
    data_json = json.load(file)


def search_by_number():
    search_number = input("Write the number which you want search: ")
    if len(search_number) == 10 and search_number.isdigit():
        if search_number in data_json.keys():
            print(data_json[search_number])
        else:
            print("Nothing found")
    else:
        print("Write the number without letters wih lenght 10: ")
        return search_by_number()


def search_by_name():
    search_name = input("Write the name which you want search: ").capitalize()
    numbers_of_contacts = 0
    if search_name.isdigit():
        print("Please write a name not a number")
        return search_by_name()
    else:
        for number, data in data_json.items():
            if search_name == data["name"]:
                print(number, data["last_name"], data["name"], data["city"])
                numbers_of_contacts += 1
        if numbers_of_contacts == 0:
            print("Nothing found")


def search_by_last_name():
    search_last_name = input("Write the last name which you want search: ").capitalize()
    numbers_of_contacts = 0
    if search_last_name.isdigit():
        print("Please write a last name not a number")
        return search_by_last_name()
    else:
        for number, data in data_json.items():
            if search_last_name == data.get("last_name"):
                print(number, data["last_name"], data["name"], data["city"])
                numbers_of_contacts += 1
        if numbers_of_contacts == 0:
            print("Nothing found")


def search_by_full_name():
    search_name = input("Write the name which you want search: ").capitalize()
    search_last_name = input("Write the last name which you want search: ").capitalize()
    numbers_of_contacts = 0
    if search_last_name.isdigit() or search_name.isdigit():
        print("Please write letters not a number")
        return search_by_full_name()
    else:
        for number, data in data_json.items():
            if search_name == data.get("name") and search_last_name == data.get("last_name"):
                print(number, data["last_name"], data["name"], data["city"])
                numbers_of_contacts += 1
        if numbers_of_contacts == 0:
            print("Nothing found")


def search_by_city():
    search_city = input("Write the city where live person which you want search: ").capitalize()
    numbers_of_contacts = 0
    if search_city.isdigit():
        print("Please write letters not a number")
        return search_by_full_name()
    else:
        for number, data in data_json.items():
            if search_city == data.get("city"):
                print(number, data["last_name"], data["name"], data["city"])
                numbers_of_contacts += 1
        if numbers_of_contacts == 0:
            print("Nothing found")


def creating_new_contact():
    new_number = input("Write a number: ")
    new_name = input("Write a name: ").capitalize()
    new_last_name = input("Write a last_name: ").capitalize()
    new_city = input("Write a city: ").capitalize()
    data_json[new_number] = {
        "name": new_name,
        "last_name": new_last_name,
        "city": new_city
    }


def deleting_contact():
    del_contact = input("write a number which you want delete:  ")
    if del_contact in data_json.keys():
        del data_json[del_contact]


def update_number():
    update_phone_number = input("Write a number which datas you want change: ")
    update_name = input("Write a new name: ").capitalize()
    update_last_name = input("Write a new last name: ").capitalize()
    update_city = input("Write a new city: ").capitalize()
    numbers_of_contacts = 0
    for number, datas in data_json.items():
        if number == update_phone_number:
            datas["name"] = update_name
            datas["last_name"] = update_last_name
            datas["city"] = update_city
            numbers_of_contacts += 1
    if numbers_of_contacts == 0:
        print("Nothing found")


def phonebook_menu():
    answer = 0
    while answer != 9:
        answer = input("1 add new contact\n"
                       "2 search by the name            3 search by the last name\n"
                       "4 search by the full name       5 search by the number\n"
                       "6 search by the city            7 delete number\n"
                       "8 update number\n"
                       "9 exit\n"
                       "Please write a number between 1-9\n")
        if answer == "1":
            creating_new_contact()
        elif answer == "2":
            search_by_name()
        elif answer == "3":
            search_by_last_name()
        elif answer == "4":
            search_by_full_name()
        elif answer == "5":
            search_by_number()
        elif answer == "6":
            search_by_city()
        elif answer == "7":
            deleting_contact()
        elif answer == "8":
            update_number()
        elif answer == "9":
            with open('phonebook.json', 'w') as b_file:
                json.dump(data_json, b_file, ensure_ascii=False, indent=4)


phonebook_menu()
