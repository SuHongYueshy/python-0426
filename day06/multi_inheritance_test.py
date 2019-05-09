class Clock(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


class Calendar(object):

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class CalendarClock(Calendar, Clock):

    def __init__(self, year, month, day, hour, minute, second):
        Calendar.__init__(self, year, month, day)
        Clock.__init__(self, hour, minute, second)

    def display(self):
        print('%d-%d-%d %d:%d:%d' % (self.year, self.month, self.day, self.hour, self.minute, self.second,))


cc = CalendarClock(2019, 5, 6, 14, 50, 60)

cc.display()