### TEST SCRIPT ###

    #stop music
    #$ inv.add("defaultCore")
    #$ inv.add("defaultFrame")
    #$ inv.add("defaultThruster")
    
    #$ inv.add("defaultBuster")
    #$ inv.add("defaultDaggers")
    #$ inv.add("defaultKatana")
    #$ inv.add("defaultPistol")
    #$ inv.add("defaultRifle")
    #$ inv.add("defaultSMG")
    
    #call screen inventory_screen


init python:
    equipment = {"e001" : ["Equipment #001",
                           "Some details about Equipment #001 that is a core element.",
                           "icon_gun1",
                           "core",
                           [("hp", 50), ("energy", -10), ("damage", 0), ("combo", 0)],
                           100,
                           40,
                           10
                          ],
        "e002" : ["Equipment #002",
               "Some details about Equipment #001",
               "icon_gun2",
               "core",
               [("hp", -10), ("energy", 40), ("damage", 10), ("combo", 20)],
               60,
               30,
               20
              ],
        "e003" : ["Equipment #003",
               "Some details about Equipment #003",
               "icon_thrust",
               "thrust",
               [("hp", -30), ("energy", 30), ("damage", 40), ("combo", 50)],
               70,
               50,
               10
               ],
        "e004" : ["Equipment #004",
               "Some details about Equipment #004",
               "icon_melee1",
               "melee",
               [("hp", 50), ("energy", -40), ("damage", 0), ("combo", 0)],
               30,
               60,
               15
              ],
        "e005" : ["Equipment #005",
               "Some details about Equipment #005",
               "icon_frame",
               "frame",
               [("hp", 50), ("energy", 80), ("damage", 10), ("combo", 0)],
               50,
               50,
               10
              ],
        "e006" : ["Equipment #006",
               "Some details about Equipment #006",
               "icon_gun3",
               "core",
               [("hp", 90), ("energy", 70), ("damage", 70), ("combo", 60)],
               25,
               80,
               8
              ],
        "None" : ["",
               "",
               "slot",
               "",
               [],
               0,
               0,
               0
              ],
        "maxfist" : ["GODHAND",
               "3/10 - IGN",
               "icon_melee1",
               "melee",
               [("hp", 9999), ("energy", 9999), ("damage", 9999), ("combo", 99)],
               0,
               9999,
               99
               ],
        "defaultBuster" : ["Buster Sword",
               "An energy-costly weapon most suitable for dealing high-damage single blows rather than chaining together attacks.",
               "icon_melee3",
               "melee",
               [("hp", 0), ("energy", 10), ("damage", 40), ("combo", 0)],
               0,
               40,
               0
               ],
        "defaultDaggers" : ["Twin Blades",
               "A weapon set designed for dealing low-damage blows but yielding higher damage potential with each successive strike.",
               "icon_melee2",
               "melee",
               [("hp", 0), ("energy", 0), ("damage", 5), ("combo", 10)],
               0,
               5,
               10
               ],
        "defaultKatana" : ["Katana",
               "A trusted blade with average capabilities.",
               "icon_melee1",
               "melee",
               [("hp", 0), ("energy", 0), ("damage", 15), ("combo", 5)],
               0,
               15,
               5
               ],
        "defaultPistol" : ["Semiautomatic Pistol",
               "A reliable firearm with average capabilities.",
               "icon_gun1",
               "range",
               [("hp", 0), ("energy", 0), ("damage", 15), ("combo", 5)],
               0,
               15,
               5
               ],
        "defaultRifle" : ["Gauss Rifle",
               "An energy-costly weapon most suitable for dealing high-damage single blows rather than chaining together attacks.",
               "icon_gun4",
               "range",
               [("hp", 0), ("energy", 23), ("damage", 80), ("combo", 0)],
               0,
               80,
               0
               ],
        "defaultSMG" : ["Submachine Guns",
               "A weapon set designed for dealing low-damage blows but yielding higher damage potential with each successive strike.",
               "icon_gun2",
               "range",
               [("hp", 0), ("energy", 0), ("damage", 5), ("combo", 10)],
               0,
               5,
               10
               ],
        "defaultCore" : ["Mysterious Core",
               "The core that my father helped work on.",
               "icon_core",
               "core",
               [("hp", 0), ("energy", 0), ("damage", 0), ("combo", 0)],
               50,
               0,
               0
               ],
        "defaultThruster" : ["Jet Thrusters",
               "Some older tech that uses steel-melting jet fuel.",
               "icon_thrust",
               "thrust",
               [("hp", 0), ("energy", 0), ("damage", 0), ("combo", 0)],
               0,
               0,
               0
               ],
        "defaultFrame" : ["American Frame",
               "A framework design typical of GEAR manufactured in the USA.",
               "icon_frame",
               "frame",
               [("hp", 50), ("energy", 0), ("damage", 0), ("combo", 0)],
               0,
               0,
               0
               ],
           }

    class Inventory():
        def __init__(self, name, limit):
            """
            name     - The name of the inventory. Can be anything
            limit    - The maximum number of items the player is allowed to have
            store    - A list which contains the items player has aquired
            equipped - Current Equipped items.
            """
            self.name       = name
            self.limit      = limit
            self.store      = []
            self.equipped   = {"core"   : "None",
                               "thrust" : "None",
                               "melee"  : "None",
                               "range"  : "None",
                               "frame"  : "None",
                               "misc"   : "None"
                              }
        
        def add(self, e_id):
            """
            e_id - The id of the equipment to be equipped
            """
            if len(self.store) < self.limit:
                self.store.append(e_id)
            else:
                print "Inventory is full. Remove something first"
        
        def remove(self, e_id):
            """
            e_id - The id of the equipment to be equipped
            """
            if e_id in self.store:
                self.store.remove(e_id)
            elif e_id in self.equipped.values():
                self.unequip(e_id)
                self.store.remove(e_id)
        
        def equip(self, e_id):
            """
            e_id - The id of the equipment to be equipped
            """
            if self.equipped[equipment[e_id][3]] is not None:
                _old_id = self.equipped[equipment[e_id][3]]
                self.unequip(_old_id)
            self.equipped[equipment[e_id][3]] = e_id
            for i in equipment[e_id][4]:
                setattr(store, i[0], eval(i[0]) + i[1])
            self.remove(e_id)
            return
        
        def unequip(self, e_id):
            """
            e_id - The id of the equipment to be equipped
            """
            if equipment[e_id][3]in self.equipped:
                self.equipped[equipment[e_id][3]] = "None"
                for i in equipment[e_id][4]:
                    setattr(store, i[0], eval(i[0]) - i[1])
                self.add(e_id)
        
        def filter(self, type):
            """
            type - The type equipment to be shown. Can be any of the key in dict self.equipped
            """
            return [i for i in self.store if type in equipment[i]]
        
    
    # A custom Action to Equip items.
    class Equip(Action):
        def __init__(self, e_id):
            """
            e_id - The id of the equipment to be equipped.
            
            Usage Example: Equip('e001')
            """
            self.e_id = e_id
        
        def __call__(self):
            inv.equip(self.e_id)
            renpy.restart_interaction()

style inventory_text is text:
    font "Comfortaa-Regular.ttf"
    color "#6ABBFD"
    size 20
    min_width 145
    text_align 0.0

style inventory_number is text:
    font "Mechsuit.ttf"
    color "#6ABBFD"
    size 11.5

screen inventory_screen():
    default tab = "core"
    
    add "gui/inventory/base.jpg"
    add "gui/inventory/vertical_line.png" xpos 591 ypos 841
    add "gui/inventory/vertical_line.png" xpos 1440 ypos 841

    vbox:
        xpos 55
        ypos 44
        spacing 8
        for i, j in inv.equipped.iteritems():
            button:
                xysize (114, 114)
                if j == "None":
                    background "gui/inventory/%s.png" %equipment[j][2]
                    text _("[i]") text_align 0.5 size 20 color "#ffffff" align(0.5, 0.5)
                else:
                    idle_background "gui/inventory/%s_N.png" %equipment[j][2]
                    hover_background "gui/inventory/%s_H.png" %equipment[j][2]
                    selected_background "gui/inventory/%s_C.png" %equipment[j][2]
                    hovered Show("stats_show", data = equipment[j])
                    unhovered Hide("stats_show")
                action [SelectedIf(tab==i), SetScreenVariable("tab", i)]
    
    $ data = inv.filter(tab)
    $ ele  = 0
    
    hbox:
        xpos 678
        ypos 41
        spacing 18
        for i in ["core", "thrust", "melee", "range", "frame", "misc"]: # for i in inv.equipped.keys():
            button:
                xysize (171, 36)
                idle_background "gui/inventory/btn_N.png"
                hover_background "gui/inventory/btn_H.png"
                selected_idle_background "gui/inventory/btn_C.png"
                text _("[i]") text_align 0.5 size 32 color "#ffffff" align(0.5, 0.5)
                action [SelectedIf(tab==i), SetScreenVariable("tab", i)]
    
    grid 9 5:
        xpos 689
        ypos 133
        spacing 8
        for i in data:
            button:
                xysize(114, 114)
                idle_background ("gui/inventory/%s_N.png" %equipment[i][2])
                hover_background ("gui/inventory/%s_H.png" %equipment[i][2])
                selected_background ("gui/inventory/%s_C.png" %equipment[i][2])
                hovered Show("stats_show", data = equipment[i])
                unhovered Hide("stats_show")
                action [Equip(i), Play("sound", "audio/sfx/Inventory/%s.wav" %tab), SetVariable("invLoadout", "%s" %tab), SetVariable("invStance", "%s" %tab), Hide("stats_show")] #action [Equip(i), Play("sound", "audio/sfx/Inventory/%s.wav" %tab), Hide("stats_show")]
        for j in range(45 - len(data)):
            null height 114
    
    imagebutton:
        idle "gui/inventory/checkmark.png"
        hover "gui/inventory/checkmark.png"
        action [Hide("inventory_screen"), Return()]
        xpos 1804
        ypos 648
        
    imagebutton:
        idle "gui/return.png"
        hover "gui/return.png"
        action [Play("sound", "audio/sfx/Inventory/misc.wav"), SetVariable("invLoadout", "default"), SetVariable("invStance", "default")]
        xpos 595
        ypos 10

    vbox:
        xpos 60
        ypos 850 # 860
        spacing 18
        hbox:
            text "ARMOR" style "inventory_text" min_width 160
            text "[hp]" style "inventory_number"
        hbox:
            text "ENERGY" style "inventory_text" min_width 160
            text "[energy]" style "inventory_number"
        hbox:
            text "DAMAGE" style "inventory_text" min_width 160
            text "[damage]" style "inventory_number"
        hbox:
            text "COMBO X" style "inventory_text" min_width 160
            text "[combo]" style "inventory_number"
        
    #add "mc inv" xoffset 50 yoffset 25 xzoom -0.85 yzoom 0.85
    if invLoadout == "melee" or invLoadout == "range":
        
        if "defaultBuster" in inv.equipped.values():
            add "mc inv" xoffset 200 yoffset 25 xzoom -0.85 yzoom 0.85
        elif "defaultKatana" in inv.equipped.values():
            add "mc inv" xoffset 100 yoffset 25 xzoom -0.85 yzoom 0.85
        elif "defaultPistol" in inv.equipped.values():
            add "mc inv" xoffset 125 yoffset 25 xzoom -0.85 yzoom 0.85
        else:
            add "mc inv" xoffset 50 yoffset 25 xzoom -0.85 yzoom 0.85
            
    else:
        add "mc inv" xoffset 50 yoffset 25 xzoom -0.85 yzoom 0.85

screen stats_show(data):
    text ("%s" %data[0]) style "inventory_text" size 40 xpos 670 ypos 835 # xpos 678
    text ("%s" %data[1]) style "inventory_text" size 30 xmaximum 740 xpos 698 ypos 902
    
    vbox:
        xpos 1470
        ypos 914
        spacing 14
        hbox:
            text "ENERGY USED" style "inventory_text"
            bar:
                xysize (261, 21)
                left_bar "gui/inventory/smallbar_green.png"
                right_bar "gui/inventory/smallbar.png"
                range 1000
                value data[5]
        hbox:
            text "DAMAGE" style "inventory_text"
            bar:
                xysize (261, 21)
                left_bar "gui/inventory/smallbar_orange.png"
                right_bar "gui/inventory/smallbar.png"
                range 100
                value data[6]
        hbox:
            text "MULTIPLIER" style "inventory_text"
            bar:
                xysize (261, 21)
                left_bar "gui/inventory/smallbar_red.png"
                right_bar "gui/inventory/smallbar.png"
                range 100
                value data[7]