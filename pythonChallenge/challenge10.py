# Create a function that converts any string value to a Sentence  case,
# Then  write  a  unit  test  that  checks  thefunction's correctness.


def sentence_case(s):
    sentence = "the cow can run"
    return sentence.capitalize()


print(sentence_case("the cow can run"))