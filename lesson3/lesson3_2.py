def base(name, surname, year, town, email, phone_number):
    full_base = f'Name: {name}, Surname: {surname}, Year: {year}, Town: {town}, Email: {email}, Number: {phone_number}'
    return full_base


print("1 - Name, 2 - Surname, 3 - year, 4 - Town, 5 - Email, 6 - Phone number ")
print(base(name=input(), surname=input(), year=input(), town=input(), email=input(), phone_number=input()))
