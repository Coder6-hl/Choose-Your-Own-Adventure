# scene_2.py

def play_scene():
    """
    Scene 2: The Blood-Stained Highway
    - Section A: The road after escaping the motel
    - Section B: The abandoned gas station
    - Returns "scene_3", "quit", or a branch (e.g., "scene_2a")
    """

    print("\n=== SCENE 2: THE BLOOD-STAINED HIGHWAY ===")
    print("You burst out of the motel, lungs burning. The road ahead is cracked and streaked with dark stains.")
    print("Your car is GONE. Only a puddle of black oil remains where you parked it.")
    print("In the distance, a flickering neon sign reads 'LAST CHANCE GAS'.\n")
    
    # --- SECTION A ---
    choice_a = input("Do you 'search' the oil puddle or 'move on' toward the gas station? ").lower().strip()

    if choice_a == "search":
        print("\nYou kneel beside the oil. It's too thick... and warm. Your fingers brush something metallic.")
        print("It's your license plate, bent like something CRUSHED your car. The oil smells like copper.")
        print("Scratches in the asphalt lead toward the gas station.")
    elif choice_a == "move on":
        print("\nYou hurry away. Behind you, the oil puddle BUBBLES violently.")
        print("A low growl echoes from the motel. You don't look back.")
    else:
        print("\nYou freeze. The wind carries a whisper: 'Run.'")

    # --- SECTION B ---
    print("\n--- The Last Chance Gas Station ---")
    print("The station's windows are shattered. A corpse in a mechanic's uniform slumps against a pump.")
    print("Its chest is ripped open—no heart inside. The door to the garage creaks open and shut rhythmically.")
    print("From inside, a radio crackles: '...EMERGENCY BROADCAST... STAY INDOORS... THEY HUNT AT NIGHT...'\n")
    
    choice_b = input("Do you 'investigate' the garage or 'ignore' it (search the store instead)? ").lower().strip()

    if choice_b == "investigate":
        print("\nInside the garage, tools hover in midair, moving on their own.")
        print("The radio suddenly screams static. The door SLAMS shut behind you.")
        print("In the mirror, a figure stands behind you—but when you turn, nothing's there.")
    elif choice_b == "ignore":
        print("\nYou enter the store. Shelves are toppled, cash register smashed open.")
        print("A message is scrawled on the wall in blood: 'THEY WEAR FACES AT NIGHT.'")
        print("The corpse outside is now GONE.")
    else:
        print("\nYour indecision costs you. The garage door flies open—something DRAGS the corpse inside.")

    # Next scene (could branch based on choices)
    return "scene_3"  # Or "scene_2_garage"/"scene_2_store" for alternate paths