#!/usr/bin/env python3
import json

# Cargar ambos archivos
with open('Enemies.json', 'r', encoding='utf-8') as f:
    enemies_en = json.load(f)

with open('Enemies_ES.json', 'r', encoding='utf-8') as f:
    enemies_es = json.load(f)

print("="*80)
print("EJEMPLOS DE TRADUCCIONES DE ENEMIES.JSON")
print("="*80)

# Mostrar algunos ejemplos interesantes
ejemplos = [
    ("Rat", "Enemigo básico"),
    ("Rat King", "Enemigo jefe"),
    ("Angel Of Death", "Enemigo especial"),
    ("Tickletest", "Enemigo con advice/lore"),
    ("-- RATS --", "Separador de sección"),
    ("Giant Roach", "Enemigo compuesto"),
    ("Pierre", "Nombre francés"),
    ("Balaclava", "Término traducible"),
    ("Crawling Hand", "Enemigo descriptivo"),
    ("Shadow Fred", "Variante de enemigo"),
]

print("\nEJEMPLOS DE NOMBRES TRADUCIDOS:")
print("-" * 80)

for nombre_en, descripcion in ejemplos:
    # Buscar el enemigo en ambos archivos
    for i, enemy in enumerate(enemies_en):
        if enemy is not None and enemy.get('name') == nombre_en:
            nombre_es = enemies_es[i]['name']
            print(f"\n{descripcion}:")
            print(f"  EN: {nombre_en}")
            print(f"  ES: {nombre_es}")

            # Si tiene advice/lore, mostrarlo
            if enemy.get('note') and ('advice:' in enemy['note'] or 'lore:' in enemy['note']):
                print(f"\n  Note original:")
                print(f"    {enemy['note']}")
                print(f"  Note traducida:")
                print(f"    {enemies_es[i]['note']}")
            break

print("\n" + "="*80)
print("VERIFICACIÓN DE CAMPOS TÉCNICOS NO TRADUCIDOS:")
print("="*80)

# Verificar que los campos técnicos no se hayan traducido
campos_tecnicos_ok = True
for i, enemy in enumerate(enemies_es):
    if enemy is None:
        continue

    if 'note' in enemy and enemy['note']:
        # Verificar que los tags técnicos sigan en inglés
        note = enemy['note']
        if any(tag in note for tag in ['<baseSprite:', '<level:', '<enemyType:', '<moveCloseOb:']):
            # Los tags deben mantenerse en inglés
            if '<baseEsprite:' in note or '<nivel:' in note or '<tipoEnemigo:' in note:
                print(f"❌ ERROR: Tags técnicos traducidos en enemigo {i}")
                campos_tecnicos_ok = False
                break

if campos_tecnicos_ok:
    print("✅ Todos los campos técnicos se mantuvieron sin traducir (correcto)")

print("\n" + "="*80)
