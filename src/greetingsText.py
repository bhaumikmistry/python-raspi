import datetime

class TimeDate:

    def __init__(self):
        """
        init all the global class variable 

        constructor 
        """
        print("Object created")
        print("Variables updated")
        now = datetime.datetime.now()
        self.m_hour = now.hour
        self.m_mins = now.minute
        self.m_year = now.year
        self.m_month = now.month
        self.m_day = now.day
        self.m_time = now.time
        self.m_date = now.date
        self.m_weekday = datetime.datetime.today().weekday()

    def get_time(self):
        """
        return time in hh:mm format
        
        @param  none
        @return time string
        """
        res = '{}:{}'.format(self.m_hour, self.m_mins)
        return res

    def get_date(self):
        """
        return date in mm/dd/yyyy
        
        @param  none
        @return date string
        """
        res = '{}/{}/{}'.format(self.m_month, self.m_day, self.m_year)
        return res

    def join_string(self,one,two):
        """
        Private method to join two strings

        @param  string one
        @param  string two
        @reurn  addition of one and two
        """
        res = '{} {}'.format(one,two)
        return res

    def get_greetings(self):
        """
        Depending upon time and day it reurns greetings
    
        @param  none
        @return string
        """
        print(self.m_hour)
        print(self.m_weekday)
        greeting = "Have a good day"
        if self.m_hour >= 5 and self.m_hour < 12:
            greeting = "Good Morning"

        if self.m_hour >= 12 and self.m_hour < 15:
            greeting = "Good Afternoon"

        if self.m_hour >= 15 and self.m_hour < 17:
            greeting = "Good Evening"
        
        if self.m_hour >= 17 or self.m_hour < 5:
            greeting = "Good Night"

        if self.m_hour >= 5 and self.m_hour < 17 and self.m_weekday == 4:
            greeting = self.join_string(greeting,"Happy Friday")

        if self.m_hour >= 17 and self.m_hour < 5 and self.m_weekday == 4:
            greeting = self.join_string(greeting,"Have a good Weekend")

        if self.m_weekday == 5 or self.m_weekday == 6:
            greeting = self.join_string(greeting,"Happy Weekend")
        return greeting