from termcolor import colored, cprint


portal_img = colored("""
████████████████████▓▓▓▓▓████████████▓▓▓▓█▓▓▓▓▓▓▓▓
██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓
██▓█████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▓▓▓▓
▓▓█████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████▓▓
▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████
██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████
██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███
█████▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓███
████▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓█
██▓▓▓▓▓▒▓▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓
██▓▓▓▓▒▓▓▓▓▓▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓
█▓▓▓▓▒▓▓▓▓▓▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▓▓▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▓▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▓▓▓▓▓▓▓▓
▓▓▓▒▒▒▓▓▓▓▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▓▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒░▒▒▒▓▓▓▓▓▓▓▓
▓▓▓▓▒▒▓▓▓▓▒▒▒░░░░░░░░░░▒▒░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓
▓▓▓▓▓▒▒▓▓▓▒▒▒░░░░░░░░░░▓██░░░░░░░░░░░░▒▒▒▓▓▓▓▓▓▓▓▓
█▓▓▓▓▓▒▓▓▓▒▒▒▒░░░░░░░░▒███▒░░░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓
████▓▓▓▓▓▓▓▒▒▒▒░░░░░░░▓███▓▒░░░░░░░░░▒▒▒▒▒▓▓▓▓████
█▓█▓▓▓▓▒▓▓▓▒▒▒▒▒░░░░░▒▓██▓▓▒░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓█
█▓▓▓▓▓▒▒▒▓▓▒▒▒▒▒▒░░░░▒▓▓█▓▒▓░░░░░░░░▒▒▒▒▒▒▒▓▓▓▓▓▓█
███▓▓▓▓▒▒▒▒▓▒▒▒▒▒▒▒░░░▒▓▓▓▒▒░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓██
███▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒░░░▓▓▓▒░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓█
████▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░▓▓▓▒░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██
█████▓█▓▓▓▒▒▒▒▒░▒░░░░░░▒▓▓░░░░░░░░░▒▒▒▓▓▓▓▓▓▓▓████
███████▓▓▓▓▒▓▒▒▒▒░░░░░░▒▒▒░░░░░░░▒▒▒▒▒▓▓▓▓▓▓▓▓████
████▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░▒▒░░░░░░░▒▒▒▒▓▒▒▒▓▓▓▓▓▓▓▓▓
""", 'blue')
print(portal_img)

squirel_img = colored("""
                      
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▒▒▒▒▒▒░░░░░
░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▒░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▒▓░░░░░░░░░░
░░░░░░░░░░░░▒░░░░░░░▒▓▓▓▓▓▓▓▓▒▒░░░░░░░░░
░░░░░▓▒░░░░░▓░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░
░░░░░▒▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░
░░░░░░▒▓▓▓▓▓▒▒░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░
░░░░░░▒▓▓▒▒▓▒▒▒░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▒▒░░░░
░░░░░░░▒▒▒▒▒▓▓▒▓▒░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓░░░░
░░░░░░░▒▒▒▒▒▓▓▓▓▓▓▓▒░░░░░░▒▓▓▓▓▓▓▓▓▓▒░░░
░░░░░░░▒▓▒▒▒▓▓▓▓▓▓▓▓▒░░░░░▒▓▓▓▓▓▓▓▓▓▓░░░
░░░░░░░▒▓▓▒▓▓▓▓▓▓▓▓▒▒▒▒░░░▓▓▓▓▓▓▓▓▓▓▓░░░
░░░░░░▒▓▓▒░▒▒▒▒░░▒▒▒▒▒▓▒░▒▓▓▓▓█▓▓▓▓▓░░░░
░░░░░░▒▒░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓██▓▓▓▓▒░░░░
░░░░░▒▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓██▓▓▓▓▒░░░░░░
░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒░░░░░░░░░
░░░░░░░░░░░░▒▓▓▓▓▓▒▒▒▒▒▓▓▓▒░░░░░░░░░░░░░
░░░░░░░░░░░▒░▒▒▒▓▓▒▒▒▒▒▒▓▓▓▒▒▒▒░░░░░░░░░
░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
""", 'green')

print(squirel_img)