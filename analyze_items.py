#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para analizar Items.json y extraer todos los textos traducibles
"""

import json
import re
from collections import defaultdict

def extract_translatable_texts(json_file):
    """Extrae todos los textos traducibles del archivo Items.json"""

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Diccionarios para almacenar textos únicos
    names = set()
    descriptions = set()
    notes = set()

    # Contadores
    total_items = 0
    items_with_name = 0
    items_with_description = 0
    items_with_note = 0

    for item in data:
        if item is None:
            continue

        total_items += 1

        # Extraer nombres
        if 'name' in item and item['name']:
            names.add(item['name'])
            items_with_name += 1

        # Extraer descripciones
        if 'description' in item and item['description']:
            descriptions.add(item['description'])
            items_with_description += 1

        # Extraer notas
        if 'note' in item and item['note']:
            notes.add(item['note'])
            items_with_note += 1

    # Generar reporte
    print("=" * 80)
    print("ANÁLISIS DE Items.json")
    print("=" * 80)
    print(f"\nTotal de items (excluyendo null): {total_items}")
    print(f"Items con nombre: {items_with_name}")
    print(f"Items con descripción: {items_with_description}")
    print(f"Items con nota: {items_with_note}")
    print(f"\nTextos únicos encontrados:")
    print(f"  - Nombres únicos: {len(names)}")
    print(f"  - Descripciones únicas: {len(descriptions)}")
    print(f"  - Notas únicas: {len(notes)}")

    # Mostrar ejemplos
    print("\n" + "=" * 80)
    print("EJEMPLOS DE NOMBRES (primeros 20):")
    print("=" * 80)
    for i, name in enumerate(sorted(names)[:20], 1):
        print(f"{i:3d}. {name}")

    print("\n" + "=" * 80)
    print("EJEMPLOS DE DESCRIPCIONES (primeras 10):")
    print("=" * 80)
    for i, desc in enumerate(sorted(descriptions)[:10], 1):
        print(f"{i:3d}. {desc[:100]}{'...' if len(desc) > 100 else ''}")

    print("\n" + "=" * 80)
    print("NOTAS ÚNICAS:")
    print("=" * 80)
    for i, note in enumerate(sorted(notes), 1):
        print(f"{i:3d}. {note[:100]}{'...' if len(note) > 100 else ''}")

    # Guardar textos en archivos para referencia
    with open('/home/user/data/items_names.txt', 'w', encoding='utf-8') as f:
        for name in sorted(names):
            f.write(f"{name}\n")

    with open('/home/user/data/items_descriptions.txt', 'w', encoding='utf-8') as f:
        for desc in sorted(descriptions):
            f.write(f"{desc}\n---\n")

    with open('/home/user/data/items_notes.txt', 'w', encoding='utf-8') as f:
        for note in sorted(notes):
            f.write(f"{note}\n---\n")

    print("\n" + "=" * 80)
    print("Archivos generados:")
    print("  - items_names.txt")
    print("  - items_descriptions.txt")
    print("  - items_notes.txt")
    print("=" * 80)

    return {
        'names': sorted(names),
        'descriptions': sorted(descriptions),
        'notes': sorted(notes)
    }

if __name__ == '__main__':
    extract_translatable_texts('/home/user/data/Items.json')
