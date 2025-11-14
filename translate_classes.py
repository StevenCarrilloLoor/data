#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para traducir Classes.json de Look Outside RPG Maker al español
Traduce solo los campos 'name' de las clases, preservando todos los códigos de juego
"""

import json
import sys

def load_translation_dict():
    """Carga el diccionario de traducción"""
    with open('classes_translation_dict.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def translate_classes(classes_data, translation_dict):
    """
    Traduce los nombres de las clases recursivamente

    Args:
        classes_data: Lista de clases del JSON
        translation_dict: Diccionario con traducciones

    Returns:
        Lista de clases traducida
    """
    nombres = translation_dict['nombres']

    stats = {
        'total_classes': 0,
        'translated': 0,
        'empty': 0,
        'not_found': 0
    }

    for i, class_obj in enumerate(classes_data):
        if class_obj is None:
            continue

        stats['total_classes'] += 1

        # Traducir el nombre de la clase
        if 'name' in class_obj:
            original_name = class_obj['name']

            if original_name == '':
                stats['empty'] += 1
            elif original_name in nombres:
                class_obj['name'] = nombres[original_name]
                stats['translated'] += 1
                print(f"✓ Clase {i}: '{original_name}' → '{class_obj['name']}'")
            else:
                stats['not_found'] += 1
                print(f"⚠ Clase {i}: '{original_name}' NO ENCONTRADO en diccionario")

        # Los campos 'note' NO se traducen porque contienen códigos de juego
        # como <GuardSkill:133>, <noHeavyWpn>, etc.

    return classes_data, stats

def main():
    print("=" * 70)
    print("TRADUCIENDO CLASSES.JSON AL ESPAÑOL")
    print("=" * 70)
    print()

    # Cargar diccionario de traducción
    print("Cargando diccionario de traducción...")
    translation_dict = load_translation_dict()
    print(f"✓ {len(translation_dict['nombres'])} traducciones cargadas\n")

    # Cargar Classes.json
    print("Cargando Classes.json...")
    with open('Classes.json', 'r', encoding='utf-8') as f:
        classes_data = json.load(f)
    print(f"✓ {len(classes_data)} entradas cargadas\n")

    # Traducir
    print("Traduciendo clases...\n")
    translated_data, stats = translate_classes(classes_data, translation_dict)

    # Guardar resultado
    output_path = 'Classes_ES.json'
    print(f"\nGuardando {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=4)
    print(f"✓ Archivo guardado: {output_path}\n")

    # Estadísticas
    print("=" * 70)
    print("ESTADÍSTICAS DE TRADUCCIÓN")
    print("=" * 70)
    print(f"Total de clases procesadas: {stats['total_classes']}")
    print(f"Nombres traducidos:         {stats['translated']}")
    print(f"Nombres vacíos:             {stats['empty']}")
    print(f"No encontrados:             {stats['not_found']}")
    print(f"\nCompletitud: {stats['translated']}/{stats['total_classes'] - stats['empty']} " +
          f"({100 * stats['translated'] / max(1, stats['total_classes'] - stats['empty']):.1f}%)")
    print("=" * 70)

    if stats['not_found'] > 0:
        print("\n⚠ ADVERTENCIA: Algunos nombres no se encontraron en el diccionario")
        print("   Revisa la salida anterior para ver cuáles faltan")
        return 1

    print("\n✅ TRADUCCIÓN COMPLETADA EXITOSAMENTE")
    return 0

if __name__ == '__main__':
    sys.exit(main())
