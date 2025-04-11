# scene_1.py

def play_scene():
    """
    Horror Story: The Abandoned Asylum
    - Section A: Wake up in the asylum (Choice: explore/exit)
    - Section B: Encounter the supernatural (Choice: follow/ignore)
    - Returns "scene_2" or "quit".
    """
    
    print("\n=== THE ABANDONED ASYLUM ===")
    print("You wake up on the cold floor of a derelict asylum. Moonlight filters through broken\nwindows, illuminating rusted surgical tools and overturned gurneys. The air reeks of rot.")
    print("A flickering [EXIT] sign glows red down the hallway.")
    
    # --- SECTION A ---
    choice_a = input("\nDo you 'explore' the room or sprint for the 'exit'? ").lower().strip()
    
    if choice_a == "explore":
        print("\nYou crawl to your feet, squinting at the peeling walls. A child's laughter echoes\nfrom a room marked 'TREATMENT 4'. Your fingers brush a dusty patient file—it has YOUR name.")
    elif choice_a == "exit":
        print("\nYou bolt for the door, but it slams shut. The laughter turns to a whisper:\n'You signed the consent form, remember?'")
    else:
        print("\n(You freeze in panic. The asylum decides for you.)")
        choice_a = "explore"  # Default to explore
    
    # --- SECTION B ---
    print("\nA bloodied wheelchair creaks toward you. From the darkness comes a wet,\ndragging sound. Your pulse races.")
    
    choice_b = input("Do you 'follow' the noise or 'ignore' it? ").lower().strip()
    
    if choice_b == "follow":
        print("\nYou step into a morgue. A drawer labeled 'SUBJECT 13' slides open.\nInside lies a corpse... with YOUR face. Its eyes snap open.")
    elif choice_b == "ignore":
        print("\nYou shut your eyes—but the dragging speeds up. Something cold grabs your ankle.\nA voice wheezes: 'You’re late for your appointment.'")
    else:
        print("\n(Your silence is answer enough. The thing approaches.)")
        choice_b = "follow"  # Default to follow
    
    # --- NEXT SCENE ---
    input("\n[Press Enter to continue...]")
    return "scene_2"  # Both choices lead to the next scene