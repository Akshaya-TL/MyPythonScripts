class mycalendar:

     def __init__(self, DDMMYYYY):
        if type(DDMMYYYY) != str:
            raise TypeError
        self.DDMMYYYY = DDMMYYYY
        if len(self.DDMMYYYY) < 8:
            raise ValueError
        self.date  = int(self.DDMMYYYY[:2])
        self.month = int(self.DDMMYYYY[2:4])
        self.year  = int(self.DDMMYYYY[4:])
        self.reminder = ['add reminder'] * 5
        self.valid_dates = { 1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31} 
    
     def __repr__(self):
         return f'self.prev_date() << {self.date}/{self.month}/{self.year} << self.nxt_date()' 

     def DEBUG(self):
         return ''' Input Date: %d/%d/%d \n Day:   %s \n It is a leap year: %s \n Reminders: %s \n nxt_date: %s \n prev_date: %s'''%(selfdate, self.month, self.year, self.day(), self.isleapyear(self.year), self[:], self.nxt_date(), self.prev_date())

     def isleapyear(self,input_year):
         self.input_year = input_year
         if self.input_year % 100 != 0:
             return self.input_year % 4 == 0
         return self.input_year % 400 == 0

     def odd_day_calc(self):
         self.month_wise = {1: 3, 3: 3, 4: 2, 5: 3, 6: 2, 7: 3, 8: 3, 9: 2, 10: 3, 11: 2, 12: 3}
         if self.isleapyear(self.year):
             self.month_wise[2] = 1
         else:
             self.month_wise[2] = 0

         # algorithm for odd day calculation
         self.year_odd_days  = 0
         self.month_odd_days = 0
         for year in range(1, self.year % 400):
             if self.isleapyear(year):
                 self.year_odd_days += 2
             else:
                 self.year_odd_days += 1
         
         for month in range(1,self.month):
             self.month_odd_days += self.month_wise[month]

         self.total_odd_days = self.year_odd_days + self.month_odd_days + self.date % 7
         return self.total_odd_days % 7

     def day(self):
         self.day = {0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'}
         return self.day[self.odd_day_calc()]

     def __setitem__(self, number, data):
         self.reminder[number - 1] = data

     def __getitem__(self, index):
         return self.reminder[index]

     def age_calculator(self, DOB, input_date):
         self.DOB        = str(DOB)
         self.input_date = str(input_date)
         if int(self.DOB[2:4]) <= int(self.input_date[2:4]):
             self.age_years = int(self.input_date[4:]) - int(self.DOB[4:])
         else:
             self.age_years = int(self.input_date[4:]) - int(self.DOB[4:]) -1
         
         if int(self.DOB[:5]) == int(self.input_date[:5]):
             self.age_months = 0
         elif int(self.DOB[:2]) >= int(self.input_date[:2]):
             self.age_months = 12 - int(self.DOB[2:4]) + int(self.input_date[2:4]) 
         else: 
             self.age_months = 12 -  int(self.DOB[2:4]) + int(self.input_date[2:4]) - 1
         return f' You are {self.age_years} years and {self.age_months} months.'  
     
     def nxt_date(self):
         if self.isleapyear(self.year):
            self.valid_dates[2] = 29
         else:
             self.valid_dates[2] = 28
         self.date += 1
         while self.date not in range(1, self.valid_dates[self.month] + 1):
               self.date = 1
               self.month += 1
               while self.month not in range(1,13):
                   self.month = 1
                   self.year += 1
         return f' %d/%d/%d'%(self.date, self.month, self.year)

     def prev_date(self):
         if self.isleapyear(self.year):
            self.valid_dates[2] = 29
         else:
             self.valid_dates[2] = 28
         self.date -= 1
         while self.date not in range(1, self.valid_dates[self.month] + 1):
             self.date = self.valid_dates[self.month - 1]
             self.month -= 1
         return f'%d/%d/%d'%(self.date, self.month, self.year)

m = mycalendar('25032020')
m[1] = ' Session @ ZOOM '
m[2] = ' hello ' 
print(m.DEBUG())
print(m.nxt_date())
print(m.age_calculator(23112001,23032020))
print(m.age_calculator(23112001,23112020))
