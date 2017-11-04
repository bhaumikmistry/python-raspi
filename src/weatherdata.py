from weather import Weather
'''
Wrapper for the weather api
since the api needs much more low level
inputs and formating on front end

weather = Weather()
Lookup WOEID via http://weather.yahoo.com.
Using https://github.com/AnthonyBloomer/weather-api

Get weather forecasts for the upcoming days.
forecasts = location.forecast()
for forecast in forecasts:
    print(forecast.text())
    print(forecast.date())
    print(forecast.high())
    print(forecast.low())
'''
class Weatherdata:

    def __init__(self):
        """
        Constructor with basic
        variable init

        @post   creates a weather object
                from weather api
        """
        self.woeid = -1
        self.city = ''
        self.tempc = 0.0
        self.tempf = 0.0
        self.weather = Weather()
    
    def addcity(self,cityname):
        """
        Adds city to the current object
        this object can only be used for
        this city name, or a new city name
        but can not be reinitialized with WOEID

        @param  cityname string
        @return void
        @post   creats a current city related object
        """
        if self.woeid < 0:
            self.city = cityname
            self.weather_obj = self.weather.lookup_by_location('{}'.format(cityname))

    def addwoeid(self,woeidint):
        """
        Adds city to the current object
        using woeid which is where on earth ID
        this object can only be used for
        this woeid, or a new woeid
        but can not be reinitialized with
        city names

        @param  woeid int
        @return void
        @post   creats a current city related object
        """
        if len(self.city) == 0:
            self.woeid = woeidint
            self.weather_obj = self.weather.lookup(woeidint)

    def getTemp(self,unit):
        """
        Uses the current city object and 
        gets temp in F, depedning upon the 
        unit string, it returns the F or C temp

        @param  unit String 'f' or 'c'
        @return Temprature String with unit append
        """
        self.tempf = int(self.weather_obj.condition()['temp'])
        if unit =='f':
            res = '{}{}'.format(self.tempf,unit.upper())
            return res
        elif unit == 'c':
            self.tempc = self.ftoc(self.tempf)
            res = '{}{}'.format(self.tempc,unit.upper())            
            return res
        else:
            return False

    def getTempCondition(self):
        """
        get Temprature condition in text
        sunny, rainy, cloudy, etc

        @param  none
        @return tempcondition String
        """
        self.tempcondition = self.weather_obj.condition()['text']
        return self.tempcondition


    def ftoc(self,f):
        """
        F to C convert
        private method for temp converions
        used by getTemp() and getFeelslike()
        @param  F int
        @return C int
        """
        c = (f - 32) * 5/9
        return c

    def getWind(self):
        """
        get wind related information 
        fetches wind, wind direction and wind unit

        @param none
        @return string 
        """
        degree = int(self.weather_obj.wind()['direction'])
        self.winddirection = self.degToCompass(degree)
        self.wind = int(self.weather_obj.wind()['speed'])
        self.windunit = self.weather_obj.units()['speed']
        res = '{} {} {}'.format(self.winddirection,self.wind,self.windunit)
        return res

    def getfeelslike(self,unit):
        """
        get feels like returns temprature
        change due to wind
        
        also known as chill

        @param  unit    String
        @return         String
        """
        self.feelslikef = int(self.weather_obj.wind()['chill'])
        if unit =='f':
            res = '{}{}'.format(self.feelslikef,unit.upper())
            return res
        elif unit == 'c':
            self.feelslikec = self.ftoc(self.feelslikef)
            res = '{}{}'.format(self.feelslikec,unit.upper())            
            return res
        else:
            return False

    def degToCompass(self,num):
        """
        Degree to Direction
        Used by the getWind() class rto convert
        degrees into direction
        
        @param  num     int
        @return         int
        """
        val=int((num/22.5)+.5)
        arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
        return arr[(val % 16)]

if __name__ == "__main__":
    wd = Weatherdata()
    wd.addwoeid(12758583)
    print(wd.getTemp('f'))
    print(wd.getTemp('c'))
    print(wd.getWind())
    print(wd.getTempCondition())
    print(wd.getfeelslike('c'))