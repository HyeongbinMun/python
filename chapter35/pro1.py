class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    @staticmethod
    def is_time_valid(time):
        hour, minute, secend = map(int, time.split(':'))
        if hour >= 24 or minute >= 60 or secend >= 60:
            return False
        else:
            return True
    @classmethod
    def from_string(cls, time):
        hour, minute, second = map(int, time.split(':'))
        ti = cls(hour, minute, second)
        return ti

time_string = input()
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')