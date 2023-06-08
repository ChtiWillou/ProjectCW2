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
                    idle "stats_icon"
                    hover "stats_icon_hover"
                    hovered Show("disp_info",None,info="Show Stats"), Show("QuickStats")
                    unhovered Hide("disp_info"), Hide("QuickStats")
                    action Hide("disp_info"), ToggleScreen("StatsSubMenu"), Hide("TimeSubMenu"), Hide("ActionsSubMenu")
                text " "               
                imagebutton:
                    idle "clock_icon"
                    hover "clock_icon_hover"
                    hovered Show("disp_info",None,info="Add time")
                    unhovered Hide("disp_info")
                    action Hide("disp_info"), ToggleScreen("TimeSubMenu"), Hide("StatsSubMenu"), Hide("ActionsSubMenu")
                text " "                
                imagebutton:
                    idle "next_day_icon"
                    hover "next_day_icon_hover"
                    hovered Show("disp_info",None,info="Next day")
                    unhovered Hide("disp_info")
                    action Hide("disp_info"), Hide("ActionsSubMenu"), Call("changeDay")

        frame:
            background None
            xalign 0.2 yalign 0.0
            ysize 80
            padding 0,0
            margin 0,0
            textbutton "[Date.Output]" text_color "#ffffff" yalign 0.5

        frame:
                background None
                xalign 1.0 yalign 0.0
                vbox:
                    imagebutton:
                        idle "time"
                        hover "time"
                        hovered Show("disp_info",None,info="Actions")
                        unhovered Hide("disp_info")
                        action Hide("disp_info"), ToggleScreen("ActionsSubMenu"), Hide("StatsSubMenu"), Hide("TimeSubMenu")

        frame:
            background None
            xalign 0.9 yalign 0.0
            hbox:
                imagebutton:
                    idle "move"
                    hover "move"
                    hovered Show("disp_info",None,info="Move in...")
                    unhovered Hide("disp_info")
                    action Hide("disp_info"), ToggleScreen("LocationsSubMenu")

screen disp_info(info):
    frame:
        background "#00000060"
        xalign 0.5 yalign 0.94
        text "[info]"

screen ActionsSubMenu():
        frame:
            background "#00000060"
            xalign 1.0 ypos 80
            xsize 230 ysize 250
            padding 0,0
            margin 0,0
            vbox:
                textbutton "Sell pictures":
                    hovered Show("disp_info",None,info="Sell your pictures")
                    unhovered Hide("disp_info")
                    action Hide("Picture_exchange"), Hide("disp_info"), Hide("ActionsSubMenu")#, Call("selling_pictures")
                textbutton "Study":
                    hovered Show("disp_info",None,info="Study 1 hour")
                    unhovered Hide("disp_info")
                    action Hide("disp_info"), Hide("ActionsSubMenu")#, Call("Study")
                textbutton "Read about Hacking":
                    hovered Show("disp_info",None,info="Study 1 hour")
                    unhovered Hide("disp_info")
                    action Hide("disp_info"), Hide("ActionsSubMenu")#, Call("StudyHacking")
                textbutton "Read about Yoga":
                    hovered Show("disp_info",None,info="Study 1 hour")
                    unhovered Hide("disp_info")
                    action Hide("disp_info"), Hide("ActionsSubMenu")#, Call("StudyYoga")
                textbutton "Read about Photography":
                    hovered Show("disp_info",None,info="Study 1 hour")
                    unhovered Hide("disp_info")
                    action Hide("disp_info"), Hide("ActionsSubMenu")#, Call("StudyPhoto")

screen LocationsSubMenu():
    frame:
        background "#00000060"
        xalign 1.0 ypos 80
        xsize 100 ysize 150
        padding 0,0
        margin 0,0
        vbox:
            textbutton "Bob's Room":
                hovered Show("disp_info",None,info="Bob's Room")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("disp_info")
            textbutton "Lisa's Room":
                hovered Show("disp_info",None,info="Lisa's Room")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("disp_info")
            textbutton "Kitchen":
                hovered Show("disp_info",None,info="Kitchen")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("disp_info"), SetVariable("curLocForEvent","Kitchen"), Jump("GAMECONTINUE")
            textbutton "Dining Room":
                hovered Show("disp_info",None,info="Dining Room")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("disp_info"), SetVariable("curLocForEvent","Diningroom"), Jump("GAMECONTINUE")
            textbutton "TV Room":
                hovered Show("disp_info",None,info="TV Room")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("disp_info")  
            textbutton "Bathroom":
                hovered Show("disp_info",None,info="Bathroom")
                unhovered Hide("disp_info")
                action Hide("LocationsSubMenu"), Hide("disp_info")

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
        xpos 0 yalign 1.0
        xsize 250 ysize 225
        padding 0,0
        margin 0,0
        vbox:
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