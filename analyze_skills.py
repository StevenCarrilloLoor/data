#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analiza Skills.json y extrae todos los textos únicos para traducción
"""

import json
from collections import defaultdict

# Leer el archivo
with open('/home/user/data/Skills.json', 'r', encoding='utf-8') as f:
    skills = json.load(f)

# Diccionarios para almacenar textos únicos
unique_texts = {
    'names': set(),
    'descriptions': set(),
    'message1': set(),
    'message2': set(),
    'notes': set()
}

# Estadísticas
stats = {
    'total_skills': 0,
    'non_empty_skills': 0,
    'with_name': 0,
    'with_description': 0,
    'with_message1': 0,
    'with_message2': 0,
    'with_note': 0
}

# Extraer textos
for skill in skills:
    if skill is None:
        continue

    stats['total_skills'] += 1

    # Verificar si tiene contenido
    has_content = False

    if skill.get('name', '').strip():
        unique_texts['names'].add(skill['name'])
        stats['with_name'] += 1
        has_content = True

    if skill.get('description', '').strip():
        unique_texts['descriptions'].add(skill['description'])
        stats['with_description'] += 1
        has_content = True

    if skill.get('message1', '').strip():
        unique_texts['message1'].add(skill['message1'])
        stats['with_message1'] += 1
        has_content = True

    if skill.get('message2', '').strip():
        unique_texts['message2'].add(skill['message2'])
        stats['with_message2'] += 1
        has_content = True

    if skill.get('note', '').strip():
        unique_texts['notes'].add(skill['note'])
        stats['with_note'] += 1
        has_content = True

    if has_content:
        stats['non_empty_skills'] += 1

# Convertir sets a listas ordenadas
for key in unique_texts:
    unique_texts[key] = sorted(list(unique_texts[key]))

# Mostrar estadísticas
print("=" * 80)
print("ESTADÍSTICAS DE SKILLS.JSON")
print("=" * 80)
print(f"Total de skills en el archivo: {stats['total_skills']}")
print(f"Skills con contenido: {stats['non_empty_skills']}")
print(f"Skills con nombre: {stats['with_name']}")
print(f"Skills con descripción: {stats['with_description']}")
print(f"Skills con message1: {stats['with_message1']}")
print(f"Skills con message2: {stats['with_message2']}")
print(f"Skills con note: {stats['with_note']}")
print()
print("TEXTOS ÚNICOS A TRADUCIR:")
print(f"Nombres únicos: {len(unique_texts['names'])}")
print(f"Descripciones únicas: {len(unique_texts['descriptions'])}")
print(f"Message1 únicos: {len(unique_texts['message1'])}")
print(f"Message2 únicos: {len(unique_texts['message2'])}")
print(f"Notes únicos: {len(unique_texts['notes'])}")
print()

# Guardar textos únicos en archivo JSON para revisión
output = {
    'statistics': stats,
    'unique_texts': {
        'names': unique_texts['names'],
        'descriptions': unique_texts['descriptions'],
        'message1': unique_texts['message1'],
        'message2': unique_texts['message2'],
        'notes': unique_texts['notes']
    }
}

with open('/home/user/data/skills_unique_texts.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print("Textos únicos guardados en: skills_unique_texts.json")
print()

# Mostrar algunos ejemplos
print("=" * 80)
print("EJEMPLOS DE NOMBRES (primeros 20):")
print("=" * 80)
for i, name in enumerate(unique_texts['names'][:20], 1):
    print(f"{i}. {name}")

print()
print("=" * 80)
print("EJEMPLOS DE DESCRIPCIONES (primeras 10):")
print("=" * 80)
for i, desc in enumerate(unique_texts['descriptions'][:10], 1):
    print(f"{i}. {desc[:100]}..." if len(desc) > 100 else f"{i}. {desc}")

print()
print("=" * 80)
print("EJEMPLOS DE MESSAGE1 (primeros 15):")
print("=" * 80)
for i, msg in enumerate(unique_texts['message1'][:15], 1):
    print(f"{i}. {msg}")
