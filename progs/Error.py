class WeekDayError(Exception):
    pass


class Weeker:
    week = {'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6, 'Sun': 7}

    def __init__(self, day):
        if day in Weeker.week.keys():
            self.number = Weeker.week[day]
        else:
            raise WeekDayError

    def __str__(self):
        for key, value in Weeker.week.items():
            if self.number == value:
                return key

    def add_days(self, n):
        self.number = (self.number + n) % 7

    def subtract_days(self, n):
        if n % 7 != 0:
            self.number = (7 - (n % 7) + self.number)
        print(self.number)
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')

except WeekDayError:
    print("Sorry, I can't serve your request.")