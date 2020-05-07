# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
#screen say(who, what, side_image=None, two_window=False):

#    # Decide if we want to use the one-window or two-window variant.
#    if not two_window:

#        # The one window variant.
#        window:
#            id "window"
#            xpadding 0
#            ypadding 0
#            xsize 1600
#            ysize 200
#            vbox:
#                style "say_vbox"

#                if who:
#                    frame:
#                        background Frame("ui/chat/1.png",2,0,120,0)
#                        ysize 50
#                        right_padding 90
#                        left_padding 40
#                        text who id "who" yalign .5
#                frame:
#                    background None
#                    xpadding 30
#                    text what id "what"
#            vbox:
#                xalign 1.0 yalign 1.0
#                use quick_m

#    else:

#        # The two window variant.
#        vbox:
#            style "say_two_window_vbox"

#            if who:
#                window:
#                    style "say_who_window"

#                    text who:
#                        id "who"

#            window:
#                id "window"

#                has vbox:
#                    style "say_vbox"

#                text what id "what"

#    # If there's a side image, display it above the text.
#    if side_image:
#        add side_image
#    else:
#        add SideImage() xalign 0.0 yalign 1.0

#    # Use the quick menu.

#####################################################################chat 2
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"
            xpadding 0
            ypadding 0
            ysize 300
            background Frame("ui/chat/3.png",0,52,0,2)
            vbox:
                style "say_vbox"
                xsize 1400
                xalign .5
                ypos 60
                spacing 10
                if who:
                    text who id "who" bold False size 38
                text what id "what"
            vbox:
                xalign 1.0 yalign 1.0
                use quick_m

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.

##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:
                    fixed:
                        fit_first True
                        button:
                            action action
                            style "menu_choice_button"
                            idle_background "#000c"
                            hover_background "#fffb"
                            yminimum 50
                            xpadding 70
                            ypadding 10
                            #at keys(0)
                            text caption style "menu_choice"
                        add "ui/ch/1.png" xalign 0.0 yalign 0.0
                        add "ui/ch/2.png" xalign 1.0 yalign 1.0


                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.85)
        xmaximum int(config.screen_width * 0.85)
    style menu_choice is button_text:
        #clear
        idle_color "#fff"
        hover_color "#000"
        size 25

##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    frame:
        xalign .5 yalign .5
        background "#000c"
        xsize 800
        vbox:
            text prompt style "input_prompt" xpos 20
            frame:
                background "#000c"
                xfill True
                input id "input" style "input_text"

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
transform keys(x=0,y=0,ft=.4):
    parallel:
        alpha 0 yoffset y xoffset x
        easein ft alpha 1 yoffset 0 xoffset 0
    parallel:
        on hover:
            easein .4 alpha .8
        on idle:
            easein .4 alpha 1.0
        on selected_hover:
            easein .4 alpha .8
        on selected_idle:
            easein .4 alpha .4
transform barandom:
    alpha renpy.random.randint(0,2)
    pause renpy.random.random()
    alpha renpy.random.randint(0,2)
    pause renpy.random.random()
    alpha renpy.random.randint(0,2)
    pause renpy.random.random()
    alpha renpy.random.randint(0,2)
    pause renpy.random.random()
    repeat
transform rottin:
    subpixel True

    easein renpy.random.random()*2 rotate renpy.random.randint(0,360)
    easein renpy.random.random()*2 rotate renpy.random.randint(0,360)
    easein renpy.random.random()*2 rotate renpy.random.randint(0,360)
    easein renpy.random.random()*2 rotate renpy.random.randint(360,720)
    repeat
transform posrot(r=0,z=1,y=0):
    rotate r
    zoom z
    yoffset y
    pause 1
    easein .8 yoffset 0
transform fadinout:
    linear 10 alpha .2
    linear 10 alpha 1
    repeat
transform inbar(d=0):
    xoffset 700
    pause 3
    pause d
    easein .3 xoffset 0
    pause 8-d
    easeout .3 xoffset 700
    repeat
transform sprk:
    xanchor .1 yanchor .5
    linear 1.0 xoffset -1340 yoffset 0
    rotate -45
    linear .1 xoffset -1367 yoffset 26
    rotate 45
    linear .3 xoffset -1500 yoffset -100
    xoffset 0 yoffset 0 rotate 0
    pause renpy.random.randint(2,6)
    repeat

transform movin(x=0,y=0):
    xoffset x
    yoffset y
    easein .8 xoffset 0 yoffset 0
define onevar = 23
screen main_menu():
    tag ext
    add "ui/mm/bgd.png"
    add "ui/bg/bgd.png" at fadinout

    # Austin Edit - Plays main menu music if previously muted
    #timer 0.5 action SetMute('music', False)
    if renpy.music.is_playing(channel='soundroom1'):
        timer 0.001 action Stop(channel='music', fadeout=1) #timer 0.5 action SetMute('music', True) #timer 0.5 action Stop(channel='music', fadeout=1)
    else:
        timer 0.001 action Play("music", "audio/music/Bring It On! [INSTRUMENTAL].ogg")

    timer 0.1 repeat True action SetVariable('onevar', onevar+1)
    text str(onevar)
    hbox:
        xalign .1
        yalign .7
        spacing -30
        for i in range(3):
            add "ui/bg/1.png" at barandom alpha .3
    hbox:
        xalign .422
        yalign .114
        spacing -15
        for i in range(4):
            add "ui/bg/2.png" at barandom alpha .8
    hbox:
        xalign 1.0
        yalign .465
        spacing -35
        for i in range(5):
            add "ui/bg/3.png" at inbar(i) alpha .4
    hbox:
        xalign .87
        yalign .97
        spacing 5
        for i in range(4):
            add "ui/bg/4.png" at barandom alpha .4
    hbox:
        xalign .98
        yalign .1
        spacing 5
        for i in range(10):
            add "ui/bg/4.png" at barandom alpha .3
    frame:
        xpos -110 ypos -40
        background None
        at movin(2000)
        add "ui/bg/11.png"
        add "ui/bg/12.png" at rottin xpos -51 ypos -51
        add "ui/bg/13.png" at rottin xpos 68 ypos 68
    frame:
        xpos -1100 ypos 300
        background None
        at posrot(90,.8,1000)
        add "ui/bg/11.png"
        add "ui/bg/12.png" at rottin xpos -51 ypos -51
    frame:
        xalign 1.038 yalign .09
        background None
        at sprk
        add "ui/bg/sprk.png"

    add "ui/mm/title.png" at keys(0,-100) xalign .5 yalign .495
    hbox:
        spacing -50
        xalign 0.5
        yalign 0.85
        imagebutton:
            idle "ui/mm/start.png"
            hover "ui/mm/start.png"
            focus_mask True
            action Start()
            at keys(-500)
        imagebutton:
            idle "ui/mm/load.png"
            hover "ui/mm/load.png"
            focus_mask True
            action ShowMenu("load",0)
            at keys(0,50)
        imagebutton:
            idle "ui/mm/settings.png"
            hover "ui/mm/settings.png"
            focus_mask True
            action ShowMenu("preferences",0)
            at keys(0,-50)
        imagebutton:
            idle "ui/mm/extras.png"
            hover "ui/mm/extras.png"
            focus_mask True
            action ShowMenu("extras")
            at keys(0,50)
        imagebutton:
            idle "ui/mm/exit.png"
            hover "ui/mm/exit.png"
            focus_mask True
            action Quit(confirm=False)
            at keys(500)

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():
    hbox:
        spacing -50
        xalign 0.5
        yalign 0.85
        imagebutton:
            idle "ui/mm/save.png"
            hover "ui/mm/save.png"
            focus_mask True
            action ShowMenu("save")
            at keys(-500)
        imagebutton:
            idle "ui/mm/load.png"
            hover "ui/mm/load.png"
            focus_mask True
            action ShowMenu("load")
            at keys(0,50)
        imagebutton:
            idle "ui/mm/settings.png"
            hover "ui/mm/settings.png"
            focus_mask True
            action ShowMenu("preferences")
            at keys(0,-50)
        imagebutton:
            idle "ui/mm/main.png"
            hover "ui/mm/main.png"
            focus_mask True
            action MainMenu()
            at keys(0,50)
        imagebutton:
            idle "ui/mm/exit.png"
            hover "ui/mm/exit.png"
            focus_mask True
            action Quit()
            at keys(500)
screen navigation1():
    hbox:
        spacing -50
        xalign 0.5
        yalign 0.85
        imagebutton:
            idle "ui/mm/start.png"
            hover "ui/mm/start.png"
            focus_mask True
            action Start()
            at keys(-500)
        imagebutton:
            idle "ui/mm/load.png"
            hover "ui/mm/load.png"
            focus_mask True
            action ShowMenu("load",0)
            at keys(0,50)
        imagebutton:
            idle "ui/mm/settings.png"
            hover "ui/mm/settings.png"
            focus_mask True
            action ShowMenu("preferences",0)
            at keys(0,-50)
        imagebutton:
            idle "ui/mm/extras.png"
            hover "ui/mm/extras.png"
            focus_mask True
            action [Hide("preferences"),Hide("load"),ShowMenu("extras")]
            at keys(0,50)
        imagebutton:
            idle "ui/mm/exit.png"
            hover "ui/mm/exit.png"
            focus_mask True
            action Quit()
            at keys(500)
##############################################################################
# Save, Load
transform delbu:
    alpha .7
    on hover:
        linear .4 alpha 1.0
    on idle:
        linear .4 alpha .7
screen file_picker():
    style_group "file_picker"
    hbox:
        spacing -30
        xalign .5
        yalign .235
        imagebutton:
            idle "ui/sav/bc.png"
            hover "ui/sav/bc.png"
            focus_mask True
            action FilePagePrevious()
            at keys(0,0,1)
        imagebutton:
            idle "ui/sav/au.png"
            hover "ui/sav/au.png"
            focus_mask True
            action FilePage("auto")
            at keys(0,50)
        imagebutton:
            idle "ui/sav/q.png"
            hover "ui/sav/q.png"
            focus_mask True
            action FilePage("quick")
            at keys(0,-50)
        for i in range(1, 7):
            textbutton str(i):
                xoffset -2
                xsize 94
                ysize 30
                at keys(0,50)
                background "ui/sav/1.png"
                action FilePage(i)
        imagebutton:
            idle "ui/sav/nx.png"
            hover "ui/sav/nx.png"
            focus_mask True
            action FilePageNext()
            at keys(0,0,1)

        $ columns = 2
        $ rows = 2

        # Display a grid of file slots.
    grid columns rows:
        xalign .5
        yalign .48
        transpose True
        spacing 10
        style_group "file_picker"

        # Display ten file slots, numbered 1 - 10.
        for i in range(1, columns * rows + 1):

            # Each file slot is a button.
            frame:
                xsize 430
                ysize 242
                xpadding 0
                ypadding 0
                background None
                if i > 2:
                    at keys(300)
                else:
                    at keys(-300)

                button:
                    action FileAction(i)
                    xsize 430
                    ysize 242
                    xpadding 0
                    ypadding 0
                    background "#0009"
                    foreground "ui/sav/fg.png"
                    has hbox
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)
                    key "save_delete" action FileDelete(i)
                textbutton _(" ") action FileDelete(i) background "ui/q/del.png" at delbu xsize 25 ysize 25 yalign .99 xalign .01
                text "[file_name]" xalign .99 yalign .99
                text "[file_time!t]\n[save_name!t]" xalign .05 yalign .06


screen save():
    tag menu
    frame:
        xsize 1200
        ysize 800
        xalign .5
        yalign .5
        background "#fffc"
        button:
            xfill True
            yfill True
            action NullAction()
            background None
        imagebutton:
            xalign .99
            yalign .014
            idle "ui/set/close.png"
            hover "ui/set/close.png"
            action [Hide("save"),Return()]
            at keys
    use navigation
    use file_picker

screen load(n=1):
    tag menu
    frame:
        xsize 1200
        ysize 800
        xalign .5
        yalign .5
        background "#fffc"
        button:
            xfill True
            yfill True
            action NullAction()
            background None
        imagebutton:
            xalign .99
            yalign .014
            idle "ui/set/close.png"
            hover "ui/set/close.png"
            action [Hide("load"),Return()]
            at keys
    if n:
        use navigation
    else:
        use navigation1
    use file_picker

init -2:
    $ config.thumbnail_width = 430
    $ config.thumbnail_height = 242

    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text:
        font "anita.ttf"
        size 25
    style file_picker_button_text:
        size 15
        color "#fff"
        font "Interceptor.otf"
        ypos 16


##############################################################################
# Preferences
#init python:
#    renpy.music.register_channel("ambient", "ambient",  loop=True)
#    renpy.music.register_channel("ambient2", "ambient",  loop=True)
#    renpy.music.register_channel("sound2", "sfx",  loop=False)
#    renpy.music.register_channel("sound3", "sfx",  loop=False)
transform fad:
    alpha 0
    pause .5
    linear .4 alpha 1
transform keys1(x=0,y=0,ft=.4):
    parallel:
        alpha 0 yoffset y xoffset x
        easein ft alpha 1 yoffset 0 xoffset 0
    parallel:
        on hover:
            easein .4 alpha .8
        on idle:
            easein .4 alpha 0.4
        on selected_hover:
            easein .4 alpha .8
        on selected_idle:
            easein .4 alpha 1.0
screen preferences(n=1):
    tag menu

    style_group "prefs"
#    frame:
#        xalign .5
#        yalign .5
#        vbox:
#            hbox:
#                frame:
#                    has vbox:
#                        bar value Preference("music volume") maximum(560, 50) left_gutter 270 right_gutter 45 left_bar "ui/set/mu2.png"  right_bar "ui/set/mu1.png"
#                        bar value Preference("sound volume") maximum(560, 50) left_gutter 270 right_gutter 45 left_bar "ui/set/so2.png"  right_bar "ui/set/so1.png"
#                frame:
#                    has vbox:
#                        bar value Preference("text speed") maximum(560, 50) left_gutter 270 right_gutter 45 left_bar "ui/set/txt2.png"  right_bar "ui/set/txt1.png"
#                        bar value Preference("auto-forward time") maximum(560, 50) left_gutter 270 right_gutter 45 left_bar "ui/set/fwd2.png"  right_bar "ui/set/fwd1.png"
#            hbox:
#                frame:
#                    has vbox:
#                        imagebutton:
#                            idle "ui/set/win.png"
#                            hover "ui/set/win.png"
#                            focus_mask True
#                            action Preference("display", "window")
#                        imagebutton:
#                            idle "ui/set/full.png"
#                            hover "ui/set/full.png"
#                            focus_mask True
#                            action Preference("display", "fullscreen")
#                frame:
#                    has vbox:
#                        imagebutton:
#                            idle "ui/set/transall.png"
#                            hover "ui/set/transall.png"
#                            focus_mask True
#                            action Preference("transitions", "all")
#                        imagebutton:
#                            idle "ui/set/transnon.png"
#                            hover "ui/set/transnon.png"
#                            focus_mask True
#                            action Preference("transitions", "none")
#            hbox:
#                frame:
#                    has vbox:
#                        imagebutton:
#                            idle "ui/set/skipseen.png"
#                            hover "ui/set/skipseen.png"
#                            focus_mask True
#                            action Preference("skip", "seen")
#                        imagebutton:
#                            idle "ui/set/skipall.png"
#                            hover "ui/set/skipall.png"
#                            focus_mask True
#                            action Preference("skip", "all")
#                        imagebutton:
#                            idle "ui/set/skp.png"
#                            hover "ui/set/skp.png"
#                            focus_mask True
#                            action Skip()
#                frame:
#                    has vbox:
#                        imagebutton:
#                            idle "ui/set/stop.png"
#                            hover "ui/set/stop.png"
#                            focus_mask True
#                            action Preference("after choices", "stop")
#                        imagebutton:
#                            idle "ui/set/keep.png"
#                            hover "ui/set/keep.png"
#                            focus_mask True
#                            action Preference("after choices", "skip")
#                        imagebutton:
#                            idle "ui/set/Joystick.png"
#                            hover "ui/set/Joystick.png"
#                            focus_mask True
#                            action Preference("joystick")
    frame:
        xsize 1200
        ysize 800
        xalign .5
        yalign .5
        background "#fffc"
        add "ui/set/1.png" at fad xalign .12 yalign .335
        button:
            xfill True
            yfill True
            action NullAction()
            background None
        imagebutton:
            xalign .99
            yalign .014
            idle "ui/set/close.png"
            hover "ui/set/close.png"
            action [Hide("preferences"),Return()]
            at keys
        #at fad
        vbox:
            xalign .5
            yalign .32
            bar value Preference("music volume") maximum(530, 50) left_gutter 270 right_gutter 45 left_bar "ui/set/ms2.png"  right_bar "ui/set/ms1.png" at keys(-500)
            bar value Preference("sound volume") maximum(530, 50) left_gutter 270 right_gutter 45 left_bar "ui/set/su2.png"  right_bar "ui/set/su1.png" at keys(500)
            bar value Preference("ambient volume") maximum(530, 50) left_gutter 270 right_gutter 45 left_bar "ui/set/am2.png"  right_bar "ui/set/am1.png" at keys(-500)
            bar value Preference("voice volume") maximum(530, 50) left_gutter 270 right_gutter 45 left_bar "ui/set/vo2.png"  right_bar "ui/set/vo1.png" at keys(500)
            bar value Preference("text speed") maximum(530, 50) left_gutter 270 right_gutter 45 left_bar "ui/set/sp2.png"  right_bar "ui/set/sp1.png" at keys(-500)
            bar value Preference("auto-forward time") maximum(530, 50) left_gutter 270 right_gutter 45 left_bar "ui/set/fw2.png"  right_bar "ui/set/fw1.png" at keys(500)
            hbox:
                spacing -50
                if _preferences.fullscreen:
                    imagebutton:
                        idle "ui/set/wi.png"
                        hover "ui/set/wi.png"
                        focus_mask True
                        action Preference("display", "window")
                        at keys1(-500)
                else:
                    imagebutton:
                        idle "ui/set/wi.png"
                        hover "ui/set/wi.png"
                        focus_mask True
                        action Preference("display", "any window")
                        at keys1(-500)

                imagebutton:
                    idle "ui/set/wi1.png"
                    hover "ui/set/wi1.png"
                    focus_mask True
                    action Preference("display", "fullscreen")
                    at keys1(500)
#            hbox:
#                spacing -50
#                imagebutton:
#                    idle "ui/set/tr.png"
#                    hover "ui/set/tr.png"
#                    focus_mask True
#                    action Preference("transitions", "all")
#                    at keys1(-500)
#                imagebutton:
#                    idle "ui/set/tr1.png"
#                    hover "ui/set/tr1.png"
#                    focus_mask True
#                    action Preference("transitions", "none")
#                    at keys1(500)
            hbox:
                spacing -50
                imagebutton:
                    idle "ui/set/se.png"
                    hover "ui/set/se.png"
                    focus_mask True
                    action Preference("skip", "seen")
                    at keys1(-500)
                imagebutton:
                    idle "ui/set/se1.png"
                    hover "ui/set/se1.png"
                    focus_mask True
                    action Preference("skip", "all")
                    at keys1(500)
            hbox:
                spacing -50
                imagebutton:
                    idle "ui/set/ss.png"
                    hover "ui/set/ss.png"
                    focus_mask True
                    action Preference("after choices", "stop")
                    at keys1(-500)
                imagebutton:
                    idle "ui/set/ss1.png"
                    hover "ui/set/ss1.png"
                    focus_mask True
                    action Preference("after choices", "skip")
                    at keys1(500)
#            hbox:
#                spacing -50
#                imagebutton:
#                    idle "ui/set/be.png"
#                    hover "ui/set/be.png"
#                    focus_mask True
#                    action Skip()
#                    at keys1(-500)
#                imagebutton:
#                    idle "ui/set/jo.png"
#                    hover "ui/set/jo.png"
#                    focus_mask True
#                    action Preference("joystick")
#                    at keys1(500)
    if n:
        use navigation
    else:
        use navigation1

#    frame:
#        has vbox:
#            text "Display"
#            textbutton _("Windowed"):
#                action Preference("display", "window")
#                idle_background Frame("ui/set/btn.png",2,0,120,0)
#                hover_background Frame("ui/set/btn1.png",2,0,120,0)
#                ysize 60
#                right_padding 110
#        frame:
#            style_group "pref"
#            has vbox

#            label _("Display")


#        frame:
#            style_group "pref"
#            has vbox

#            label _("Transitions")


#        frame:
#            style_group "pref"
#            has vbox

#            label _("Text Speed")

#        frame:
#            style_group "pref"
#            has vbox




#    vbox:
#        frame:
#            style_group "pref"
#            has vbox

#            label _("Skip")


#        frame:
#            style_group "pref"
#            has vbox



#        frame:
#            style_group "pref"
#            has vbox

#            label _("After Choices")


#        frame:
#            style_group "pref"
#            has vbox

#            label _("Auto-Forward Time")


#            if config.has_voice:
#                textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

#    vbox:
#        frame:
#            style_group "pref"
#            has vbox

#            label _("Music Volume")


#        frame:
#            style_group "pref"
#            has vbox

#            label _("Sound Volume")


#            if config.sample_sound:
#                textbutton _("Test"):
#                    action Play("sound", config.sample_sound)
#                    style "soundtest_button"

#        if config.has_voice:
#            frame:
#                style_group "pref"
#                has vbox

#                label _("Voice Volume")
#                bar value Preference("voice volume")

#                textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
#                if config.sample_voice:
#                    textbutton _("Test"):
#                        action Play("voice", config.sample_voice)
#                        style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        ymargin 5

    style prefs_vbox:
        spacing 5

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0
    style prefs_button_text:
        font "Interceptor.otf"
    style prefs_text:
        font "Interceptor.otf"
##############################################################################
default exswitch = 0
screen extras:
    
    ### Austin Edit - WARNING text for unhidden images in gallery for spoilers
    if testWarning == 0:
        frame:
            xpadding 10
            ypadding 5
            xalign 0.5
            yalign 0.8
            
            vbox:
                text "{font=mechsuit.ttf}{size=24}WARNING! \n For the Ace Academy Alpha build, the gallery images are NOT obscured. \n This means all CG scenes are immediately available for viewing and WILL contain spoilers. Thank you for your understanding. \n Click to continue with the Extras menu.{/size}{/font}" xalign 0.5 yalign 0.8
                key "K_SPACE" action SetScreenVariable("testWarning", 1)
                key "K_SPACE" action ShowMenu("extras")
                
    ###
    
    tag ext
    add "ui/mm/bg.jpg"
    vbox:
        xalign .5
        yalign .5
        spacing 5
        imagebutton:
            idle "ui/ex/ga.png"
            hover "ui/ex/ga.png"
            focus_mask True
            action Show("gallery")
            at keys(-500)
        imagebutton:
            idle "ui/ex/mr.png"
            hover "ui/ex/mr.png"
            focus_mask True
            action Show("soundroom")
            at keys(500)
        imagebutton:
            idle "ui/ex/cr.png"
            hover "ui/ex/cr.png"
            focus_mask True
            action Show("credits")
            at keys(-500)
        imagebutton:
            idle "ui/ex/mm.png"
            hover "ui/ex/mm.png"
            focus_mask True
            action Show("main_menu")
            at keys(500)
init python:
    renpy.music.register_channel("soundroom1", "soundroom1",  loop=True)
    renpy.music.register_channel("soundroom2", "soundroom_2",  loop=False)
screen soundroom:
    tag ext
    add "ui/mm/bg.jpg"
#    add "ui/ex/000.png" xalign .5 yalign .915 alpha .2
#    add "ui/ex/00.png" xalign .5 yalign .002 alpha .2

    ### Austin Edit - Stops main menu music if it is playing
    if renpy.music.is_playing(channel='music'):
        timer 0.5 action Stop(channel='music', fadeout=1) #timer 0.5 action SetMute('music', True) #timer 0.5 action Stop(channel='music', fadeout=1)
    ###
    
    frame:
        xfill True
        ysize 0.8
        yalign .3
        xalign 1.0
        background None
        left_padding 0
        hbox:
            xalign 1.0
            frame:
                xsize .968
                left_padding 0
                background None
                viewport id "muroom":
                    draggable True
                    mousewheel True
                    xinitial 200
                    frame:
                        xfill True
                        background None
                        hbox:
                            #xfill True
                            xalign .5
                            #spacing 10
                            yalign .5
                            box_wrap True
                            for m in range(len(muscix)):
                                frame:
                                    background None
                                    fixed:
                                        xalign .5
                                        fit_first True
                                        frame:
                                            xalign .5
                                            xsize .68
                                            xpadding 40
                                            ypadding 40
                                            background "#000c"
                                            has hbox
                                            xalign .5
                                            spacing 20
                                            textbutton " " action Play("soundroom1", muscix[m].split("=",1)[1], selected=True) xsize 50 ysize 50 background "ui/ex/play.png" at keys1(-100)

                                            text muscix[m].split("=",1)[0] yalign .5 font "anita.ttf" size 20
                                        add "ui/ch/1.png" xalign 0.0 yalign 0.0
                                        add "ui/ch/2.png" xalign 1.0 yalign 1.0
            frame:
                background None
                vbar value YScrollValue("muroom") bar_invert True left_bar "#0ff2" right_bar "#0ff2" thumb "#fff3" xalign 1.0

#    textbutton _(" ") action SetVariable('pixbar', 0) background "ui/ex/000.png" xalign .5 yalign .92 xsize 100 ysize 100
#    textbutton _(" ") action SetVariable('pixbar', 0) background "ui/ex/00.png" xalign .5 xsize 100 ysize 100
    hbox:
        yalign .98
        xalign .5
        spacing 10
        bar value MixerValue('soundroom1') maximum(530, 50) left_gutter 270 right_gutter 45 left_bar "ui/set/ms2.png"  right_bar "ui/set/ms1.png" at keys(-500)
        if renpy.music.is_playing(channel='soundroom1'):
            #textbutton " " action Stop(channel='soundroom1', fadeout=None) xsize 50 ysize 50 background "ui/ex/pause.png" at keys1(-100)
            textbutton " " action Stop(channel='soundroom1', fadeout=None) xsize 50 ysize 50 background "ui/ex/stop.png" at keys1(-100)

        #bar value MixerValue('soundroom2') maximum(530, 50) left_gutter 270 right_gutter 45 left_bar "ui/set/su2.png"  right_bar "ui/set/su1.png" at keys(500)

    frame:
        background Frame("ui/chat/2.png",120,0,2,0)
        ysize 50
        right_padding 10
        left_padding 60
        xalign 1.0
        yalign 1.0
        imagebutton:
            yalign .5
            idle "ui/q/del.png"
            hover "ui/q/del.png"
            action Show("extras")
            at keys(100)

###############
define pixno = 0
define pixnum = 0
define pixbar = 1

transform gall(x=0,y=0,ft=.4):
    parallel:
        alpha 0 yoffset y xoffset x
        easein ft alpha 1 yoffset 0 xoffset 0
    parallel:
        on hover:
            easein .4 alpha .8
        on idle:
            easein .4 alpha 0.4
        on selected_hover:
            easein .4 alpha .8
        on selected_idle:
            easein .4 alpha 1.0

screen gallery:
    tag ext
    add "ui/mm/bg.jpg"
    frame:
        xpadding 0
        ypadding 0
        background None
        if persistent.gpix[pixnum][0]:
            add persistent.gpix[pixnum][2] yalign 1.0 xalign .5
        else:
            text "Locked" xalign .5 yalign .5 font "anita.ttf" size 45
        frame:
            background Frame("ui/chat/1.png",2,0,120,0)
            right_padding 70
            left_padding 15
            text str(persistent.gpix[pixnum][1]) font "anita.ttf" size 25
        vbox:
            yalign .92
            xfill True
            if pixbar:
                textbutton _(" ") action SetVariable('pixbar', 0) background "ui/ex/000.png" xalign .5 xsize 100 ysize 100
                frame:
                    ysize 200
                    background None
                    xfill True
                    xpadding 0
                    vbox:
                        xalign .5
                        hbox:
                            spacing -30
                            xalign .5
                            yoffset -5
                            imagebutton:
                                idle "ui/sav/bc.png"
                                hover "ui/sav/bc.png"
                                focus_mask True
                                action If(pixno>0, SetVariable('pixno', pixno-6))
                                at gall

                            for m in range(13):
                                button:
                                    xsize 94
                                    ysize 30
                                    xoffset -2
                                    background "ui/sav/1.png"
                                    at gall
                                    text str(m+1) size 20 xalign .5 yalign .5 font "anita.ttf"
                                    action SetVariable('pixno', m*6)
                            imagebutton:
                                idle "ui/sav/nx.png"
                                hover "ui/sav/nx.png"
                                focus_mask True
                                action If(pixno<m*6, SetVariable('pixno', pixno+6))
                                at gall
                        if pixno < 78:
                            frame:
                                background "#000c"
                                xfill True
                                ypadding 5
                                hbox:
                                    spacing 5
                                    xalign .5
                                    for ps in range(6):
                                        if persistent.gpix[ps+pixno][0]:
                                            button:
                                                xpadding 2
                                                ypadding 2
#                                                xsize 128
#                                                ysize 72
                                                background "#0ffa"
                                                at gall
                                                action SetVariable('pixnum', ps+pixno)
                                                add persistent.gpix[ps+pixno][2] xalign .5 zoom .16 crop(0,0,1920,1080)
                                        else:
                                            button:
                                                xpadding 2
                                                ypadding 2
                                                xsize 312
                                                ysize 179
                                                background "#0ffa"
                                                at gall
                                                action SetVariable('pixnum', ps+pixno)
                                                text "Locked" xalign .5 yalign .5 font "anita.ttf" size 45
                        else:
                            frame:
                                background "#000c"
                                xfill True
                                ypadding 5
                                hbox:
                                    spacing 5
                                    xalign .5
                                    for ps in range(2):
                                        button:
                                            xpadding 2
                                            ypadding 2
                                            xsize 128
                                            ysize 72
                                            background "#0ffa"
                                            at gall
                                            action SetVariable('pixnum', ps+pixno)
                                            add persistent.gpix[ps+pixno][2] xalign .5 zoom .16 crop(0,0,1920,1080)
            else:
                textbutton _(" ") action SetVariable('pixbar', 1) background "ui/ex/00.png" xalign .5 ypos 40 xsize 100 ysize 100

    frame:
        background Frame("ui/chat/2.png",120,0,2,0)
        ysize 50
        right_padding 10
        left_padding 60
        xalign 1.0
        yalign 1.0
        imagebutton:
            yalign .5
            idle "ui/q/del.png"
            hover "ui/q/del.png"
            action Show("extras")
            at keys(100)

init -2:
    style gally_button:
        size_group "yesno"

#########
screen credits:
    tag ext
    style_group "cred"
    add "ui/mm/bg.jpg"
    frame:
        xfill True ysize 0.8 yalign .3 xalign 1.0 background None left_padding 0
        hbox:
            xalign 1.0
            frame:
                xsize .968 left_padding 0 background None
                viewport id "muroom":
                    draggable True mousewheel True xinitial 200
                    frame:
                        xfill True background None
                        vbox:
                            spacing 60
                            text "Staff"
                            vbox:
                                spacing 20
                                frame:
                                    xsize 1000
                                    text "Producers"
                                vbox:
                                    spacing 10
                                    text "Dishu Khan"
                                    text "Rishu Khan"
                                    text "Donnie Roos"
                                    text "Ex Zee"
                                    text "Mahkcloud"

                            vbox:
                                spacing 20
                                frame:
                                    xsize 1000
                                    text "Director"
                                vbox:
                                    spacing 10
                                    text "Dishu Khan"

                            vbox:
                                spacing 20
                                frame:
                                    xsize 1000
                                    text "Artists"
                                vbox:
                                    spacing 10
                                    text "Sunimu"
                                    text "Keith Chan Xeikth"
                                    text "Badriel"
                                    text "Teagirl-vn"
                                    text "Shoji"
                                    text "KiaAzad"

                            vbox:
                                spacing 20
                                frame:
                                    xsize 1000
                                    text "Writers"
                                vbox:
                                    spacing 10
                                    text "Alisia Faust"
                                    text "Dishu Khan"

                            vbox:
                                spacing 20
                                frame:
                                    xsize 1000
                                    text "Programmers"
                                vbox:
                                    spacing 10
                                    text "Austin Bryant"
                                    text "Dishu Khan"

                            vbox:
                                spacing 20
                                frame:
                                    xsize 1000
                                    text "Composer"
                                vbox:
                                    spacing 10
                                    text "Christopher Escalante"

                            vbox:
                                spacing 20
                                frame:
                                    xsize 1000
                                    text "Audio Production"
                                vbox:
                                    spacing 10
                                    text "Dishu Khan"

                            vbox:
                                spacing 20
                                frame:
                                    xsize 1000
                                    text "OPENING - \"Dual Swords\"" 
                                vbox:
                                    spacing 10
                                    text "Song/Arrangement/Mix&Master - Vulkain"
                                    text "Lyrics - Saint"
                                    text "Singers - Hikaru & Vulkain"

                            vbox:
                                spacing 20
                                frame:
                                    xsize 1000
                                    text "Voice Talent"
                                vbox:
                                    spacing 10
                                    text "Tina \"Pickle131\" Kim - Nikki"
                                    text "Sydney \"Sydsnap\" Poniewaz - Kaori Itami"
                                    text "Samantha Chan - Yuuna Misaki"
                                    text "Angela Lorenzana - Valerie Belle"
                                    text "Alexandra Boodram - Mayu Akemi"
                                    text "Kim Morton - Shou Shinjirou"
                                    text "Bradley Petyak - Kaito Hikari"
                                    text "Amanda Lee - Mei Satomi // AmaLee"
                                    text "Miguel Moran - Akira Masata // Various Roles"
                                    text "James Brown Jr. - Eagle // Various Roles"
                                    text "Olivia Steele - Yuki Hikari // Various Roles"
                                    text "Kyle Lumash - Ken Kokan // Various Roles"
                                    text "Christopher Escalante - Various Roles"
                                    text "Lee Turner - Various Roles"
                                    text "Peter Colon - Various Roles"
                                    text "Luci W. - Various Roles"
                                    text "Alexandria B. - Various Roles"
                                    text "Arthur Romeo - Various Roles"

                            

                            text "Supporters"
                            vbox:
                                spacing 20
                                frame:
                                    xsize 1000 xalign .5
                                    text "PixelFader - PFL3" 
                                vbox:
                                    text "Konrad Michalek"
                                    text "Matthew Harper"
                                    text "Toh Xin Tian"
                                    text "Tomi Arola"
                                    text "BirdmanGA - \"Hypatia's Engineer\""
                                    text "Oruun - \"If a regular 'Visual Novel' is like Ketchup, then 'ACE Academy' is like 'Mayu'\""
                                    text "Butlee"
                                    text "Christopher Oates"
                                    text "Steinar Hagen"
                                    text "terrman - \"(insert witty comment here)\""
                                    text "Vox Chaotica - \"I have paid mad Patreon money to state that Valerie is best girl, and everyone else is objectively wrong.\""
                                    text "Liam Poole"
                                    text "SpriteReaction"
                                    text "BjÃ¶rn 'Rainwolf' Oberbrodhage"
                                    text "Daniel Evans"
                                    text "Jimmylamtk"
                                    text "technocat"
                                    text "Sean Jewett - \"...K-k-kaori!!!!!!!!! Q_Q...\""
                                    text "Thomas Richard Wall"
                                    text "Tristan Medina"
                                    text "IIIllIIl"
                                    text "Jacob Harmon"
                                    text "Gin"
                                    text "BlaÅ¾"
                                    text "Mikhail Solomatin"
                                    text "Aegeta"
                                    text "Austichar - \"Know what'd be kickass? A neko Gear with, like, dual wield rail guns.\""
                                    text "Lukas 'Vladek' Frehner - \"Love to Valerie, best Waifu ever!\""
                            vbox:
                                spacing 20
                                frame:
                                    xsize 1000 xalign .5
                                    text "PixelFader - PFL2" 
                                vbox:
                                    text "BitFaze"
                                    text "Om Chaudhari"
                                    text "Candy-Sama"
                                    text "Tanner Visser"
                                    text "Sam G"
                                    text "Daniel Needs"
                                    text "Jack Mccallam - \"Mom I made it!\""
                                    text "Callum Horton - \"Hey Ric!\""
                                    text "hkthui"
                            vbox:
                                spacing 20
                                frame:
                                    xsize 1000 xalign .5
                                    text "PixelFader - PFL1" 
                                vbox:
                                    text "The Crushor - \"Silver Wings of Valor\""
                                    text "James Connally"
                                    text "Ben Goldstein"
                                    text "CrashRocks1419"
                                    text "Lukas 'Vladek' Frehner"
                                    text "David \"Spanish Dave\" Carvalho - \"I'm portuguese, dammit!\""
                                    text "Duc"
                                    text "Peter Villumsen"
                                    text "Daniel Chung - \"Cedroes was here.\""

                            vbox:
                                spacing 20
                                frame:
                                    xsize 1000 xalign .5
                                    text "PixelFader - KS" 
                                vbox:
                                    text "Jorgen Robertson"
                                    text "Daniel Kruse"
                                    text "Gilbert"
                                    text "Aaron - Exiled WereSheep in Torment"
                                    text "Anthony"
                                    text "Jambles"
                                    text "Phoenix"
                                    text "Matthew Spreeman"
                                    text "RUI CHENG"
                                    text "Kingz"
                                    text "Kyle Abeyta"
                                    text "Wade Clemons"
                                    text "First Mate Shou"
                                    text "Daniel Evans"
                                    text "ZeroGamer"
                                    text "Mr_Enigma"
                                    text "KennyJ"
                                    text "Hubert Volecek"
                                    text "Erwin Sutrisno"
                                    text "Alec Greenbank"
                                    text "Bryan"
                                    text "Luke Harrison"
                                    text "Erde"
                                    text "Alexander John Aristotle Kimball"
                                    text "BuffAnimeScientist"
                                    text "Bryan Tsang"
                                    text "Cap'n Kaori"
                                    text "Redcomet"
                                    text "YP Lim"
                                    text "Rei Aoki"
                                    text "William Taylor Lashbrook"
                                    text "Alen Wong"
                                    text "Lukasz Pawlus"
                                    text "Simon W. Steen"
                                    text "LordRevan"
                                    text "Océane Gulini"
                                    text "Iikka Yli-Kuivila"
                                    text "Solomatin Mikhail"
                                    text "Erwin Matthew Patalinghug"
                                    text "Annatalonstv"

                            vbox:
                                spacing 20
                                frame:
                                    xsize 1000 xalign .5
                                    text "Credits - KS" 
                                vbox:
                                    text "Quynh Thai"
                                    text "tobymage@hotmail.co.uk"
                                    text "christopher oates"
                                    text "Mathew Fang"
                                    text "Jan Martin"
                                    text "Riley O"
                                    text "Kanbei N.Q.B"
                                    text "Ian Howell"
                                    text "Emma Snowden"
                                    text "Marcus Salvano"
                                    text "Maverick Salvano"
                                    text "HybridKoala"
                                    text "AlexM"
                                    text "Jeffrey Esquibel"
                                    text "David Luke Williams"
                                    text "Levi Moreno"
                                    text "Taylor Staley"
                                    text "Nat Chandhaketh"
                                    text "Andrew S Burns"
                                    text "Bastiaan Rours"
                                    text "Kyler Markowski"
                                    text "RocK_M"
                                    text "Adam Tropf"
                                    text "kyle bray"
                                    text "Sebastian Dittel"
                                    text "Riley Dark"
                                    text "Lukasz Przyborowski"
                                    text "Jordan Pugeda"
                                    text "Seuya Oniell"
                                    text "Stian H. G."
                                    text "Heather Christmas"
                                    text "Patrice Fournier"
                                    text "VkBest"
                                    text "Ryuutai"
                                    text "Taylor Collins"
                                    text "Mayu The Pirate"
                                    text "Christopher Larrimore"
                                    text "Boop"
                                    text "Hobbles"
                                    text "Nayamu"
                                    text "Vol"
                                    text "AbdulAziz Al-Kaboor"
                                    text "Chris Lefebvre"
                                    text "Ryan Kabir"
                                    text "Ryan Jones"
                                    text "Paul Broad"
                                    text "Chua Chong Yi"
                                    text "Michael Brand"
                                    text "Lin Liren"
                                    text "Andreas"
                                    text "Tom George"
                                    text "David Green"
                                    text "Jan Marius Holmen"
                                    text "Dina Edgar"
                                    text "Geoffrey Gilmore"
                                    text "Chris Almquist"
                                    text "nicolas fjellman"
                                    text "Philip Chan"
                                    text "Stephan Hansen"
                                    text "Tomi Arola"
                                    text "Richard Wagener"
                                    text "Sascha Basta"
                                    text "flexxdk"
                                    text "Tobie Collier"
                                    text "Dan Chadek"
                                    text "Angad Singh"
                                    text "Pascal Ziegler"
                                    text "Joshua Valdez"
                                    text "Jacob Keifer"
                                    text "MITCHELL FRAZER"
                                    text "Jeff Thompson"
                                    text "Adam Massingham"
                                    text "andrew iyog"
                                    text "Katrin Koch"
                                    text "Hunter Ragland"
                                    text "Tristan Medina - \"I'm on to you Dishu!\""
                                    text "Gustavo Ortiz"
                                    text "Pyry Rauhala"
                                    text "Alexis Perron"
                                    text "Tom Rothamel"
                                    text "Pesky Pyjak"
                                    text "saodhar"
                                    text "Dawn_"
                                    text "Calvin Collins"
                                    text "Timothy Chappell"
                                    text "Chris Marquardson"
                                    text "Richard Ford"
                                    text "tom"
                                    text "Mark Shaw"
                                    text "Morten Wiborg"
                                    text "John"
                                    text "Carlos Bruno Alves"
                                    text "Dynadrag"
                                    text "Gadgetman!"
                                    text "김태우"
                                    text "Greg Polander"
                                    text "Nathaniel Pahl"
                                    text "Mr.Quija"
                                    text "Ivan Nicolas"
                                    text "Braedon"
                                    text "Merc"
                                    text "Vincentius Robby"
                                    text "Mike Penny"
                                    text "Alex Phrom"
                                    text "Jonathan Cogan"
                                    text "Levi McConnell"
                                    text "Clayton Baker"
                                    text "Mika Flinkman"
                                    text "Brandon Edwards"
                                    text "Matthew Jacob Chua Wepee"
                                    text "Anakiro"
                                    text "Joseph Shivak"
                                    text "Shadekirby321"
                                    text "Mathias"
                                    text "Seto Konowa"
                                    text "G. Ryan"
                                    text "Doug Gordon"
                                    text "M. van Dortmont"
                                    text "Leon Bryce-Stenzel"
                                    text "Lars Mattsson"
                                    text "Shane LaRue"
                                    text "Sen Harada"
                                    text "lytel"
                                    text "Eric Amtmanis"
                                    text "Sarnitru"
                                    text "Kyle Pinder"
                                    text "Ben-Allen Hofmann"
                                    text "Cameron Justin Taylor"
                                    text "Jonathan Tsao"
                                    text "Luke \"RidiculousLuke\" Smith"
                                    text "Rusty Katt"
                                    text "Guillaume Lebigot"
                                    text "Nico Verbruggen"
                                    text "RhaelLathe"
                                    text "Marco Lau"
                                    text "Pete.B"
                                    text "Lazzarus"
                                    text "Thanh Pham"
                                    text "Owen Sa"
                                    text "Kai Hellmeier"
                                    text "David Lyons"
                                    text "WiredRM"
                                    text "Rolando Contreras"
                                    text "Tjalling Lankreijer"
                                    text "Peter Charrington"
                                    text "Steve (deleted)"
                                    text "Negima"
                                    text "Nicholas Pitson"
                                    text "Matt Brown"
                                    text "Anaël Verrier"
                                    text "Chris Bastion"
                                    text "Ulrik Søgaard"
                                    text "winta"
                                    text "James Kahalewai III"
                                    text "HackaFreak (deleted)"
                                    text "AlmostHuman"
                                    text "Daniel Compton"
                                    text "Otto Flick"
                                    text "Tj C"
                                    text "Harry Grewal"
                                    text "Benoton"
                                    text "Andrew Camner"
                                    text "Darn"
                                    text "Rafael Chave"
                                    text "Kyle Wooten"
                                    text "Antonio Osegueda"
                                    text "Daniel Lin"
                                    text "Stephen Krause"
                                    text "Smexykins"
                                    text "Børre"
                                    text "Boomer Barr"
                                    text "Gavin McGee"
                                    text "Robbie Boerner"
                                    text "Shannon Plaice"
                                    text "Oscar Ulloa"
                                    text "Calvin"
                                    text "Cody Dalton Bagley"
                                    text "Scott Raboy"
                                    text "Accelsharp"
                                    text "Michael Sato"
                                    text "Chao Wa Cho"
                                    text "João Dias"
                                    text "LD_AKA_Blaze"
                                    text "arperson"
                                    text "Ronny Seidel"
                                    text "Danny Kiregbaum Laursen"
                                    text "Niall"
                                    text "Hunter"
                                    text "Kurt K"
                                    text "James Rooney"
                                    text "Isaac Broadbent"
                                    text "Edwin Keecha"
                                    text "D'Vreaux Fontaine"
                                    text "John Rudberg"
                                    text "Steven E."
                                    text "CavemanMC"
                                    text "Shosuke"
                                    text "Anthony Capote"
                                    text "Travis Fuller"
                                    text "Dave Jareckas"
                                    text "Scott Nairn"
                                    text "Jeff"
                                    text "Robert Diaz"
                                    text "Markuli"
                                    text "Sven"
                                    text "Josh Bennett"
                                    text "Miguel De serpa"
                                    text "Jared Ritter"
                                    text "Eleanor Walker"
                                    text "Simon Sterchi"
                                    text "Edward Moreno"
                                    text "Fridgecrisis Games"
                                    text "Scott Tuinstra"
                                    text "garkham"
                                    text "Christopher Chan"
                                    text "manpapper"
                                    text "Darryl Warcup"
                                    text "Nico B"
                                    text "Tony Evans"
                                    text "Thulium"
                                    text "Michael James Musumeci"
                                    text "Adam H"
                                    text "Marcus Soll"
                                    text "WizardFromTheWest"
                                    text "Matthew Leone"
                                    text "Christopher Scherer"
                                    text "Aaron Delino"
                                    text "Зеро"
                                    text "Michael Green"
                                    text "Jackson Dzus"
                                    text "Christopher J Headley"
                                    text "Yorai"
                                    text "Never_Land-_-"
                                    text "Gonsalo Ceja"
                                    text "Brian Griffin"
                                    text "Cesar Gonzalez"
                                    text "King-Koinzell"
                                    text "Shinamaru"
                                    text "Jacob Wayne Miller"
                                    text "Ash Barker"
                                    text "David Mendez"
                                    text "Karbunos"
                                    text "Julian"
                                    text "Aaron W"
                                    text "Yogiri"
                                    text "MalinwaGaming"
                                    text "Alex F"
                                    text "Jason Banks-Smith"
                                    text "Jardine"
                                    text "Moonflow43"
                                    text "Christopher Hardy"
                                    text "alexander weber"
                                    text "Haken Browning"
                                    text "Rebecca"
                                    text "Christian Ellis"
                                    text "Logan Poast"
                                    text "Milagro Mendoza"
                                    text "Aaron Yun"
                                    text "Tobias Schwarz"
                                    text "Christopher Peer"
                                    text "Mark Choi"
                                    text "Sean Mailloux"
                                    text "Pierre Kühne"
                                    text "ron crory"
                                    text "Jamie DeBruin"
                                    text "sopheark phan"
                                    text "Mathias \"Taykerz\""
                                    text "Matthew Guerra"
                                    text "Tyler Briddelle"
                                    text "Jordan Kline"
                                    text "Roencia Game Creators"
                                    text "Michael Connell"
                                    text "Scott Small"
                                    text "Joshua Peng"
                                    text "gekiganwing"
                                    text "FSH"
                                    text "Canyon"
                                    text "CtrlAltFaceroll"
                                    text "Chayne VandeZande"
                                    text "Alectoromancy"
                                    text "Michael Denstman"
                                    text "Marissa"
                                    text "Ghostly_Dobrik"
                                    text "Patrick Russell"
                                    text "@Deesconcerted"
                                    text "Florian Fremeaux"
                                    text "Leon Han"
                                    text "Jacques Alexander Katzoff"
                                    text "Bryan Lyon"
                                    text "Paul H"
                                    text "John J. Walsh IV"
                                    text "robotsheepboy"
                                    text "Matthew De Leon"
                                    text "Cristobal Mera"
                                    text "Kevin Nunnelly"
                                    text "Mathias Tellefsen"
                                    text "Chriss"
                                    text "Xwarzone"
                                    text "Joe Dyson"
                                    text "KT"
                                    text "Shawn Poulen"
                                    text "Daya Adianto"
                                    text "eh4rris"
                                    text "MatthewB"
                                    text "Tim Yordan"
                                    text "Anthony Cash"
                                    text "Agus Hartono"
                                    text "Sigfried"
                                    text "James Dyer"
                                    text "Ada Ballard"
                                    text "Jordan Reid"
                                    text "Isaac Lawrence"
                                    text "ABruneianKickstarterBacker"
                                    text "Matthew Moreni"
                                    text "Thomas Zilling - Tormented WoOS of OOoE"
                                    text "Leevi Pietiläinen"
                                    text "Kramoule"
                                    text "Ly w"
                                    text "Mike McCarthy"
                                    text "Justin Kunstman"
                                    text "Kuo Wei Lee"
                                    text "JJ Lee"
                                    text "Kai Miang"
                                    text "Matthew Hochberg"
                                    text "DCQ"
                                    text "Michal Karásek"
                                    text "Janosch Kaufmann"
                                    text "Marcin Starzyk"
                                    text "andrew Richardson"
                                    text "Chris_JS"
                                    text "Ryley Giordanengo"
                                    text "Guillem VIDAL"
                                    text "tom"
                                    text "Emil Jinstrand"
                                    text "Albert"
                                    text "Alexander Probst"
                                    text "Austin Liao"
                                    text "Li Rao"
                                    text "Henry Phan"
                                    text "Jaknk"
                                    text "Taedirk"
                                    text "Mark Ruiz"
                                    text "Judy Fan"
                                    text "Chandra \"Sakura\" Hughes"
                                    text "Konbon"
                                    text "Lubrioz"
                                    text "ZuiQuanX"
                                    text "jimmy chou"
                                    text "Federico Giovanni Sala"
                                    text "Steψhen"
                                    text "Sven Albion"
                                    text "Jakob Thorsager Petersen"
                                    text "Eric Mundt"
                                    text "Cody Jolin"
                                    text "David McCarthy"
                                    text "Randy Jin"
                                    text "Chris Kuieck"
                                    text "Joshua Wu"
                                    text "Devon Darroch"
                                    text "Michael Sand"
                                    text "Eric Zhang"
                                    text "Andrew Harvey"
                                    text "Jelly Paladin"
                                    text "Henrik Ekebro"
                                    text "Andrew Craig"
                                    text "Kid Andersson"
                                    text "Daniel Debney"
                                    text "josh billington"
                                    text "Michael Polis"
                                    text "Harold Oduardo"
                                    text "Rubberside"
                                    text "scyleung"
                                    text "masterdgk"
                                    text "Glaring Mistake"
                                    text "Boss Sirikul"
                                    text "Michele Dellolio"
                                    text "Thomas Custer"
                                    text "Guilherme Chelli de Almeida"
                                    text "Jesus"
                                    text "Simon Wares"
                                    text "Ole Andreas Gresholt"
                                    text "Tamir Gilboa"
                                    text "Casey"
                                    text "\"Too Tired and Busy\" Fred"
                                    text "Chris Taran"
                                    text "Tiago Martins"
                                    text "Phillip Rechnitzer"
                                    text "WanderingWlf"
                                    text "Ryan Tabb"
                                    text "Frank Barr"
                                    text "Glen Risha"
                                    text "Cevontae Miller"
                                    text "Erich L."
                                    text "Thaddeus Witmore"
                                    text "Hamilton Bradford"
                                    text "Simon Holk"
                                    text "Hadies"
                                    text "Kennan Ward"
                                    text "Juan Araya"
                                    text "Jasen Betts"
                                    text "Aleix Cintero Sàez"
                                    text "Young"
                                    text "TrickZter"
                                    text "Zacky Chun-pong Leung"

            frame:
                background None
                vbar value YScrollValue("muroom") bar_invert True left_bar "#0ff2" right_bar "#0ff2" thumb "#fff3" xalign 1.0
    frame:
        background Frame("ui/chat/2.png",120,0,2,0)
        ysize 50
        right_padding 10
        left_padding 60
        xalign 1.0
        yalign 1.0
        imagebutton:
            yalign .5
            idle "ui/q/del.png"
            hover "ui/q/del.png"
            action Show("extras")
            at keys(100)
init -1:
    style cred_text:
        size 30 xalign .5
    style cred_vbox:
        xalign .5
    style cred_frame:
        background Frame("ui/ex/n.png",100,0,100,0)
##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
init python:
    config.quit_action = Quit()
screen yesno_prompt(message, yes_action, no_action):
    #add "ui/mm/bg.jpg"
    modal True
    frame:
        xsize 1200
        ysize 800
        xalign .5
        yalign .5
        xpadding 40
        background "#fffc"
        frame:
            style_group "yesno"
            background "#000c"
            xfill True
            yalign .5
            ypadding 50

            has vbox:
                xalign .5
                yalign .5
                spacing 30

            label _(message):
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100
                imagebutton:
                    xalign .5
                    yalign .82
                    idle "ui/yn/y.png"
                    hover "ui/yn/y.png"
                    focus_mask True
                    action yes_action
                    at keys(-500)
                imagebutton:
                    xalign .5
                    yalign .82
                    idle "ui/yn/n.png"
                    hover "ui/yn/n.png"
                    focus_mask True
                    action no_action
                    at keys(500)

        # Right-click and escape answer "no".
        key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
define kkk=0
#transform qut:
#    alpha .3
#    on hover:
#        linear .4 alpha 1.0
#    on idle:
#        linear .4 alpha .7
#screen quick_m:

#    frame:
#        background Frame("ui/chat/2.png",120,0,2,0)
#        ysize 50
#        right_padding 10
#        left_padding 60
#        hbox:
#            style_group "quick"
#            yalign .5
#            spacing 5
#            if ss:
#                textbutton _(" ") action Rollback() background "ui/q/0.png" at qut
##                textbutton _(" ") action ShowMenu('save') background "ui/q/1.png"
#                textbutton _(" ") action QuickSave() background "ui/q/1.png" at qut
#                textbutton _(" ") action QuickLoad() background "ui/q/2.png" at qut
#                textbutton _(" ") action Skip() background "ui/q/3.png" at qut
#                textbutton _(" ") action Skip(fast=True, confirm=True) background "ui/q/7.png" at qut
#                textbutton _(" ") action Preference("auto-forward", "toggle") background "ui/q/5.png" at qut
#                textbutton _(" ") action ShowMenu('preferences') background "ui/q/6.png" at qut
#                textbutton _(" ") action SetVariable("ss",0) background "ui/q/4.png" at qut
#            else:
#                textbutton _(" ") action SetVariable("ss",1) background "ui/q/4.png" at qut
##                if _preferences.auto-forward time==enable:
##                    textbutton _(" ") action Skip(fast=True, confirm=True) background "ui/q/7.png"
#init -2:
#    style quick_button:
#        is default
#        background None
#        xpadding 5
#        xsize 25
#        ysize 25
#    style quick_button_text:
#        is default
#        size 14
#        idle_color "#fff"
#        hover_color "#ccc"
#        selected_idle_color "#cc08"
#        selected_hover_color "#cc0"
#        insensitive_color "#4448"

transform qut:
    alpha .7
    on hover:
        linear .4 alpha 1.0
    on idle:
        linear .4 alpha .7
screen quick_m:

    frame:
        background Frame("ui/chat/2.png",120,0,2,0)
        ysize 50
        ypadding 0
        right_padding 10
        left_padding 60
        hbox:
            style_group "quick"
            yalign .5
            spacing 10
            if kkk:
#                textbutton _("Back") action Rollback() background "ui/q/0.png" at qut
#                textbutton _(" ") action ShowMenu('save') background "ui/q/1.png"
                textbutton _("Q.Save") action QuickSave() background "ui/q/1.png" at qut
                textbutton _("Q.Load") action QuickLoad() background "ui/q/2.png" at qut
                textbutton _("Skip") action Skip() background "ui/q/3.png" at qut
#                textbutton _("F.Skip") action Skip(fast=True, confirm=True) background "ui/q/7.png" at qut
                textbutton _("Auto") action Preference("auto-forward", "toggle") background "ui/q/5.png" at qut
                textbutton _("Prefs") action ShowMenu('preferences') background "ui/q/6.png" at qut
                textbutton _(" ") action SetVariable("kkk",0) background "ui/q/4.png" at qut
            else:
                textbutton _(" ") action SetVariable("kkk",1) background "ui/q/4.png" at qut
#                if _preferences.auto-forward time==enable:
#                    textbutton _(" ") action Skip(fast=True, confirm=True) background "ui/q/7.png"
init -2:
    style quick_button:
        is default
        background None
        left_padding 40
        xminimum 50
        ysize 50

    style quick_button_text:
        is default
        size 20
        xpadding 100

        yalign .6
        idle_color "#fff"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#fff8"
