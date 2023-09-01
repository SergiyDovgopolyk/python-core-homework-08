from datetime import date, datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    current_date = date.today()
    current_year = current_date.year
    current_day_of_week = current_date.strftime('%A')

    # Словник для збереження імен користувачів
    birthdays_per_week = defaultdict(list)

    if users:
        for user in users:
            name = user['name']
            birthday = user['birthday']
            birthday_this_year = birthday.replace(year=current_year)
            if birthday < current_date:
                continue

            elif birthday_this_year < current_date:
                # День народження вже минув у цьому році, перевіряємо на наступний рік. Ось тут помику не можу зрозуміти
                birthday_this_year = birthday.replace(year=current_year + 1)
            
            elif birthday_this_year.weekday() >= 5:
                # Якщо день народження випав на вихідний, то відображаємо його в понеділок
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
                
            day_name = birthday_this_year.strftime('%A')
            birthdays_per_week[day_name].append(name)
    else:
        return dict()

    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

