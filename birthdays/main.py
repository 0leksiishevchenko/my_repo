from datetime import datetime, timedelta, date
from collections import defaultdict

def get_birthdays_per_week(users):
    now = date.today()
    
    list_days = [now + timedelta(i) for i in range(7)]

    dict_tuple_days = {(date_.month, date_.day) : date_.strftime('%A') for date_ in list_days}
    dict_congrats = defaultdict(list)
    for user in users:
        user_birthday = user["birthday"]
        user_tuple_birthday = (user_birthday.month, user_birthday.day)
        if user_tuple_birthday in dict_tuple_days:
            dict_congrats[dict_tuple_days[user_tuple_birthday]].append(user["name"])

    if dict_congrats['Sunday'] + dict_congrats['Saturday'] and now.weekday() != 0:
        dict_congrats['Monday'] = dict_congrats['Saturday'] + dict_congrats['Sunday'] + dict_congrats['Monday']
    
    del dict_congrats['Saturday'], dict_congrats['Sunday']
    
    return dict(dict_congrats)


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
