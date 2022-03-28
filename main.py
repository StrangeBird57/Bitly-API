# import file_operations
# from faker import Faker
import random

ALPHABET = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

SKILLS = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд'
]


def rewrite_on_runic(text):
    runic_text = ""
    for symbol in text:
        runic_text += ALPHABET[symbol]
    return runic_text


def create_character(fake):
    character_skills = random.sample(SKILLS, 3)
    for i in range(len(character_skills)):
        character_skills[i] = rewrite_on_runic(character_skills[i])
    print(1)
    # context = {
    #     "job": fake.job(),
    #     "town": fake.city(),
    #     "strength": random.randint(3, 18),
    #     "agility": random.randint(3, 18),
    #     "endurance": random.randint(3, 18),
    #     "intelligence": random.randint(3, 18),
    #     "luck": random.randint(3, 18),
    #     "skill_1": character_skils[0],
    #     "skill_2": character_skils[1],
    #     "skill_3": character_skils[2],
    # }
    #
    # if random.randint(1, 100) % 2:
    #     context["first_name"] = fake.first_name_male()
    #     context["last_name"] = fake.last_name_male()
    # else:
    #     context["first_name"] = fake.first_name_female()
    #     context["last_name"] = fake.last_name_female()
    #
    # file_operations.render_template("charsheet.svg", "result.svg", context)


def main():
    fake =1# Faker("ru_RU")
    create_character(fake)


if __name__ == '__main__':
    main()
