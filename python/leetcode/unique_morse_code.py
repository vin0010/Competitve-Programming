"""

"""


def unique_morse_representations(words):
    my_map = {"a": ".-",
              "b": "-...",
              "c": "-.-.",
              "d": "-..",
              "e": ".",
              "f": "..-.",
              "g": "--.",
              "h": "....",
              "i": "..",
              "j": ".---",
              "k": "-.-",
              "l": ".-..",
              "m": "--",
              "n": "-.",
              "o": "---",
              "p": ".--.",
              "q": "--.-",
              "r": ".-.",
              "s": "...",
              "t": "-",
              "u": "..-",
              "v": "...-",
              "w": ".--",
              "x": "-..-",
              "y": "-.--",
              "z": "--.."}
    result_set=set()
    for word in words:
        result = ""
        for i in word:
            result += my_map[i.lower()]
        result_set.add(result)
    return len(result_set)
    # print(len(result_set))


unique_morse_representations(["gin", "zen", "gig", "msg"])
