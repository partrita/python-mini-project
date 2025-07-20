def is_vowel(char):
    """
    Checks if a character is a vowel.
    Args:
        char (str): The character to check.
    Returns:
        bool: True if the character is a vowel, False otherwise.
    """
    return char.lower() in 'aeiou'

def minion_game(s):
    """
    Plays the Minion Game to determine the winner based on substrings.

    Args:
        s (str): The input string for the game.
                 Assumed to be a single word without spaces.
    """
    # Game rules are already displayed to the user before this function is called.
    # Player names are not strictly needed for the game logic itself,
    # but we'll keep them for personalized output.
    stuart_name = input("Enter name of player 1 (Stuart, forms words starting with consonants): \n")
    kevin_name = input("Enter name of player 2 (Kevin, forms words starting with vowels): \n")

    s = s.upper()  # Ensure string is uppercase for consistent indexing and comparison
    n = len(s)
    stuart_score = 0
    kevin_score = 0

    # Iterate through each possible starting position for substrings
    for i in range(n):
        if is_vowel(s[i]):
            # If the character at index i is a vowel, Kevin gets points
            # The number of substrings starting with s[i] is n - i
            kevin_score += (n - i)
        else:
            # If the character at index i is a consonant, Stuart gets points
            # The number of substrings starting with s[i] is n - i
            stuart_score += (n - i)

    print("\n--- Overall Score ---")
    print(f"{stuart_name} (Consonants): {stuart_score} points")
    print(f"{kevin_name} (Vowels): {kevin_score} points")
    print("---------------------\n")

    if stuart_score > kevin_score:
        print(f"🥳 {stuart_name} wins with a score of {stuart_score}!")
    elif kevin_score > stuart_score:
        print(f"🥳 {kevin_name} wins with a score of {kevin_score}!")
    else:
        print("🤝 It's a Draw!")

# --- Game Start ---
instruction = """
Welcome to the Minion Game!

**Game Rules:**
1. Both players are given the same string (a single, capital word without spaces).
2. Both players create substrings using letters from this string.
3. Stuart makes words starting with **consonants**.
4. Kevin makes words starting with **vowels**.
5. The game ends when all possible substrings have been considered.

A player gets +1 point for each **occurrence** of a valid substring in the original string.
"""

print(instruction)
initial_string = input("Please enter a single word (capital letters, no spaces): \n")
minion_game(initial_string)