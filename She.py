import streamlit as st
import time 
import sys

def typing_effect(text, delay=0.03):
    """Simulates smooth typing effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animated_loading():
    """Displays a soothing loading animation"""
    animation = ["(っ˘̩╭╮˘̩)っ", "(っ˘̩╭╮˘̩)っ♡", "(っ˘̩╭╮˘̩)っ💖", "(っ˘̩╭╮˘̩)っ💞"]
    for _ in range(3):
        for frame in animation:
            sys.stdout.write("\r" + frame)
            sys.stdout.flush()
            time.sleep(0.5)
    print("\n")

def display_message():
    """Displays a heartfelt message"""
    message = """
    ─────────────────────────────────────────────
                🌸 Hey, My Precious Bestie!(Meri Pyari Gadhi) 🌸
    ─────────────────────────────────────────────
    
    I know today might not be easy for you, 
    and that's okay. You're allowed to feel frustrated.
    But guess what? You're never alone in this.
    
    No matter how tough the day gets, 
    remember that you are incredibly strong, 
    beautiful, and absolutely irreplaceable.

    So take a deep breath, snuggle into something cozy, 
    and know that I'm sending you the biggest, warmest hug 
    across the universe. 🤗💖
    
    You're magic. You always have been. 
    And I’ll always be here to remind you of that. 💕
    """
    typing_effect(message, delay=0.02)

def display_poem():
    """A short, sweet poem just for her"""
    poem = """
    🌷 A Little Note Just for You 🌷

    On days like this, when skies feel gray,  
    And all your worries won’t drift away,  
    I hope you know, I’m here to stay,  
    To cheer you up in every way. 💖

    The world is brighter 'cause you're in it,  
    Your smile could heal in just a minute.  
    So rest your mind, don't stress a bit,  
    You’ve got my love—every single bit. 🌸  
    """
    typing_effect(poem, delay=0.05)

def display_ascii_art():
    """Displays a cute heart ASCII art"""
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

def final_message():
    """A beautiful ending to cherish her heart"""
    typing_effect("\n💖 No matter what happens, I'll always be here for you. 💖", delay=0.02)
    typing_effect("You are loved, appreciated, and the most amazing person ever. 🌸", delay=0.02)
    typing_effect("Now, give yourself a big smile because you deserve all the happiness in the world! 😊💕", delay=0.02)

    print("\n✨ *'You're not just my best friend, you're my family. And families always stick together.'* 💫")
    print("\n🎈 Sending virtual balloons to brighten your day! 🎈\n")
    
    for _ in range(5):
        sys.stdout.write("🎈 ")
        sys.stdout.flush()
        time.sleep(0.5)
    
    print("\n\n💞 Always remember: You are special, you are loved, and you are never alone. 💞")

if __name__ == "__main__":
    animated_loading()
    display_message()
    display_ascii_art()
    display_poem()
    final_message()

    
