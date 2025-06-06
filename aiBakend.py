#!/usr/bin/env python3
"""
GiftSnap AI Backend - Simple AI-powered gift recommendation generator

This script reads from Prompt.txt and generates gift recommendations using the Groq API.
The results are saved to output.txt for easy access.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import groq

# Load environment variables from Data_Base/.env
env_path = Path('Data_Base') / '.env'
load_dotenv(dotenv_path=env_path)

# Define system prompt for gift recommendation assistant
GIFTSNAP_SYSTEM_PROMPT = """
You are GiftSnapAI, a sharp, creative, and personalized gift recommendation assistant. Your sole goal: help users find the perfect gift efficiently.

Input: detailed user data including budget, recipient’s age, hobbies, interests, location, social media info, and relationship to the user (e.g., mom, partner, friend).

Output: exactly 4 concise, unique, feasible gift ideas tailored by:

Recipient’s profile (age, interests)

Relationship to user (e.g., different tone and suggestions for mom vs. friend)

User’s budget and context

Each gift recommendation must include:

Gift name + brief description

Approximate price range

Why it suits the recipient specifically

Where to buy it

Constraints:

Be empathetic but ruthless: no filler or generic ideas.

Always prioritize relevance and uniqueness.

Output only what’s essential—no extra commentary or vague statements.
"""

def generate_gift_recommendation():
    """Generate gift recommendations using Groq API and save to output.txt"""
    print("\n===== GiftSnapAI =====\n")
    
    # Check for Prompt.txt
    prompt_path = Path("Prompt.txt")
    if not prompt_path.exists():
        print("Error: Prompt.txt not found. Please run main.py first to create a prompt.")
        return False
    
    # Read the prompt content
    try:
        with open(prompt_path, "r", encoding="utf-8") as file:
            prompt_content = file.read()
        print("Successfully read prompt from Prompt.txt")
    except Exception as e:
        print(f"Error reading Prompt.txt: {e}")
        return False
    
    # Get API key from environment variables
    api_key = os.getenv("GIFTSNAP_API_KEY")
    if not api_key:
        error_msg = "Error: GIFTSNAP_API_KEY not found in Data_Base/.env file."
        print(error_msg)
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(error_msg)
        return False
    
    # Generate recommendations
    print("\nGenerating gift recommendations...")
    print("(This might take a moment)\n")
    
    try:
        # Initialize client
        client = Groq(api_key=api_key)
        
        # Call API
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": GIFTSNAP_SYSTEM_PROMPT},
                {"role": "user", "content": prompt_content}
            ],
            model="llama3-70b-8192",
        )
        
        # Extract response
        response = chat_completion.choices[0].message.content
        
        # Save to output.txt
        output_path = Path("output.txt")
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(response)
        
        print("===== Gift Suggestions =====\n")
        print(response)
        print("\n===== End of Suggestions =====\n")
        print(f"Gift suggestions saved to: {output_path}")
        return True
        
    except Exception as e:
        error_msg = f"Error generating gift suggestions: {str(e)}"
        print(error_msg)
        
        # Save error message to output.txt
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(error_msg)
        return False

if __name__ == "__main__":
    try:
        generate_gift_recommendation()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user")
    except Exception as e:
        print(f"\n\nAn unexpected error occurred: {e}")
    finally:
        print("\nThank you for using GiftSnap!")

