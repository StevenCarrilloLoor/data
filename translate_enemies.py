#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de traducción para Enemies.json de RPG Maker - Look Outside
Traduce 548 nombres de enemigos + textos especiales
Mantiene tono de horror lovecraftiano/surrealista
"""

import json
import os
import re

# ============================================================================
# DICCIONARIO DE TRADUCCIÓN - NOMBRES DE ENEMIGOS
# ============================================================================
# Traducción manual contextual manteniendo el tono de horror del juego

ENEMY_NAMES = {
    # === SECCIONES/CATEGORÍAS ===
    "-- MEATWORLD --": "-- MUNDO DE CARNE --",
    "--Apt12--": "--Apto12--",
    "--BLACKOUT--": "--APAGÓN--",
    "--Basement NPCs--": "--NPCs del Sótano--",
    "--CURSED VISITORS": "--VISITANTES MALDITOS",
    "--Door Knock": "--Llamada a la Puerta",
    "--FLOODED BASEMENT--": "--SÓTANO INUNDADO--",
    "--FloodedBasementEX--": "--SótanoInundadoEX--",
    "--Frozen Apartment--": "--Apartamento Congelado--",
    "--Guts--": "--Tripas--",
    "--Medic Tent--": "--Carpa Médica--",
    "--Multiface Apt--": "--Apto Multicara--",
    "--Other--": "--Otro--",
    "--Pit--": "--Foso--",
    "--RATS--": "--RATAS--",
    "--Rat Arena--": "--Arena de Ratas--",
    "--Taxidermy Apartment--": "--Apartamento de Taxidermia--",
    "--Taxiextras--": "--Taxiextras--",
    "--WITNESSES--": "--TESTIGOS--",
    "--Worm--": "--Gusano--",
    "-crossword tomb": "-tumba de crucigrama",

    # === ENTIDADES MISTERIOSAS (símbolos interrogantes) ===
    "? ? ? ?? ? ?? ??": "? ? ? ?? ? ?? ??",
    "? ???? ?????": "? ???? ?????",
    "? Float": "? Flotante",
    "? Ghost": "? Fantasma",
    "? Hang": "? Colgante",
    "? Hanging": "? Colgando",
    "? Looking": "? Mirando",
    "? Walk": "? Caminante",
    "?? Crawl": "?? Arrastre",
    "?? Hide": "?? Escondido",
    "?? Lash": "?? Látigo",
    "?? Scuttle": "?? Escabullir",
    "?? Stack": "?? Apilado",
    "?? Take": "?? Tomar",
    "?? Tangle": "?? Enredado",
    "?? Three": "?? Tres",
    "??? ?? ?? ???": "??? ?? ?? ???",
    "??? ?? ?????": "??? ?? ?????",
    "??? Fear": "??? Miedo",
    "??? Grow": "??? Crecer",
    "??? Scare": "??? Asustar",
    "??? Scatter": "??? Dispersar",
    "??? Two Face": "??? Dos Caras",
    "??? Worm": "??? Gusano",
    "???? Ceiling": "???? Techo",
    "???? Cluster": "???? Cúmulo",
    "???? Corpse": "???? Cadáver",
    "???? Float": "???? Flotante",
    "???? Laugh": "???? Risa",
    "???? Sphinx": "???? Esfinge",
    "???? Split": "???? Partido",
    "???? Teeth": "???? Dientes",
    "???? Trio": "???? Trío",
    "????? ??? ??": "????? ??? ??",

    # === PERSONAJES Y NPCS ===
    "neighbor": "vecino",
    "Eugene": "Eugene",
    "Nestor": "Néstor",
    "Papineau": "Papineau",
    "Shadow": "Sombra",
    "Sybil": "Sybil",
    "Wounded Neighbor": "Vecino Herido",
    "Vincent": "Vincent",
    "Pierre": "Pierre",
    "Baby Teeth": "Dientes de Leche",
    "Clint": "Clint",
    "Madison": "Madison",
    "Joel": "Joel",
    "Benjamin": "Benjamín",
    "Montgomery": "Montgomery",
    "Xaria": "Xaria",
    "Dan's Mom": "Mamá de Dan",
    "Danielle": "Danielle",
    "Darryl": "Darryl",
    "Emmanuel": "Emmanuel",
    "Ernest": "Ernest",
    "Esther": "Esther",
    "Father Andrew": "Padre Andrew",
    "Hellen": "Hellen",
    "Humphrey": "Humphrey",
    "Jasper": "Jasper",
    "Jean-Pierre": "Jean-Pierre",
    "Jeanne": "Jeanne",
    "Jennifer": "Jennifer",
    "Jon": "Jon",
    "Kaeley": "Kaeley",
    "Laurent": "Laurent",
    "Louis": "Louis",
    "Lyle": "Lyle",
    "Marshall": "Marshall",
    "Marvin": "Marvin",
    "Michael": "Michael",
    "Musette": "Musette",
    "Mutt": "Perro",
    "Noah": "Noah",
    "Phillippe": "Philippe",
    "Placide": "Plácido",
    "Priest": "Sacerdote",
    "Rana": "Rana",
    "Robert": "Robert",
    "Roderigue": "Rodrigo",
    "Steve": "Steve",
    "Steve jr": "Steve jr",
    "Stuart": "Stuart",
    "Summer": "Summer",
    "Sylvain": "Sylvain",
    "Claire": "Claire",

    # === ASTRONOMERS (Los Cuatro Exaltados) ===
    "Aster": "Aster",
    "Aster, the Dream Eater": "Aster, el Devorador de Sueños",
    "Aurelius": "Aurelio",
    "Beryl": "Berilo",
    "Beryl of the Hundred Maws": "Berilo de las Cien Fauces",
    "Exalted Four": "Los Cuatro Exaltados",
    "Spine Taker Aurelius": "Aurelio el Toma-Espinas",

    # === MONSTRUOS HUMANOIDES ===
    "Leering Husk": "Cáscara Lasciva",
    "Teratoma": "Teratoma",
    "Clown Tail": "Cola de Payaso",
    "Toothling": "Dientecillo",
    "Tooth Fairy": "Hada de los Dientes",
    "Rotten tooth": "Diente Podrido",
    "Maniac": "Maníaco",
    "Beggar": "Mendigo",
    "Creep": "Repugnante",
    "Grinning Woman": "Mujer Sonriente",
    "Grinning Beast": "Bestia Sonriente",
    "Strange Lady": "Dama Extraña",
    "Lost Child": "Niño Perdido",
    "Tall Man": "Hombre Alto",
    "Face Taker": "Toma-Caras",
    "Gentle Face": "Cara Gentil",
    "Hideface": "Escondecaras",
    "Headface": "Carabeza",
    "Stretchface": "Caraestira",
    "Facehead": "Cabecara",
    "Faceless Husk": "Cáscara Sin Rostro",
    "Mad Husk": "Cáscara Loca",
    "Fleshy Husk": "Cáscara Carnosa",
    "Gaunt Husk": "Cáscara Demacrada",
    "Hollow Husk": "Cáscara Hueca",
    "Empty Hall": "Pasillo Vacío",
    "Cluster Husk": "Cáscara Racimo",
    "Double Husk": "Cáscara Doble",
    "Small Husk": "Cáscara Pequeña",
    "Husk": "Cáscara",
    "Drooling Husk": "Cáscara Babeante",
    "Spider Husk": "Cáscara Araña",

    # === MONSTRUOS OCULARES ===
    "Bottom Eye": "Ojo Inferior",
    "Top Eye": "Ojo Superior",
    "Big Eye": "Ojo Grande",
    "Eye Legs": "Ojo Patas",
    "Eye Shoulder": "Ojo Hombro",
    "Eye Sucker": "Chupador de Ojos",
    "Eye Rat": "Ojo Rata",
    "Wiggle Eye": "Ojo Serpenteante",
    "Eyecluster": "Racimo de Ojos",
    "Crowded Eyes": "Ojos Apiñados",
    "The Eyes": "Los Ojos",
    "Emerald Eye": "Ojo Esmeralda",
    "Eternal Eye": "Ojo Eterno",
    "Golden Eye": "Ojo Dorado",
    "Ruby Eye": "Ojo Rubí",
    "Sapphire Eye": "Ojo Zafiro",
    "Gawker": "Mirón",
    "Glance": "Vistazo",
    "Observer": "Observador",
    "Onlooker": "Espectador",
    "Peeking": "Espiando",
    "Witness": "Testigo",
    "Panopticon": "Panóptico",

    # === MONSTRUOS DENTALES/BOCA ===
    "Mouth": "Boca",
    "Mouth Rat": "Rata Boca",
    "Papillae": "Papilas",
    "Tonsil": "Amígdala",
    "Underbite": "Prognatismo",
    "Twojaws": "Dosmandíbulas",
    "Lokjaw": "Mandíbula Rota",
    "Masticator": "Masticador",
    "The Maws": "Las Fauces",
    "Hell Mouth": "Boca Infernal",

    # === GUSANOS Y CRIATURAS SERPENTINAS ===
    "Worm": "Gusano",
    "Great Worm": "Gran Gusano",
    "Large Worm": "Gusano Grande",
    "??? Worm": "??? Gusano",
    "Face Worm": "Gusano Cara",
    "Long face worm": "Gusano cara larga",
    "Tall Face Worm": "Gusano Cara Alta",
    "Finger Worm": "Gusano Dedo",
    "Leg Worm": "Gusano Pierna",
    "Leg Knotworm": "Gusano Nudo Pierna",
    "Meat Worm": "Gusano de Carne",
    "Worm Body": "Cuerpo de Gusano",
    "Worm Foot": "Pie de Gusano",
    "Worm Hand": "Mano de Gusano",
    "Worm Head": "Cabeza de Gusano",
    "Worm Shop": "Tienda del Gusano",

    # === RATAS ===
    "Rat": "Rata",
    "Big Rat": "Rata Grande",
    "Giant Rat": "Rata Gigante",
    "Belly Rat": "Rata Vientre",
    "Eye Rat": "Rata Ojo",
    "Mouth Rat": "Rata Boca",
    "Lantern Rat": "Rata Linterna",
    "Poison Rat": "Rata Venenosa",
    "Tail Rat": "Rata Cola",
    "Teeth Rat": "Rata Dientes",
    "Throat Rat": "Rata Garganta",
    "Rat Beast": "Bestia Rata",
    "Rat Bug": "Rata Insecto",
    "Rat Champion": "Campeón Rata",
    "Rat Clump": "Grupo de Ratas",
    "Rat Freak": "Monstruo Rata",
    "Rat Guardian": "Guardián Rata",
    "Rat Hole": "Agujero de Rata",
    "Rat King": "Rey Rata",
    "Rat Swarm": "Enjambre de Ratas",
    "Rat Thing": "Cosa Rata",
    "Ratiarus": "Ratiarus",
    "Brainrattler": "Cerebrorrateador",

    # === CUCARACHAS ===
    "Giant Roach": "Cucaracha Gigante",
    "Roach Man": "Hombre Cucaracha",

    # === ARAÑAS Y ARTRÓPODOS ===
    "Spider": "Araña",
    "Spider Husk": "Cáscara Araña",
    "Sewer Spider": "Araña de Alcantarilla",
    "Harvestman": "Opilión",
    "Centifingers": "Cien Dedos",
    "Centipede Arm": "Brazo Ciempiés",
    "Centipede Kid": "Niño Ciempiés",
    "Fangipede": "Colmillipiés",
    "Sadipede": "Tristipiés",
    "Electropede": "Electropiés",
    "Tirepede": "Neumatipiés",

    # === GARRAPATAS ===
    "Big Tick": "Garrapata Grande",
    "Boss Tick": "Jefe Garrapata",
    "Small Tick": "Garrapata Pequeña",
    "Furnace Tick": "Garrapata Horno",
    "Tickmonger": "Mercader de Garrapatas",
    "Lil Tickle": "Cosquillita",
    "Tingler": "Hormigueante",

    # === INSECTOS Y CRIATURAS VOLANTES ===
    "Bat": "Murciélago",
    "Crow": "Cuervo",
    "Drain Fly": "Mosca de Drenaje",
    "Fly Man": "Hombre Mosca",
    "Fly Kid": "Niño Mosca",
    "Grasshopper": "Saltamontes",
    "Caterpillar": "Oruga",
    "Winged": "Alado",

    # === CRIATURAS ACUÁTICAS ===
    "Angler": "Rape",
    "Crab": "Cangrejo",
    "Traffic Crab": "Cangrejo de Tráfico",
    "Dragonfish": "Pez Dragón",
    "Jellyfish": "Medusa",
    "Leech": "Sanguijuela",
    "Tooth Leech": "Sanguijuela Diente",
    "Piranhaman": "Hombre Piraña",
    "Piranha Left Arm": "Piraña Brazo Izquierdo",
    "Piranha Left Eye": "Piraña Ojo Izquierdo",
    "Piranha Mouth": "Piraña Boca",
    "Piranha Nose": "Piraña Nariz",
    "Piranha Right Arm": "Piraña Brazo Derecho",
    "Piranha Right Eye": "Piraña Ojo Derecho",
    "Sailfish": "Pez Vela",
    "Seastar": "Estrella de Mar",
    "Shark": "Tiburón",
    "Shrimp": "Camarón",
    "Shrimp Knight": "Caballero Camarón",
    "Slug man": "Hombre Babosa",
    "Olm": "Proteo",
    "Olmling": "Proteito",

    # === ANFIBIOS Y REPTILES ===
    "Crocodile": "Cocodrilo",
    "Croco Kid": "Niño Cocodrilo",
    "Salamander": "Salamandra",

    # === MONSTRUOS DE MANOS Y EXTREMIDADES ===
    "Hand": "Mano",
    "Crawling Hand": "Mano Reptante",
    "The Crawling Hand": "La Mano Reptante",
    "Hand Swarm": "Enjambre de Manos",
    "Hand Mutant": "Mutante de Mano",
    "Grasper": "Agarrador",
    "The Claws": "Las Garras",
    "Feely": "Palpador",
    "Touchy": "Tocador",
    "High Five": "Choca Esos Cinco",
    "Armknot": "Nudo de Brazo",
    "Limbs": "Extremidades",
    "Limb Thief": "Ladrón de Extremidades",
    "Elbows": "Codos",
    "Hand Grenade": "Granada de Mano",
    "Armed Grenade": "Granada Armada",

    # === MONSTRUOS DE CABEZA ===
    "Back Head": "Cabeza Trasera",
    "Bottom Head": "Cabeza Inferior",
    "Left Head": "Cabeza Izquierda",
    "Lower Head": "Cabeza Baja",
    "Right Head": "Cabeza Derecha",
    "Top Head": "Cabeza Superior",
    "Top Right Head": "Cabeza Superior Derecha",
    "Head Mutant": "Mutante de Cabeza",
    "Louis' Head": "Cabeza de Louis",
    "Tumorhead": "Cabeza de Tumor",
    "Shockhead": "Cabeza de Descarga",
    "Screaming Skull": "Cráneo Gritante",

    # === MONSTRUOS DE CUERPO/PARTES ===
    "Underbody": "Bajocuerpo",
    "Louis' Torso": "Torso de Louis",
    "Louis' Upper Half": "Mitad Superior de Louis",
    "Louis' Lower Half": "Mitad Inferior de Louis",
    "Louis' Tail": "Cola de Louis",
    "Louis' Leg": "Pierna de Louis",
    "Leg Mutant": "Mutante de Pierna",
    "Split Tail": "Cola Partida",
    "Ribcage Bloom": "Floración de Costilla",
    "Ventricle": "Ventrículo",

    # === SOMBRAS Y CRIATURAS OSCURAS ===
    "Crawling Shade": "Sombra Reptante",
    "Hanging Shade": "Sombra Colgante",
    "Moaning Shade": "Sombra Gimiente",
    "Stumbling Shade": "Sombra Tropezante",
    "Writhing Shade": "Sombra Retorcida",
    "Shadowling": "Sombrío",

    # === ESPORAS Y HONGOS ===
    "Spore Mother": "Madre Espora",
    "Spore Brain": "Cerebro Espora",
    "Spore Hand": "Mano Espora",
    "Spore Head": "Cabeza Espora",
    "Spore Torso": "Torso Espora",
    "Spore Shambler": "Deambulador Espora",
    "Laughing Mold": "Moho Risueño",

    # === PLANTAS Y VEGETACIÓN ===
    "Great Flower": "Gran Flor",
    "Skull Flower": "Flor de Cráneo",
    "Crimson Bloom": "Floración Carmesí",
    "Grass Freak": "Monstruo de Hierba",
    "Moss Freak": "Monstruo de Musgo",
    "Mossling": "Musguito",
    "Root Freak": "Monstruo de Raíz",
    "Seed Freak": "Monstruo de Semilla",
    "Skitterbush": "Arbusto Escurridizo",

    # === MILITARES Y SOLDADOS ===
    "Soldier": "Soldado",
    "Commando": "Comando",
    "Enforcer": "Ejecutor",
    "Scout": "Explorador",
    "Attacker": "Atacante",
    "Bayonet": "Bayoneta",
    "Gatling": "Gatling",
    "Man At Arms": "Hombre de Armas",
    "Heavy Armored": "Fuertemente Blindado",
    "Rifle Mole": "Topo de Rifle",
    "Shotgun Mole": "Topo de Escopeta",
    "Rocket Launcher": "Lanzacohetes",
    "Colonel Squeakum": "Coronel Chillón",
    "Colonel Squeakums": "Coronel Chillones",
    "Sapper": "Zapador",
    "Minesweeper": "Dragaminas",
    "Trench Digger": "Cavador de Trincheras",
    "Landmite": "Mina Terrestre",
    "Memorial": "Memorial",

    # === VEHÍCULOS ===
    "APC": "Transporte Blindado",
    "Cop Car": "Patrulla",
    "SWAT Truck": "Camión SWAT",
    "Hellride": "Viaje Infernal",

    # === COMERCIANTES Y NPCS ===
    "Food Trader": "Comerciante de Comida",
    "Gun Trader": "Comerciante de Armas",
    "General Trader": "Comerciante General",
    "Curio Trader": "Comerciante de Curiosidades",
    "Doctor": "Doctor",
    "Delivery Guy": "Repartidor",
    "Pizza Guy": "Pizzero",
    "Gamer": "Jugador",
    "Gamer Supreme": "Jugador Supremo",

    # === MONSTRUOS ESPECÍFICOS (JEFES Y ÚNICOS) ===
    "Boiler Beast": "Bestia de Caldera",
    "Furnace": "Horno",
    "Sewer Beast": "Bestia de Alcantarilla",
    "Elevator Thing": "Cosa del Ascensor",
    "Janitor": "Conserje",
    "Taxidermy": "Taxidermia",
    "Shutterbug": "Fotógrafo",
    "Stargazer": "Contemplador de Estrellas",
    "Spine": "Espina",
    "Spinero": "Espinoso",
    "Angel": "Ángel",
    "Angel Of Death": "Ángel de la Muerte",
    "Mask": "Máscara",
    "The Visitor": "El Visitante",
    "Hydra": "Hidra",
    "Chaos Quartet": "Cuarteto del Caos",
    "Discordant Triune": "Trino Discordante",
    "Unholy Duet": "Dúo Profano",
    "Chorus of One": "Coro de Uno",
    "Co-Authors": "Co-Autores",
    "Godhead Fred": "Fred Deidad",
    "Bright Fred": "Fred Brillante",
    "Faceless Fred": "Fred Sin Rostro",
    "Fred Who Bites": "Fred Que Muerde",
    "Green Fred, Left": "Fred Verde, Izquierda",
    "Green Fred, Right": "Fred Verde, Derecha",
    "Green Fred, Upper": "Fred Verde, Superior",
    "Hidden Fred": "Fred Oculto",
    "Scared Fred": "Fred Asustado",
    "Shadow Fred": "Fred Sombra",
    "Toxic Fred": "Fred Tóxico",
    "Tumor Fred": "Fred Tumor",
    "Wriggly Fred": "Fred Serpenteante",

    # === OBJETOS ANIMADOS ===
    "Tire Stack": "Pila de Neumáticos",
    "Traffic Cone": "Cono de Tráfico",
    "Wheel": "Rueda",
    "Rear-View Mirror": "Espejo Retrovisor",
    "Polaroid": "Polaroid",
    "Typewrither": "Máquina de Escribir",
    "Scissors": "Tijeras",
    "Needles": "Agujas",
    "Cable Jumper": "Cables de Arranque",
    "Wirecutter": "Cortacables",
    "Suture Wire": "Alambre de Sutura",

    # === ROPA Y ACCESORIOS ANIMADOS ===
    "Balaclava": "Pasamontañas",
    "Bandaged": "Vendado",
    "Bottines": "Botines",
    "Cowboy Hat": "Sombrero Vaquero",
    "Not A Cowboy Hat": "No Es Un Sombrero Vaquero",
    "Trapper Hat": "Gorro de Cazador",
    "Crutches": "Muletas",
    "Earmuffs": "Orejeras",
    "Manchon": "Manguito",
    "Manteau": "Abrigo",
    "Pompom": "Pompón",
    "Scarf": "Bufanda",
    "Triscarf": "Tribufanda",
    "Trenchcoat": "Gabardina",
    "Tuque": "Gorro",

    # === MONSTRUOS ELEMENTALES Y ABSTRACTOS ===
    "Bite Elemental": "Elemental de Mordida",
    "Bite child": "Niño mordida",
    "Slash child": "Niño corte",
    "Stab child": "Niño apuñalado",
    "Gaze child": "Niño mirada",
    "Confusion": "Confusión",
    "Hunger": "Hambre",
    "Lethargy": "Letargo",
    "Famine": "Hambruna",

    # === TRABAJADORES Y OFICIOS ===
    "Craftsman": "Artesano",
    "Scrivener's Corpse": "Cadáver del Escribano",
    "Mummified Scribe": "Escriba Momificado",
    "Dessicated Author": "Autor Desecado",
    "Draft": "Borrador",
    "Derivative": "Derivado",
    "Wailing Poet": "Poeta Llorón",
    "Pundit": "Erudito",
    "Swordmaster": "Maestro de Espada",
    "Swordmaster Comatus": "Maestro de Espada Comatus",
    "Swordsgamer": "Espadajugador",

    # === PERSONAJES DE APARIENCIA HUMANA ===
    "Argot": "Argot",
    "Auguste": "Auguste",
    "Camille": "Camille",
    "Carlos": "Carlos",
    "Cateline": "Cateline",
    "Charles": "Charles",
    "Charlie": "Charlie",
    "Choco": "Choco",
    "Cinnamon": "Canela",
    "Clementine": "Clementina",
    "Colin": "Colin",
    "Clyde": "Clyde",
    "Frederic": "Federico",
    "Glenn": "Glenn",
    "Goths": "Góticos",
    "Hobbs": "Hobbs",
    "Lou": "Lou",
    "Marcus": "Marcus",
    "Milledoigts": "Milledoigts",
    "Main Gauche": "Main Gauche",
    "Surgeon": "Cirujano",
    "Ursuline": "Ursuline",
    "Wilhelmina": "Guillermina",

    # === NIÑOS Y CRIATURAS JÓVENES ===
    "Bite child": "Niño mordida",
    "Centipede Kid": "Niño Ciempiés",
    "Cosmo Kid": "Niño Cosmo",
    "Croco Kid": "Niño Cocodrilo",
    "Eyeball Kid": "Niño Globo Ocular",
    "Eyestalk Kid": "Niño Pedúnculo Ocular",
    "Fly Kid": "Niño Mosca",
    "Game Kid": "Niño Juego",
    "Gaze child": "Niño mirada",
    "Lost Child": "Niño Perdido",
    "Service Dog": "Perro de Servicio",
    "Slash child": "Niño corte",
    "Spooky Kid": "Niño Espeluznante",
    "Stab child": "Niño apuñalado",
    "Tentacles Kid": "Niño Tentáculos",

    # === MONSTRUOS DE APARIENCIA GROTESCA ===
    "Bloated Attacker": "Atacante Hinchado",
    "Crawl Corpse": "Cadáver Reptante",
    "Crawler": "Rastrero",
    "Crawling": "Arrastrándose",
    "Scuttling": "Escabulléndose",
    "Scrabbly": "Arañador",
    "Screaming guts": "Tripas Gritando",
    "Floating Corpse": "Cadáver Flotante",
    "Drowning": "Ahogándose",
    "???? Corpse": "???? Cadáver",
    "Infected": "Infectado",
    "Stressed-out": "Estresado",
    "Convoluted": "Enrevesado",
    "Half-Baked": "A Medio Hacer",
    "Indulgent": "Indulgente",
    "Obsession": "Obsesión",
    "Predator": "Depredador",
    "Devourer": "Devorador",
    "Ghoul": "Carroñero",
    "Mannikin": "Maniquí",

    # === MONSTRUOS DE TUBO/TUBERÍA ===
    "Pipe Man": "Hombre Tubo",
    "Pipe Man Back": "Hombre Tubo Espalda",
    "Pipe Man Face": "Hombre Tubo Cara",
    "Pipe Man Misery": "Hombre Tubo Miseria",
    "Pipe Man Scuttle": "Hombre Tubo Escabullir",
    "Pipe Man Snake": "Hombre Tubo Serpiente",
    "Tall Pipe Man": "Hombre Tubo Alto",

    # === MONSTRUOS DE LENGUA ===
    "left tongue": "lengua izquierda",
    "middle tongue": "lengua media",
    "right tongue": "lengua derecha",

    # === CEREBROS Y PARÁSITOS ===
    "Brainleech": "Sanguijuela Cerebral",
    "Electrophage": "Electrófago",

    # === MONSTRUOS MARINOS/BESTIALES ===
    "Grizzly": "Oso Pardo",
    "Moose": "Alce",
    "Rhinoceros": "Rinoceronte",
    "Tiger": "Tigre",
    "Octopus": "Pulpo",

    # === MONSTRUOS DE PINTURA ===
    "Green Paintling": "Pinturita Verde",

    # === TUMORES Y CRECIMIENTOS ===
    "Left Tumor": "Tumor Izquierdo",
    "Right Tumor": "Tumor Derecho",

    # === TENTÁCULOS ===
    "Left Tentacles": "Tentáculos Izquierdos",
    "Right Tentacles": "Tentáculos Derechos",

    # === GUARDIAS Y PROTECTORES ===
    "Guardian": "Guardián",
    "Left Guard": "Guardia Izquierdo",
    "Right Guard": "Guardia Derecho",
    "Rider": "Jinete",

    # === MONSTRUOS DE COMIDA ===
    "Fruit": "Fruta",
    "Mad Pie": "Pastel Loco",

    # === LINTERNAS Y LUZ ===
    "Lantern": "Linterna",

    # === ESPEJO Y REFLEJO ===
    "reflection": "reflejo",

    # === ANIMALES DIVERSOS ===
    "Roadkill": "Atropellado",

    # === PERSONAJES ABSTRACTOS/ESPECIALES ===
    "Libra": "Libra",
    "Same Old Dan": "El Mismo Dan de Siempre",
    "XIN-AMON": "XIN-AMON",
    "\\N[40]": "\\N[40]",

    # === VARIOS/OTROS ===
    "Tough Guy": "Tipo Duro",
    "Twitchy Guy": "Tipo Nervioso",
    "Key Woman": "Mujer Llave",
    "Mr. Henderson": "Sr. Henderson",
    "Commuters": "Pasajeros",
    "Rapscallion": "Granuja",
    "Rascal": "Pícaro",
    "Scamp": "Bribón",
    "Rowdy Biker": "Motociclista Alborotador",
    "Rodencutor": "Roejecutor",

    # === WIGGLES Y CRIATURAS SERPENTEANTES ===
    "Wiggles": "Serpenteante",
    "Lil Stretchy": "Estiradito",

    # === WIPER ===
    "Wiper": "Limpiaparabrisas",

    # === PERSONAS NORMALES ===
    "dummyEnemy": "enemigoPrueba",
    "TestDummy": "ManiquíPrueba",
    "Tickletest": "PruebaCosquillas",

    # === THE CRIMSON SCOURGE ===
    "The Crimson Scourge": "El Azote Carmesí",

    # === SUPER VERSIONES ===
    "Super Esther": "Súper Esther",
    "Super Noah": "Súper Noah",
}

# ============================================================================
# TEXTOS ESPECIALES (ADVICE Y LORE)
# ============================================================================

ADVICE_TEXTS = {
    "Try smashing it into bits.": "Intenta hacerlo pedazos."
}

LORE_TEXTS = {
    "I think this is just a little guy.": "Creo que este es solo un pequeñín."
}

# ============================================================================
# FUNCIÓN PRINCIPAL DE TRADUCCIÓN
# ============================================================================

def translate_enemies_json(input_file, output_file):
    """
    Traduce Enemies.json del inglés al español
    """
    print("=" * 80)
    print("TRADUCCIÓN DE ENEMIES.JSON - LOOK OUTSIDE")
    print("=" * 80)

    # Leer archivo original
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"\n✓ Archivo leído: {input_file}")
    print(f"  Total de enemigos: {len(data)} (incluyendo null)")

    stats = {
        'names': 0,
        'advice': 0,
        'lore': 0,
        'total': 0
    }

    # Traducir cada enemigo
    for i, enemy in enumerate(data):
        if enemy is None:
            continue

        # Traducir nombre
        if 'name' in enemy and enemy['name'] in ENEMY_NAMES:
            enemy['name'] = ENEMY_NAMES[enemy['name']]
            stats['names'] += 1
            stats['total'] += 1

        # Traducir textos en note (advice y lore)
        if 'note' in enemy and enemy['note']:
            note = enemy['note']

            # Traducir advice
            for orig, trad in ADVICE_TEXTS.items():
                if orig in note:
                    note = note.replace(f'<advice:{orig}>', f'<advice:{trad}>')
                    stats['advice'] += 1
                    stats['total'] += 1

            # Traducir lore
            for orig, trad in LORE_TEXTS.items():
                if orig in note:
                    note = note.replace(f'<lore:{orig}>', f'<lore:{trad}>')
                    stats['lore'] += 1
                    stats['total'] += 1

            enemy['note'] = note

    # Guardar archivo traducido
    os.makedirs(os.path.dirname(output_file) if os.path.dirname(output_file) else '.', exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"✓ Archivo traducido guardado: {output_file}")

    # Mostrar estadísticas
    print("\n" + "=" * 80)
    print("ESTADÍSTICAS DE TRADUCCIÓN")
    print("=" * 80)
    print(f"  Nombres de Enemigos:      {stats['names']:3d} traducciones")
    print(f"  Textos <advice:>:         {stats['advice']:3d} traducciones")
    print(f"  Textos <lore:>:           {stats['lore']:3d} traducciones")
    print(f"  {'-' * 78}")
    print(f"  TOTAL:                    {stats['total']:3d} traducciones")
    print("=" * 80)

    print("\n✓ Traducción completada exitosamente!")

    return stats

# ============================================================================
# EJECUCIÓN
# ============================================================================

if __name__ == "__main__":
    input_file = "/home/user/data/Enemies.json"
    output_file = "/home/user/data/outputs/Enemies_ES.json"

    try:
        stats = translate_enemies_json(input_file, output_file)
    except Exception as e:
        print(f"\n✗ Error durante la traducción: {e}")
        import traceback
        traceback.print_exc()
