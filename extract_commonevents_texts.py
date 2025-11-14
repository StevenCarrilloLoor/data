#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para extraer todos los textos traducibles de CommonEvents.json
"""

import json
import os

def extract_texts_from_commonevents(json_path):
    """Extrae todos los textos traducibles del archivo CommonEvents.json"""

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    texts = {
        'names': set(),
        'dialogues': set(),
        'choices': set(),
        'other_texts': set()
    }

    stats = {
        'total_events': 0,
        'events_with_names': 0,
        'code_401_count': 0,
        'code_102_count': 0,
        'other_codes_with_text': 0
    }

    # Códigos de RPG Maker que pueden contener texto
    text_codes = {
        401: 'dialogues',      # Mostrar texto (diálogos)
        102: 'choices',        # Opciones de elección
        356: 'other_texts',    # Nombre del sistema
        117: 'other_texts',    # Llamar evento común
        118: 'other_texts',    # Etiquetar
        408: 'other_texts',    # Comentarios
    }

    for event in data:
        if event is None:
            continue

        stats['total_events'] += 1

        # Extraer nombre del evento
        if 'name' in event and event['name'] and event['name'].strip():
            texts['names'].add(event['name'])
            stats['events_with_names'] += 1

        # Extraer textos de la lista de comandos
        if 'list' in event:
            for command in event['list']:
                code = command.get('code', 0)
                parameters = command.get('parameters', [])

                # Code 401: Diálogos (texto en parameters[0])
                if code == 401 and len(parameters) > 0:
                    text = parameters[0]
                    if isinstance(text, str) and text.strip():
                        texts['dialogues'].add(text)
                        stats['code_401_count'] += 1

                # Code 102: Opciones de elección (array de strings en parameters[0])
                elif code == 102 and len(parameters) > 0:
                    choices_array = parameters[0]
                    if isinstance(choices_array, list):
                        for choice in choices_array:
                            if isinstance(choice, str) and choice.strip():
                                texts['choices'].add(choice)
                                stats['code_102_count'] += 1

                # Code 356: Sistema de nombre
                elif code == 356 and len(parameters) > 0:
                    text = parameters[0]
                    if isinstance(text, str) and text.strip():
                        texts['other_texts'].add(text)
                        stats['other_codes_with_text'] += 1

                # Code 408: Comentarios (pueden ser importantes)
                elif code == 408 and len(parameters) > 0:
                    text = parameters[0]
                    if isinstance(text, str) and text.strip():
                        # Solo agregar comentarios que parezcan relevantes
                        if not text.startswith('//') and not text.startswith('#'):
                            texts['other_texts'].add(text)
                            stats['other_codes_with_text'] += 1

    # Convertir sets a listas ordenadas
    for key in texts:
        texts[key] = sorted(list(texts[key]))

    return texts, stats

def main():
    json_path = '/home/user/data/CommonEvents.json'

    print("🔍 Analizando CommonEvents.json...")
    print("=" * 70)

    texts, stats = extract_texts_from_commonevents(json_path)

    print("\n📊 ESTADÍSTICAS:")
    print(f"  Total de eventos: {stats['total_events']}")
    print(f"  Eventos con nombre: {stats['events_with_names']}")
    print(f"  Diálogos (code 401): {stats['code_401_count']}")
    print(f"  Opciones (code 102): {stats['code_102_count']}")
    print(f"  Otros textos: {stats['other_codes_with_text']}")

    print("\n📝 TEXTOS ÚNICOS EXTRAÍDOS:")
    print(f"  Nombres de eventos: {len(texts['names'])}")
    print(f"  Diálogos únicos: {len(texts['dialogues'])}")
    print(f"  Opciones únicas: {len(texts['choices'])}")
    print(f"  Otros textos únicos: {len(texts['other_texts'])}")

    total_unique = sum(len(texts[k]) for k in texts)
    print(f"\n  ✅ TOTAL TEXTOS ÚNICOS: {total_unique}")

    # Guardar en archivo JSON para revisión
    output_path = '/home/user/data/commonevents_extracted_texts.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(texts, f, ensure_ascii=False, indent=2)

    print(f"\n💾 Textos extraídos guardados en: {output_path}")

    # Mostrar algunos ejemplos
    print("\n" + "=" * 70)
    print("📋 EJEMPLOS DE TEXTOS ENCONTRADOS:")
    print("=" * 70)

    if texts['names']:
        print("\n🏷️  NOMBRES DE EVENTOS (primeros 10):")
        for name in texts['names'][:10]:
            print(f"  - {name}")

    if texts['dialogues']:
        print("\n💬 DIÁLOGOS (primeros 15):")
        for dialogue in texts['dialogues'][:15]:
            # Truncar diálogos muy largos
            display = dialogue if len(dialogue) <= 80 else dialogue[:77] + "..."
            print(f"  - {display}")

    if texts['choices']:
        print("\n🔘 OPCIONES (primeras 10):")
        for choice in texts['choices'][:10]:
            print(f"  - {choice}")

    print("\n" + "=" * 70)

if __name__ == '__main__':
    main()
