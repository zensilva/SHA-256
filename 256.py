#################################################################################
##                                SHA - 256 Converter                          ##
##                         Date of development: February 11, 2022              ##
##                          Last modified: April 20, 2023                      ##
##                             Designed by: Zen K. Silva                       ##
#################################################################################

import hashlib
import getpass
import pyfiglet

ascii_banner = pyfiglet.figlet_format("SHA-" + "256".upper())
print(ascii_banner.lower())

print("           /\\")
print("          /__\\")
print("         /\\  /\\")
print("        /__\\/__\\")
print("       /\\      /\\")
print("      /__\\    /__\\")
print("     /\\  /\\  /\\  /\\")
print("    /__\\/__\\/__\\/__\\")

counter = 0

while True:
    text = getpass.getpass(prompt="\n\n. . . . . . .")
    if text == 'exit':
        break
    counter += 1
    print(f"\n--- session {counter} ---")
    try:
        sha256_hash = hashlib.sha256(text.encode()).hexdigest()
        print("\n\noutput:")
        print("-" * 50)
        print(sha256_hash)
        print("-" * 50)
    except:
        print("\nerror: invalid input.")

    answer = input("\n\nagain? (y/n): ").lower()
    if answer == "n" or answer == "no":
        break

input("\npress enter to exit.")
