#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para traducir Items.json del juego Look Outside de inglés a español
Aplica todas las traducciones del diccionario items_translation_dict.py
"""

import json
import sys

# Importar diccionarios de traducción
from items_translation_dict import NAMES, DESCRIPTIONS, NOTES
from items_translation_dict_additional import NAMES_ADDITIONAL, DESCRIPTIONS_ADDITIONAL

# Combinar diccionarios (los adicionales sobrescriben si hay duplicados)
ALL_NAMES = {**NAMES, **NAMES_ADDITIONAL}
ALL_DESCRIPTIONS = {**DESCRIPTIONS, **DESCRIPTIONS_ADDITIONAL}

def translate_items(input_file, output_file):
    """
    Traduce Items.json usando los diccionarios de traducción
    """
    print("=" * 80)
    print("TRADUCCIÓN DE ITEMS.JSON - Look Outside")
    print("Inglés → Español")
    print("=" * 80)

    # Leer archivo original
    print(f"\n📖 Leyendo: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Contadores
    total_items = 0
    names_translated = 0
    descriptions_translated = 0
    notes_translated = 0
    names_not_found = []
    descriptions_not_found = []

    # Traducir cada item
    print("\n🔄 Traduciendo items...")
    for item in data:
        if item is None:
            continue

        total_items += 1

        # Traducir nombre
        if 'name' in item and item['name']:
            original_name = item['name']
            if original_name in ALL_NAMES:
                item['name'] = ALL_NAMES[original_name]
                names_translated += 1
            else:
                if original_name.strip():  # Solo reportar si no está vacío
                    names_not_found.append(original_name)

        # Traducir descripción
        if 'description' in item and item['description']:
            original_desc = item['description']
            if original_desc in ALL_DESCRIPTIONS:
                item['description'] = ALL_DESCRIPTIONS[original_desc]
                descriptions_translated += 1
            else:
                if original_desc.strip():  # Solo reportar si no está vacío
                    descriptions_not_found.append(original_desc)

        # Traducir notas (solo las que están en el diccionario)
        if 'note' in item and item['note']:
            original_note = item['note']
            if original_note in NOTES:
                item['note'] = NOTES[original_note]
                notes_translated += 1

    # Guardar archivo traducido
    print(f"\n💾 Guardando: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # Reporte final
    print("\n" + "=" * 80)
    print("REPORTE DE TRADUCCIÓN")
    print("=" * 80)
    print(f"\n📊 Estadísticas:")
    print(f"  Total de items procesados: {total_items}")
    print(f"  Nombres traducidos: {names_translated}")
    print(f"  Descripciones traducidas: {descriptions_translated}")
    print(f"  Notas traducidas: {notes_translated}")
    print(f"  TOTAL TRADUCCIONES: {names_translated + descriptions_translated + notes_translated}")

    # Advertencias
    if names_not_found:
        print(f"\n⚠️  Nombres sin traducción encontrada: {len(set(names_not_found))}")
        unique_names = sorted(set(names_not_found))[:10]
        for name in unique_names:
            print(f"    - {name}")
        if len(set(names_not_found)) > 10:
            print(f"    ... y {len(set(names_not_found)) - 10} más")

    if descriptions_not_found:
        print(f"\n⚠️  Descripciones sin traducción encontrada: {len(set(descriptions_not_found))}")
        unique_descs = sorted(set(descriptions_not_found))[:5]
        for desc in unique_descs:
            preview = desc[:80] + "..." if len(desc) > 80 else desc
            print(f"    - {preview}")
        if len(set(descriptions_not_found)) > 5:
            print(f"    ... y {len(set(descriptions_not_found)) - 5} más")

    # Éxito
    if not names_not_found and not descriptions_not_found:
        print("\n✅ ¡TRADUCCIÓN COMPLETADA AL 100%!")
    else:
        completion = ((names_translated + descriptions_translated) /
                     (names_translated + descriptions_translated +
                      len(set(names_not_found)) + len(set(descriptions_not_found)))) * 100
        print(f"\n✅ Traducción completada al {completion:.1f}%")

    print("\n" + "=" * 80)
    print(f"✅ Archivo generado: {output_file}")
    print("=" * 80)

    return {
        'total_items': total_items,
        'names_translated': names_translated,
        'descriptions_translated': descriptions_translated,
        'notes_translated': notes_translated,
        'names_not_found': len(set(names_not_found)),
        'descriptions_not_found': len(set(descriptions_not_found))
    }

if __name__ == '__main__':
    input_file = '/home/user/data/Items.json'
    output_file = '/home/user/data/Items_ES.json'

    try:
        stats = translate_items(input_file, output_file)
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
