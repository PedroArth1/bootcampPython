alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from logocaesar import logo

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

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

def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        indice = alphabet.index(letter)
        indiceShift = indice + shift
        cipher_text += alphabet[indiceShift]
    print(f"The encoded text is {cipher_text}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' backwards in the alphabet by the shift amount and print the decrypted text.
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
    cipher_text = ""
    for letter in text:
        indice = alphabet.index(letter)
        indiceShift = indice - shift
        cipher_text += alphabet[indiceShift]
    print(f"The decoded text is {cipher_text}")


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt AND decrypt a message.



#part 3
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.


def caesar(text, shift):
    cipher_text = ""
    if direction == "encode":
        for letter in text:
            indice = alphabet.index(letter)
            indiceShift = indice + shift
            cipher_text += alphabet[indiceShift]
        print(f"The encoded text is {cipher_text}")
    else:
        
        for letter in text:
            indice = alphabet.index(letter)
            indiceShift = indice - shift
            cipher_text += alphabet[indiceShift]
        print(f"The decoded text is {cipher_text}")

caesar(text, shift)
