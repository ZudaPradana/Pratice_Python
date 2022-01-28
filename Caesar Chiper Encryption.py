alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] * 2
chiper = input('Encode or Decode :\n')
text = input('letter: ').lower()
shift = int(input('Shift on number: '))

def encode(text_encode, shift_encode):
    encode = ''
    for letter in text_encode:
        position = alphabet.index(letter)
        new_position = position + shift_encode
        new_letter = alphabet[new_position]
        encode += new_letter
    print(encode)


def decode(text_encode, shift_encode):
    decode = ''
    for letter in text_encode:
        position = alphabet.index(letter)
        new_position = position - shift_encode
        new_letters = alphabet[new_position]
        decode += new_letters
    print(decode)


if chiper == 'encode':
    encode(text_encode=text, shift_encode=shift)
elif chiper == 'decode':
    decode(text_encode=text, shift_encode=shift)
