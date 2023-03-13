# Add your code here

#Date class
class Date:
    #constructor for the day, month and year
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

    #built in str function to return the date format
    def __str__(self):
        return "day:" + self.day + ",month:" + self.month + ",year:" + self.year
        
#Datetime class that inherits the Date class
class DateTime(Date):
    #The constructor while also calling the super for the varibales from the Date class
    def __init__(self,day,month,year,hours,minutes,seconds):
        super().__init__(day,month,year)
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    #calls the super class and add additional ouput
    def __str__(self):
        return super().__str__() + "--" + self.hours+":"+ self.minutes+":"+self.seconds

#function to convert the dates and passes the specific format
def DateConvertor(dateFormat):
    #Another function to go through the dates that have been passed through
    # "*" is used since it allows you to pass an arbitrary number of arguments to a function
    # it will unpack the dates into separate elements, so the for loop can later go through each of them
    def newFormat(*rawDates):
        #an array for the dates are created
        dates = []
        #For loop for each date that is passed through
        for rawDate in rawDates:
            #The dates are cleaned so the hypens are removed
            dateArray =  rawDate.split("-")

            #if statements to check what type of formatted is required
            #then the dates are fixed accordingly and added to the date array
            if dateFormat == "Big":
                dates.append(Date(dateArray[2],dateArray[1],dateArray[0]))
                
            elif dateFormat == "Little":
                dates.append(Date(dateArray[0],dateArray[1],dateArray[2]))
                
            elif dateFormat == "Middle":
                dates.append(Date(dateArray[1],dateArray[0],dateArray[2]))
        #returns the dates array
        return dates
    #the function to actually converts the dates, it is returned so that it is actually called when
    #DateConvertor is called
    return newFormat


# Please use the following names to recieve the corresponding functions as they return from the outer function calls
bigEndianParser = DateConvertor("Big")
littleEndianParser = DateConvertor("Little")
middleEndianParser = DateConvertor("Middle")

# Testing
def test_DateObjectCreation():
    d = Date('1','3','2020')
    assert d.__str__() == 'day:1,month:3,year:2020'

def test_DateTimeObjectCreation():
    dt = DateTime('1','3','2020', '11','22','33')
    assert dt.__str__() == 'day:1,month:3,year:2020--11:22:33'


def testBigEndian1():
    parsedDates = bigEndianParser('2021-03-31')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
    
def testBigEndian3():
    parsedDates = bigEndianParser('2021-03-31','2020-04-5','2019-05-15')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
    assert parsedDates[1].__str__() == 'day:5,month:04,year:2020'
    assert parsedDates[2].__str__() == 'day:15,month:05,year:2019'

def testLittelEndian1():
    parsedDates = littleEndianParser('31-03-2021')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
    
def testLittelEndian3():
    parsedDates = littleEndianParser('31-03-2021','5-04-2020','15-05-2019')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
    assert parsedDates[1].__str__() == 'day:5,month:04,year:2020'
    assert parsedDates[2].__str__() == 'day:15,month:05,year:2019'

def testMiddleEndian1():
    parsedDates = middleEndianParser('03-31-2021')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
    
def testMiddleEndian3():
    parsedDates = middleEndianParser('03-31-2021','04-5-2020','05-15-2019')
    assert type(parsedDates) == type([])
    assert parsedDates[0].__str__() == 'day:31,month:03,year:2021'
    assert parsedDates[1].__str__() == 'day:5,month:04,year:2020'
    assert parsedDates[2].__str__() == 'day:15,month:05,year:2019'