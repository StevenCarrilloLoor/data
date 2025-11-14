#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRADUCTOR COMPLETO DE STATES.JSON
Look Outside - RPG Maker MV
Inglés → Español

Estados del juego: Bleeding, Poison, Stun, etc.
"""

import json
import copy

print("="*80)
print("TRADUCTOR DE STATES.JSON - Look Outside")
print("="*80)
print()

# ============================================================================
# DICCIONARIO COMPLETO DE TRADUCCIONES
# ============================================================================

# NOMBRES DE ESTADOS
STATE_NAMES = {
    # Estados básicos del sistema
    "Unconscious": "Inconsciente",
    "Guard": "Guardia",
    "Immortal": "Inmortal",

    # Estados de combate principales
    "Poison": "Envenenamiento",
    "Blind": "Ceguera",
    "Silence": "Silencio",
    "Confusion": "Confusión",
    "Sleep": "Sueño",
    "Paralysis": "Parálisis",
    "Stun": "Aturdimiento",
    "Charm": "Encanto",
    "Rage": "Furia",
    "Panic": "Pánico",

    # Sangrado (niveles)
    "Bleed1": "Sangrado 1",
    "Bleed2": "Sangrado 2",
    "Bleed3": "Sangrado 3",
    "Bleeding": "Sangrando",

    # Estados de ácido
    "Acid": "Ácido",
    "Acid Burn": "Quemadura Ácida",

    # Estados elementales
    "Burn": "Quemadura",
    "Burning": "Ardiendo",
    "Freeze": "Congelado",
    "Frozen": "Congelado",
    "Shock": "Descarga",
    "Electrified": "Electrificado",

    # Buffs y Debuffs
    "Bless": "Bendición",
    "Curse": "Maldición",
    "Strength Up": "Fuerza Aumentada",
    "Strength Down": "Fuerza Reducida",
    "Defense Up": "Defensa Aumentada",
    "Defense Down": "Defensa Reducida",
    "Agility Up": "Agilidad Aumentada",
    "Agility Down": "Agilidad Reducida",
    "Ballistics Up": "Balística Aumentada",
    "Ballistics Down": "Balística Reducida",
    "Evasion Up": "Evasión Aumentada",
    "Evasion Down": "Evasión Reducida",

    # Estados especiales del juego
    "Guilt": "Culpa",
    "Brain": "Cerebro",
    "Bloodlust": "Sed de Sangre",
    "Bloodlust X": "Sed de Sangre X",
    "Blood Madness": "Locura Sanguinaria",
    "Beastmode": "Modo Bestia",
    "Biting Armor": "Armadura Mordiente",
    "Boils": "Forúnculos",
    "Assimilate": "Asimilar",
    "Attracted Attention": "Atención Atraída",
    "Bad Dan": "Dan Malo",
    "Anti-blind": "Anti-ceguera",
    "Already Appointed": "Ya Designado",
    "AdBreak": "Pausa Publicitaria",
    "AltPose": "Pose Alternativa",

    # Estados de regeneración/degeneración
    "Regen": "Regeneración",
    "Poison Regen": "Regeneración de Veneno",
    "HP Regen": "Regeneración de PV",
    "STM Regen": "Regeneración de EST",
    "HP Drain": "Drenaje de PV",
    "STM Drain": "Drenaje de EST",

    # Estados de protección
    "Barrier": "Barrera",
    "Shield": "Escudo",
    "Reflect": "Reflejo",
    "Absorb": "Absorber",

    # Estados de movimiento
    "Stalked": "Acechado",
    "Marked": "Marcado",
    "Hunted": "Cazado",
    "Tracked": "Rastreado",

    # Estados de enfermedad
    "Sick": "Enfermo",
    "Disease": "Enfermedad",
    "Infected": "Infectado",
    "Plague": "Plaga",
    "Fever": "Fiebre",

    # Estados mentales
    "Fear": "Miedo",
    "Terror": "Terror",
    "Madness": "Locura",
    "Insanity": "Demencia",
    "Trance": "Trance",
    "Hypnosis": "Hipnosis",
    "Mind Control": "Control Mental",

    # Estados de combate avanzados
    "Counter": "Contraataque",
    "Reflect": "Reflejo",
    "Evade": "Evadir",
    "Provoke": "Provocar",
    "Taunt": "Burla",

    # Estados de tiempo
    "Haste": "Prisa",
    "Slow": "Lento",
    "Stop": "Parar",
    "Quick": "Rápido",

    # Estados específicos del juego
    "Dungeon Dance": "Danza de Mazmorra",
    "Digestion": "Digestión",
    "Consumed": "Consumido",
    "Devoured": "Devorado",
    "Absorbed": "Absorbido",

    # Estados de armas
    "Disarmed": "Desarmado",
    "Weapon Break": "Arma Rota",
    "Armor Break": "Armadura Rota",

    # Estados de visibilidad
    "Invisible": "Invisible",
    "Hidden": "Oculto",
    "Stealth": "Sigilo",
    "Exposed": "Expuesto",

    # Estados de resistencia
    "Resistant": "Resistente",
    "Vulnerable": "Vulnerable",
    "Immune": "Inmune",
    "Weak": "Débil",

    # Estados varios
    "Drunk": "Ebrio",
    "Nausea": "Náusea",
    "Dizzy": "Mareado",
    "Exhausted": "Exhausto",
    "Tired": "Cansado",
    "Energized": "Energizado",
    "Focused": "Concentrado",
    "Distracted": "Distraído",

    # Estados de transformación
    "Transform": "Transformación",
    "Morphed": "Transformado",
    "Shapeshifted": "Cambio de Forma",

    # Estados de invocación
    "Summoned": "Invocado",
    "Banished": "Desterrado",
    "Sealed": "Sellado",

    # Estados de muerte
    "Doomed": "Condenado",
    "Death Sentence": "Sentencia de Muerte",
    "Zombie": "Zombi",
    "Undead": "No-muerto",

    # Estados de elemento
    "Wet": "Mojado",
    "Oiled": "Aceitado",
    "Dried": "Seco",

    # Estados de combate especial
    "Berserk": "Furia Salvaje",
    "Defend": "Defender",
    "Charge": "Cargar",
    "Prepare": "Preparar",
}

# MENSAJES DE ESTADO
# Patrón de reemplazos para mensajes
MESSAGE_PATTERNS = {
    # Verbos comunes
    "falls asleep": "se duerme",
    "wakes up": "se despierta",
    "is poisoned": "está envenenado",
    "is no longer poisoned": "ya no está envenenado",
    "is confused": "está confundido",
    "is no longer confused": "ya no está confundido",
    "is paralyzed": "está paralizado",
    "is no longer paralyzed": "ya no está paralizado",
    "is blinded": "está cegado",
    "is no longer blinded": "ya no está cegado",
    "is silenced": "está silenciado",
    "is no longer silenced": "ya no está silenciado",
    "is stunned": "está aturdido",
    "is no longer stunned": "ya no está aturdido",
    "is charmed": "está encantado",
    "is no longer charmed": "ya no está encantado",

    # Estados activos
    "has fallen unconscious": "ha caído inconsciente",
    "is slain": "ha sido asesinado",
    "revives": "revive",
    "recovered": "se recuperó",
    "is recovering": "se está recuperando",

    # Efectos
    "feels": "siente",
    "becomes": "se vuelve",
    "is now": "ahora está",
    "starting to": "comienza a",
    "stops": "deja de",

    # Sangrado
    "is bleeding": "está sangrando",
    "bleeding stops": "el sangrado se detiene",
    "blood loss": "pérdida de sangre",

    # Descripciones
    "easier to hit": "más fácil de golpear",
    "harder to hit": "más difícil de golpear",
    "very ill": "muy enfermo",
    "invulnerable": "invulnerable",
    "vulnerable": "vulnerable",

    # Acciones
    "attracted attention": "atrajo atención",
    "beginning the": "comenzando la",
    "being digested": "siendo digerido",
    "follows fire safety rules": "sigue las reglas de seguridad contra incendios",

    # Estados específicos
    "guilt": "culpa",
    "madness": "locura",
    "bloodlust": "sed de sangre",
}

# TRADUCCIONES DIRECTAS DE MENSAJES COMPLETOS
MESSAGE_TRANSLATIONS = {
    "%1 has fallen unconscious!": "¡%1 ha caído inconsciente!",
    "%1 is slain!": "¡%1 ha sido asesinado!",
    "%1 revives!": "¡%1 revive!",
    "%1 falls asleep!": "¡%1 se duerme!",
    "%1 wakes up!": "¡%1 se despierta!",
    "%1 is poisoned!": "¡%1 está envenenado!",
    "%1 is no longer poisoned.": "%1 ya no está envenenado.",
    "%1 is confused!": "¡%1 está confundido!",
    "%1 is no longer confused.": "%1 ya no está confundido.",
    "%1 is paralyzed!": "¡%1 está paralizado!",
    "%1 is no longer paralyzed.": "%1 ya no está paralizado.",
    "%1 is blinded!": "¡%1 está cegado!",
    "%1 is no longer blinded.": "%1 ya no está cegado.",
    "%1 is silenced!": "¡%1 está silenciado!",
    "%1 is no longer silenced.": "%1 ya no está silenciado.",
    "%1 is stunned!": "¡%1 está aturdido!",
    "%1 is no longer stunned.": "%1 ya no está aturdido.",
    "%1 feels guilt...": "%1 siente culpa...",
    "%1 feels invulnerable!": "¡%1 se siente invulnerable!",
    "%1 feels very ill...": "%1 se siente muy enfermo...",
    "%1 becomes easier to hit!": "¡%1 se vuelve más fácil de golpear!",
    "%1 becomes harder to hit!": "¡%1 se vuelve más difícil de golpear!",
    "%1 attracted attention to herself!": "¡%1 atrajo atención hacia sí misma!",
    "%1 beginning the dungeon dance!": "¡%1 comienza la danza de mazmorra!",
    "%1 begrudgingly follows fire safety rules.": "%1 sigue a regañadientes las reglas de seguridad contra incendios.",
    "%1 being digested! Max HP is halved!": "¡%1 está siendo digerido! ¡PV máximos reducidos a la mitad!",
}

# NOTAS
NOTE_TRANSLATIONS = {
    "State #1 will be added when HP hits 0.": "El estado #1 se añade cuando los PV llegan a 0.",
}

# ============================================================================
# FUNCIONES DE TRADUCCIÓN
# ============================================================================

def translate_name(name):
    """Traduce nombre de estado"""
    if not name or name.strip() == "":
        return name
    return STATE_NAMES.get(name, name)

def translate_message(msg):
    """Traduce mensaje de estado"""
    if not msg or msg.strip() == "":
        return msg

    # 1. Intentar traducción directa
    if msg in MESSAGE_TRANSLATIONS:
        return MESSAGE_TRANSLATIONS[msg]

    # 2. Aplicar patrones
    translated = msg
    for eng, esp in MESSAGE_PATTERNS.items():
        translated = translated.replace(eng, esp)

    return translated

def translate_note(note):
    """Traduce nota"""
    if not note or note.strip() == "":
        return note

    # Traducción directa
    if note in NOTE_TRANSLATIONS:
        return NOTE_TRANSLATIONS[note]

    # Patrones comunes
    translated = note
    translated = translated.replace("State #", "Estado #")
    translated = translated.replace("will be added when", "se añade cuando")
    translated = translated.replace("HP hits", "los PV llegan a")

    return translated

# ============================================================================
# CARGAR Y TRADUCIR
# ============================================================================

print("[1/5] Cargando States.json...")
with open('States.json', 'r', encoding='utf-8') as f:
    states_data = json.load(f)

print(f"   ✓ {len([s for s in states_data if s])} estados cargados")

print("\n[2/5] Aplicando traducciones...")

stats = {
    "names_trans": 0,
    "names_total": 0,
    "msg1_trans": 0,
    "msg1_total": 0,
    "msg2_trans": 0,
    "msg2_total": 0,
    "msg3_trans": 0,
    "msg3_total": 0,
    "msg4_trans": 0,
    "msg4_total": 0,
    "notes_trans": 0,
    "notes_total": 0,
}

states_translated = copy.deepcopy(states_data)

for state in states_translated:
    if state is None:
        continue

    # Name
    if state.get("name"):
        stats["names_total"] += 1
        original = state["name"]
        state["name"] = translate_name(original)
        if state["name"] != original:
            stats["names_trans"] += 1

    # Messages
    for i in range(1, 5):
        msg_key = f"message{i}"
        if state.get(msg_key):
            stats[f"msg{i}_total"] += 1
            original = state[msg_key]
            state[msg_key] = translate_message(original)
            if state[msg_key] != original:
                stats[f"msg{i}_trans"] += 1

    # Note
    if state.get("note"):
        stats["notes_total"] += 1
        original = state["note"]
        state["note"] = translate_note(original)
        if state["note"] != original:
            stats["notes_trans"] += 1

print(f"   ✓ Nombres: {stats['names_trans']}/{stats['names_total']} traducidos")
print(f"   ✓ Message1: {stats['msg1_trans']}/{stats['msg1_total']} traducidos")
print(f"   ✓ Message2: {stats['msg2_trans']}/{stats['msg2_total']} traducidos")
print(f"   ✓ Message3: {stats['msg3_trans']}/{stats['msg3_total']} traducidos")
print(f"   ✓ Message4: {stats['msg4_trans']}/{stats['msg4_total']} traducidos")
print(f"   ✓ Notes: {stats['notes_trans']}/{stats['notes_total']} traducidas")

print("\n[3/5] Guardando States_ES.json...")

with open('States_ES.json', 'w', encoding='utf-8') as f:
    json.dump(states_translated, f, indent=4, ensure_ascii=False)

file_size = len(json.dumps(states_translated, ensure_ascii=False)) / 1024
print(f"   ✓ Archivo guardado: States_ES.json ({file_size:.1f} KB)")

print("\n[4/5] Generando reporte...")

untranslated = []
for orig, trans in zip(states_data, states_translated):
    if orig is None or trans is None:
        continue
    if orig.get("name") and orig["name"] == trans["name"]:
        if orig["name"].strip():
            untranslated.append(orig["name"])

untranslated = sorted(list(set(untranslated)))
print(f"   ✓ Nombres sin traducir: {len(untranslated)}")

if untranslated:
    with open('states_untranslated.txt', 'w', encoding='utf-8') as f:
        f.write("Nombres de estados sin traducir:\n")
        f.write("="*60 + "\n")
        for name in untranslated:
            f.write(f"{name}\n")

print("\n[5/5] Ejemplos de traducción:")
print("="*80)

examples = [
    (1, "Unconscious"),
    (2, "Guard"),
    (4, "Poison"),
    (5, "Blind"),
]

for state_id, expected_name in examples:
    if state_id < len(states_data) and states_data[state_id]:
        orig = states_data[state_id]
        trans = states_translated[state_id]
        print(f"\n[Estado #{state_id}] {orig.get('name', 'N/A')} → {trans.get('name', 'N/A')}")
        if orig.get('message1'):
            print(f"   Msg1: {orig['message1']}")
            print(f"      → {trans['message1']}")
        if orig.get('message4'):
            print(f"   Msg4: {orig['message4']}")
            print(f"      → {trans['message4']}")

print("\n" + "="*80)
print("✅ TRADUCCIÓN COMPLETADA!")
print("="*80)
print(f"Archivo: States_ES.json ({file_size:.1f} KB)")
print(f"Nombres: {stats['names_trans']}/{stats['names_total']} " +
      f"({stats['names_trans']*100//stats['names_total'] if stats['names_total'] > 0 else 0}%)")
print(f"Mensajes totales: {stats['msg1_trans']+stats['msg2_trans']+stats['msg3_trans']+stats['msg4_trans']}")
print(f"Pendientes: {len(untranslated)} nombres")
print("="*80)
