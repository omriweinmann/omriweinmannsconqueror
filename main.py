class Localization:
    def __init__(self, array):
        self.array = array
        
language = "Sp"
        
localization = {
    "eng_idl" : {"En" : "e", "Sp" : "e"},
    "eng_idu" : {"En" : "E", "Sp" : "E"},
    "eng_name" : {"En" : "Great Britain", "Sp" : "Gran Bretaña"},
    "eng_adj" : {"En" : "British", "Sp" : "Británico/a,"}
    "cul_weo" : {"En" : "Western European", "Sp" : "de Europeo Occidental" }
}

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
    def __init__(self,culture assimilation)
        self.culture = culture
        self.assimilation = assimilation

new_test = Faction("e", "eng", Attributes("cul_weu", 4))

print(get_dual_localed(new_test.namedef, "adj"))

print("""\
_ _ _ _ _ o o o o _ _ o o o o o
_ _ _ o _ _ _ o o _ o o o o o o
_ _ _ o _ _ o _ _ _ o o o o o o
_ o _ o _ _ o o o o o o o o o o
_ _ _ _ _ o o o o o o o o o o o
_ _ _ _ o o o o o o o o o o o o
_ _ _ o o o o o o o o o o o o o
_ _ _ _ o o o o o o o o o _ _ o
_ o o o o _ _ o o _ o o _ _ _ _
_ o o o o _ _ _ o _ o _ o o o o
_ o o o _ _ _ _ o _ o _ o o o o
_ _ _ _ o o o _ _ _ _ _ _ _ _ o
_ _ o o o o o o _ _ _ _ _ _ o o
_ o o o o o o o o _ o o o _ o o
_ o o o o o o o o o o o o o _ o
o o o o o o o o o o o o o o _ _    
                    """)






