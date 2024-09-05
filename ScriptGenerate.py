import random
import string
import os
import hashlib
from datetime import datetime
from faker import Faker
from pystyle import Colors, Colorate, Center
import qrcode

fake = Faker()

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def generate_custom_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Невозможно создать пароль: не выбраны символы для использования.")
    
    return ''.join(random.choice(characters) for _ in range(length))

def prompt_password_criteria():
    length = int(input("Введите длину пароля: "))
    use_uppercase = input("Использовать заглавные буквы? (y/n): ").lower() == 'y'
    use_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
    use_symbols = input("Использовать символы? (y/n): ").lower() == 'y'
    
    return generate_custom_password(length, use_uppercase, use_digits, use_symbols)

def generate_number(country_code):
    number = fake.phone_number()
    return f"+{country_code} {number}"

def generate_identity():
    return fake.name()

def generate_mullvad_key():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

def generate_discord_token():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(59))

def generate_credit_card():
    return fake.credit_card_number(card_type=None)

def generate_email():
    return fake.email()

def generate_birthdate():
    return fake.date_of_birth()

def generate_uuid():
    return fake.uuid4()

def generate_mac():
    return fake.mac_address()

def generate_address():
    return fake.address()

def generate_username():
    return fake.user_name()

def generate_quote():
    return fake.sentence()

def generate_company():
    return fake.company()

def generate_job():
    return fake.job()

def generate_license_plate():
    return fake.license_plate()

def generate_ssn():
    return fake.ssn()

def generate_coordinates():
    latitude = round(random.uniform(-90.0, 90.0), 6)
    longitude = round(random.uniform(-180.0, 180.0), 6)
    return f"Latitude: {latitude}, Longitude: {longitude}"

def generate_fake_news():
    headlines = [
        "Ученые обнаружили новый вид насекомых в Амазонке",
        "Известный актер объявил о своем участии в новом проекте",
        "Исследование показало, что шоколад полезен для здоровья",
        "Новая технология обещает революцию в медицине",
        "Археологи нашли древний артефакт в Египте"
    ]
    bodies = [
        "Сегодня утром команда исследователей сообщила о своем открытии.",
        "Событие вызвало бурную реакцию в социальных сетях.",
        "Эксперты предсказывают значительное влияние на индустрию.",
        "Местные жители выражают свою поддержку.",
        "Новость распространилась с невероятной скоростью."
    ]
    return f"Headline: {random.choice(headlines)}\nBody: {random.choice(bodies)}"

def generate_color_palette():
    def random_color():
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))
    palette = [random_color() for _ in range(5)]
    return palette

def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img_path = "qrcode.png"
    img.save(img_path)
    return img_path

def generate_bitcoin_address():
    return fake.cryptocurrency_address()

def generate_bitcoin_private_key():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(64))

def generate_stock_profile():
    return {
        "company": fake.company(),
        "symbol": ''.join(random.choices(string.ascii_uppercase, k=4)),
        "price": round(random.uniform(10, 1000), 2),
        "volume": random.randint(1000, 1000000)
    }

def generate_medical_profile():
    return {
        "name": fake.name(),
        "age": random.randint(0, 100),
        "blood_type": random.choice(["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]),
        "conditions": [fake.word() for _ in range(random.randint(0, 5))]
    }

def generate_passport_details():
    return {
        "passport_number": ''.join(random.choices(string.ascii_uppercase + string.digits, k=9)),
        "name": fake.name(),
        "nationality": fake.country(),
        "birthdate": fake.date_of_birth(),
        "expiry_date": fake.date_between(start_date="today", end_date="+10y")
    }

def print_gradient_text(text):
    print(Colorate.Vertical(Colors.blue_to_cyan, text))

def print_menu():
    title = """
░██████╗░█████╗░██████╗░██╗██████╗░████████╗░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗███████╗
██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░█████╗░░
░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██╔══╝░░
██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░███████╗
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
"""
    developer = "Developer: Killstraut | Timmu"
    lines = "═" * 72

    print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(title)))
    print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(developer)))
    print("\n" + Center.XCenter(lines))
    
    menu = """
╔═══════════════════════════════════════════════════════════════════════════════════╗
║  1. Генерация Пароля             15. Генерация Должности                          ║
║  2. Генерация Номера             16. Генерация Номера Лицензии                    ║
║  3. Генерация Личности           17. Генерация SSN                                ║
║  4. Генерация Ключей Мулвад      18. Генерация QR-кода                            ║
║  5. Генерация Токенов Дискорд    19. Генерация Координат                          ║
║  6. Генерация Банковской Карты   20. Генерация Фальшивых Новостей                 ║
║  7. Генерация Email              21. Генерация Цветовых Палитр                    ║
║  8. Генерация Даты Рождения      22. Генерация QR-кода                            ║
║  9. Генерация UUID               23. Генерация Адреса Биткойна                    ║
║ 10. Генерация MAC-адреса         24. Генерация Приватного Ключа Биткойна          ║
║ 11. Генерация Адреса             25. Генерация Профиля Акций                      ║
║ 12. Генерация Имени Пользователя 26. Генерация Медицинского Профиля               ║
║ 13. Генерация Цитаты             27. Генерация Паспортных Данных                  ║
║ 14. Генерация Названия Компании  0. Выход                                         ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
"""

    print(Center.XCenter(menu))
    choice = input("\nВыберите опцию: ")
    return choice

def main():
    while True:
        choice = print_menu()
        if choice == "0":
            break
        elif choice == "1":
            print(generate_password())
        elif choice == "2":
            print(prompt_password_criteria())
        elif choice == "3":
            print(generate_number("1"))
        elif choice == "4":
            print(generate_identity())
        elif choice == "5":
            print(generate_mullvad_key())
        elif choice == "6":
            print(generate_discord_token())
        elif choice == "7":
            print(generate_credit_card())
        elif choice == "8":
            print(generate_email())
        elif choice == "9":
            print(generate_birthdate())
        elif choice == "10":
            print(generate_uuid())
        elif choice == "11":
            print(generate_mac())
        elif choice == "12":
            print(generate_address())
        elif choice == "13":
            print(generate_username())
        elif choice == "14":
            print(generate_quote())
        elif choice == "15":
            print(generate_company())
        elif choice == "16":
            print(generate_job())
        elif choice == "17":
            print(generate_license_plate())
        elif choice == "18":
            data = input("Введите данные для QR-кода: ")
            qr_path = generate_qr(data)
            print(f"QR-код сохранен по пути {qr_path}")
        elif choice == "19":
            print(generate_coordinates())
        elif choice == "20":
            print(generate_fake_news())
        elif choice == "21":
            print(generate_color_palette())
        elif choice == "22":
            data = input("Введите данные для QR-кода: ")
            qr_path = generate_qr(data)
            print(f"QR-код сохранен по пути {qr_path}")
        elif choice == "23":
            print(generate_bitcoin_address())
        elif choice == "24":
            print(generate_bitcoin_private_key())
        elif choice == "25":
            print(generate_stock_profile())
        elif choice == "26":
            print(generate_medical_profile())
        elif choice == "27":
            print(generate_passport_details())
        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")
        input("\nНажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    main()
