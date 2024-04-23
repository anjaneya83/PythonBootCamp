import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    encrypted_text=[]
    alphabet_len=len(alphabet)-1
    for letter in text:
        idx=alphabet.index(letter)
        new_pos=idx+shift
        if alphabet_len-new_pos < 0:
            new_pos = new_pos-alphabet_len-1
        encrypted_text.append(alphabet[new_pos])
    print(f"The encoded text is {''.join(encrypted_text)}")

def decrypt(text,shift):
    decrypted_text=""
    alphabet_len=len(alphabet)-1
    for letter in text:
        idx=alphabet.index(letter)
        new_pos=idx-shift
        decrypted_text+=alphabet[new_pos]
    print(f"The decrypted text is {decrypted_text}")
  
def caesar(start_text,shift_amount,cipher_direction):
    crypted_text=""
    alphabet_len =len(alphabet)-1
    for letter in start_text:
        try:
            idx =alphabet.index(letter)
            if cipher_direction == "encode":
                new_pos=idx+shift_amount
                if alphabet_len-new_pos < 0:
                    new_pos = new_pos-alphabet_len-1
            elif cipher_direction == "decode":
                new_pos =idx-shift_amount
            else:
                print("Invalid direction")
                return
            crypted_text+=alphabet[new_pos]
        except ValueError:
            crypted_text+=letter
    print(f"The {cipher_direction}ed text is {crypted_text}")
print(art.logo)
continue_execution = "yes"
while continue_execution == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    continue_execution=input("Do you want to restart the program? Type either 'yes' or 'no': ")

   