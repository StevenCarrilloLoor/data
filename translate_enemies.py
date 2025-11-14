#!/usr/bin/env python3
import json
import re

# Cargar el diccionario de traducciones
with open('enemies_translation_dict.json', 'r', encoding='utf-8') as f:
    translations = json.load(f)

# Cargar el archivo de enemigos
with open('Enemies.json', 'r', encoding='utf-8') as f:
    enemies = json.load(f)

# Contadores para estadísticas
nombres_traducidos = 0
advice_traducidos = 0
lore_traducidos = 0
total_enemigos = 0

# Función para traducir texto dentro de tags
def translate_tag_content(note, tag, translation_dict):
    count = 0
    # Patrón para encontrar <tag:contenido>
    pattern = rf'<{tag}:([^>]+)>'

    def replacer(match):
        nonlocal count
        original_text = match.group(1)
        if original_text in translation_dict:
            count += 1
            return f'<{tag}:{translation_dict[original_text]}>'
        return match.group(0)  # No cambiar si no está en el diccionario

    translated = re.sub(pattern, replacer, note)
    return translated, count

# Traducir cada enemigo
for enemy in enemies:
    if enemy is None:
        continue

    total_enemigos += 1

    # Traducir nombre
    if 'name' in enemy and enemy['name'] in translations['nombres']:
        enemy['name'] = translations['nombres'][enemy['name']]
        nombres_traducidos += 1

    # Traducir advice y lore en el campo note
    if 'note' in enemy and enemy['note']:
        original_note = enemy['note']

        # Traducir advice
        enemy['note'], advice_count = translate_tag_content(
            enemy['note'], 'advice', translations['advice']
        )
        advice_traducidos += advice_count

        # Traducir lore
        enemy['note'], lore_count = translate_tag_content(
            enemy['note'], 'lore', translations['lore']
        )
        lore_traducidos += lore_count

# Guardar el archivo traducido
output_file = 'Enemies_ES.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(enemies, f, ensure_ascii=False, indent=4)

# Mostrar estadísticas
print("="*80)
print("TRADUCCIÓN COMPLETADA")
print("="*80)
print(f"Total de enemigos procesados: {total_enemigos}")
print(f"Nombres traducidos: {nombres_traducidos}")
print(f"Advice traducidos: {advice_traducidos}")
print(f"Lore traducidos: {lore_traducidos}")
print(f"\nArchivo generado: {output_file}")
print("="*80)
