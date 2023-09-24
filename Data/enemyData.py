from TLT.constants import *
ENEMY_LIST = { 
    "Dragoon":{
        "name" : "Dragoon",
        "x" : 2 ,
        "y" : 0 ,
        "width" : 64,
        "height" : 64 ,
        "color" : PINK ,
        "atk" : 25,
        "hp" : 1000,
		"endurance" : 7,
		"critical" : 60,
		"defCritical" : 10,
		"class" : "Drake",
        "spells_List":[
            {
				"name" : "Déplacement",
                "image" : "sampleDeplacement",
				"type" : "Mouvement",
				"direction":"Aérienne",
				"description" :"Esquive une attaque en allant sur 1 case à côté.",
                "element":"neutre",
                "range":1,
                "zone" :1,
				"cost":				
				{
				  "hp" : 0,
				  "endurance" : 2
				},
				"gain":
				{
				  "hp" : 0,
				  "endurance" : 0
				},				
				"gcd":1,
				"damage": 0
			},
            {
				"name" : "Soufle draconique",
                "image" : "sampleAttaque",
				"type" : "Attaque",
				"direction":"Aérienne",
				"description" :"lance un tsunami",
                "element":"feu",
                "range":1,
                "rangeForm": "Diamond",
                "zone" :3,
                "zoneForm" : "NormalLine",
				"cost":				
				{
				  "hp" : 0,
				  "endurance" : 2
				},
				"gain":
				{
				  "hp" : 0,
				  "endurance" : 0
				},				
				"gcd":1,
				"damage": 100
			},
            {
				"name" : "Heal",
                "image" : "sampleDefense",
				"type" : "Défense",
				"direction":"Aérienne",
				"description" :"Soigne de 10 pdv",
                "element":"neutre",
                "range":1,
                "rangeForm": "Target",
                "zone" :1,
                "zoneForm" : "Target",
				"cost":				
				{
				  "hp" : 0,
				  "endurance" : 2
				},
				"gain":
				{
				  "hp" : 10,
				  "endurance" : 0
				},				
				"gcd":1,
				"damage": 0
			}
        ]
    }
    
}