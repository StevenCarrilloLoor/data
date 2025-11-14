#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Encuentra los textos que faltan en el diccionario de traducción
"""

import json
from items_translation_dict import NAMES, DESCRIPTIONS, NOTES
from items_translation_dict_additional import NAMES_ADDITIONAL, DESCRIPTIONS_ADDITIONAL

# Combinar diccionarios
ALL_NAMES = {**NAMES, **NAMES_ADDITIONAL}
ALL_DESCRIPTIONS = {**DESCRIPTIONS, **DESCRIPTIONS_ADDITIONAL}

def find_missing_texts():
    with open('/home/user/data/Items.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    missing_names = set()
    missing_descriptions = set()

    for item in data:
        if item is None:
            continue

        # Nombres faltantes
        if 'name' in item and item['name']:
            name = item['name']
            if name not in ALL_NAMES and name.strip():
                missing_names.add(name)

        # Descripciones faltantes
        if 'description' in item and item['description']:
            desc = item['description']
            if desc not in ALL_DESCRIPTIONS and desc.strip():
                missing_descriptions.add(desc)

    # Guardar en archivos
    with open('/home/user/data/missing_names.txt', 'w', encoding='utf-8') as f:
        for name in sorted(missing_names):
            f.write(f"{name}\n")

    with open('/home/user/data/missing_descriptions.txt', 'w', encoding='utf-8') as f:
        for desc in sorted(missing_descriptions):
            f.write(f"{desc}\n---\n")

    print(f"Nombres faltantes: {len(missing_names)}")
    print(f"Descripciones faltantes: {len(missing_descriptions)}")
    print("\nPrimeros 20 nombres faltantes:")
    for i, name in enumerate(sorted(missing_names)[:20], 1):
        print(f"{i:3d}. {name}")

if __name__ == '__main__':
    find_missing_texts()
