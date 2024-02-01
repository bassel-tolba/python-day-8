import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = "yes"
while answer == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def crypt(a, b, c):
        cryption = ""
        for char in a:
            
            if char in alphabet:
                postion = alphabet.index(char)
                if c == "encode":   
            
                    postion += b
                    if postion > 25:
                        postion -= 26
                    func = "encoded"
                if c == "decode":
                    postion -= b
                    if postion < 0:
                        postion += 26
                    func = "decoded"
                char = alphabet[postion]    
            elif char not in alphabet:
                char = char
            
                
            cryption += char
        print(f"the {func} text is this '{cryption}'")

    crypt(a=text, b=shift, c=direction)
    answer = input("type 'yes' if you want to go again otherwise type 'no'")
print("Goodbye")
# encrypt(a= text, b= shift)

# def decrypt(a, b):
#     decryption = ""
#     for char in a:
#         postion = alphabet.index(char)
#         postion -= b
#         if postion < 0:
#             postion += 26
#         char = alphabet[postion]
#         decryption += char
#     print(f"the decrypted text is this '{decryption}'")
# encrypt(a= text, b= shift)
# decrypt(a= text, b= shift)
# if direction == "incode":
#     # print("you were incoding a message")
#     encrypt(a= text, b= shift)
# elif direction == "decode":
#     # print("you were decoding a message")
#     decrypt(a= text, b= shift)