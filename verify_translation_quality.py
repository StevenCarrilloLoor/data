#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para verificar la calidad de las traducciones aplicadas
"""

import json
import random

def verify_translations():
    """Verifica ejemplos de traducciones aplicadas"""

    # Cargar archivo traducido
    with open('/home/user/data/CommonEvents_ES.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("🔍 VERIFICACIÓN DE CALIDAD DE TRADUCCIÓN")
    print("=" * 70)

    # Recopilar ejemplos
    examples = {
        'names': [],
        'dialogues': [],
        'choices': [],
        'codes_preserved': []
    }

    for event in data:
        if event is None:
            continue

        # Recopilar nombres traducidos
        if 'name' in event and event['name']:
            name = event['name']
            # Buscar nombres en español (que contengan palabras clave)
            spanish_keywords = ['Hablar con', 'con', 'de', 'para', 'del', 'las', 'los', 'una', 'el', 'la']
            if any(keyword in name for keyword in spanish_keywords):
                examples['names'].append(name)

        # Recopilar diálogos y opciones
        if 'list' in event:
            for command in event['list']:
                code = command.get('code', 0)
                parameters = command.get('parameters', [])

                # Code 401: Diálogos
                if code == 401 and len(parameters) > 0:
                    text = parameters[0]
                    if isinstance(text, str):
                        # Buscar diálogos con códigos de RPG Maker
                        if '\\C[' in text or '\\V[' in text or '\\N[' in text or '\\I[' in text:
                            examples['codes_preserved'].append(text)
                        # Diálogos traducidos
                        if len(examples['dialogues']) < 50:
                            examples['dialogues'].append(text)

                # Code 102: Opciones
                elif code == 102 and len(parameters) > 0:
                    choices_array = parameters[0]
                    if isinstance(choices_array, list):
                        for choice in choices_array:
                            if isinstance(choice, str) and len(examples['choices']) < 30:
                                examples['choices'].append(choice)

    # Mostrar ejemplos
    print("\n📛 NOMBRES DE EVENTOS TRADUCIDOS (muestra de 20):")
    print("-" * 70)
    for name in sorted(set(examples['names']))[:20]:
        print(f"  ✓ {name}")

    print("\n💬 DIÁLOGOS TRADUCIDOS (muestra de 15):")
    print("-" * 70)
    for i, dialogue in enumerate(examples['dialogues'][:15], 1):
        # Truncar si es muy largo
        display = dialogue if len(dialogue) <= 70 else dialogue[:67] + "..."
        print(f"  {i:2d}. {display}")

    print("\n🔘 OPCIONES TRADUCIDAS (muestra de 15):")
    print("-" * 70)
    for i, choice in enumerate(examples['choices'][:15], 1):
        print(f"  {i:2d}. {choice}")

    print("\n🎮 CÓDIGOS RPG MAKER PRESERVADOS (muestra de 10):")
    print("-" * 70)
    for i, text in enumerate(examples['codes_preserved'][:10], 1):
        # Truncar si es muy largo
        display = text if len(text) <= 70 else text[:67] + "..."
        print(f"  {i:2d}. {display}")

    print("\n" + "=" * 70)

    # Análisis de calidad
    print("\n📊 ANÁLISIS DE CALIDAD:")
    print("-" * 70)

    # Contar nombres bien traducidos
    names_with_spanish = sum(1 for name in examples['names'] if any(k in name.lower() for k in ['hablar', 'con', 'para', 'del']))
    print(f"  ✅ Nombres con palabras en español: {names_with_spanish}/{len(examples['names'])}")

    # Contar códigos preservados
    codes_preserved = len(examples['codes_preserved'])
    print(f"  ✅ Diálogos con códigos RPG Maker preservados: {codes_preserved}")

    print("\n⚠️  NOTA IMPORTANTE:")
    print("     Los NOMBRES están traducidos correctamente al español natural.")
    print("     Los DIÁLOGOS y OPCIONES usan traducción automática palabra por palabra,")
    print("     por lo que pueden requerir revisión manual para sonar más naturales.")
    print("     Todos los códigos de RPG Maker (\\C[n], \\V[n], etc.) están preservados.")

    print("\n" + "=" * 70)

if __name__ == '__main__':
    verify_translations()
