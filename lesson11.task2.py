import json

def load_phonebook(book_name):
    try:
        with open(book_name + '.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_phonebook(book_name, phonebook):
    with open(book_name + '.json', 'w') as f:
        json.dump(phonebook, f)

def add_record(phonebook):
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    phone = input("Введите номер телефона: ")
    city = input("Введите город: ")
    record = {
        "name": name,
        "surname": surname,
        "phone": phone,
        "city": city
    }
    phonebook[phone] = record
    print("Запись успешно добавлена")

def search_by_name(phonebook):
    name = input("Введите имя: ")
    matches = []
    for record in phonebook.values():
        if record["name"] == name:
            matches.append(record)
    if matches:
        for match in matches:
            print(match)
    else:
        print("Записи не найдены")

def search_by_surname(phonebook):
    surname = input("Введите фамилию: ")
    matches = []
    for record in phonebook.values():
        if record["surname"] == surname:
            matches.append(record)
    if matches:
        for match in matches:
            print(match)
    else:
        print("Записи не найдены")

def search_by_fullname(phonebook):
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    matches = []
    for record in phonebook.values():
        if record["name"] == name and record["surname"] == surname:
            matches.append(record)
    if matches:
        for match in matches:
            print(match)
    else:
        print("Записи не найдены")

def search_by_phone(phonebook):
    phone = input("Введите номер телефона: ")
    record = phonebook.get(phone)
    if record:
        print(record)
    else:
        print("Запись не найдена")

def search_by_city(phonebook):
    city = input("Введите город: ")
    matches = []
    for record in phonebook.values():
        if record["city"] == city:
            matches.append(record)
    if matches:
        for match in matches:
            print(match)
    else:
        print("Записи не найдены")

def remove_record(phonebook):
    phone = input("Введите номер телефона: ")
    record = phonebook.pop(phone, None)
    if record:
        print("Запись успешно удалена")
    else:
        print("Запись не найдена")

def update_record(phonebook):
    phone = input("Введите номер телефона: ")
    record = phonebook.get(phone)
    if record:
        name = input(f"Введите новое имя ({record['name']}): ")
        surname = input(f"Введите новую фамилию ({record['surname']}): ")
        city = input(f"Введите новый город ({record['city']}): ")
        new_record = {
            "name": name if name else record["name"],
            "surname": surname if surname else record["surname"],
            "phone": phone,
            "city": city if city else record["city"]
        }
        phonebook[phone] = new_record
        print("Запись успешно обновлена")
    else:
        print("Запись не найдена")

def main():
    book_name = input("Введите имя телефонной книги: ")
    phonebook = load_phonebook(book_name)
    while True:
        action = input("Выберите действие: (1) добавить запись, (2) поиск по имени, (3) поиск по фамилии, \
            (4) поиск по полному имени, (5) поиск по номеру телефона, (6) поиск по городу или штату, \
            (7) удалить запись, (8) обновить запись, (9) выход: ")
        if action == "1":
            add_record(phonebook)
        elif action == "2":
            search_by_name(phonebook)
        elif action == "3":
            search_by_surname(phonebook)
        elif action == "4":
            search_by_fullname(phonebook)
        elif action == "5":
            search_by_phone(phonebook)
        elif action == "6":
            search_by_city(phonebook)
        elif action == "7":
            remove_record(phonebook)
        elif action == "8":
            update_record(phonebook)
        elif action == "9":
            save_phonebook(book_name, phonebook)
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
