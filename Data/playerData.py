from  TLT.constants import *
PLAYER_LIST = {
    "Gynsora":{ 
		"name" : "Gynsora",
        "x" : 2 ,
        "y" : 3,
        "width" : 64,
        "height" : 64 ,
        "color" : ELECTRIK ,
        "atk" : 25,
        "hp" : 2000,
		"endurance" : 7,
		"critical" : 50,
		"defCritical" : 10,
        "class" : "Berserk",
        "spells_List":[
            {
				"name" : "Déplacement",
                "image" : "sampleDeplacement",
				"type" : "Mouvement",
				"direction":"Aérienne",
				"description" :"Esquive une attaque en allant sur 1 case à côté.",
                "element":"neutre",
                "range":2,
                "rangeForm": "Diamond",
                "zone" :3,
                "zoneForm" : "Target",
				"cost":				
				{
				  "hp" : 0,
				  "endurance" : 2
				},
				"Gain":
				{
				  "hp" : 0,
				  "endurance" : 0
				},				
				"Gcd":1,
				"Damage": 0
			},
            {
				"name" : "Tsunami",
                "image" : "sampleAttaque",
				"type" : "Attaque",
				"direction":"Aérienne",
				"description" :"lance un tsunami",
                "element":"eau",
                "range":1,
                "rangeForm": "Cross",
                "zone" :3,
                "zoneForm" : "NormalLine",
				"cost":				
				{
				  "hp" : 0,
				  "endurance" : 2
				},
				"Gain":
				{
				  "hp" : 0,
				  "endurance" : 0
				},				
				"Gcd":1,
				"Damage": 250
			}
        ]
	}
}


# "class" : "Berserker",
#         "spellDef":[
#             {
# 				"name" : "Evitement",
#                 "image" : "",
# 				"type" : "Defense",
# 				"direction":"Frontale",
# 				"description" :"Esquive une attaque en allant sur 1 case à côté.",
#                 "element":"neutre",
#                 "range":1,
#                 "zone" :1,
# 				"cost":				
# 				{
# 				  "hp" : 0,
# 				  "endurance" : 2
# 				},
# 				"Gain":
# 				{
# 				  "hp" : 0,
# 				  "endurance" : 0
# 				},				
# 				"Gcd":1,
# 				"Damage": 0
# 			},
#             {
# 				"name" : "Régénération",
#                 "image" : "",
# 				"type" : "Defense",
# 				"direction":"Aerienne",
# 				"description" :"Régènere 1000 point de vie.",
#                 "element":"neutre",
#                 "range":0,
#                 "zone" :1,
# 				"cost":				
# 				{
# 				  "hp" : 0,
# 				  "endurance" : 2
# 				},
# 				"Gain":
# 				{
# 				  "hp" : 1000,
# 				  "endurance" : 0
# 				},				
# 				"Gcd":4,
# 				"Damage": 0
# 			},
#             {
# 				"name" : "Bouclier Cryo",
#                 "image" : "",
# 				"type" : "Defense",
# 				"direction":"Frontale",
# 				"description" :"Place un bouclier de glace sur la case de départ peut stopper ou gener une attaque",
#                 "element":"glace",
#                 "range":1,
#                 "zone" :1,
# 				"cost":				
# 				{
# 				  "hp" : 0,
# 				  "endurance" : 2
# 				},
# 				"Gain":
# 				{
# 				  "hp" : 0,
# 				  "endurance" : 0
# 				},				
# 				"Gcd":3,
# 				"Damage": 0
# 			}
#         ],
#         "spellAtk":[
#              {
# 				"name" : "Cri Sanguinaire",
#                 "image" : "",
# 				"type" : "Attaque",
# 				"direction":"Aerienne",
# 				"description" :"vous détruisez tout autour de vous.",
#                 "element":"neutre",
#                 "range":3,
#                 "zone" :1,
# 				"cost":				
# 				{
# 				  "hp" : 50,
# 				  "endurance" : 2
# 				},
# 				"Gain":
# 				{
# 				  "hp" : 0,
# 				  "endurance" : 0
# 				},				
# 				"Gcd":3,
# 				"Damage": 200
# 			},
#             {
# 				"name" : "Tsunami",
#                 "image" : "",
# 				"type" : "Attaque",
# 				"direction":"Frontale",
# 				"description" :"Lance un déferlante d'eau",
#                 "element":"eau",
#                 "range":4,
#                 "zone" :1,
# 				"cost":				
# 				{
# 				  "hp" : 0,
# 				  "endurance" : 3
# 				},
# 				"Gain":
# 				{
# 				  "hp" : 0,
# 				  "endurance" : 0
# 				},				
# 				"Gcd":1,
# 				"Damage": 700
# 			},
#             {
# 				"name" : "Cyclone",
#                 "image" : "",
# 				"type" : "Attaque",
# 				"direction":"Laterale",
# 				"description" :"Déchaîne un cyclone",
#                 "element":"vent",
#                 "range":4,
#                 "zone" :3,
# 				"cost":				
# 				{
# 				  "hp" : 0,
# 				  "endurance" : 3
# 				},
# 				"Gain":
# 				{
# 				  "hp" : 0,
# 				  "endurance" : 0
# 				},				
# 				"Gcd":2,
# 				"Damage": 600
# 			}

#         ]
   