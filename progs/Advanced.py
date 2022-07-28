class TimeInterval:
    def __init__(self, hours, minutes, seconds):
        self.check_data_type(hours, minutes, seconds)
        self.hours = hours
        self.minutes = minutes
        self.s = seconds
        self.check_data_consistency()
        self.seconds = seconds + minutes*60 + hours*3600
        self.result="{0:02d}:{1:02d}:{2:02d}"

    def __str__(self):
        return self.result.format(self.hours, self.minutes, self.s)

    def __add__(self, other):
        return self.result.format((self.seconds + other.seconds) // 3600, ((self.seconds + other.seconds) % 3600) // 60, ((self.seconds + other.seconds) %3600) %60)

    def __mul__(self, other):
        return self.result.format((self.seconds * other) // 3600, ((self.seconds * other) % 3600) // 60, ((self.seconds * other) % 3600) % 60)

    def __sub__(self, other):
        return self.result.format((self.seconds - other.seconds) // 3600, ((self.seconds - other.seconds) % 3600) // 60, ((self.seconds - other.seconds) % 3600) %60)

    def check_data_consistency(self):
        try:
            assert 0 <= self.hours <= 23
            assert 0 <= self.minutes <= 59
            assert 0 <= self.s <= 59
        except AssertionError:
            print("This is AssertionError, program will exit")
            exit()

    def check_data_type(self, *args):
        check_types_result = list(map(lambda x: type(x) is int, args))
        if False in check_types_result:
            print ("Incorrect data, program will exit")
            exit()

    def next_seconds(self, adseconds):
        self.adseconds= self.seconds+ adseconds
        return self.result.format(self.adseconds // 3600, (self.adseconds % 3600) // 60, (self.adseconds %3600) %60)

    def prev_seconds(self, suseconds):
        self.suseconds = self.seconds - suseconds
        return self.result.format(self.suseconds // 3600, (self.suseconds % 3600) // 60, (self.suseconds % 3600) % 60)

fti = TimeInterval(21, 58, 50)
sti = TimeInterval(1, 45, 22)
print(fti)
print(sti)
print(fti + sti)
print(fti * 2)
print(fti - sti)
print(fti.next_seconds(62))
print(fti.prev_seconds(62))
