label GAME:        
    show screen Header()
    scene home_bg with dissolve     

    # Here we enter an 'infinite loop' to play the game
    while PlayGame:
        # each event should come back to this label:
        label GAMECONTINUE:            
            # Reset the BlockToCall in case of event triggering
            $ BlockToCall = ""                      

            # Code to parse EVENTS array and eventually call a block if an event is triggered
            python:
                for q in EVENTS:
                    if q.EventCheck(Date):
                        BlockToCall = q.Block
            
            if BlockToCall <> "":
                call expression BlockToCall
            elif curLocForEvent <> "":                
                call expression curLocForEvent
            
            # This pauses the game until a new action like changing room or advancing time
            window hide
            $ renpy.pause(hard=True)
    
    return


label Diningroom:
    $ curLoc = "Dining room"
    $ curLocForEvent = "Diningroom"

    if DiningRoomFirstVisit:
        hide screen Header        
        scene diningroom_bg with dissolve
        m "This is our dining room"
        $ DiningRoomFirstVisit = False
    else:
        scene diningroom_bg with dissolve     
    
    show screen Header 

    return

label Kitchen:
    $ curLoc = "Kitchen"
    $ curLocForEvent = "Kitchen"

    if KitchenFirstVisit:
        hide screen Header        
        scene kitchen_bg with dissolve
        m "This is our kitchen"
        $ KitchenFirstVisit = False
    else:
        scene kitchen_bg with dissolve     
    
    show screen Header 

    return



# Label called when we want to add an hour
label add1hour:
    $ Date.AddHours(1)
    return

# Label called when we want to add two hours
label add2hours:
    $ Date.AddHours(2)
    return  

# Label called when we want to 30 minutes
label add30min:
    $ Date.AddMinutes(30)
    return

# Label called when we want to advance one day
# We'll jump on the day after at 07:00AM on WorkingDays and 09:00AM on Weekend
label changeDay:    
    if Date.Hours == 0:
        if Date.WeekdaysList[Date.DayInWeek] in WeekendTuple:
            $ Date.Hours = 9
            $ Date.Minutes = 0
        else:
            $ Date.Hours = 7
            $ Date.Minutes = 0
    else:
        $ Date.AddHours(24)
        if Date.WeekdaysList[Date.DayInWeek] in WeekendTuple:
            $ Date.Hours = 9
            $ Date.Minutes = 0
        else:
            $ Date.Hours = 7
            $ Date.Minutes = 0
    return
    