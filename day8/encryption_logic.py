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
    
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)
else:
    print("invalid direction")

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

        
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.