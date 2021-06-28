class Date:
    days_in_months = [0, 31, 28, 31,  30,  31,  30,  31,  31,  30,  31, 30, 31]
    cum_days_in_months = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    month_names = ["", "January", "February", "March", "April", "May", "June", "July", "August", 
    "September", "October", "November", "December"]
    def __init__(self, day, month, year):
        if not 1 <= month <= 12:
            print("Invalid month")
            raise ValueError
        self.month = month
        self.day = day
        self.year = year
        if not 1 <= day <= Date.days_in_months[month] + self.leap_adjustment():
            print("Invalid day")
            raise ValueError      

    def __repr__(self):
        return "%02d %s, %d" %(self.day, (Date.month_names[self.month])[:3], self.year)

# logic: a number is divisible by 4 if its last 2 digits are divisible by 4

    def is_leap_year(self):
        yy = self.year // 100 if self.year % 100 == 0 else self.year % 100
        return yy % 4 == 0
    
    def leap_adjustment(self):
        return int(self.month == 2 and self.is_leap_year())

    def is_last_day(self):
        return self.day == Date.days_in_months[self.month] + leap_adjustment

    def is_first_day(self):
        return self.day == 1

    def tomorrow(self):
        if self.is_last_day():
            if self.month == 12:
                self.day, self.month = 1, 1
                self.year += 1
            else:
                self.day = 1
                self.month += 1
        else:
            self.day += 1

    def next_day(self, step = 1):
       for _ in range(step):
           self.tomorrow()
    
    def yesterday(self):
        if self.is_first_day():
            if self.month == 1:
                self.day, self.month = 31, 12
                self.year -= 1
            else:
                self.month -= 1
                self.day = Date.days_in_months[self.month] +self.leap_adjustment()
        else:
            self.day -= 1
       

    def prev_day(self, step = 1):
        for _ in range(step):
            self.yesterday()

d = Date(29, 2,2000)
print(d)
d.yesterday()
print(d)

