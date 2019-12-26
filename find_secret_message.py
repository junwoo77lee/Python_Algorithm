from typing import List

# Find a secret message in a code
# for example, if you are looking for the message "swordfish" inside the code "pqsoiwoqcrldfweiqwsh",
# You can find it by using the greedy algorithm


def find_secret_message(message: str, code:str) -> bool:
    # try to find a secret message inside the code, then return a boolean value whether it is found or not.
    index = 0
    found = ''
    for letter in message:
        while index < len(code):
            if code[index] == letter:
                found += letter
                break
            index += 1
    
    return True if found == message else False