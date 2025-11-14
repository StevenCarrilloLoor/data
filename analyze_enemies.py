#!/usr/bin/env python3
import json
import re

# Leer el archivo
with open('Enemies.json', 'r', encoding='utf-8') as f:
    enemies = json.load(f)

# Conjuntos para almacenar textos únicos
nombres = set()
advice_texts = set()
lore_texts = set()

# Contador de enemigos
enemy_count = 0

# Analizar cada enemigo
for enemy in enemies:
    if enemy is None:
        continue

    enemy_count += 1

    # Extraer nombre
    if 'name' in enemy and enemy['name']:
        name = enemy['name'].strip()
        if name and name != 'dummyEnemy':
            nombres.add(name)

    # Extraer advice y lore del campo note
    if 'note' in enemy and enemy['note']:
        note = enemy['note']

        # Buscar <advice:...>
        advice_matches = re.findall(r'<advice:([^>]+)>', note)
        for advice in advice_matches:
            advice_texts.add(advice.strip())

        # Buscar <lore:...>
        lore_matches = re.findall(r'<lore:([^>]+)>', note)
        for lore in lore_matches:
            lore_texts.add(lore.strip())

print(f"Total de enemigos: {enemy_count}")
print(f"\nNombres únicos: {len(nombres)}")
print(f"Advice únicos: {len(advice_texts)}")
print(f"Lore únicos: {len(lore_texts)}")

print("\n" + "="*80)
print("NOMBRES DE ENEMIGOS:")
print("="*80)
for name in sorted(nombres):
    print(f'  "{name}"')

if advice_texts:
    print("\n" + "="*80)
    print("ADVICE TEXTS:")
    print("="*80)
    for advice in sorted(advice_texts):
        print(f'  "{advice}"')

if lore_texts:
    print("\n" + "="*80)
    print("LORE TEXTS:")
    print("="*80)
    for lore in sorted(lore_texts):
        print(f'  "{lore}"')
