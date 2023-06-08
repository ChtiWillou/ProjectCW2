init python:
    ############################################################################
    ## Class Calendar
    ############################################################################
    class Calendar(object):
        def __init__(self, p_Hours, p_Minutes, p_DayInMonth, p_DayInWeek, p_MonthsList, p_MonthInYear, p_WeekdaysList, p_MonthdaysList):
            self.Hours = p_Hours
            self.Minutes = p_Minutes
            self.DayInMonth = p_DayInMonth
            self.DayInWeek = p_DayInWeek
            self.MonthsList = p_MonthsList
            self.MonthInYear = p_MonthInYear
            self.WeekdaysList = p_WeekdaysList
            self.MonthdaysList = p_MonthdaysList

        @property
        def Output(self):
            return self.WeekdaysList[self.DayInWeek] + ", " + self.MonthsList[self.MonthInYear] + " " + str(self.DayInMonth + 1) + " - " + str(self.Hours).zfill(2) + ":" + str(self.Minutes).zfill(2)

        def AddHours(self, hours):
            self.Hours += hours
            if self.Hours > 23:
                self.Hours -= 24
                self.DayInWeek += 1
                self.DayInMonth += 1
            if self.DayInWeek > 6:
                self.DayInWeek = 0
            if (self.DayInMonth + 1) > self.MonthdaysList[self.MonthInYear]:
                self.MonthInYear += 1
                self.DayInMonth = 0
            if self.MonthInYear > 11:
                self.MonthInYear = 0

        def AddMinutes(self, minutes):
            self.Minutes += minutes
            if self.Minutes > 59:
                self.Minutes -= 60
                self.Hours += 1
            if self.Hours > 23:
                self.Hours -= 24
                self.DayInWeek += 1
                self.DayInMonth += 1
            if self.DayInWeek > 6:
                self.DayInWeek = 0
            if (self.DayInMonth + 1) > self.MonthdaysList[self.MonthInYear]:
                self.MonthInYear += 1
                self.DayInMonth = 0
            if self.MonthInYear > 11:
                self.MonthInYear = 0
    
    ############################################################################
    ## Class MainCharacter
    ############################################################################
    class MainCharacter(object):
        def __init__(self, p_Name, p_Money, p_Strength, p_Intel, p_Stealth, p_Location):
                self.Name = p_Name            
                self.Money = p_Money
                self.Strength = p_Strength
                self.Intel = p_Intel
                self.Stealth = p_Stealth
                self.Location = p_Location

        def WinMoney(self, amount):
            self.Money += amount

        def LoseMoney(self, amount):
            self.Money -= amount
            if self.Money < 0:
                self.Money = 0

        def IncreaseStrength(self, value):
            self.Strength += value
            if self.Strength > 10:
                self.Strength = 10

        def DecreaseStrength(self, value):
            self.Strength -= value
            if self.Strength < 1:
                self.Strength = 0

        def IncreaseIntel(self, value):
            self.Intel += value
            if self.Intel > 10:
                self.Intel = 10

        def DecreaseIntel(self, value):
            self.Intel -= value
            if self.Intel < 1:
                self.Intel = 0

        def IncreaseStealth(self, value):
            self.Stealth += value
            if self.Stealth > 10:
                self.Stealth = 10

        def DecreaseStealth(self, value):
            self.Stealth -= value
            if self.Stealth < 1:
                self.Stealth = 0         

    ############################################################################
    ## Class GirlCharacter
    ############################################################################
    class GirlCharacter(object):
        def __init__(self, p_Name, p_Money, p_Mood, p_Feelings, p_Shyness, p_Arousal, p_Location, p_WeekTS, p_WeekendTS):
            self.Name = p_Name
            self.Money = p_Money
            self.Mood = p_Mood            
            self.Feelings = p_Feelings
            self.Shyness = p_Shyness
            self.Arousal = p_Arousal
            self.Location = p_Location
            self.WeekTS = p_WeekTS
            self.WeekendTS = p_WeekendTS

        def WinMoney(self, amount):
            self.Money += amount

        def LoseMoney(self, amount):
            self.Money -= amount
            if self.Money < 0:
                self.Money = 0
        
        def IncreaseMood(self, value):
            self.Mood += value
            if self.Mood > 10:
                self.Mood = 10

        def DecreaseMood(self, value):
            self.Mood -= value
            if self.Mood < 1:
                self.Mood = 0
        
        def IncreaseFeelings(self, value):
            self.Feelings += value
            if self.Feelings > 10:
                self.Feelings = 10
        
        def DecreaseFeelings(self, value):
            self.Feelings -= value
            if self.Feelings < 1:
                self.Feelings = 0
        
        def IncreaseShyness(self, value):
            self.Shyness += value
            if self.Shyness > 10:
                self.Shyness = 10
        
        def DecreaseShyness(self, value):
            self.Shyness -= value
            if self.Shyness < 1:
                self.Shyness = 0

        def IncreaseArousal(self, value):
            self.Arousal += value
            if self.Arousal > 10:
                self.Arousal = 10
        
        def DecreaseArousal(self, value):
            self.Arousal -= value
            if self.Arousal < 1:
                self.Arousal = 0
    
    ############################################################################
    ## Class Event
    ############################################################################
    class Event(object):
        # Hour = time on which the event can be triggered
        # Minutes = minutes on which the event can be triggered
        # DayOfWeek = Day on wich the event can be triggered => 7 for everyday
        # Location = Where the events happens
        #   Possible values for Location:
        #   - "EveRoom","LynnRoom","LinaRoom","BobRoom"
        #   - "Kitchen","TVRoom","DiningRoom","Bathroom","Hallway","Pool"
        #   - "Groceries","Lingerie","Boutique","Cafe","Jewelry","School"
        # IsAvailable = Is the event unlocked and can happen
        # Block = The label to call when the event occurs
        # Done = If the event happened once yet
        # Progress = value set to 0 to start - can upgrade if this is a progressing event

        def __init__(self, p_Hour, p_Minutes, p_DayOfWeek, p_Location, p_Block, p_IsAvailable, p_Progress, p_Done, p_Auto):
            self.Hour = p_Hour
            self.Minutes = p_Minutes
            self.DayOfWeek = p_DayOfWeek
            self.Location = p_Location
            self.Block = p_Block
            self.IsAvailable = p_IsAvailable
            self.Progress = p_Progress           
            self.Done = p_Done            
            self.Auto = p_Auto            

        def EventCheck(self, c):
            if self.Auto and ((self.DayOfWeek == 7 or self.DayOfWeek == c.DayInWeek) and self.Hour == c.Hours and self.IsAvailable):
                return True
            else:
                if self.DayOfWeek == 8:
                    if c.DayInWeek in workweek_num and self.Hour == c.Hours and self.Minutes == c.Minutes and self.Location == curLocForEvent and self.IsAvailable:
                        return True    
                    else:
                        return False
                elif self.DayOfWeek == 9:
                    if c.DayInWeek in weekend_num and self.Hour == c.Hours and self.Minutes == c.Minutes and self.Location == curLocForEvent and self.IsAvailable:
                        return True
                    else:
                        return False
                elif ((self.DayOfWeek == 7 or self.DayOfWeek == c.DayInWeek) and self.Hour == c.Hours and self.Minutes == c.Minutes and self.Location == curLocForEvent and self.IsAvailable):
                    return True
                else:
                    return False

        def SetUnAvailable(self):
            self.IsAvailable = False

        def SetAvailable(self):
            self.IsAvailable = True

        def SetDone(self):
            global Events_Counter
            if self.Done == False:
                Events_Counter += 1
                self.Done = True


