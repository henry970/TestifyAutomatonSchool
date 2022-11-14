#   Write  a  Python  program  that  checks  if  a  string  is  apalindrome,
#   Then  optionally  write  a  unit  test  to  checkyour program's correctness

def is_a_palindrome(string):
    if string == string[::-1]:
        print("Is Palindrome")




is_a_palindrome("memes")
is_a_palindrome("madam")
is_a_palindrome("raddar")
is_a_palindrome("Daified")
is_a_palindrome("2/22/22")
