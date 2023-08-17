from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(text, shift, direction):
    if direction != 'encode' and direction != 'decode':
        print("Invalid mode. I'm outta here.")
        return
    
    processed_text = ''

    if direction == 'decode':
        shift *= -1
        
    for l in text:
        if l in alphabet:
            index_letter = alphabet.index(l)
            shifted_index_letter = index_letter + shift
            processed_text += alphabet[shifted_index_letter]
        else:
            processed_text += l

    print(f"The {direction}d text is {processed_text}")

print(logo)

continue_running = True
while continue_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    ceasar(text, shift, direction)
    user_continue_input = input("Do you want to restart? Type 'yes' to continue or 'no' to exit.\n")
    if user_continue_input != 'yes':
        continue_running = False