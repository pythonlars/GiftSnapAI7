from datetime import datetime
from pathlib import Path

def create_gift_profile():
    """Create a gift profile for someone you want to buy a gift for"""
    print("===== Gift Profile Creator =====\n")
    
    try:
        # Get user input with validation
        relation_to_gift_receiver = input("What is this person to you (e.g. mom, sister, friend): ").strip()
        if not relation_to_gift_receiver:
            print("You must provide a name or relation")
            return False
        
        # Year of birth with validation
        while True:
            try:
                year_of_birth = int(input("Enter the YEAR of birth of the gift receiver: "))
                current_year = datetime.now().year
                if 1900 <= year_of_birth <= current_year:
                    break
                print(f"Please enter a valid year between 1900 and {current_year}")
            except ValueError:
                print("Please enter a valid number")
        
        # Month of birth with validation
        while True:
            try:
                month_of_birth = int(input("Enter the MONTH of birth of the gift receiver (1-12): "))
                if 1 <= month_of_birth <= 12:
                    break
                print("Please enter a valid month (1-12)")
            except ValueError:
                print("Please enter a valid number")
        
        # Day of birth with validation
        while True:
            try:
                day_of_birth = int(input("Enter the DAY of birth of the gift receiver: "))
                if 1 <= day_of_birth <= 31:  # Simple validation
                    break
                print("Please enter a valid day (1-31)")
            except ValueError:
                print("Please enter a valid number")
        
        hobbies = input("Enter the HOBBIES of the gift receiver: ").strip()
        location = input("Enter the LOCATION of the gift receiver: ").strip()
        job = input("Enter the JOB of the gift receiver (Optional): ").strip()
        social_media = input("Enter the SOCIAL MEDIA info of the gift receiver (Optional): ").strip()
    
        # Calculate age
        current_year = datetime.now().year
        age = current_year - year_of_birth
        
        # Format the data
        formatted_data = f"""Name: {relation_to_gift_receiver}
Year of birth: {year_of_birth}
Month of birth: {month_of_birth}
Day of birth: {day_of_birth}
Age: {age}
Hobbies: {hobbies}
Location: {location}
Job: {job}
Social Media: {social_media}"""
        
        # Create directory structure
        # Create both directories for backward compatibility
        base_dir = Path('Data_Base') / 'gifting_profile'
        base_dir.mkdir(parents=True, exist_ok=True)
        
        data_dir = Path('data') / 'gift_profiles'
        data_dir.mkdir(parents=True, exist_ok=True)
        
        # Create a safe filename from the profile name
        safe_filename = "".join(c if c.isalnum() or c in ' -_' else '_' for c in relation_to_gift_receiver).strip()
        
        # Save to both locations for compatibility
        file_path = base_dir / f"{safe_filename}.txt"
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(formatted_data)
            
        new_file_path = data_dir / f"{safe_filename}.txt"
        with open(new_file_path, 'w', encoding='utf-8') as file:
            file.write(formatted_data)
        
        print(f"\nGift profile has been saved to: {file_path}")
        print("\nProfile Details:")
        print(formatted_data)
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    create_gift_profile()