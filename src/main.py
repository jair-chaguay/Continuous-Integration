"""
Command-line interface (CLI) module for interacting with the MembershipManager.

This module allows the user to:
- Select a membership plan
- Add additional features
- Set the number of members
- Calculate the final membership cost
- Exit the program

The CLI includes:
- Input validation
- Confirmation prompts (Y/N)
- Descriptive error messages
"""

from src.membership import MembershipManager


def ask_confirmation(message="Are you sure? (Y/N): "):
     
    """
    Ask the user to confirm an action using a Yes/No question.

    Args:
        message (str): The confirmation message shown to the user.

    Returns:
        bool: True if the user confirmed with 'Y', False otherwise.
    """
    
    while True:
        confirm = input(message).strip().lower()
        if confirm in ("y", "n"):
            return confirm == "y"
        print("Enter Y or N")



def ask_int(message):
    """
    Ask the user to enter a valid integer.

    Args:
        message (str): The prompt to display.

    Returns:
        int: A valid integer entered by the user.
    """
    
    while True:
        value = input(message).strip()
        if value.isdigit():
            return int(value)
        print("Invalid input")

def run():
    """
    Run the interactive command-line interface for membership management.

    The loop displays a menu with the following options:
    1. Select membership plan
    2. Add additional feature
    3. Set number of members
    4. Calculate total cost
    5. Exit program

    Returns:
        float or int:
            - Final total cost when option 4 is selected
            - -1 if the program exits without calculation
    """
    manager = MembershipManager()

    while True:
        print("\n--- MENÚ ---")
        print("1. Select membership plan")
        print("2. Add additional feature")
        print("3. Set number of members")
        print("4. Calculate total cost")
        print("5. Exit")

        choice = input("Optionn: ").strip()

        # PLAN
        if choice == "1":
            print("\nAvailable plans:", manager.get_plans())
            name = input("Enter a plan name: ")

            if not manager.select_plan(name):
                print("Invalid or unavailable plan")
                continue

            if not ask_confirmation("Confirm selected plan? (Y/N): "):
                manager.selected_plan = None
                print("Plan selection cancelled")
            else:
                print("Plan Successfully selected")

        # ADDTIONAL FEATURES
        elif choice == "2":
            print("Features:", manager.get_features_list())
            name = input("Enter a feature name: ")

            if not manager.add_feature(name):
                print("Invalid feature or already added")
                continue

            if not ask_confirmation("Confirm adding this feature? (Y/N): "):
                manager.features = [f for f in manager.features if f["name"] != name]
                print("Feature addition cancelled")
            else:
                print("Feature added")

        # MEMBERS
        elif choice == "3":
            count = ask_int("Number of members: ")

            if not manager.set_members(count):
                print("Number of mebers must be at least 1")
                continue

            print("Members count updated")

        # TOTAL
        elif choice == "4":
            total = manager.calculate_total()
            print("TOTAL =", total)
            return total

        # EXIT
        elif choice == "5":
            if ask_confirmation(" Exit? (Y/N): "):
                print("Finishing...")
                return -1

        else:
            print("Invalid option. Please choose a valid menu option")
