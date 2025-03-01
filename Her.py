import time

def display_message():
    message = """
    ───────────────────────────────────────
        Hey, my amazing bestie ❤️
    ───────────────────────────────────────

    I know you're feeling frustrated right now, 
    and I just want you to know that I'm here for you. 
    No cramps, mood swings, or discomfort can take away 
    how strong and incredible you are. 

    Close your eyes, take a deep breath, 
    and imagine me giving you the biggest, warmest hug! 🤗

    Remember, you're not alone in this. 
    I'll always be by your side—whether it's to make you laugh, 
    listen to your rants, or just remind you how special you are.

    You deserve all the love, comfort, and care in the world. 
    So, drink some warm tea, wrap yourself in a blanket, 
    and let yourself rest. 💖

    You're loved. You're appreciated. 
    And this too shall pass. 

    🌸 With all my warmth and love,
       Your annoying but caring bestie 💕
    """
    for char in message:
        print(char, end="", flush=True)
        time.sleep(0.02)  # Smooth typing effect
    print("\n")

def display_ascii_art():
    heart = """
       *****     *****  
     **     ** **     **
    **       ***       **
    **                 **
     **               **
       **           **
         **       **  
           **   **    
             **  
    """
    print(heart)


    

if __name__ == "__main__":
    display_ascii_art()
    display_message()