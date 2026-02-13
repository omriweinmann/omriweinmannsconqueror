import math
import random

class Coordinate:
	def __init__(self, x, y, theatre):
		self.x = x
		self.y = y
		self.theatre = theatre

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

	"End" : {"En" : "End", "Sp" : "Fin"},
	"Back" : {"En" : "Back", "Sp" : "Atrás"},
	"Main" : {"En" : "Main", "Sp" : "Principal"},
	"Map" : {"En" : "Map", "Sp" : "Mapa"},
	"Economy" : {"En": "Economy","Sp" : "Economía"},
	"Cancel" : {"En": "Cancel","Sp" : "Cancelar"},
	"rng" : {"En" : "Random", "Sp" : "Azar"},
	"List" : {"En" : "List", "Sp" : "Lista"},
	"Yes" : {"En" : "Yes", "Sp" : "Sí"},
	"No" : {"En" : "No", "Sp" : "No"},

	
	"0" : {"En" : "0", "Sp" : "0"},
	"1" : {"En" : "1", "Sp" : "1"},
	"2" : {"En" : "2", "Sp" : "2"},
	"3" : {"En" : "3", "Sp" : "3"},
	"4" : {"En" : "4", "Sp" : "4"},
	"5" : {"En" : "5", "Sp" : "5"},
	"6" : {"En" : "6", "Sp" : "6"},
	"7" : {"En" : "7", "Sp" : "7"},
	"8" : {"En" : "8", "Sp" : "8"},
	"9" : {"En" : "9", "Sp" : "9"},
	
	"zero_help" : {"En" : "0: Help", "Sp" : "0: Ayuda"},
	"end_end_turn" : {"En" : "End: End Turn", "Sp" : "Fin: Finalizar turno"},
	"back_return" : {"En" : "Back: Return to Previous Screen", "Sp" : "Atrás: Volver a la pantalla anterior"},
	"cancel_cancel_action" : {"En" : "Cancel: Cancel Action", "Sp" : "Cancelar: Cancelar acción"},
	"list_list_provinces" : {"En" : "List: List of Owned Provinces", "Sp" : "Lista: Lista de provincias poseídas"},
	"one_map_screen" : {"En" : "1: Map", "Sp" : "1: Mapa"},
	"one_political_map" : {"En" : "1: Political Map", "Sp" : "1: Mapa político"},
	"one_improve_economy" : {"En" : "1: Improve a chosen province's economy", "Sp" : "1: Mejorar la economía de una provincia elegida."},
	"two_economy_map" : {"En" : "2: Economy Levels", "Sp" : "2: Niveles económicos"},
	"two_economy_screen" : {"En" : "2: Economy", "Sp" : "2: Economía"},
	"two_improve_economy_rng" : {"En" : "2: Improve a random province's economy", "Sp" : "2: Mejorar la economía de una provincia aleatoria."},
	"three_potential_map" : {"En" : "3: Economy Potentials", "Sp" : "3: Potencial económico"},
	"three_improve_economy_low" : {"En" : "3: Improve the economy of the poorest province", "Sp" : "3: Mejorar la economía de la provincia más pobre."},
	"four_coastal_map" : {"En" : "4: Coastal Levels", "Sp" : "4: Niveles costeros"},
	"what_theatre" : {"En" : "Theatre (0 for choices): ", "Sp" : "Teatro (0 para ver las opciones): "},
	"ask_coord" : {"En" : "Coordinates (ex. 'a,a'): ", "Sp" : "Coordenadas (ej. 'a,a'): "},
	
	"turn" : {"En" : "Turn", "Sp" : "Turno"},
	"screen" : {"En" : "Screen", "Sp" : "Pantalla"},
	"input_zero_help" : {"En" : "(Press 0 for choices): ", "Sp" : "(Presione 0 para ver las opciones): "},
	"yn" : {"En" : "Yes/No: ", "Sp" : "Sí/No"},
	
	"theatre" : {"En" : "Theatre", "Sp" : "Escenario"},
	"theatres" : {"En" : "Theatres", "Sp" : "Escenarios"},
	"test1" : {"En" : "Test1", "Sp" : "Test1 Sp"},
	"test2" : {"En" : "Test2", "Sp" : "Test2 Sp"},

	"action_will_cost" : {"En" : "This action will cost @one@ pounds", "Sp" : "Esta acción costará @one@ libras"},
	"no_money" : {"En" : "You do not have @one@ pounds", "Sp" : "No tienes @one@ libras"},
	"you_have" : {"En" : "You have @one@ pounds", "Sp" : "Tienes @one@ libras"},
	"no_own_province" : {"En" : "You do not own this province", "Sp" : "No eres dueño de esta provincia"},
	"already_own_province" : {"En" : "You already own this province", "Sp" : "Ya eres dueño de esta provincia"},
	"invalid_format_coord" : {"En" : "Invalid Format (ex. 'a,a')", "Sp" : "Formato no válido (ej. 'a,a')"},
	"invalid_province" : {"En" : "Invalid Province (May be water, or impassable)", "Sp" : "Provincia no válida (puede ser agua o intransitable)"},
}

def num_2_l(n):
	b = '`'
	number = int(n)
	if number > 26:
		b = '@'
		number -= 26
	return chr(ord(b)+number)




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
		"r _ _ e"
	],
	[
		"r r",
		"r _",
		"r _"
	]
]

theatre_def = {
	"rng": -7,
	"test1" : 0,
	"test2" : 1,
}

def get_localed(key):
	if key in localization:
		k = localization[key]
		if language in k:
			l = k[language]
			return l
	return key

def gl(k):
	return get_localed(k)
		

def get_dual_localed(key, key2):
	return localization[key + "_" + key2][language]

class Faction:
	def __init__(self, ide, namedef, attributes,goods):
		self.ide = ide
		self.namedef = namedef
		self.attributes = attributes
		self.goods = goods

class Attributes:
	def __init__(self,culture, assimilation, stagnation):
		self.culture = culture
		self.assimilation = assimilation
		self.stagnation = stagnation

factions = {
	"x" : Faction("x", "reb", Attributes("cul_brb",4,5), [2500]),
	"e" : Faction("e", "eng", Attributes("cul_weu",4,1), [2500]),
	"d" : Faction("d", "den", Attributes("cul_weu",4,3), [2500]),
	"s" : Faction("s", "swe", Attributes("cul_eeu",4,3), [2500]),
	"r" : Faction("r", "rus", Attributes("cul_eeu",4,3), [2500]),
	"l" : Faction("l", "pol", Attributes("cul_eeu",4,3), [2500]),
	"p" : Faction("p", "pru", Attributes("cul_weu",4,2), [2500]),
	"g" : Faction("g", "ger", Attributes("cul_weu",4,2), [2500]),
	"f" : Faction("f", "fra", Attributes("cul_weu",4,2), [2500]),
	"a" : Faction("a", "aus", Attributes("cul_weu",4,3), [2500]),
	"i" : Faction("i", "ita", Attributes("cul_weu",4,3), [2500]),
	"o" : Faction("o", "ott", Attributes("cul_isl",4,4), [2500]),
	"ñ" : Faction("ñ", "spa", Attributes("cul_weu",4,4), [2500]),
	"t" : Faction("t", "por", Attributes("cul_weu",4,4), [2500]),
	"†" : Faction("†", "pap", Attributes("cul_weu",4,5), [2500]),
	"m" : Faction("m", "mor", Attributes("cul_isl",4,5), [2500])
}

faction = ""

def get_keys(dictionary):
	return list(dictionary.keys())

def get_key_from_val(v, dict):
	list = get_keys(dict)
	for x in list:
		if dict[x] == v:
			return x

def list_localed(list):
	new_list = []
	for item in list:
		new_list.append(gl(item))
	return new_list

def dl(v):
	list = get_keys(localization)
	for x in list:
		if localization[x][language] == v:
			return x

def get_faction_local(idl,key):
	return get_dual_localed(factions[idl].namedef, key)

#print(get_faction_local("†", "name")) # prints "Papal States"
#print(get_faction_local("t", "adj")) # prints "Portuguese"
#print(get_faction_local("e", "idu")) # prints "E"
#print(get_faction_local("o", "idl")) # prints "o"

def put_s_into_gl(replacements, replacee):
	pre_process = gl(replacee)
	post_process = pre_process.split("@")
	keys_replacements = get_keys(replacements)
	end = ""
	for cut in post_process:
		if cut in get_keys(replacements):
			end = end + str(replacements[cut])
		else:
			end = end + cut
	return end
		
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
			Province(None, 4, 2, 2, None, "cul_isl"),
		],
		[

		],
		[
			Province(None, 3, 3, 2, None, "cul_eeu"), Province(None, 4, 3, 2, None, "cul_weu"),
		]
	],
	[
		[
			Province(None, 3, 0, 2, None, "cul_eeu"), Province(None, 3, 3, 2, None, "cul_eeu")
		],
		[
			Province(None, 2, 1, 2, None, "cul_eeu"),
		],
		[
			Province(None, 2, 1, 2, None, "cul_eeu"),
		]
	]
] 

def input_loop(string:str, answers):
	while True:
		i = input(string)
		if answers == None or i in answers:
			return i

def rng_theatre_id():
	a = len(theatre_def)-1
	b = random.randrange(0,a)
	return b

def get_provinces_owned(faction, theatre):
	search_through = []
	if theatre == -7:
		for th in provinces:
			search_through.extend(th)
	else:
		search_through = provinces[theatre]
	list = []
	for st in search_through:
		for province in st:
			if province.owner == faction:
				list.append(province)
	return list
	

def theatre_input_loop():
	options = [gl("Cancel"), gl("0")]
	localed_l = list_localed(get_keys(theatre_def))
	options.extend(localed_l)
	while True:
		input_map_theatre = input_loop(gl("what_theatre"), options)
		if input_map_theatre == gl("Cancel"):
			return "Cancelled"
		elif input_map_theatre == gl("0"):
			print(gl("cancel_cancel_action"))
			print(gl("zero_help"))
			string = gl("theatres") + ": "
			for l in localed_l:
				print(" - " + l)
		else:
			theatre_answered = int(theatre_def[dl(input_map_theatre)])
			b = None
			if theatre_answered == -7:
				b = rng_theatre_id()
				#print(range(len(theatre_def)-1))
			else:
				b = theatre_answered
			return b

def province_input_loop(type, faction):
	theatre = theatre_input_loop()
	while True:
		inp = input(gl("ask_coord"))
		spl = inp.split(",")
		if not len(spl) == 2:
			print(gl("invalid_format_province"))
		else:
			province = provinces[theatre][ord(spl[0])-97][ord(spl[1])-97]
			if type == 1 and not province.owner == faction:
				print(gl("no_own_province"))
			elif type == 2 and province.owner == faction:
				print(gl("already_own_province"))

def print_divider(length):
	string = "X"
	for x in range(length):
		string = string + "-"
	string = string + "X"
	print(string)

def print_map_divider(length):
	string = "X"
	for x in range(length):
		if x % 2 == 0:
			string = string + "-"
		else:
			string = string + num_2_l(str(math.ceil(x/2)))
	string = string + "X"
	print(string)

def printe():
	print("")

def print_map(map_mode, theatre):
	print_divider(len(start[theatre][0])+2)
	nyy = 0
	key_list = []
	for y in start[theatre]:
		nyy = nyy + 1
		nx = 0
		string = num_2_l(str(nyy)) + " "
		strings_for_keys = [

		]
		for x in y:
			if not (not (x == "_" or x == "+" or x == " ") and factions.get(x)):
				string += x
			else:
				rx = provinces[theatre][nyy-1][nx]
				t = ""
				#print(map_mode)
				if map_mode == 1 or map_mode == "econ_mode":
					if rx.owner == faction:
						if map_mode == 1:
							t = get_faction_local(rx.owner, "idu")
						else:
							t = gl(str(rx.economy))
					else:
						if map_mode == 1:
							t = get_faction_local(rx.owner, "idl")
						else:
							t = "+"
					key_list = [
						"Uppercase Letter: Your faction",
						"Lowercase Letter: Other factions",
						"_: Bodies of water",
						"+: Impassable territory"
					]
				elif map_mode == 2:
					t = gl(str(rx.economy))
					key_list = [
						"Number: Economy Level",
						"_: Bodies of water",
						"+: Impassable territory"
					]
				elif map_mode == 3:
					t = gl(str(rx.potential))
					key_list = [
						"Number: Potential Economy Level",
						"_: Bodies of water",
						"+: Impassable territory"
					]
				elif map_mode == 4:
					t = gl(str(rx.port))
					key_list = [
						"0: Inland",
						"1: Coastal",
						"2: Port",
						"3: International Port",
						"_: Bodies of water",
						"+: Impassable territory"
					]
				string += t
				nx += 1
		print(string + " |")
	print_map_divider(len(start[theatre][0])+2)
	printe()
	for s in key_list:
		print(s)
	printe()

def calc_economy_upgrade(province):
	level = province.economy
	potential = province.potential
	stagnation = factions[province.owner].attributes.stagnation
	return int(250.0 * (2.0 ** float(level)) * (1.1 ** float(stagnation)) * (1.1 ** float(potential)))

def pay_input_loop(amount):
	printe()
	s = {
		"one" : amount
	}
	if factions[faction].goods[0] >= amount:
		print(put_s_into_gl(s, "action_will_cost"))
		s2 = {
			"one" : factions[faction].goods[0]
		}
		print(put_s_into_gl(s2, "you_have"))
		if input_loop(gl("yn"), [gl("Yes"),gl("No")]):
			factions[faction].goods[0] -= amount
			return True
	else:
		print(put_s_into_gl(s, "no_money"))
	printe()
	return False

def province_input_loop(type, f):
	theatre = theatre_input_loop()
	while not theatre == "Cancelled":
		inp = input(gl("ask_coord"))
		if inp == gl("Cancel"):
			return "Cancelled"
		spl = inp.split(",")
		#print(spl)
		if not len(spl) == 2:
			print(gl("invalid_format_coord"))
		else:
			t = provinces[theatre]
			ord_1 = ord(spl[1])-97
			#print(ord_1)
			if len(t) >= ord_1 + 1:
				ord_0 = ord(spl[0])-97
				#print(ord_0)
				good_to_go = False
				for iterate in t[ord_1]:
					if iterate.coord.x == ord_0 + 1:
						good_to_go = True
						break
				if good_to_go:
					province = t[ord_1][ord_0]
					if type == 1 and not province.owner == f:
						print(gl("no_own_province"))
					elif type == 2 and province.owner == f:
						print(gl("already_own_province"))
					else:
						return province
				else:
					print(gl("invalid_province"))
			else:
				print(gl("invalid_province"))
	return "Cancelled"
	
def Start():
	print("Language?: En/Sp")
	input_start_language = input_loop("""""", ["En","Sp"])
	global language
	language = input_start_language
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
					coord = Coordinate(nx,ny,ntheatre)
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
		printe()
		print_divider(5)
		print(gl("turn")+":", what_turn)
		print_divider(5)
		printe()
		screen = "Main"
		print(gl("screen")+":", gl(screen))
		while turn:
			if screen == "Main":
				input_main_generic = input_loop(gl("input_zero_help"), [get_localed("0"),get_localed("1"),gl("2"),get_localed("End")])
				if input_main_generic == gl("0"):
					print(gl("end_end_turn"))
					print(gl("zero_help"))    
					print(gl("one_map_screen"))
					print(gl("two_economy_screen"))
				elif input_main_generic == gl("1"):
					screen = "Map"
					printe()
					print(gl("screen")+":", gl(screen)) 
					printe()
				elif input_main_generic == gl("End"):
					turn = False
				elif input_main_generic == gl("2"):
					screen = "Economy"
					printe()
					print(gl("screen")+":", gl(screen))
					printe()
			elif screen == "Map":
				input_map_generic = input_loop(gl("input_zero_help"), [get_localed("End"),get_localed("Back"),get_localed("0"),get_localed("1"),gl("2"),gl("3"),gl("4"), gl("List")])
				if input_map_generic == gl("Back"):
					screen = "Main"
					printe()
					print(gl("screen")+":", gl(screen)) 
					printe()
				elif input_map_generic == gl("End"):
					turn = False
				elif input_map_generic == gl("0"):
					print(gl("end_end_turn"))
					print(gl("back_return"))
					print(gl("zero_help"))    
					print(gl("list_list_provinces"))
					print(gl("one_political_map"))
					print(gl("two_economy_map"))
					print(gl("three_potential_map"))
					print(gl("four_coastal_map"))
				elif input_map_generic == gl("List"):
					p = get_provinces_owned(faction, -7)
					printe()
					if len(p) == 0:
						print("None")
					else:
						for r in p:
							coord = r.coord
							the_str = gl(get_key_from_val(coord.theatre,theatre_def))
							
							print(the_str+": ("+num_2_l(coord.x)+", "+num_2_l(coord.y)+"), Econ:"+str(r.economy))
					printe()
				else:
					b = theatre_input_loop()

					if not b == "Cancelled":
						printe()
						print_map(int(input_map_generic),b)
						printe()
							
			elif screen == "Economy":
				input_economy_generic = input_loop(gl("input_zero_help"), [get_localed("End"),get_localed("Back"),get_localed("0"),get_localed("1"),gl("2"),gl("3"),gl("4")])
				if input_economy_generic == gl("Back"):
					screen = "Main"
					printe()
					print(gl("screen")+":", gl(screen)) 
					printe()
				elif input_economy_generic == gl("End"):
					turn = False
				elif input_economy_generic == gl("0"):
					print(gl("end_end_turn"))
					print(gl("back_return"))
					print(gl("zero_help"))
					print(gl("one_improve_economy"))
					print(gl("two_improve_economy_rng"))
					print(gl("three_improve_economy_low"))
				elif input_economy_generic == gl("1"):
					province = province_input_loop(1, faction)
					if not province == "Cancelled":
						coord = province.coord
						the_str = gl(get_key_from_val(coord.theatre,theatre_def))
						print(the_str+": ("+num_2_l(coord.x)+", "+num_2_l(coord.y)+"), Econ:"+str(province.economy))
						if pay_input_loop(calc_economy_upgrade(province)):
							print("Province economy has been improved")
							provinces[coord.theatre][coord.y-1][coord.x-1].economy += 1
				elif input_economy_generic == gl("2"):
					province = random.choice(get_provinces_owned(faction, -7))
					coord = province.coord
					the_str = gl(get_key_from_val(coord.theatre,theatre_def))
					print(the_str+": ("+num_2_l(coord.x)+", "+num_2_l(coord.y)+"), Econ:"+str(province.economy))
					if pay_input_loop(calc_economy_upgrade(province)):
						print("Province economy has been improved")
						provinces[coord.theatre][coord.y-1][coord.x-1].economy += 1
				elif input_economy_generic == gl("3"):
					province = None
					for p in get_provinces_owned(faction, -7):
						if province == None or province.economy > p.economy:
							province = p
					coord = province.coord
					the_str = gl(get_key_from_val(coord.theatre,theatre_def))
					print(the_str+": ("+num_2_l(coord.x)+", "+num_2_l(coord.y)+"), Econ:"+str(province.economy))
					if pay_input_loop(calc_economy_upgrade(province)):
						print("Province economy has been improved")
						provinces[coord.theatre][coord.y-1][coord.x-1].economy += 1
					
Start() 