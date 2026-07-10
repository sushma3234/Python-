phone_book = {
    "Ram": "9841234567",
    "Sita": "9812345678",
    "Hari": "9801234567"
}

name = input("Enter name: ")

if name in phone_book:
    print("Phone number:", phone_book[name])
else:
    print("Contact not found")