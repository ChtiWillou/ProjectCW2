init python:
    def rfr_pause (pdelay = 1.0, hard = False):
        renpy.pause ((pdelay * delay_factor), hard = (hard and hard_indicator))
    
    def Reading(topic):
        global NbHackRead
        global NbYogaRead
        global NbPhotoRead
        global BobObj
        
        if topic == "Hack":
            NbHackRead += 1
            if NbHackRead == 5:
                NbHackRead = 0
                if BobObj.HackingSkills < 10:   
                    BobObj.IncreaseHackingSkills(1)              
        elif topic == "Yoga":
            NbYogaRead += 1
            if NbYogaRead == 5:
                NbYogaRead = 0
                if BobObj.YogaSkills < 10:   
                    BobObj.IncreaseYogaSkills(1)
        elif topic == "Photo":
            NbPhotoRead += 1
            if NbPhotoRead == 5:
                NbPhotoRead = 0
                if BobObj.PhotoSkills < 10:   
                    BobObj.IncreasePhotoSkills(1)        
        return
    
    def Study():
        global NbStudyHours
        global BobObj

        NbStudyHours += 1
        if NbStudyHours == 10:
            NbStudyHours = 0
            if BobObj.Intel < 10:   
                BobObj.IncreaseIntel(1)
    
    def Sport():
        global NbSportHours
        global BobObj
        
        NbSportHours += 1
        if NbSportHours == 10:
            NbSportHours = 0
            if BobObj.Strength < 10:   
                BobObj.IncreaseStrength(1)