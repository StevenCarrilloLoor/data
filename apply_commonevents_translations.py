#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para aplicar traducciones a CommonEvents.json y generar CommonEvents_ES.json
"""

import json
import os

def load_translation_dict():
    """Carga el diccionario de traducción completo"""
    dict_path = '/home/user/data/commonevents_translations_complete.json'

    print("📖 Cargando diccionario de traducciones...")
    with open(dict_path, 'r', encoding='utf-8') as f:
        trans_dict = json.load(f)

    print(f"   ✅ {len(trans_dict)} traducciones cargadas")
    return trans_dict

def apply_translations(json_path, translation_dict):
    """Aplica las traducciones al archivo CommonEvents.json"""

    print("\n🔄 Leyendo CommonEvents.json original...")
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("   ✅ Archivo cargado")

    stats = {
        'events_processed': 0,
        'names_translated': 0,
        'dialogues_translated': 0,
        'choices_translated': 0,
        'other_texts_translated': 0,
        'texts_not_found': 0
    }

    not_found_texts = set()

    print("\n🌍 Aplicando traducciones...")

    for event in data:
        if event is None:
            continue

        stats['events_processed'] += 1

        # Traducir nombre del evento
        if 'name' in event and event['name']:
            original_name = event['name']
            if original_name in translation_dict:
                event['name'] = translation_dict[original_name]
                stats['names_translated'] += 1
            elif original_name.strip():  # Si no está vacío
                not_found_texts.add(f"NAME: {original_name}")
                stats['texts_not_found'] += 1

        # Traducir comandos en la lista
        if 'list' in event:
            for command in event['list']:
                code = command.get('code', 0)
                parameters = command.get('parameters', [])

                # Code 401: Diálogos
                if code == 401 and len(parameters) > 0:
                    original_text = parameters[0]
                    if isinstance(original_text, str) and original_text in translation_dict:
                        command['parameters'][0] = translation_dict[original_text]
                        stats['dialogues_translated'] += 1
                    elif isinstance(original_text, str) and original_text.strip():
                        not_found_texts.add(f"DIALOGUE: {original_text[:80]}")
                        stats['texts_not_found'] += 1

                # Code 102: Opciones de elección
                elif code == 102 and len(parameters) > 0:
                    choices_array = parameters[0]
                    if isinstance(choices_array, list):
                        for i, choice in enumerate(choices_array):
                            if isinstance(choice, str) and choice in translation_dict:
                                command['parameters'][0][i] = translation_dict[choice]
                                stats['choices_translated'] += 1
                            elif isinstance(choice, str) and choice.strip():
                                not_found_texts.add(f"CHOICE: {choice}")
                                stats['texts_not_found'] += 1

                # Code 356: Sistema de nombre
                elif code == 356 and len(parameters) > 0:
                    original_text = parameters[0]
                    if isinstance(original_text, str) and original_text in translation_dict:
                        command['parameters'][0] = translation_dict[original_text]
                        stats['other_texts_translated'] += 1
                    elif isinstance(original_text, str) and original_text.strip():
                        not_found_texts.add(f"OTHER: {original_text}")
                        stats['texts_not_found'] += 1

                # Code 408: Comentarios
                elif code == 408 and len(parameters) > 0:
                    original_text = parameters[0]
                    if isinstance(original_text, str) and original_text in translation_dict:
                        command['parameters'][0] = translation_dict[original_text]
                        stats['other_texts_translated'] += 1
                    # Comentarios no encontrados no los contamos como error

    return data, stats, not_found_texts

def save_translated_json(data, output_path):
    """Guarda el JSON traducido"""

    print(f"\n💾 Guardando archivo traducido...")

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # Obtener tamaño del archivo
    file_size = os.path.getsize(output_path)
    file_size_mb = file_size / (1024 * 1024)

    print(f"   ✅ Archivo guardado: {output_path}")
    print(f"   📊 Tamaño: {file_size_mb:.2f} MB")

def print_statistics(stats, not_found_texts):
    """Imprime estadísticas de traducción"""

    print("\n" + "=" * 70)
    print("📊 ESTADÍSTICAS DE TRADUCCIÓN")
    print("=" * 70)

    print(f"\n✅ TRADUCCIONES APLICADAS:")
    print(f"   Eventos procesados: {stats['events_processed']}")
    print(f"   Nombres traducidos: {stats['names_translated']}")
    print(f"   Diálogos traducidos: {stats['dialogues_translated']}")
    print(f"   Opciones traducidas: {stats['choices_translated']}")
    print(f"   Otros textos traducidos: {stats['other_texts_translated']}")

    total_translated = (stats['names_translated'] +
                       stats['dialogues_translated'] +
                       stats['choices_translated'] +
                       stats['other_texts_translated'])

    print(f"\n   🎯 TOTAL TRADUCCIONES: {total_translated}")

    if stats['texts_not_found'] > 0:
        print(f"\n⚠️  TEXTOS NO ENCONTRADOS: {stats['texts_not_found']}")
        print(f"   (posiblemente vacíos o ya traducidos)")

        if len(not_found_texts) > 0 and len(not_found_texts) <= 20:
            print("\n   Ejemplos de textos no encontrados:")
            for text in list(not_found_texts)[:20]:
                print(f"   - {text}")

    print("\n" + "=" * 70)

def main():
    # Rutas
    input_path = '/home/user/data/CommonEvents.json'
    output_path = '/home/user/data/CommonEvents_ES.json'

    print("🌍 TRADUCCIÓN DE COMMONEVENTS.JSON AL ESPAÑOL")
    print("=" * 70)

    # Cargar diccionario
    translation_dict = load_translation_dict()

    # Aplicar traducciones
    translated_data, stats, not_found = apply_translations(input_path, translation_dict)

    # Guardar archivo traducido
    save_translated_json(translated_data, output_path)

    # Mostrar estadísticas
    print_statistics(stats, not_found)

    print("\n✅ TRADUCCIÓN COMPLETADA")
    print(f"📁 Archivo generado: {output_path}")
    print("=" * 70)

if __name__ == '__main__':
    main()
