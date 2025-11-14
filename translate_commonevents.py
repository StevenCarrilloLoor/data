#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para traducir CommonEvents.json al español
"""

import json
import re

def load_extracted_texts():
    """Carga los textos extraídos"""
    with open('/home/user/data/commonevents_extracted_texts.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def create_translation_dictionary():
    """Crea el diccionario de traducción completo"""

    texts = load_extracted_texts()

    # Diccionario de traducción
    translations = {
        'names': {},
        'dialogues': {},
        'choices': {},
        'other_texts': {}
    }

    print("🌍 Iniciando traducción de CommonEvents.json...")
    print("=" * 70)

    # TRADUCIR NOMBRES DE EVENTOS
    print("\n📛 Traduciendo nombres de eventos...")
    translations['names'] = translate_event_names(texts['names'])
    print(f"   ✅ {len(translations['names'])} nombres traducidos")

    # TRADUCIR DIÁLOGOS (este será el más grande)
    print("\n💬 Traduciendo diálogos...")
    print(f"   ⏳ Procesando {len(texts['dialogues'])} diálogos...")
    translations['dialogues'] = translate_dialogues(texts['dialogues'])
    print(f"   ✅ {len(translations['dialogues'])} diálogos traducidos")

    # TRADUCIR OPCIONES
    print("\n🔘 Traduciendo opciones...")
    translations['choices'] = translate_choices(texts['choices'])
    print(f"   ✅ {len(translations['choices'])} opciones traducidas")

    # TRADUCIR OTROS TEXTOS
    print("\n📝 Traduciendo otros textos...")
    translations['other_texts'] = translate_other_texts(texts['other_texts'])
    print(f"   ✅ {len(translations['other_texts'])} otros textos traducidos")

    # CREAR DICCIONARIO MAESTRO (unificar todas las categorías)
    master_dict = {}
    for category in translations.values():
        master_dict.update(category)

    total = len(master_dict)
    print(f"\n✅ TOTAL TRADUCCIONES: {total}")
    print("=" * 70)

    return master_dict, translations

def translate_event_names(names):
    """Traduce los nombres de eventos
    NOTA: Muchos son nombres técnicos o de código, se traducen solo los descriptivos
    """
    trans = {}

    # Nombres técnicos que NO se traducen (nombres de funciones, variables, etc.)
    technical_names = {
        '---', '--PARTY MEMBER TALK--', '-MWEntryPoint-', '-sdr-',
        'AltPose', 'BattleEnd', 'BattleStart', 'BattleTurn',
        'BoilerRoomMonsterControl', 'BrainAnim', 'BuyItemTable',
        'ChangedRooms', 'CharCreate', 'CharEvent', 'CharaClosing',
        'CheckIfMonsterClose', 'CheckIfMonsterWandersIn', 'CheckNewParty',
        'Cooking', 'Crafting', 'DT_General  |301-400', 'DT_OnePerson|201-300',
        'DT_Priority |001-100', 'DT_TwoPeople|101-200', 'DanMoney',
        'DanQuest', 'DanViewers', 'DinnerTalk_Root', 'Diseases',
        'FallInHole', 'FleshAnim', 'FloodedAptBubble', 'FloodedAptCleanup',
        'FungusEffects', 'FungusFade', 'GetFidget', 'HolesAnim',
        'HourPassed', 'IntestAnim', 'JumpDown', 'Katana',
        'LandlordRent', 'MWCore', 'MaskedShadowSpawn', 'Mirror      |501-600',
        'MortonRemoveJunk', 'MoveClose', 'MoveFar', 'NewParty',
        'NormPose', 'OpenBox', 'Parallel', 'PhilippeAtk',
        'Plant', 'RandEvent', 'Recipe', 'ReturnMoney',
        'RoachWars', 'Scan', 'SessionStart', 'ShadowSpawns',
        'Shower      |401-500', 'Sleeping', 'StepSoundTrigger',
        'Stepped', 'StoryEvent', 'SybilReveal', 'TameLandmine',
        'TickTock', 'TimePasses', 'Torment', 'Transform',
        'Unmask', 'WORKSPACE', 'WormBodyAtk', 'astronomerCorrection',
        'autoDisplay', 'carKey', 'checkAstronomerState', 'checkDiscPuzzle',
        'coinSockDmgCalc', 'consumeLunch', 'convertIllusoryItems',
        'cookingSkill', 'deepBsmt_EventSetup', 'describeSlide',
        'diffSetup', 'digging', 'display', 'dizzyBattleUpdate',
        'eatCookedMeal', 'enterFlesh', 'exaltedFourTalk',
        'examineWindow', 'floodedAptEffects', 'floodedAptTimer',
        'grabDoorEnc', 'greenPaintingHeadbite', 'handleSnacks',
        'hellenSpawn', 'junkGiveRewards', 'kaeleyLockpickReact',
        'laptop', 'laptop_news', 'laptop_readEmail', 'laptop_social',
        'leaveFlesh', 'manageSaveRights', 'marvinTalk',
        'meleeAttack', 'mortonItemUse', 'neighborGeneralNews',
        'neighborGoodbye', 'neighborGreeting', 'neighborHerNews',
        'neighborTalkRoot', 'neighborWhatYouNeed', 'neighborYournews',
        'neighborYournews_Story', 'newDay', 'painterportrait3talk',
        'parallaxCalc', 'powerOutageCheck', 'randomItemGet',
        'ratFriendInteraction'
    }

    # Traducciones de nombres descriptivos
    descriptive_trans = {
        "Appear At Jeanne's": "Aparecer en casa de Jeanne",
        "Aster-Get it back": "Aster-Recuperarlo",
        "Aster-Give Offering": "Aster-Dar ofrenda",
        "Audrey": "Audrey",
        "AudreyTalk": "HablarAudrey",
        "Basement Pit": "Foso del sótano",
        "Battle Brew": "Brebaje de batalla",
        "Caustic Brew": "Brebaje cáustico",
        "CheeseForTheColonel": "QuesoParaElCoronel",
        "ClownNightmare": "PesadillaPayaso",
        "CrosswordHell": "InfiernoCrucigrama",
        "Eugene Shop/Nestor Shop": "Tienda Eugene/Tienda Nestor",
        "Guinea Pig": "Conejillo de indias",
        "HellenQuest": "MisiónHellen",
        "HellenQuestPlantInteract": "MisiónHellenInteractuarPlanta",
        "Joel Attacks": "Joel ataca",
        "LeighQuest": "MisiónLeigh",
        "Mask On": "Máscara puesta",
        "MedicInAJar": "MédicoEnTarro",
        "Meteor Strike": "Golpe meteoro",
        "Playtest Diff Option": "Opción dificultad prueba",
        "Soul Feast": "Festín de almas",
        "Talk Aster": "Hablar con Aster",
        "Talk Aster N/A": "Hablar con Aster N/D",
        "Talk Audrey": "Hablar con Audrey",
        "Talk Dan": "Hablar con Dan",
        "Talk Ernest": "Hablar con Ernest",
        "Talk Hellen": "Hablar con Hellen",
        "Talk Joel": "Hablar con Joel",
        "Talk Leigh": "Hablar con Leigh",
        "Talk Lyle": "Hablar con Lyle",
        "Talk Lyle N/A": "Hablar con Lyle N/D",
        "Talk Montgomery": "Hablar con Montgomery",
        "Talk Morton": "Hablar con Morton",
        "Talk Papineau": "Hablar con Papineau",
        "Talk Phillippe": "Hablar con Phillippe",
        "Talk Roaches": "Hablar con cucarachas",
        "Talk Sophie": "Hablar con Sophie",
        "Talk Spider N/A": "Hablar con araña N/D",
        "Talk Xaria": "Hablar con Xaria",
        "TellJasperAboutSybil": "ContarleJasperSobreSybil",
        "ThePhilDelusion": "LaDelusiónDePhil",
        "TombLetter": "CartaTumba",
        "candy Machine": "máquina de dulces",
        "duct tape": "cinta adhesiva",
        "giant revolver": "revólver gigante",
        "hardmodetest blockade": "bloqueo prueba modo difícil",
        "metal detector blip": "pitido detector de metales",
        "new DT GENERAL stuff": "cosas nuevas DT GENERAL",
        "pick door encounters": "encuentros elegir puerta",
        "play videogame": "jugar videojuego",
        "ran away": "huyó",
        "return home": "volver a casa",
    }

    # Nombres de videojuegos (mantener en inglés o traducir según contexto)
    game_names = {
        "game:BloodGhoulOrgy": "game:BloodGhoulOrgy",
        "game:Catafalque": "game:Catafalque",
        "game:CrosswordChallenge": "game:DesafíoCrucigrama",
        "game:FrogitAboutIt": "game:FrogitAboutIt",
        "game:Glitchy": "game:Glitchy",
        "game:HonkosGrandJourney": "game:ElGranViajeDeHonko",
        "game:KillToShoot": "game:KillToShoot",
        "game:Madwheels97": "game:Madwheels97",
        "game:MassacrePrincess": "game:PrincesaMasacre",
        "game:Myrmidon": "game:Myrmidon",
        "game:MyrmidonXII": "game:MyrmidonXII",
        "game:Octocook": "game:Octocook",
        "game:ReptileFootball": "game:FútbolReptil",
        "game:Screamatorium": "game:Screamatorium",
        "game:SpaceTruckerz": "game:CamioneroEspacial",
        "game:SuperJumplad": "game:SuperJumplad",
        "game:SuperJumplad3": "game:SuperJumplad3",
        "game:UnlabeledGame": "game:JuegoSinEtiqueta",
        "game:WakeTheBloodKnight": "game:DespertarCaballeroSangre",
        "game:Wizardshell": "game:Wizardshell",
        "game:Wraithscourge": "game:Wraithscourge",
    }

    # Combinar todos
    for name in names:
        if name in technical_names:
            trans[name] = name  # Mantener igual
        elif name in descriptive_trans:
            trans[name] = descriptive_trans[name]
        elif name in game_names:
            trans[name] = game_names[name]
        else:
            # Si no está en ninguna categoría, mantener igual
            trans[name] = name

    return trans

def translate_dialogues(dialogues):
    """Traduce los diálogos
    NOTA: Esta es la parte más grande. Voy a traducir por lotes.
    """
    trans = {}

    # Debido al volumen masivo, voy a procesar solo una muestra aquí
    # y luego cargar traducciones desde un archivo separado
    # Por ahora, retorno un diccionario vacío y lo procesaremos después

    print("   ⚠️  NOTA: Debido al volumen masivo de diálogos (10,696),")
    print("      se requiere un procesamiento por lotes...")

    return trans

def translate_choices(choices):
    """Traduce las opciones de elección"""
    trans = {}

    # Por ahora retorno vacío, procesaremos después
    return trans

def translate_other_texts(others):
    """Traduce otros textos"""
    trans = {}

    # Por ahora retorno vacío, procesaremos después
    return trans

def main():
    master_dict, categorized = create_translation_dictionary()

    # Guardar diccionario categorizado
    output_path = '/home/user/data/commonevents_translations.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(categorized, f, ensure_ascii=False, indent=2)

    print(f"\n💾 Diccionario guardado en: {output_path}")

if __name__ == '__main__':
    main()
