from datetime import datetime, timedelta


users = [
    {'name': 'Andy', 'birthday': datetime(year=2000, month=4, day=21)},
    {'name': 'Bill', 'birthday': datetime(year=1993, month=4, day=21)},
    {'name': 'Sarah', 'birthday': datetime(year=1983, month=4, day=22)},
    {'name': 'Ted', 'birthday': datetime(year=2001, month=4, day=23)},
    {'name': 'Casey', 'birthday': datetime(year=1998, month=4, day=24)},
    {'name': 'Tina', 'birthday': datetime(year=1993, month=4, day=24)},
    {'name': 'Lisa', 'birthday': datetime(year=2020, month=4, day=25)},
    {'name': 'John', 'birthday': datetime(year=1997, month=4, day=26)},
    {'name': 'Kris', 'birthday': datetime(year=1991, month=4, day=27)},
    {'name': 'Stive', 'birthday': datetime(year=1995, month=4, day=28)},

    {'name': 'Dyke', 'birthday': datetime(year=2000, month=4, day=20)},
    {'name': 'Kan', 'birthday': datetime(year=1993, month=4, day=19)},
    {'name': 'Inga', 'birthday': datetime(year=1983, month=4, day=29)},
    {'name': 'Elisa', 'birthday': datetime(year=2001, month=4, day=30)},
    {'name': 'Philipe', 'birthday': datetime(year=1998, month=5, day=1)},
    {'name': 'Alex', 'birthday': datetime(year=1993, month=5, day=2)},
    {'name': 'Rita', 'birthday': datetime(year=2020, month=5, day=3)},
    {'name': 'Roy', 'birthday': datetime(year=1997, month=5, day=4)},
    {'name': 'Henry', 'birthday': datetime(year=1991, month=5, day=5)},
    {'name': 'Mikhel', 'birthday': datetime(year=1995, month=5, day=6)},
    {'name': 'Rita', 'birthday': datetime(year=2020, month=5, day=7)},

    {'name': 'Kris', 'birthday': datetime(year=1997, month=5, day=8)},
    {'name': 'Andy', 'birthday': datetime(year=1991, month=5, day=9)},
    {'name': 'Kan', 'birthday': datetime(year=1995, month=5, day=10)}
   
]


def get_birthdays_per_week(users: list) -> None:

    FDAYS = 7
    curent_day = datetime.today()
    exect_list = ['Saturday','Sunday']
    seven_days_list = []
    exect = ''
    
    
    if curent_day.strftime('%A') == 'Monday':
        curent_day -= timedelta(days=2)
    
    for d in range(FDAYS):
    
        delta = timedelta(days = d)
        seven_days_list.append(curent_day.date() + delta)

    print(seven_days_list)

   
    for item in seven_days_list:
        names = ''
        
        for user in users:
            if user['birthday'].month == item.month and user['birthday'].day == item.day:
                
                name_day = item.strftime('%A')  
                user_name = user['name']

                if name_day not in exect_list:
                    if names != '':
                        names = ', '.join([names, user_name])
                    else:
                        names = user_name
                else:
                    if exect != '':
                        exect = ', '.join([exect, user_name])
                    else:
                        exect = user_name
            
        if name_day in exect_list:
            pass
        elif name_day == 'Monday':
            print(f'{name_day}: {names}, {exect}')
        else:
            print(f'{name_day}: {names}')
    print(exect)
        

    

get_birthdays_per_week(users)