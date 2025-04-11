# scene_3.py

def play_scene():
    """
    Scene 3: The Mirror Gallery
    - Section A: Entering the endless hallway of mirrors
    - Section B: Confronting the doppelgänger
    - Returns "scene_4", "scene_3a" (bad end), or "quit"
    """

    print("\n=== SCENE 3: THE MIRROR GALLERY ===")
    print("You stumble into a long hallway lined with floor-to-ceiling mirrors.")
    print("Your reflections don't move when you do. Some show you wounded. One shows you dead.")
    print("The air smells of ozone and rotting flowers. A whisper echoes: 'Which one is really you?'\n")
    
    # --- SECTION A ---
    choice_a = input("Do you 'look around' carefully or 'call out'? ").lower().strip()

    if choice_a == "look around":
        print("\nYou notice one mirror is different - its frame is made of bone.")
        print("Your reflection there smiles at you. Its eyes are solid black.")
        print("When you blink, it steps closer to the glass.")
    elif choice_a == "call out":
        print("\n'Hello?' Your voice bounces endlessly between mirrors.")
        print("After a pause, your own voice answers: 'Hello...' but slower, distorted.")
        print("The reflections all turn to stare at you.")
    else:
        print("\nParalysis grips you. The mirrors begin fogging up from an unseen breath.")

    # --- SECTION B ---
    print("\n--- The Center Mirror ---")
    print("The bone-framed mirror now stands directly in your path.")
    print("Your doppelgänger presses against the glass, mouthing words you can't hear.")
    print("The other reflections have vanished. The glass begins to crack.\n")
    
    choice_b = input("Do you 'hide' your eyes or 'push forward' to confront it? ").lower().strip()

    if choice_b == "hide":
        print("\nYou cover your eyes. Ice-cold fingers brush your wrists.")
        print("When you look again, the mirror is empty... but your reflection is gone too.")
        print("You feel something following just behind you, matching your every step...")
        return "scene_4"
    elif choice_b == "push forward":
        print("\nYou charge at the mirror. The glass shatters but makes no sound.")
        print("Your double catches your wrist. Its skin feels like wet paper.")
        print("'We've been waiting,' it whispers as the other mirrors start bleeding...")
        return "scene_4"
    else:
        print("\nThe hesitation costs you. The double steps out of the mirror.")
        print("Its face melts as it reaches for you. The world goes dark...")
        return "scene_3a"  # Bad ending branch

    return "scene_4"  # Default continuation