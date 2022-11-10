'''
Write a function that takes a sentence as an input
parameter where each word in the sentence is
separated by a space. The function should replace
each blank with a hyphen and then return the
modified sentence.
'''
def fun(sent):
    sent = sent.replace(" ", "-")
    return sent

print(fun("Mandar Hemraj Patil"))

