class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
language = "En"
        
localization = {
    "reb_idl" : {"En" : "x", "Sp" : "x"},
    "reb_idu" : {"En" : "X", "Sp" : "X"},
    "reb_name" : {"En" : "Natives", "Sp" : "Nativos"},
    "reb_adj" : {"En" : "Native", "Sp" : "Nativo/a"},
    
    "eng_idl" : {"En" : "e", "Sp" : "e"},
    "eng_idu" : {"En" : "E", "Sp" : "E"},
    "eng_name" : {"En" : "Britain", "Sp" : "Bretaña"},
    "eng_adj" : {"En" : "British", "Sp" : "Británico/a,"},
   
    "den_idl" : {"En" : "d", "Sp" : "d"},
    "den_idu" : {"En" : "D", "Sp" : "D"},
    "den_name" : {"En" : "Denmark", "Sp" : "Dinamarca"},
    "den_adj" : {"En" : "Danish", "Sp" : "Danés/esa"},
    
    "swe_idl" : {"En" : "s", "Sp" : "s"},
    "swe_idu" : {"En" : "S", "Sp" : "S"},
    "swe_name" : {"En" : "Sweden", "Sp" : "Suecia"},
    "swe_adj" : {"En" : "Swedish", "Sp" : "Sueco/a"},
    
    "rus_idl" : {"En" : "r", "Sp" : "r"},
    "rus_idu" : {"En" : "R", "Sp" : "R"},
    "rus_name" : {"En" : "Russia", "Sp" : "Rusia"},
    "rus_adj" : {"En" : "Russian", "Sp" : "Ruso/a"},
    
    "pol_idl" : {"En" : "l", "Sp" : "l"},
    "pol_idu" : {"En" : "L", "Sp" : "L"},
    "pol_name" : {"En" : "Poland", "Sp" : "Polonia"},
    "pol_adj" : {"En" : "Polish", "Sp" : "Polaco/a"},
    
    "pru_idl" : {"En" : "p", "Sp" : "p"},
    "pru_idu" : {"En" : "P", "Sp" : "P"},
    "pru_name" : {"En" : "Prussia", "Sp" : "Prusia"},
    "pru_adj" : {"En" : "Prussian", "Sp" : "Prusio/a"},
    
    "ger_idl" : {"En" : "g", "Sp" : "g"},
    "ger_idu" : {"En" : "G", "Sp" : "G"},
    "ger_name" : {"En" : "German States", "Sp" : "Estados Alemanes"},
    "ger_adj" : {"En" : "German", "Sp" : "Alemán/ana"},
    
    "fra_idl" : {"En" : "f", "Sp" : "f"},
    "fra_idu" : {"En" : "F", "Sp" : "F"},
    "fra_name" : {"En" : "France", "Sp" : "Francia"},
    "fra_adj" : {"En" : "French", "Sp" : "Francés/esa"},
    
    "aus_idl" : {"En" : "a", "Sp" : "a"},
    "aus_idu" : {"En" : "A", "Sp" : "A"},
    "aus_name" : {"En" : "Austria", "Sp" : "Austria"},
    "aus_adj" : {"En" : "Austrian", "Sp" : "Austriaco/a"},
    
    "ita_idl" : {"En" : "i", "Sp" : "i"},
    "ita_idu" : {"En" : "I", "Sp" : "I"},
    "ita_name" : {"En" : "Italian States", "Sp" : "Estados Italianos"},
    "ita_adj" : {"En" : "Italian", "Sp" : "Italiano/a"},
    
    "ott_idl" : {"En" : "o", "Sp" : "o"},
    "ott_idu" : {"En" : "O", "Sp" : "O"},
    "ott_name" : {"En" : "Turkey", "Sp" : "Turquía"},
    "ott_adj" : {"En" : "Ottoman", "Sp" : "Otomano/a"},
    
    "spa_idl" : {"En" : "ñ", "Sp" : "ñ"},
    "spa_idu" : {"En" : "Ñ", "Sp" : "Ñ"},
    "spa_name" : {"En" : "Spain", "Sp" : "España"},
    "spa_adj" : {"En" : "Spanish", "Sp" : "Español/a"},
    
    "por_idl" : {"En" : "t", "Sp" : "t"},
    "por_idu" : {"En" : "T", "Sp" : "T"},
    "por_name" : {"En" : "Portugal", "Sp" : "Portugal"},
    "por_adj" : {"En" : "Portuguese", "Sp" : "Portugués/esa"},
    
    "pap_idl" : {"En" : "†", "Sp" : "†"},
    "pap_idu" : {"En" : "✚", "Sp" : "✚"},
    "pap_name" : {"En" : "Papal States", "Sp" : "Estados Pontificios"},
    "pap_adj" : {"En" : "Papal", "Sp" : "Pontificio/a"},
    
    "mor_idl" : {"En" : "m", "Sp" : "m"},
    "mor_idu" : {"En" : "M", "Sp" : "M"},
    "mor_name" : {"En" : "Morocco", "Sp" : "Marruecos"},
    "mor_adj" : {"En" : "Moroccan", "Sp" : "Marroquí"},
    
    "cul_brb" : {"En" : "Barbarian", "Sp" : "Bárbaro"},
    "cul_weu" : {"En" : "Western European", "Sp" : "Europeo Occidental" },
    "cul_eeu" : {"En" : "Eastern European", "Sp" : "Europa del Este"},
    "cul_isl" : {"En" : "Islamic", "Sp" : "Islam"},
}

"""
start = [
    [
        "_ _ _ _ _ d d s s _ _ r r r r +",
        "_ _ _ e _ _ _ s s _ r r r r r +",
        "_ _ _ e _ _ d _ _ _ l l r r r +",
        "_ e _ e _ _ d p p p p l l l r +",
        "_ _ _ _ _ g g g p l l l l l r +",
        "_ _ _ _ f f g g p p a l l l r r",
        "_ _ _ f f f f + a a a a l l r r"
        "_ _ _ _ f f i a a a a o o _ _ r",
        "_ ñ ñ ñ ñ _ _ i i _ o o _ _ _ _",
        "_ t ñ ñ ñ _ _ _ † _ o _ o o o o",
        "_ t ñ ñ _ _ _ _ i _ o _ o o o o",
        "_ _ _ _ o o o _ _ _ _ _ _ _ _ o",
        "_ _ m m + + + o _ _ _ _ _ _ o o",
        "_ m m + + + + o o _ o o o _ o o",
        "_ x + + + + + + o o o o o o _ o",
        "x + + + + + + + + + + o o o _ _"
    ]
]
"""


start = [
    [
        "_ e _ o",
        "+ e t o",
        "_ _ _ _",
        "_ _ _ e"
    ]
]
def get_localed(key):
    return localization[key][language]
    
def get_dual_localed(key, key2):
    return localization[key + "_" + key2][language]
        
class Faction:
    def __init__(self, ide, namedef, attributes):
        self.ide = ide
        self.namedef = namedef
        self.attributes = attributes
        
class Attributes:
    def __init__(self,culture, assimilation):
        self.culture = culture
        self.assimilation = assimilation

factions = {
    "x" : Faction("x", "reb", Attributes("cul_brb",4)),
    "e" : Faction("e", "eng", Attributes("cul_weu",4)),
    "d" : Faction("d", "den", Attributes("cul_weu",2)),
    "s" : Faction("s", "swe", Attributes("cul_eeu",2)),
    "r" : Faction("r", "rus", Attributes("cul_eeu",1)),
    "l" : Faction("l", "pol", Attributes("cul_eeu",2)),
    "p" : Faction("p", "pru", Attributes("cul_weu",2)),
    "g" : Faction("g", "ger", Attributes("cul_weu",2)),
    "f" : Faction("f", "fra", Attributes("cul_weu",2)),
    "a" : Faction("a", "aus", Attributes("cul_weu",2)),
    "i" : Faction("i", "ita", Attributes("cul_weu",2)),
    "o" : Faction("o", "ott", Attributes("cul_isl",1)),
    "ñ" : Faction("ñ", "spa", Attributes("cul_weu",2)),
    "t" : Faction("t", "por", Attributes("cul_weu",2)),
    "†" : Faction("†", "pap", Attributes("cul_weu",2)),
    "m" : Faction("m", "mor", Attributes("cul_isl",2))
}

faction = ""

def get_keys(dictionary):
    return list(dictionary.keys())

def get_faction_local(idl,key):
    return get_dual_localed(factions[idl].namedef, key)
    
#print(get_faction_local("†", "name")) # prints "Papal States"
#print(get_faction_local("t", "adj")) # prints "Portuguese"
#print(get_faction_local("e", "idu")) # prints "E"
#print(get_faction_local("o", "idl")) # prints "o"

class Province:
    def __init__(self, owner, potential, port, economy, coord, culture):
        self.owner = owner
        self.potential = potential
        self.port = port
        self.economy = economy
        self.coord = coord
        self.culture = culture                                                                                
        
provinces = [
    [
        [
            Province(None, 4, 0, 2, None, "cul_weu"),
            Province(None, 4, 0, 2, None, "cul_isl"),
        ],
        [
            Province(None, 4, 1, 2, None, "cul_weu"),
            Province(None, 4, 1, 2, None, "cul_weu"),
            Province(None, 4, 1, 2, None, "cul_isl"),
        ],
        [
            
        ],
        [
            Province(None, 4, 2, 2, None, "cul_weu"),
        ]
    ]
] 

def input_loop(string:str, answers):
    while True:
        i = input(string)
        if answers == None or i in answers:
            return i

def print_divider(length):
    string = "X"
    for x in range(length):
        string = string + "-"
    string = string + "X"
    print(string)

def print_map(map_mode, theatre):
    if map_mode == 1:
        print_divider(len(start[theatre][0])+2)
        nyy = 0
        for y in start[theatre]:
            nyy = nyy + 1
            nx = 0
            string = "| "
            for x in y:
                if not (not (x == "_" or x == "+" or x == " ") and factions.get(x)):
                    string += x
                else:
                    rx = provinces[theatre][nyy-1][nx].owner
                    t = ""
                    if rx == faction:
                        t = get_faction_local(rx, "idu")
                    else:
                        t = get_faction_local(rx, "idl")
                    string += t
                    nx += 1
            print(string + " |")
        print_divider(len(start[theatre][0])+2)

def Start():
    
    print("Language?: En/Sp")
    #input_start_language = input_loop("""""", ["En","Sp"])
    #language = input_start_language
    print("Faction?")
    input_start_country = input_loop("", get_keys(factions))
    global faction
    faction = input_start_country
    ntheatre = -1
    for theatre in start:
        ntheatre += 1
        ny = 0
        for y in theatre:
            ny += 1
            nx = 0
            mx = 0
            for x in y:
                if not (x == "_" or x == "+" or x == " ") and factions.get(x):
                    nx += 1
                    coord = Coordinate(nx,ny)
                    #print("!"+x+"!")
                    #print(coord.x, coord.y)
                    provinces[ntheatre][ny-1][nx-1].owner = x
                    provinces[ntheatre][ny-1][nx-1].coord = coord
                    provinces[ntheatre][ny-1][nx-1].culture = factions[x].attributes.culture
    
    turn_loop = True
    what_turn = 0
    while turn_loop:
        turn = True
        what_turn += 1
        print("Turn:", what_turn)
        screen = "Main"
        print("Screen:", screen)
        while turn:
            if screen == "Main":
                input_main_generic = input_loop("(Press 0 for choices): ", ["0","1","End"])
                if input_main_generic == "0":
                    print("End: End Turn")
                    print("0: Help")    
                    print("1: Map")    
                elif input_main_generic == "1":
                    screen = "Map"
                    print("Screen:", screen)
                elif input_main_generic == "End":
                    turn = False
            if screen == "Map":
                input_map_generic = input_loop("(Press 0 for choices):", ["End","Back","0","1"])
                if input_map_generic == "Back":
                    screen = "Main"
                    print("Screen:", screen)
                elif input_map_generic == "End":
                    turn = False
                elif input_map_generic == "0":
                    print("End: End Turn")
                    print("Back: Return to previous screen")
                    print("0: Help")    
                    print("1: Political Map Mode")
                else:
                    print_map(int(input_main_generic),0)
    
Start()