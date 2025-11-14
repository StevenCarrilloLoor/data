#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de traducción para System.json de RPG Maker - Look Outside
Traduce del inglés al español manteniendo estructura y códigos de control
"""

import json
import os

# ============================================================================
# DICCIONARIO DE TRADUCCIÓN
# ============================================================================

# Tipos de armadura
ARMOR_TYPES = {
    "General Armor": "Armadura General",
    "Hero Only": "Solo Héroe",
    "Accessory": "Accesorio",
    "Heavy Armor": "Armadura Pesada",
    "Firearm": "Arma de Fuego",
    "Two Handed Ranged": "A Distancia Dos Manos",
    "Projectile Wpn": "Arma de Proyectiles",
    "Slingshot": "Tirachinas",
    "Junk": "Chatarra",
    "Machine": "Máquina"
}

# Elementos de combate
ELEMENTS = {
    "Crushing": "Aplastamiento",
    "Slashing": "Corte",
    "Piercing": "Perforación",
    "Fire": "Fuego",
    "Acid": "Ácido",
    "Blast": "Explosión",
    "Bullet": "Bala",
    "Armor Piercing": "Perforador de Armadura",
    "Flesh": "Carne",
    "Cold": "Frío",
    "Shock": "Descarga",
    "Shadow": "Sombra"
}

# Tipos de equipo
EQUIP_TYPES = {
    "Weapon": "Arma",
    "Ranged": "A Distancia",
    "Head": "Cabeza",
    "Body": "Cuerpo",
    "Feet": "Pies",
    "Accessory": "Accesorio",
    "Jewelry": "Joyería"
}

# Tipos de habilidad
SKILL_TYPES = {
    "Magic": "Magia",
    "Special": "Especial",
    "Ranged": "A Distancia",
    "Monster": "Monstruo",
    "Disease": "Enfermedad"
}

# Tipos de arma
WEAPON_TYPES = {
    "Simple": "Simple",
    "Bludgeon": "Contundente",
    "Slashing": "Cortante",
    "Piercing": "Perforante",
    "Two Handed Weapon": "Arma a Dos Manos"
}

# Términos básicos
TERMS_BASIC = {
    "Level": "Nivel",
    "Lv": "Nv",
    "Health": "Salud",
    "HP": "PV",
    "Stamina": "Aguante",
    "STM": "AG",
    "Ammo": "Munición",
    "EXP": "EXP"
}

# Comandos de menú
TERMS_COMMANDS = {
    "Fight": "Luchar",
    "Escape": "Huir",
    "Attack": "Atacar",
    "Guard": "Defender",
    "Item": "Objeto",
    "Skill": "Habilidad",
    "Equip": "Equipar",
    "Status": "Estado",
    "Formation": "Formación",
    "Save": "Guardar",
    "Game End": "Fin del Juego",
    "Options": "Opciones",
    "Melee": "Cuerpo a Cuerpo",
    "Gear": "Equipo",
    "Key Item": "Objeto Clave",
    "Optimize": "Optimizar",
    "Clear": "Limpiar",
    "New Game": "Nuevo Juego",
    "Continue": "Continuar",
    "To Title": "Al Título",
    "Cancel": "Cancelar",
    "Buy": "Comprar",
    "Sell": "Vender"
}

# Parámetros
TERMS_PARAMS = {
    "Max HP": "PV Máx",
    "Max Stm": "AG Máx",
    "Attack": "Ataque",
    "Defense": "Defensa",
    "Ballistics": "Balística",
    "Bull.Defense": "Def. Balística",
    "Agility": "Agilidad",
    "Luck": "Suerte",
    "Hit": "Precisión",
    "Evasion": "Evasión"
}

# Mensajes del sistema
TERMS_MESSAGES = {
    "Always Dash": "Siempre Correr",
    "Command Remember": "Recordar Comando",
    "Touch UI": "Interfaz Táctil",
    "BGM Volume": "Volumen BGM",
    "BGS Volume": "Volumen BGS",
    "ME Volume": "Volumen ME",
    "SE Volume": "Volumen SE",
    "Possession": "Posesión",
    "Current %1": "%1 Actual",
    "To Next %1": "Para Siguiente %1",
    "Which file would you like to save to?": "¿En qué archivo quieres guardar?",
    "Which file would you like to load?": "¿Qué archivo quieres cargar?",
    "File": "Archivo",
    "Autosave": "Autoguardado",
    "%1's Party": "Grupo de %1",
    "%1 approaches...": "%1 se acerca...",
    "%1 got the upper hand!": "¡%1 tomó la delantera!",
    "%1 was surprised!": "¡%1 fue sorprendido!",
    "%1 has started to escape!": "¡%1 ha comenzado a huir!",
    "However, it was unable to escape!": "¡Sin embargo, no pudo escapar!",
    "%1 was victorious!": "¡%1 fue victorioso!",
    "%1 was defeated.": "%1 fue derrotado.",
    "%1 %2 received!": "¡%1 %2 recibido!",
    "\\G%1 found!": "¡\\G%1 encontrado!",
    "%1 found!": "¡%1 encontrado!",
    "%1 is now %2 %3!": "¡%1 ahora es %2 %3!",
    "%1 learned!": "¡%1 aprendido!",
    "%1 uses %2!": "¡%1 usa %2!",
    "An excellent hit!!": "¡¡Un golpe excelente!!",
    "A painful blow!!": "¡¡Un golpe doloroso!!",
    "%1 took %2 damage!": "¡%1 recibió %2 de daño!",
    "%1 recovered %2 %3!": "¡%1 recuperó %2 %3!",
    "%1 gained %2 %3!": "¡%1 ganó %2 %3!",
    "%1 lost %2 %3!": "¡%1 perdió %2 %3!",
    "%1 was drained of %2 %3!": "¡A %1 le drenaron %2 %3!",
    "%1 took no damage!": "¡%1 no recibió daño!",
    "Miss! %1 took no damage!": "¡Fallo! ¡%1 no recibió daño!",
    "%1 evaded the attack!": "¡%1 evadió el ataque!",
    "%1 avoided the shot!": "¡%1 esquivó el disparo!",
    "%1 deflected the shot!": "¡%1 desvió el disparo!",
    "%1 made a counterattack!": "¡%1 hizo un contraataque!",
    "%1 protected %2!": "¡%1 protegió a %2!",
    "%1's %2 went up!": "¡El %2 de %1 subió!",
    "%1's %2 went down!": "¡El %2 de %1 bajó!",
    "%1's %2 returned to normal!": "¡El %2 de %1 volvió a la normalidad!",
    "There was no effect on %1!": "¡No hubo efecto en %1!"
}

# ============================================================================
# FUNCIÓN PRINCIPAL DE TRADUCCIÓN
# ============================================================================

def translate_system_json(input_file, output_file):
    """
    Traduce System.json del inglés al español
    """
    print("=" * 80)
    print("TRADUCCIÓN DE SYSTEM.JSON - LOOK OUTSIDE")
    print("=" * 80)

    # Leer archivo original
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"\n✓ Archivo leído: {input_file}")

    stats = {
        'armorTypes': 0,
        'elements': 0,
        'equipTypes': 0,
        'skillTypes': 0,
        'weaponTypes': 0,
        'terms_basic': 0,
        'terms_commands': 0,
        'terms_params': 0,
        'terms_messages': 0,
        'total': 0
    }

    # Traducir armorTypes
    if 'armorTypes' in data:
        for i, text in enumerate(data['armorTypes']):
            if text and text in ARMOR_TYPES:
                data['armorTypes'][i] = ARMOR_TYPES[text]
                stats['armorTypes'] += 1
                stats['total'] += 1

    # Traducir elements
    if 'elements' in data:
        for i, text in enumerate(data['elements']):
            if text and text in ELEMENTS:
                data['elements'][i] = ELEMENTS[text]
                stats['elements'] += 1
                stats['total'] += 1

    # Traducir equipTypes
    if 'equipTypes' in data:
        for i, text in enumerate(data['equipTypes']):
            if text and text in EQUIP_TYPES:
                data['equipTypes'][i] = EQUIP_TYPES[text]
                stats['equipTypes'] += 1
                stats['total'] += 1

    # Traducir skillTypes
    if 'skillTypes' in data:
        for i, text in enumerate(data['skillTypes']):
            if text and text in SKILL_TYPES:
                data['skillTypes'][i] = SKILL_TYPES[text]
                stats['skillTypes'] += 1
                stats['total'] += 1

    # Traducir weaponTypes
    if 'weaponTypes' in data:
        for i, text in enumerate(data['weaponTypes']):
            if text and text in WEAPON_TYPES:
                data['weaponTypes'][i] = WEAPON_TYPES[text]
                stats['weaponTypes'] += 1
                stats['total'] += 1

    # Traducir terms
    if 'terms' in data:
        # Basic terms
        if 'basic' in data['terms']:
            for i, text in enumerate(data['terms']['basic']):
                if text and text in TERMS_BASIC:
                    data['terms']['basic'][i] = TERMS_BASIC[text]
                    stats['terms_basic'] += 1
                    stats['total'] += 1

        # Command terms
        if 'commands' in data['terms']:
            for i, text in enumerate(data['terms']['commands']):
                if text and text in TERMS_COMMANDS:
                    data['terms']['commands'][i] = TERMS_COMMANDS[text]
                    stats['terms_commands'] += 1
                    stats['total'] += 1

        # Param terms
        if 'params' in data['terms']:
            for i, text in enumerate(data['terms']['params']):
                if text and text in TERMS_PARAMS:
                    data['terms']['params'][i] = TERMS_PARAMS[text]
                    stats['terms_params'] += 1
                    stats['total'] += 1

        # Message terms
        if 'messages' in data['terms']:
            for key, text in data['terms']['messages'].items():
                if text and text in TERMS_MESSAGES:
                    data['terms']['messages'][key] = TERMS_MESSAGES[text]
                    stats['terms_messages'] += 1
                    stats['total'] += 1

    # Cambiar locale a español (opcional, pero mantendremos en_US por compatibilidad)
    # data['locale'] = 'es_ES'

    # Guardar archivo traducido
    os.makedirs(os.path.dirname(output_file) if os.path.dirname(output_file) else '.', exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"✓ Archivo traducido guardado: {output_file}")

    # Mostrar estadísticas
    print("\n" + "=" * 80)
    print("ESTADÍSTICAS DE TRADUCCIÓN")
    print("=" * 80)
    print(f"  Tipos de Armadura:        {stats['armorTypes']:3d} traducciones")
    print(f"  Elementos:                {stats['elements']:3d} traducciones")
    print(f"  Tipos de Equipo:          {stats['equipTypes']:3d} traducciones")
    print(f"  Tipos de Habilidad:       {stats['skillTypes']:3d} traducciones")
    print(f"  Tipos de Arma:            {stats['weaponTypes']:3d} traducciones")
    print(f"  Términos Básicos:         {stats['terms_basic']:3d} traducciones")
    print(f"  Comandos de Menú:         {stats['terms_commands']:3d} traducciones")
    print(f"  Parámetros:               {stats['terms_params']:3d} traducciones")
    print(f"  Mensajes del Sistema:     {stats['terms_messages']:3d} traducciones")
    print(f"  {'-' * 78}")
    print(f"  TOTAL:                    {stats['total']:3d} traducciones")
    print("=" * 80)

    print("\n✓ Traducción completada exitosamente!")

    return stats

# ============================================================================
# EJECUCIÓN
# ============================================================================

if __name__ == "__main__":
    input_file = "/home/user/data/System.json"
    output_file = "/home/user/data/outputs/System_ES.json"

    try:
        stats = translate_system_json(input_file, output_file)
    except Exception as e:
        print(f"\n✗ Error durante la traducción: {e}")
        import traceback
        traceback.print_exc()
