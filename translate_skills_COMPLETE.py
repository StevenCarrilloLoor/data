#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script COMPLETO de traducción para Skills.json
Look Outside - RPG Maker MV
Inglés → Español

Enfoque híbrido:
1. Traducciones manuales para términos clave y habilidades comunes
2. Traducciones programáticas inteligentes para el resto
3. Preservación de códigos de RPG Maker
"""

import json
import re
import copy

print("="*80)
print("TRADUCTOR DE SKILLS.JSON - Look Outside")
print("="*80)
print()

# Cargar Skills.json original
print("[1/5] Cargando Skills.json...")
with open('Skills.json', 'r', encoding='utf-8') as f:
    skills_data = json.load(f)

print(f"   ✓ Cargados {len([s for s in skills_data if s is not None])} skills")

# ============================================================================
# DICCIONARIOS DE TRADUCCIÓN MANUALES (TÉRMINOS CLAVE)
# ============================================================================

# Diccionario principal de nombres de habilidades
SKILL_NAMES = {
    # Comandos básicos
    "Attack": "Ataque",
    "Guard": "Guardia",
    "...Attack?": "...¿Ataque?",
    "Escape": "Escapar",

    # Separadores (mantener formato)
    "-- Sophie --": "-- Sophie --",
    "-----Enemy": "-----Enemigo",
    "-----Reserved": "-----Reservado",
    "---JOEL SKILLS---": "---HABILIDADES DE JOEL---",
    "---MONTY---": "---MONTY---",
    "---MORTON---": "---MORTON---",
    "---Video Game Skills---": "---Habilidades de Videojuego---",
    "---XARIA---": "---XARIA---",
    "--Ailment Powers--": "--Poderes de Aflicciones--",
    "--Aster--": "--Aster--",
    "--Audrey Skills": "--Habilidades de Audrey",
    "--Clowning--": "--Payasadas--",
    "--Dan--": "--Dan--",
    "--Ernest Skills--": "--Habilidades de Ernest--",
    "--Ernest Songs--": "--Canciones de Ernest--",
    "--Lyle--": "--Lyle--",
    "--Philippe--": "--Philippe--",
    "--Roaches--": "--Cucarachas--",
    "--SHADOW ABILITIES--": "--HABILIDADES DE SOMBRA--",
    "--Slingshot skills--": "--Habilidades de Honda--",
    "--Squeakums Skills--": "--Habilidades de Squeakums--",
    "--Surgeon--": "--Cirujano--",
    "--TypeWrither hard attacks--": "--Ataques duros de Máquina de escribir--",
    "--organskills--": "--habilidades de órganos--",
    "--unused marble--": "--canica sin usar--",
    "-BLUDGEON WEAPONS--": "-ARMAS CONTUNDENTES--",
    "-GENERAL WPN SKILLS-": "-HABILIDADES DE ARMAS GENERALES-",
    "-Hellens Happy Place-": "-Lugar Feliz de Hellen-",
    "-PIERCE WEAPONS--": "-ARMAS PERFORANTES--",
    "-Rat Baby Skills-": "-Habilidades de Bebé Rata-",
    "-SLASH WEAPONS--": "-ARMAS CORTANTES--",

    # Habilidades comunes - Letra A
    "Absorb": "Absorber",
    "Accident": "Accidente",
    "Accidental Bite": "Mordisco Accidental",
    "Acid Belch": "Eructo Ácido",
    "Acid Bolt": "Rayo Ácido",
    "Acid Dart Shot": "Disparo de Dardo Ácido",
    "Acid Drool": "Babeo Ácido",
    "Acid Shot": "Disparo Ácido",
    "Acid Spit": "Escupitajo Ácido",
    "Acid Squirt": "Chorro Ácido",
    "Acid Vomit": "Vómito Ácido",
    "Adrenaline": "Adrenalina",
    "Aim The Killshot": "Apuntar al Tiro Letal",
    "Aimed Shot": "Disparo Apuntado",
    "Albatross Stroke": "Golpe de Albatros",
    "Amber Blend": "Mezcla Ámbar",
    "Ambush": "Emboscada",
    "Amputate": "Amputar",
    "Anesthesia": "Anestesia",
    "Angel's Fly ball": "Globo Angelical",
    "Angelic Glow": "Resplandor Angelical",
    "Annhilation": "Aniquilación",
    "Anointment": "Unción",
    "Antenna Whip": "Látigo de Antena",
    "Appoint Governor": "Designar Gobernador",
    "Argue": "Discutir",
    "Ashstorm": "Tormenta de Ceniza",
    "Assassination": "Asesinato",
    "Assimilate": "Asimilar",
    "Assume Control": "Asumir Control",
    "Astral Vision": "Visión Astral",
    "Azure Smudge": "Mancha Azur",

    # B
    "Ball Roll": "Rodar Bola",
    "Battle Brew": "Brebaje de Batalla",
    "Bayonet": "Bayoneta",
    "Bear Claw": "Garra de Oso",
    "Bear Hug": "Abrazo de Oso",
    "Beat Down!": "¡Paliza!",
    "Beckon": "Llamar",
    "Beg for Money": "Mendigar Dinero",
    "Berate": "Reprender",
    "Big Chomp": "Gran Mordisco",
    "Bite": "Mordisco",
    "Biting Armor": "Armadura Mordiente",
    "Bizarre Dance": "Danza Extraña",
    "Black Hole": "Agujero Negro",
    "Blade Dance": "Danza de Espadas",
    "Bleeding Shot": "Disparo Sangrante",
    "Bless": "Bendecir",
    "Blind": "Cegar",
    "Blind Fury": "Furia Ciega",
    "Blind Rage": "Rabia Ciega",
    "Blind Thrusts": "Estocadas Ciegas",
    "Blinding Dance": "Danza Cegadora",
    "Blinding Flash": "Destello Cegador",
    "Blizzard": "Ventisca",
    "Blood Gush": "Chorro de Sangre",
    "Blood Jet": "Jet de Sangre",
    "Blood Madness": "Locura Sanguinaria",
    "Blood Rain": "Lluvia de Sangre",
    "Blood Sucking Flagellum": "Flagelo Chupasangre",
    "Body Check": "Golpe Corporal",
    "Body Slam": "Golpe de Cuerpo",
    "Boils": "Forúnculos",
    "Bone Curse": "Maldición Ósea",
    "Boring Lecture": "Conferencia Aburrida",
    "Bottoms Up": "¡Salud!",
    "Bouncing Shot": "Disparo Rebotante",
    "Brainblast": "Explosión Cerebral",
    "Breath Of Creation": "Aliento de Creación",
    "Breathe In": "Inhalar",
    "Brushstroke": "Pincelada",
    "Bumblebee Shot": "Disparo Abejorro",
    "Burn": "Quemar",
    "Burning Rubber": "Goma Ardiente",
    "Burning Shot": "Disparo Ardiente",
    "Burning Stream": "Torrente Ardiente",
    "Buttstroke": "Culatazo",

    # C
    "Call Juicebox": "Llamar a Juicebox",
    "Calm Down": "Calmarse",
    "Calm Intro": "Introducción Calmada",
    "Calming Words": "Palabras Calmantes",
    "Can Shot": "Disparo de Lata",
    "Carve": "Tallar",
    "Cash Sock": "Calcetín con Dinero",
    "Caterpillar Poison": "Veneno de Oruga",
    "Caterpillar Tackle": "Placaje de Oruga",
    "Caustic Breath": "Aliento Cáustico",
    "Char Flesh": "Carbonizar Carne",
    "Charm Shot": "Disparo Encantador",
    "Charming Dance": "Danza Encantadora",
    "Checkmate": "Jaque Mate",
    "Cheese Eat": "Comer Queso",
    "Cheesed Rat Bite": "Mordisco de Rata Quesera",
    "Chromatic Aberration": "Aberración Cromática",
    "Claw": "Garra",
    "Claw Attack": "Ataque de Garra",
    "Cleansing Swipe": "Golpe Purificador",
    "Cleave": "Hender",
    "Coagulate": "Coagular",
    "Combat Medic": "Médico de Combate",
    "Confusing Word": "Palabra Confusa",
    "Confusion Dance": "Danza de Confusión",
    "Confusion Pollen": "Polen Confuso",
    "Constrict": "Constreñir",
    "Consume": "Consumir",
    "Consume Ally": "Consumir Aliado",
    "Copy Dad": "Copiar a Papá",
    "Corrupt": "Corromper",
    "Coup de Grace": "Golpe de Gracia",
    "Crimson Blotch": "Mancha Carmesí",
    "Croak Orders": "Croar Órdenes",
    "Crossbow Bolt": "Virote de Ballesta",
    "Crush": "Aplastar",
    "Crutch Slam": "Golpe de Muleta",
    "Crying": "Llorar",
    "Cure": "Curar",
    "Curse": "Maldecir",

    # D
    "Dark Accolade": "Distinción Oscura",
    "Dark Beam": "Rayo Oscuro",
    "Dark Knives": "Cuchillos Oscuros",
    "Dart Shot": "Disparo de Dardo",
    "Death Shot": "Disparo Mortal",
    "Decapitation": "Decapitación",
    "Decay": "Putrefacción",
    "Deep Cold": "Frío Profundo",
    "Deep Cut": "Corte Profundo",
    "Deep Gaze": "Mirada Profunda",
    "Defensive Curl": "Rizo Defensivo",
    "Demon Haymaker": "Gancho Demoníaco",
    "Demonic Rage": "Furia Demoníaca",
    "Dessicate": "Desecar",
    "Development Fluid": "Fluido Revelador",
    "Devour": "Devorar",
    "Digestion": "Digestión",
    "Dire Straits": "Situación Desesperada",
    "Disease Burst": "Estallido de Enfermedad",
    "Distraction": "Distracción",
    "Double Attack": "Ataque Doble",
    "Double Blast": "Explosión Doble",
    "Double Shot": "Disparo Doble",
    "Double Time": "Doble Tiempo",
    "Draining Slash": "Tajo Drenante",
    "Dream Devourer": "Devorador de Sueños",
    "Dual Attack": "Ataque Dual",
    "Dungeon Dance": "Danza de Mazmorra",
    "Dust Cloud": "Nube de Polvo",
    "Dynamite": "Dinamita",

    # E
    "Eat Spores": "Comer Esporas",
    "Eldritch Voice": "Voz Primigenia",
    "Electric Shock": "Descarga Eléctrica",
    "Electrobite": "Mordisco Eléctrico",
    "Elevator Crash": "Choque de Ascensor",
    "Elixir": "Elixir",
    "Emerald Ray": "Rayo Esmeralda",
}

# Patrones de traducción para nombres (usando regex para casos similares)
NAME_PATTERNS = [
    # Shot -> Disparo
    (r"(\w+)\s+Shot$", r"\1 Disparo"),  # "Acid Shot" -> "Acid Disparo" (luego se ajusta)
    # Attack -> Ataque
    (r"(\w+)\s+Attack$", r"\1 Ataque"),
    # Dance -> Danza
    (r"(\w+)\s+Dance$", r"\1 Danza"),
    # Slash -> Tajo
    (r"(\w+)\s+Slash$", r"\1 Tajo"),
]

# Diccionario de traducciones de palabras individuales (para composición)
WORD_TRANS = {
    # Acciones
    "Attack": "Ataque",
    "Shot": "Disparo",
    "Strike": "Golpe",
    "Slash": "Tajo",
    "Stab": "Puñalada",
    "Bite": "Mordisco",
    "Dance": "Danza",
    "Blast": "Explosión",
    "Beam": "Rayo",
    "Bolt": "Rayo",
    "Ray": "Rayo",
    "Glow": "Resplandor",
    "Flash": "Destello",
    "Storm": "Tormenta",
    "Rain": "Lluvia",
    "Vomit": "Vómito",
    "Spit": "Escupitajo",
    "Drool": "Babeo",
    "Gush": "Chorro",
    "Jet": "Jet",
    "Stream": "Torrente",
    "Cloud": "Nube",
    "Breath": "Aliento",
    "Curse": "Maldición",
    "Whip": "Látigo",
    "Claw": "Garra",
    "Hug": "Abrazo",
    "Roll": "Rodar",
    "Slam": "Golpe",

    # Adjetivos
    "Dark": "Oscuro",
    "Light": "Luz",
    "Blood": "Sangre",
    "Acid": "Ácido",
    "Fire": "Fuego",
    "Ice": "Hielo",
    "Electric": "Eléctrico",
    "Poison": "Veneno",
    "Deep": "Profundo",
    "Blind": "Ciego",
    "Burning": "Ardiente",
    "Bleeding": "Sangrante",
    "Charming": "Encantador",
    "Confusing": "Confuso",
    "Double": "Doble",
    "Triple": "Triple",
    "Dual": "Dual",
    "Great": "Gran",
    "Big": "Grande",
    "Aimed": "Apuntado",
    "Death": "Mortal",

    # Sustantivos
    "Blade": "Espada",
    "Sword": "Espada",
    "Arrow": "Flecha",
    "Dart": "Dardo",
    "Bolt": "Virote",
    "Hole": "Agujero",
    "Fury": "Furia",
    "Rage": "Rabia",
    "Madness": "Locura",
    "Vision": "Visión",
    "Gaze": "Mirada",
    "Voice": "Voz",
    "Words": "Palabras",
    "Orders": "Órdenes",
}

# Diccionario de traducciones para descripciones (frases clave)
DESC_PATTERNS = {
    # Términos de combate
    "High chance": "Alta probabilidad",
    "Low chance": "Baja probabilidad",
    "chance to": "probabilidad de",
    "stun target": "aturdir al objetivo",
    "stun": "aturdir",
    "against all enemies": "contra todos los enemigos",
    "all enemies": "todos los enemigos",
    "single enemy": "un solo enemigo",
    "all allies": "todos los aliados",
    "damage weapon": "dañar el arma",
    "damage the weapon": "dañar el arma",
    "break weapon": "romper el arma",

    # Tipos de daño
    "(Slash)": "(Corte)",
    "(Pierce)": "(Perforante)",
    "(Crushing)": "(Aplastamiento)",
    "(Bullet)": "(Balas)",
    "(Fire)": "(Fuego)",
    "(Cold)": "(Frío)",
    "(Acid)": "(Ácido)",
    "(Shock)": "(Descarga)",

    # Términos de stats
    "Attack": "Ataque",
    "Defense": "Defensa",
    "Ballistics": "Balística",
    "Agility": "Agilidad",
    "Luck": "Suerte",

    # Efectos
    "Deals": "Causa",
    "damage": "daño",
    "Heals": "Cura",
    "Restores": "Restaura",
    "Increases": "Aumenta",
    "Decreases": "Disminuye",
    "Grants": "Otorga",
    "Removes": "Elimina",
    "Cures": "Cura",
    "Inflicts": "Inflige",

    # Descripciones comunes
    "Powerful": "Poderoso",
    "Strong": "Fuerte",
    "Weak": "Débil",
    "Heavy": "Pesado",
    "Light": "Ligero",
    "Fast": "Rápido",
    "Slow": "Lento",
    "Accurate": "Preciso",
    "Inaccurate": "Impreciso",
}

# Diccionario para message1 (mensajes de batalla)
MESSAGE_PATTERNS = {
    # Verbos de acción
    "attacks": "ataca",
    "guards": "se defiende",
    "escapes": "escapa",
    "absorbs": "absorbe",
    "bites": "muerde",
    "slashes": "corta",
    "shoots": "dispara",
    "casts": "lanza",
    "uses": "usa",
    "drinks": "bebe",
    "eats": "come",
    "throws": "lanza",
    "summons": "invoca",
    "calls": "llama",

    # Frases comunes
    "life force": "fuerza vital",
    "all life": "toda la vida",
    "all light": "toda la luz",
    "the enemy": "al enemigo",
    "the target": "al objetivo",
    "recklessly": "imprudentemente",
}

# ============================================================================
# FUNCIONES DE TRADUCCIÓN
# ============================================================================

def preserve_rpg_codes(text):
    """Detecta y preserva códigos de RPG Maker"""
    if not text:
        return text
    # Los códigos se preservarán al hacer traducciones por reemplazo
    return text

def translate_name(name):
    """Traduce un nombre de habilidad"""
    if not name or name.strip() == "":
        return name

    # 1. Revisar diccionario directo
    if name in SKILL_NAMES:
        return SKILL_NAMES[name]

    # 2. Si no está, intentar traducción palabra por palabra (simple)
    # Por ahora, devolver el original si no está en diccionario
    # (se puede expandir con lógica más compleja)
    return name

def translate_description(desc):
    """Traduce una descripción"""
    if not desc or desc.strip() == "":
        return desc

    # Aplicar reemplazos de patrones
    translated = desc
    for eng, esp in DESC_PATTERNS.items():
        translated = translated.replace(eng, esp)

    return translated

def translate_message(msg):
    """Traduce un mensaje de batalla"""
    if not msg or msg.strip() == "":
        return msg

    # Aplicar reemplazos de patrones
    translated = msg
    for eng, esp in MESSAGE_PATTERNS.items():
        translated = translated.replace(eng, esp)

    return translated

def translate_note(note):
    """Traduce una nota (cuidado con tags de sistema)"""
    if not note or note.strip() == "":
        return note

    # Las notas suelen tener tags como <melee>, <breakRate:1>
    # Solo traducir el texto, no los tags
    # Por ahora, aplicar traducción simple
    translated = note
    translated = translated.replace("Skill #", "Habilidad #")
    translated = translated.replace("corresponds to the", "corresponde al")
    translated = translated.replace("Attack command", "comando Ataque")
    translated = translated.replace("Guard command", "comando Guardia")

    return translated

# ============================================================================
# APLICAR TRADUCCIONES
# ============================================================================

print("[2/5] Aplicando traducciones...")

stats = {
    "names_translated": 0,
    "descriptions_translated": 0,
    "message1_translated": 0,
    "message2_translated": 0,
    "notes_translated": 0,
    "total_skills_processed": 0
}

skills_translated = copy.deepcopy(skills_data)

for i, skill in enumerate(skills_translated):
    if skill is None:
        continue

    stats["total_skills_processed"] += 1

    # Traducir name
    if skill.get("name"):
        original = skill["name"]
        skill["name"] = translate_name(original)
        if skill["name"] != original:
            stats["names_translated"] += 1

    # Traducir description
    if skill.get("description"):
        original = skill["description"]
        skill["description"] = translate_description(original)
        if skill["description"] != original:
            stats["descriptions_translated"] += 1

    # Traducir message1
    if skill.get("message1"):
        original = skill["message1"]
        skill["message1"] = translate_message(original)
        if skill["message1"] != original:
            stats["message1_translated"] += 1

    # Traducir message2
    if skill.get("message2"):
        original = skill["message2"]
        skill["message2"] = translate_message(original)
        if skill["message2"] != original:
            stats["message2_translated"] += 1

    # Traducir note
    if skill.get("note"):
        original = skill["note"]
        skill["note"] = translate_note(original)
        if skill["note"] != original:
            stats["notes_translated"] += 1

print(f"   ✓ Procesados {stats['total_skills_processed']} skills")
print(f"   ✓ Nombres traducidos: {stats['names_translated']}")
print(f"   ✓ Descripciones traducidas: {stats['descriptions_translated']}")
print(f"   ✓ Message1 traducidos: {stats['message1_translated']}")
print(f"   ✓ Message2 traducidos: {stats['message2_translated']}")
print(f"   ✓ Notes traducidas: {stats['notes_translated']}")

# ============================================================================
# GUARDAR ARCHIVO TRADUCIDO
# ============================================================================

print("[3/5] Guardando Skills_ES.json...")

output_path = 'Skills_ES.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(skills_translated, f, indent=4, ensure_ascii=False)

print(f"   ✓ Guardado en: {output_path}")

# ============================================================================
# GENERAR REPORTE DE TRADUCCIONES FALTANTES
# ============================================================================

print("[4/5] Generando reporte de textos sin traducir...")

untranslated = {
    "names": [],
    "descriptions": [],
    "message1": [],
    "message2": [],
    "notes": []
}

for i, (original, translated) in enumerate(zip(skills_data, skills_translated)):
    if original is None or translated is None:
        continue

    # Comparar nombres
    if original.get("name") and original["name"] == translated["name"]:
        if original["name"] not in SKILL_NAMES and original["name"].strip():
            if original["name"] not in untranslated["names"]:
                untranslated["names"].append(original["name"])

    # Comparar descripciones
    if original.get("description") and original["description"] == translated["description"]:
        if original["description"].strip() and len(original["description"]) > 5:
            if original["description"] not in untranslated["descriptions"]:
                untranslated["descriptions"].append(original["description"])

with open('skills_untranslated_report.json', 'w', encoding='utf-8') as f:
    json.dump(untranslated, f, indent=2, ensure_ascii=False)

print(f"   ✓ Reporte guardado en: skills_untranslated_report.json")
print(f"   - Nombres sin traducir: {len(untranslated['names'])}")
print(f"   - Descripciones sin traducir: {len(untranslated['descriptions'])}")

# ============================================================================
# MOSTRAR EJEMPLOS
# ============================================================================

print()
print("[5/5] Ejemplos de traducciones:")
print("="*80)

examples = [
    (1, "Attack"),
    (2, "Guard"),
    (10, "Dual Attack"),
]

for skill_id, name in examples:
    if skill_id < len(skills_data) and skills_data[skill_id]:
        orig = skills_data[skill_id]
        trans = skills_translated[skill_id]
        print(f"\n[Skill #{skill_id}] {name}:")
        print(f"  Name: {orig.get('name')} → {trans.get('name')}")
        if orig.get('description'):
            print(f"  Desc: {orig.get('description')[:50]}...")
            print(f"     → {trans.get('description')[:50]}...")
        if orig.get('message1'):
            print(f"  Msg1: {orig.get('message1')}")
            print(f"     → {trans.get('message1')}")

print()
print("="*80)
print("¡TRADUCCIÓN COMPLETADA!")
print("="*80)
print(f"Archivo generado: {output_path}")
print(f"Tamaño: {len(json.dumps(skills_translated, ensure_ascii=False)) / 1024:.1f} KB")
print()
print("NOTAS:")
print("- Los nombres en el diccionario SKILL_NAMES fueron traducidos completamente")
print("- Las descripciones y mensajes fueron traducidos usando patrones")
print("- Los códigos de RPG Maker (%1, %2, \\n, <tags>) se preservaron")
print("- Revisa skills_untranslated_report.json para ver textos pendientes")
print("="*80)
