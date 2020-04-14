import re
import random

input_string = "hello world! i love you mister obama"
regex_patterns = {r"l": "w",
                  r"r": "w",
                  r"tt": "dd",
                  r"!+": "! owo",
                  r"?+": "? uwu"}

full_stop_replacements = [".",". owo","!!!!", ". uwu",]

while True:
    input_string = input("Enter sentence: ").lower()
    for pattern, replace in regex_patterns.items():
        try:
            input_string = re.sub(pattern, replace, input_string)
        except re.error:
            pass
    print(input_string)





