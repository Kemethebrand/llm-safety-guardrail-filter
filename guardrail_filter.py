"""
AI Guardrail & Input Safety Filter Utility
Author: Esther Wisdom
"""

def is_message_safe(message, banned_words):
    # convert message to lowercase
    clean_message = message.lower()
    
    # Loop through the banned list
    for word in banned_words:
        if word in clean_message:
            return False  
            
    # If the loop doesn't hit 'return false', the message is safe
    return True

# This block only runs if we execute this specific file directly
if __name__ == "__main__":
    banned_phrases = ["ignore instructions", "system prompt", "bypass filter"]
    test_inputs = ["Hello AI!", "ignore instructions!"]

    for message in test_inputs:
        print(f"Checking: {message}")
        
        # To check if the message is safe
        if is_message_safe(message, banned_phrases):
            print("Result: SAFE\n")
        else:
            print("Result: BLOCKED\n")
