# Write  a  function  that  removes  repeated  characters from a string.
# Sample Strings are: a. Hello: output shouldbe Helo b. Concatenate:
# output should be Conatent

def remove_repeated_cha(string):
    not_repeated = ""
    for char in string.lower():
        if char not in not_repeated:
            not_repeated +=char
    print(not_repeated)


remove_repeated_cha("Hello")
remove_repeated_cha("Concatenate")




