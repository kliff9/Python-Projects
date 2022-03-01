alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Function for the Program
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":          #If Statement for encode or decode          
    shift_amount *= -1
  for char in start_text:                   # Checks the User Text and finds them in the List(alphabet) and then shift to a new alphetbet based on the shift by changing the index
    if char in alphabet: 

     position = alphabet.index(char)
     new_position = position + shift_amount
     end_text += alphabet[new_position]
    else:
      end_text += char                                                                                # else statement for any letters not in alphabet
  print(f"Here's the {cipher_direction}d result: {end_text}")




game = True                                                                                            #Trigger
while game:
 direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()                    #User Chooses encode or decode
 text = input("Type your message:\n").lower()                                                          #User writes the code
 shift = int(input("Type the shift number:\n"))                                                        #User Chooses the shift number  


 shift = shift % 26                                                                                    # When user enters Large Numbers over 26 
 caesar(text, shift, direction)                                                                        # Function Executes 
 play_again= input('Would you like to play Again? Yes(y) No(n)\n').lower()                             # Play Again? 
 if play_again == 'n':
   game = False


























