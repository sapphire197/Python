# Morse Code Translator
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

# Function to convert English text to Morse code
def text_to_morse(text):
    text = text.upper()
    morse_code = ''
    for letter in text:
        if letter != ' ':
            morse_code += MORSE_CODE_DICT.get(letter, '?') + ' '
        else:
            morse_code += ' / '  # Separator for spaces between words
    return morse_code.strip()

# Function to convert Morse code to English text
def morse_to_text(morse):
    morse += ' '
    deciphered_text = ''
    morse_word = ''
    for char in morse:
        if char != ' ':
            morse_word += char
        else:
            if morse_word == '/':
                deciphered_text += ' '  # Add space between words
            else:
                for key, value in MORSE_CODE_DICT.items():
                    if morse_word == value:
                        deciphered_text += key
                        break
            morse_word = ''
    return deciphered_text

# User input and conversion selection
def morse_translator():
    while True:
        print("\nChoose an option:")
        print("1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            text = input("Enter text to convert to Morse Code: ")
            print(f"Morse Code: {text_to_morse(text)}")
        elif choice == '2':
            morse = input("Enter Morse Code to convert to text (use space for letter separation and '/' for word separation): ")
            print(f"Text: {morse_to_text(morse)}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    morse_translator()
