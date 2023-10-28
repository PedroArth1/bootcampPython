logo = '''
                         __
                         \         /
                          )__(
                          |"""""""|.-.,.---------.,.-.
                          |       | | |               | | ''-.
                          |       || |             | |..-'
                          |__| '-' '---------' '-'
                          )"""""""(
                         /__\
                       .-------------.
                      /___\
'''

print(logo)

import os
clear = lambda:os.system('cls')
response = "y"
leilao = {}
maior = 0
vencedor = ""
while response == "y":
    name = input('Whats ur name? ')
    bid = int(input('Whats ur bid? '))
    leilao[name] = bid

    response = input("Another one? y/n").lower()
    clear()
    if bid > maior:
        maior = bid
        vencedor = name
    
print(f"Winner is {vencedor} with a bid of {bid}")

        
    

    


