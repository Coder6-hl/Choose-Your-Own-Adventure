def play_scene():
    """
    Scene 4: Final Confrontation
    A choice-driven narrative where the player determines the outcome of their journey.
    """

    print("\n=== SCENE 4 ===")
    print("You stand at the crossroads of destiny. Ahead lies the challenge; behind you, the path of retreat.")

    # Section A: The First Choice
    choice_a = input("Do you 'confront' the challenge or 'turn back'? ").lower().strip()

    if choice_a == "confront":
        print("Summoning your courage, you stride forward to face the looming threat...")
    elif choice_a == "turn back":
        print("You hesitate, considering the comfort of retreat, but doubt gnaws at your soul...")
    else:
        print("Frozen by indecision, time forces your hand. The challenge lies before you.")

    print("\n--- Transitioning to the Final Decision ---")
    print("The moment has come to determine your fate. How will you proceed?")

    # Section B: The Final Decision
    choice_b = input("Do you 'fight' or 'negotiate'? ").lower().strip()

    if choice_b == "fight":
        print("A fierce battle ensues. You pour your strength into the conflict, emerging with scars and lessons.")
        print("Your journey ends here, leaving a mark on the world.")
        return "quit"
    elif choice_b == "negotiate":
        print("You seek a path of reason, extending an olive branch. The outcome is uncertain but hopeful.")
        print("Your story concludes with a new beginning.")
        return "quit"
    else:
        print("Your inaction leaves fate to decide. The adventure reaches its end, quietly and unexpectedly.")
        return "quit"

# To play the scene, simply call the function:
# play_scene()