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
                text " "               
                imagebutton:
                    idle "time_icon_idle"
                    hover "time_icon_hover"
                    hovered Show("disp_info",None,info="Add time"), Hide("LocationsSubMenu")
                    unhovered Hide("disp_info")
                    action Hide("disp_info"), ToggleScreen("TimeSubMenu")
                text " "                
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
                idle "money_icon_idle"
                hover "money_icon_hover"
                hovered Show("disp_info",None,info="Sell your pictures"), Hide("LocationsSubMenu")
                unhovered Hide("disp_info")
                action Hide("Picture_exchange"), Hide("disp_info"), Hide("ActionsSubMenu")#, Call("selling_pictures")
            imagebutton:
                idle "study_icon_idle"
                hover "study_icon_hover"
                hovered Show("disp_info",None,info="Study 1 hour"), Hide("LocationsSubMenu")
                unhovered Hide("disp_info")
                action Hide("disp_info"), Hide("ActionsSubMenu")#, Call("Study")
            imagebutton:
                idle "hack_icon_idle"
                hover "hack_icon_hover"
                hovered Show("disp_info",None,info="Read about Hacking"), Hide("LocationsSubMenu")
                unhovered Hide("disp_info")
                action Hide("disp_info"), Hide("ActionsSubMenu")#, Call("StudyHacking")
            imagebutton:
                idle "yoga_icon_idle"
                hover "yoga_icon_hover"
                hovered Show("disp_info",None,info="Read about Yoga"), Hide("LocationsSubMenu")
                unhovered Hide("disp_info")
                action Hide("disp_info"), Hide("ActionsSubMenu")#, Call("StudyYoga")
            imagebutton:
                idle "photo_icon_idle"
                hover "photo_icon_hover"
                hovered Show("disp_info",None,info="Read about Photography"), Hide("LocationsSubMenu")
                unhovered Hide("disp_info")
                action Hide("disp_info"), Hide("ActionsSubMenu")#, Call("StudyPhoto")


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
        xsize 180 ysize 225
        padding 0,0
        margin 0,0
        vbox:
            xalign 0.95
            textbutton "Bob's Room":
                xalign 1.0
                hovered Show("disp_info",None,info="Move to Bob's Room")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("disp_info"), Show("BobRoomIcons"), SetVariable("curLocForEvent","BobRoom"), Jump("GAMECONTINUE")
            textbutton "Lisa's Room":
                xalign 1.0
                hovered Show("disp_info",None,info="Move to Lisa's Room")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","LisaRoom"), Jump("GAMECONTINUE")
            textbutton "Kitchen":
                xalign 1.0
                hovered Show("disp_info",None,info="Move to Kitchen")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","Kitchen"), Jump("GAMECONTINUE")
            textbutton "Dining Room":
                xalign 1.0
                hovered Show("disp_info",None,info="Move to Dining Room")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","Diningroom"), Jump("GAMECONTINUE")
            textbutton "TV Room":
                xalign 1.0
                hovered Show("disp_info",None,info="Move to TV Room")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","TVRoom"), Jump("GAMECONTINUE") 
            textbutton "Bathroom":
                xalign 1.0
                hovered Show("disp_info",None,info="Move to Bathroom")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("BobRoomIcons"), Hide("disp_info"), SetVariable("curLocForEvent","Bathroom"), Jump("GAMECONTINUE") 

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
        background "#00000060"
        xalign 0 ypos 80
        xsize 250 ysize 470
        padding 0,0
        margin 0,0
        vbox:
            #Display Bob's Stats
            textbutton "{size=20}{color=[wcolor]}[BobObj.Name]'s quick stats{/color}{/size}"
            textbutton "{size=15}{color=[wcolor]}You have [BobObj.Money] ${/color}{/size}"
            textbutton "{size=15}{color=[wcolor]}Your strength is [BobObj.Strength] out of 10{/color}{/size}"
            bar value StaticValue(BobObj.Strength, 10) xpos 5 xsize 240 ysize 15
            textbutton "{size=15}{color=[wcolor]}Your intel is [BobObj.Intel] out of 10{/color}{/size}"
            bar value StaticValue(BobObj.Intel, 10) xpos 5 xsize 240 ysize 15
            textbutton "{size=15}{color=[wcolor]}Your stealth is [BobObj.Stealth] out of 10{/color}{/size}"
            bar value StaticValue(BobObj.Stealth, 10) xpos 5 xsize 240 ysize 15            
            textbutton ""
            #Display Lisa's Stats
            textbutton "{size=20}{color=[wcolor]}[DaughterObj.Name]'s quick stats{/color}{/size}"
            textbutton "{size=15}{color=[wcolor]}Her mood is [DaughterObj.Mood] out of 10{/color}{/size}"
            bar value StaticValue(DaughterObj.Mood, 10) xpos 5 xsize 240 ysize 15
            textbutton "{size=15}{color=[wcolor]}Her feelings are [DaughterObj.Feelings] out of 10{/color}{/size}"
            bar value StaticValue(DaughterObj.Feelings, 10) xpos 5 xsize 240 ysize 15
            textbutton "{size=15}{color=[wcolor]}Her shyness is [DaughterObj.Shyness] out of 10{/color}{/size}"
            bar value StaticValue(DaughterObj.Shyness, 10) xpos 5 xsize 240 ysize 15
            textbutton "{size=15}{color=[wcolor]}Her arousal is [DaughterObj.Arousal] out of 10{/color}{/size}"
            bar value StaticValue(DaughterObj.Arousal, 10) xpos 5 xsize 240 ysize 15