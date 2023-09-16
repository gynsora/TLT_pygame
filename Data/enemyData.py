from TLT.constants import *
ENEMY_LIST = { 
    "Dragoon":{
        "name" : "Dragoon",
        "x" : 2 ,
        "y" : 1 ,
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
				"Gain":
				{
				  "hp" : 0,
				  "endurance" : 0
				},				
				"Gcd":1,
				"Damage": 0
			}
        ]
    }
    
}