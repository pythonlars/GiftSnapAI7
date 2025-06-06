from datetime import datetime
from pathlib import Path

def collect_user_data():
    """Collect user data and save it to Data_Base/UserData.txt"""
    
    print("===== User Profile Creator =====\n")
    
    try:
        # Collect user data
        name = input("Enter your name: ")
        
        # Year of birth with validation
        while True:
            try:
                year_of_birth = int(input("Enter your year of birth: "))
                current_year = datetime.now().year
                if 1900 <= year_of_birth <= current_year:
                    break
                print(f"Please enter a valid year between 1900 and {current_year}")
            except ValueError:
                print("Please enter a valid number")
        
        # Month of birth with validation
        while True:
            try:
                month_of_birth = int(input("Enter your month of birth (1-12): "))
                if 1 <= month_of_birth <= 12:
                    break
                print("Please enter a valid month (1-12)")
            except ValueError:
                print("Please enter a valid number")
        
        # Day of birth with validation
        while True:
            try:
                day_of_birth = int(input("Enter your day of birth: "))
                if 1 <= day_of_birth <= 31:  # Simple validation
                    break
                print("Please enter a valid day (1-31)")
            except ValueError:
                print("Please enter a valid number")
                
        hobbies = input("Enter your hobbies: ")
        location = input("Enter your location: ")
        
        # Calculate age
        current_year = datetime.now().year
        age = current_year - year_of_birth
        
        # Format the data
        formatted_data = f"""Name: {name}
Year of birth: {year_of_birth}
Month of birth: {month_of_birth}
Day of birth: {day_of_birth}
Hobbies: {hobbies}
Location: {location}
Age: {age}"""
        
        # Create Data_Base directory if it doesn't exist
        data_dir = Path('Data_Base')
        data_dir.mkdir(exist_ok=True)
        
        # Save to file in Data_Base folder
        file_path = data_dir / 'UserData.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(formatted_data)
        
        print(f"\nYour information has been saved to {file_path}")
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    collect_user_data()

