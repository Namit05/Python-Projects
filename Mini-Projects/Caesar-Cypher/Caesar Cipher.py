from art import logo
print(logo)

def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    if encode_or_decode == "decode":
        shift_amount *= -1
    for char in original_text:
        if char not in alphabet :
            output_text+=char
        else:
            shifted_position = alphabet.index(char) + shift_amount

            shifted_position = shifted_position % len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d output :{output_text}")


alphabet = ["a","b", "c", "d", "e", "f", "g", "h", "i", "j","k","l","m","n","o","p","q","r","s""t","u","v","w","x","y","z",]
should_continue=True
while should_continue :
    direction = input("Type 'encode' to encrypt , type 'decode' to decrypt :\n").lower()
    text = input("Enter your message here :\n").lower()
    shift = int(input("Type the shift number :\n"))


    ceaser(text, shift, direction)
    restart=input("Do you want to do it again? Yes or No :\n").lower()
    if restart=="no":
        should_continue=False
        print("Take care bye bye")



