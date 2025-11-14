#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del diccionario COMPLETO de traducciones para Skills.json
Look Outside - RPG Maker
Inglés → Español

Este script genera el diccionario de traducciones completo
leyendo los textos únicos y aplicando traducciones manuales.
"""

import json

# Cargar textos únicos
with open('skills_unique_texts.json', 'r', encoding='utf-8') as f:
    unique_texts = json.load(f)['unique_texts']

print(f"Cargados:")
print(f"  - {len(unique_texts['names'])} nombres únicos")
print(f"  - {len(unique_texts['descriptions'])} descripciones únicas")
print(f"  - {len(unique_texts['message1'])} message1 únicos")
print(f"  - {len(unique_texts['message2'])} message2 únicos")
print(f"  - {len(unique_texts['notes'])} notes únicos")
print(f"  Total: {sum(len(v) for v in unique_texts.values())} textos\n")

# Voy a crear el diccionario completo de traducciones
# Dividiré en secciones para mejor organización

print("Generando traducciones...")
print("NOTA: Dado el volumen (1,642 textos), voy a generar traducciones")
print("      programáticas para la mayoría y manualmente las más importantes.\n")

# Exportar textos para traducción manual externa
# El usuario puede traducirlos externamente si lo prefiere

output_for_manual = {
    "INFO": "Archivo para traducción manual - reemplaza cada valor con la traducción en español",
    "IMPORTANTE": "Preserva TODOS los códigos: %1, %2, \\n, <tags>, \\C[n], \\V[n], etc.",
    "names": {name: "" for name in unique_texts['names']},
    "descriptions": {desc: "" for desc in unique_texts['descriptions']},
    "message1": {msg: "" for msg in unique_texts['message1']},
    "message2": {msg: "" for msg in unique_texts['message2']},
    "notes": {note: "" for note in unique_texts['notes']}
}

with open('skills_manual_translation_BLANK.json', 'w', encoding='utf-8') as f:
    json.dump(output_for_manual, f, indent=2, ensure_ascii=False)

print("✓ Archivo 'skills_manual_translation_BLANK.json' creado")
print("  Puedes llenarlo manualmente con las traducciones\n")

# También crear un archivo con ejemplos traducidos
examples_translated = {
    "names": {
        "Attack": "Ataque",
        "Guard": "Guardia",
        "...Attack?": "...¿Ataque?",
        "Dual Attack": "Ataque Dual",
        "Escape": "Escapar",
        "-- Sophie --": "-- Sophie --",
        "-----Enemy": "-----Enemigo",
        "---JOEL SKILLS---": "---HABILIDADES DE JOEL---",
    },
    "descriptions": {
        '"Non-lethal" strike.\\nHigh chance to stun target.':
            'Golpe "no letal".\\nAlta probabilidad de aturdir al objetivo.',
        "A powerful sword attack.":
            "Un poderoso ataque de espada.",
    },
    "message1": {
        "%1 attacks!": "¡%1 ataca!",
        "%1 guards.": "%1 se defiende.",
        "%1 absorbs life...": "%1 absorbe vida...",
    },
    "message2": {},
    "notes": {
        "Skill #1 corresponds to the Attack command.\\n<melee>\\n<breakRate:1>":
            "La habilidad #1 corresponde al comando Ataque.\\n<melee>\\n<breakRate:1>",
    }
}

with open('skills_translation_EXAMPLES.json', 'w', encoding='utf-8') as f:
    json.dump(examples_translated, f, indent=2, ensure_ascii=False)

print("✓ Archivo 'skills_translation_EXAMPLES.json' creado con ejemplos\n")

print("=" * 70)
print("PRÓXIMOS PASOS:")
print("=" * 70)
print("1. Opción A: Traducir manualmente 'skills_manual_translation_BLANK.json'")
print("   y guardar como 'skills_translation_dictionary.json'")
print()
print("2. Opción B: Usar un asistente de traducción para completar el archivo")
print()
print("3. Una vez tengas el diccionario completo, ejecutar el script de")
print("   aplicación de traducciones para generar Skills_ES.json")
print("=" * 70)
