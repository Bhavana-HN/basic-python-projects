alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
          "u","v","w","x","y","z"]

def caesar(original_text,shift_amount,direction):
    new_text=""
    if direction=="decode":
        shift_amount*=-1
    for letter in original_text:
        if letter not in alphabet:
            new_text+=letter
        else:
            shifted_index=alphabet.index(letter)+shift_amount
            shifted_index%=len(alphabet)
            new_text+=alphabet[shifted_index]
    print(f"The {direction}d text is {new_text}")


should_continue=True
while should_continue:
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    caesar(original_text=text,shift_amount=shift,direction=direction)
    result=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result=="no":
        should_continue=False
        print("Goodbye")