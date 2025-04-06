"""Create a function to play Wordle"""

__author__: str = "730471503"


def contains_char(word_secret: str, character: str) -> bool:
    """Check word for character"""
    assert len(character) == 1, f"len('{character}') is not 1"
    # check that character is in secret word
    idx: int = 0
    while idx < len(word_secret):
        if word_secret[idx] == character:
            return True
        idx = idx + 1
    return False


def emojified(word_guess: str, word_secret: str) -> str:
    """Return emojis for guess letters"""
    assert len(word_guess) == len(word_secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    emojis: str = ""
    while idx < len(word_secret):
        # check each letter one by one
        # if x letter is in right spot, append green emoji
        # if x letter is in word but not in spot, append yellow emoji
        if contains_char(word_secret=word_secret, character=word_guess[idx]) is True:
            if word_secret[idx] == word_guess[idx]:
                emojis = emojis + GREEN_BOX
            else:
                emojis = emojis + YELLOW_BOX
        # if x letter is not in word, append white emoji
        else:
            emojis = emojis + WHITE_BOX
        idx = idx + 1
    return emojis


def input_guess(expected_length: int) -> str:
    """Ask user for word of length N"""
    # Define word_guess type and prompt user for guess of N length
    word_guess = input(f"Enter a {expected_length} character word:")
    while len(word_guess) != expected_length:
        # prompt user to fix guess if wrong length
        word_guess = input(f"That wasn't {expected_length} chars! Try again:")
        # return guess to function call for main
    return word_guess


def main(secret: str) -> None:
    # define needed variables
    turn: int = 1
    word_guess: str = ""
    word_secret = secret
    # define when game will continue
    while turn <= 6 and word_guess != secret:
        print(f"===Turn {turn}/6 ===")
        # begin game by prompting user for guess
        word_guess = input_guess(expected_length=len(secret))
        # return emojis corresponding to correct or incorrect letters
        emojified(word_guess, word_secret)
        print(emojified(word_guess, word_secret))
        # recognize winner
        if word_guess == secret:
            print(f"You won in {turn}/6 turns!")
        # continue game by moving to next turn if not won
        else:
            turn += 1
            # end game if 6 turns already completed
        if turn > 6:
            print("X/6 - Sorry, try again tomorrow!")


# make code runnable as module
if __name__ == "__main__":
    main(secret="codes")
