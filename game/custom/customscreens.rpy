screen Header():
    frame:
        background "#00000060"
        xalign 0.0 yalign 0.0
        xsize 1920 ysize 80
        padding 0,0
        margin 0,0        

        frame:
            background None
            xalign 0.0 yalign 0.0
            hbox:
                imagebutton:
                    idle "user_icon_idle"
                    hover "user_icon_hover"
                    hovered Show("disp_info",None,info="Show Stats"), Show("QuickStats"), Hide("TimeSubMenu"), Hide("LocationsSubMenu")
                    unhovered Hide("disp_info"), Hide("QuickStats")
                    action Hide("disp_info")
                
                if (Date.Hours >= 0 and Date.Hours <= 1) or (Date.Hours >= 6 and Date.Hours <= 23):               
                    imagebutton:
                        idle "time_icon_idle"
                        hover "time_icon_hover"
                        hovered Show("disp_info",None,info="Add time"), Hide("LocationsSubMenu")
                        unhovered Hide("disp_info")
                        action Hide("disp_info"), ToggleScreen("TimeSubMenu")
                    
                else:
                    imagebutton:
                        idle "empty"
                imagebutton:
                    idle "nextday_icon_idle"
                    hover "nextday_icon_hover"
                    hovered Show("disp_info",None,info="Go to next day"), Hide("TimeSubMenu"), Hide("LocationsSubMenu")
                    unhovered Hide("disp_info")
                    action Hide("disp_info"), Call("changeDay")

        frame:
            background None
            xalign 0.2 yalign 0.0
            ysize 80
            padding 0,0
            margin 0,0
            textbutton "{size=25}[Date.Output]{/size}" text_color "#ffffff" yalign 0.5

        frame:
            background None
            xalign 1.0 yalign 0.0
            hbox:            
                imagebutton:
                    idle "home_icon_idle"
                    hover "home_icon_hover"
                    hovered Show("disp_info",None,info="Move to...")
                    unhovered Hide("disp_info")
                    action Hide("disp_info"), ToggleScreen("LocationsSubMenu")                
                

screen BobRoomIcons():
    frame:
        background None
        xalign 0.90 yalign 0.0
        hbox:
            imagebutton:
                idle "comp_icon_idle"
                hover "comp_icon_hover"
                hovered Show("disp_info",None,info="Go on computer"), Hide("LocationsSubMenu")
                unhovered Hide("disp_info")
                action Hide("Picture_exchange"), Hide("disp_info"), Hide("ActionsSubMenu")#, Call("selling_pictures")
            imagebutton:
                idle "study_icon_idle"
                hover "study_icon_hover"
                hovered Show("disp_info",None,info="Study 1 hour"), Hide("LocationsSubMenu")
                unhovered Hide("disp_info")
                action Hide("disp_info"), Hide("ActionsSubMenu"), Call("Study")
            imagebutton:
                idle "sport_icon_idle"
                hover "sport_icon_hover"
                hovered Show("disp_info",None,info="Sport 1 hour"), Hide("LocationsSubMenu")
                unhovered Hide("disp_info")
                action Hide("disp_info"), Hide("ActionsSubMenu"), Call("Sport")
            if BobObj.HackingSkills < 10:
                imagebutton:
                    idle "hack_icon_idle"
                    hover "hack_icon_hover"
                    hovered Show("disp_info",None,info="Read about Hacking"), Hide("LocationsSubMenu")
                    unhovered Hide("disp_info")
                    action Hide("disp_info"), Hide("ActionsSubMenu"), Call("ReadHack")
            if BobObj.YogaSkills < 10:
                imagebutton:
                    idle "yoga_icon_idle"
                    hover "yoga_icon_hover"
                    hovered Show("disp_info",None,info="Read about Yoga"), Hide("LocationsSubMenu")
                    unhovered Hide("disp_info")
                    action Hide("disp_info"), Hide("ActionsSubMenu"), Call("ReadYoga")
            if BobObj.PhotoSkills < 10:
                imagebutton:
                    idle "photo_icon_idle"
                    hover "photo_icon_hover"
                    hovered Show("disp_info",None,info="Read about Photography"), Hide("LocationsSubMenu")
                    unhovered Hide("disp_info")
                    action Hide("disp_info"), Hide("ActionsSubMenu"), Call("ReadPhoto")


screen disp_info(info):
    frame:        
        background None        
        ysize 80
        padding 0,0
        margin 0,0
        xalign 0.5 yalign 0.0
        text "[info]" yalign 0.5

screen LocationsSubMenu():
    frame:
        background "#00000060"
        xalign 1.0 ypos 80
        xsize 85 ysize 1000
        padding 5,0
        margin 0,0
        vbox:
            xalign 1.0
            imagebutton:
                xalign 1.0
                idle "bedroom_icon_idle"
                hover "bedroom_icon_hover"
                hovered Show("disp_info",None,info="Move to Bob's Room")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("disp_info"), Show("BobRoomIcons"), SetVariable("curLocForEvent","BobRoom"), Jump("GAMECONTINUE")
            #textbutton "Bob's Room":
            #    xalign 1.0
            #    hovered Show("disp_info",None,info="Move to Bob's Room")
            #    unhovered Hide("disp_info")
            #    action Hide("LocationsSubMenu"), Hide("disp_info"), Show("BobRoomIcons"), SetVariable("curLocForEvent","BobRoom"), Jump("GAMECONTINUE")
            imagebutton:
                xalign 1.0
                idle "bedroom2_icon_idle"
                hover "bedroom2_icon_hover"
                hovered Show("disp_info",None,info="Move to Lisa's Room")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","LisaRoom"), Jump("GAMECONTINUE")
            #textbutton "Lisa's Room":
            #    xalign 1.0
            #   hovered Show("disp_info",None,info="Move to Lisa's Room")
            #    unhovered Hide("disp_info")
            #    action Hide("LocationsSubMenu"), Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","LisaRoom"), Jump("GAMECONTINUE")
            imagebutton:
                xalign 1.0
                idle "kitchen_icon_idle"
                hover "kitchen_icon_hover"
                hovered Show("disp_info",None,info="Move to Kitchen")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","Kitchen"), Jump("GAMECONTINUE")
            #textbutton "Kitchen":
            #    xalign 1.0
            #    hovered Show("disp_info",None,info="Move to Kitchen")
            #    unhovered Hide("disp_info")
            #    action Hide("LocationsSubMenu"), Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","Kitchen"), Jump("GAMECONTINUE")
            #textbutton "Dining Room":
            #    xalign 1.0
            #    hovered Show("disp_info",None,info="Move to Dining Room")
            #    unhovered Hide("disp_info")
            #    action Hide("LocationsSubMenu"), Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","Diningroom"), Jump("GAMECONTINUE")
            imagebutton:
                xalign 1.0
                idle "tv_icon_idle"
                hover "tv_icon_hover"
                hovered Show("disp_info",None,info="Move to TV Room")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","TVRoom"), Jump("GAMECONTINUE")
            #textbutton "TV Room":
            #    xalign 1.0
            #    hovered Show("disp_info",None,info="Move to TV Room")
            #    unhovered Hide("disp_info")
            #    action Hide("LocationsSubMenu"), Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","TVRoom"), Jump("GAMECONTINUE") 
            imagebutton:
                xalign 1.0
                idle "bath_icon_idle"
                hover "bath_icon_hover"
                hovered Show("disp_info",None,info="Move to Bathroom")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","Bathroom"), Jump("GAMECONTINUE")
            #textbutton "Bathroom":
            #    xalign 1.0
            #    hovered Show("disp_info",None,info="Move to Bathroom")
            #    unhovered Hide("disp_info")
            #    action Hide("LocationsSubMenu"), Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","Bathroom"), Jump("GAMECONTINUE")
            imagebutton:
                xalign 1.0
                idle "jacuzzi_icon_idle"
                hover "jacuzzi_icon_hover"
                hovered Show("disp_info",None,info="Move to Jacuzzi")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("BobRoomIcons"), Hide("disp_info")#, SetVariable("curLocForEvent","Jacuzzi"), Jump("GAMECONTINUE")

screen StatsSubMenu():
    frame:
        background "#00000060"
        xpos 0 ypos 80
        xsize 100 ysize 70
        padding 0,0
        margin 0,0
        vbox:
            textbutton "Bob":
                hovered Show("disp_info",None,info="Bob's Stats")
                unhovered Hide("disp_info")
                action Hide("StatsSubMenu"), Hide("disp_info")
            textbutton "Girl":
                hovered Show("disp_info",None,info="Girl's Stats")
                unhovered Hide("disp_info")
                action Hide("StatsSubMenu"), Hide("disp_info")              

screen TimeSubMenu():
    frame:
        background "#00000060"
        xpos 80 ypos 80
        xsize 180 ysize 110
        padding 0,0
        margin 0,0
        vbox:
            textbutton "Add 30 minutes":
                hovered Show("disp_info",None,info="Add 30 minutes")
                unhovered Hide("disp_info")
                action Hide("TimeSubMenu"), Hide("disp_info"), Call("add30min")
            textbutton "Add 1 hour":
                hovered Show("disp_info",None,info="Add 1 hour")
                unhovered Hide("disp_info")
                action Hide("TimeSubMenu"), Hide("disp_info"), Call("add1hour")
            textbutton "Add 2 hours":
                hovered Show("disp_info",None,info="Add 2 hours")
                unhovered Hide("disp_info")
                action Hide("TimeSubMenu"), Hide("disp_info"), Call("add2hours")


screen QuickStats():
    frame:
        background "#000000aa"
        xalign 0 ypos 80
        xsize 320 ysize 1000
        padding 0,0
        margin 0,0
        vbox:
            #Display Bob's Stats
            textbutton "{size=20}{color=[wcolor]}[BobObj.Name]'s quick stats{/color}{/size}"
            textbutton "{size=15}{color=[wcolor]}You have [BobObj.Money] ${/color}{/size}"
            
            $ sp = 10 - NbSportHours
            textbutton "{size=15}{color=[wcolor]}Your strength is [BobObj.Strength] out of 10{/color}{/size}"
            if BobObj.Strength < 10:
                textbutton "{size=15}{color=[wcolor]}Do sport for [sp]h to improve{/color}{/size}"
            bar value StaticValue(BobObj.Strength, 10) xpos 5 xsize 310 ysize 15
            bar value StaticValue(NbSportHours, 10) xpos 5 xsize 310 ysize 15
            
            $ st = 10 - NbStudyHours
            textbutton "{size=15}{color=[wcolor]}Your intel is [BobObj.Intel] out of 10{/color}{/size}"
            if BobObj.Intel < 10:
                textbutton "{size=15}{color=[wcolor]}Study [st]h to improve{/color}{/size}"
            bar value StaticValue(BobObj.Intel, 10) xpos 5 xsize 310 ysize 15
            bar value StaticValue(NbStudyHours, 10) xpos 5 xsize 310 ysize 15
            
            $ yo = 5 - NbYogaRead
            textbutton "{size=15}{color=[wcolor]}Your Yoga Skills are [BobObj.YogaSkills] out of 10{/color}{/size}"
            if BobObj.YogaSkills < 10:
                textbutton "{size=15}{color=[wcolor]}Read about Yoga [yo]h to improve{/color}{/size}"
            bar value StaticValue(BobObj.YogaSkills, 10) xpos 5 xsize 310 ysize 15
            bar value StaticValue(NbYogaRead, 5) xpos 5 xsize 310 ysize 15
            
            $ ha = 5 - NbHackRead
            textbutton "{size=15}{color=[wcolor]}Your Hacking Skills are [BobObj.HackingSkills] out of 10{/color}{/size}"
            if BobObj.HackingSkills < 10:
                textbutton "{size=15}{color=[wcolor]}Read about Hacking [ha]h to improve{/color}{/size}"
            bar value StaticValue(BobObj.HackingSkills, 10) xpos 5 xsize 310 ysize 15 
            bar value StaticValue(NbHackRead, 5) xpos 5 xsize 310 ysize 15
            
            $ ph = 5 - NbPhotoRead
            textbutton "{size=15}{color=[wcolor]}Your Photography Skills are [BobObj.PhotoSkills] out of 10{/color}{/size}"
            if BobObj.PhotoSkills < 10:
                textbutton "{size=15}{color=[wcolor]}Read about Photography [ph]h to improve{/color}{/size}"
            bar value StaticValue(BobObj.PhotoSkills, 10) xpos 5 xsize 310 ysize 15  
            bar value StaticValue(NbPhotoRead, 5) xpos 5 xsize 310 ysize 15

            textbutton "------------------------------------------"
            #Display Lisa's Stats
            textbutton "{size=20}{color=[wcolor]}[DaughterObj.Name]'s quick stats{/color}{/size}"
            textbutton "{size=15}{color=[wcolor]}Her mood is [DaughterObj.Mood] out of 10{/color}{/size}"
            bar value StaticValue(DaughterObj.Mood, 10) xpos 5 xsize 310 ysize 15
            textbutton "{size=15}{color=[wcolor]}Her feelings are [DaughterObj.Feelings] out of 10{/color}{/size}"
            bar value StaticValue(DaughterObj.Feelings, 10) xpos 5 xsize 310 ysize 15
            textbutton "{size=15}{color=[wcolor]}Her shyness is [DaughterObj.Shyness] out of 10{/color}{/size}"
            bar value StaticValue(DaughterObj.Shyness, 10) xpos 5 xsize 310 ysize 15
            textbutton "{size=15}{color=[wcolor]}Her arousal is [DaughterObj.Arousal] out of 10{/color}{/size}"
            bar value StaticValue(DaughterObj.Arousal, 10) xpos 5 xsize 310 ysize 15