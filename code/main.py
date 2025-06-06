
"""
GiftSnap - Simple Gift Recommendation System

This script generates gift recommendations based on user and recipient profiles.
It outputs recommendations to output.txt.
"""

from pathlib import Path
from datetime import datetime
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("giftsnap")

def ensure_directories():
    """Ensure all required directories exist"""
    directories = [
        Path("Data_Base"),
        Path("Data_Base/gifting_profile"),
        Path("data/gift_profiles"),
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Directory ensured: {directory}")

def find_gift_profile(name):
    """Find a gift profile by name in either directory location"""
    # Try the primary location first
    primary_path = Path(f"Data_Base/gifting_profile/{name}.txt")
    if primary_path.is_file():
        return primary_path
    
    # Then try the secondary location
    secondary_path = Path(f"data/gift_profiles/{name}.txt")
    if secondary_path.is_file():
        return secondary_path
    
    # No matching profile found
    available_profiles = list(Path("Data_Base/gifting_profile").glob("*.txt"))
    available_profiles.extend(list(Path("data/gift_profiles").glob("*.txt")))
    
    if not available_profiles:
        print("No gift profiles found. Please create a gift profile first.")
        print("Use the gifting_profiel_generate.py script to create one.")
        exit(1)
    
    print(f"Profile '{name}' not found. Available profiles:")
    for i, profile in enumerate(available_profiles, 1):
        profile_name = profile.stem
        print(f"{i}. {profile_name}")
    
    choice = input("\nEnter the number of the profile you want to use: ")
    try:
        index = int(choice) - 1
        if 0 <= index < len(available_profiles):
            return available_profiles[index]
        else:
            print("Invalid selection. Exiting.")
            exit(1)
    except ValueError:
        print("Invalid input. Exiting.")
        exit(1)

def get_user_data():
    """Get user data from the UserData.txt file"""
    user_data_path = Path("Data_Base/UserData.txt")
    
    if not user_data_path.is_file():
        print("No user profile found. Please create your profile first.")
        print("Run the UserDataColescting.py script to create your profile.")
        exit(1)
    
    try:
        with open(user_data_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading user data: {e}")
        exit(1)

def main():
    """Main function to run the gift suggestion generator"""
    print("\n===== GiftSnapAI =====\n")
    
    # Ensure required directories exist
    ensure_directories()
    
    # Get the recipient name
    recipient = input("For who do you want to find a gift? ")
    
    gift_kind = input("What kind of gift do you want to find? (e.g. Physical gift, experience gift, self made gift etc.) ")
    
    reason = input("What kind of gift do you want to find? (e.g. Birthday, anniversary, etc.) ")
    
    # Find the gift profile
    gift_profile_path = find_gift_profile(recipient)
    print(f"Using gift profile: {gift_profile_path}")
    
    # Get user data
    user_data = get_user_data()
    
    # Get and validate budget
    while True:
        try:
            budget = int(input("Enter your budget (in currency units): "))
            if budget > 0:
                break
            print("Budget must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get and validate creativity level
    while True:
        try:
            creativity = int(input("How creative should the gift be? (1-10): "))
            if 1 <= creativity <= 10:
                break
            print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Read the gift profile data
    try:
        with open(gift_profile_path, 'r', encoding='utf-8') as f:
            gift_profile_data = f.read()
    except Exception as e:
        print(f"Error reading gift profile: {e}")
        exit(1)
    
    # Build the prompt
    prompt = f"""This is my GiftSnap Profile:
{user_data}

My budget is: {budget}

I need 4 {gift_kind} gift ideas with a creativity level of {creativity}/10 for my {gift_profile_path.stem}  with the reason {reason}:

Profile for {gift_profile_path.stem}:
------------------------------
{gift_profile_data}"""
    
    # Save the prompt to Prompt.txt
    prompt_path = Path("Prompt.txt")
    try:
        with open(prompt_path, 'w', encoding='utf-8') as f:
            f.write(prompt)
        print(f"\nPrompt created and saved to: {prompt_path}")
    except Exception as e:
        print(f"Error saving prompt: {e}")
        exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\n\nAn unexpected error occurred: {e}")
    finally:
        print("\nThank you for using GiftSnap!")