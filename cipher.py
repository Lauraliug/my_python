def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

#test
phrase = 'Practice makes perfect.' 
shift = 3

#encrypt
secret = encrypt(phrase, shift)
print(f'Encoded: {secret}')

#decrypt
result = decrypt(secret, shift)
print(f'Decoded: {result}')

#stress testing
test1 = caesar('Hello', 'world')
print(f'Invalid type: {test1}')

test2 = caesar('Hello', 100)
print(f'Range too high: {test2}')