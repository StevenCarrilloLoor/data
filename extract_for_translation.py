#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrae textos de Items.json en formato JSON para facilitar traducción
"""

import json

def extract_texts():
    with open('/home/user/data/Items.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    names = {}
    descriptions = {}
    notes_to_translate = {}

    # Notas que SÍ deben traducirse (no son códigos de sistema)
    translatable_notes = [
        "This one contains the sky",
        "correct painting",
        "incorrect painting"
    ]

    for item in data:
        if item is None:
            continue

        # Nombres
        if 'name' in item and item['name']:
            name = item['name']
            if name not in names:
                names[name] = ""  # Placeholder para traducción

        # Descripciones
        if 'description' in item and item['description']:
            desc = item['description']
            if desc not in descriptions:
                descriptions[desc] = ""  # Placeholder para traducción

        # Notas (solo las traducibles)
        if 'note' in item and item['note']:
            note = item['note']
            if note in translatable_notes and note not in notes_to_translate:
                notes_to_translate[note] = ""  # Placeholder para traducción

    # Guardar en formato JSON para facilitar edición
    output = {
        "names": names,
        "descriptions": descriptions,
        "notes": notes_to_translate
    }

    with open('/home/user/data/items_to_translate.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Nombres a traducir: {len(names)}")
    print(f"Descripciones a traducir: {len(descriptions)}")
    print(f"Notas a traducir: {len(notes_to_translate)}")
    print(f"\nArchivo generado: items_to_translate.json")

if __name__ == '__main__':
    extract_texts()
