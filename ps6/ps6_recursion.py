# 6.00x Problem Set 6
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) == 0:
        return ''
    return aStr[-1] + reverseString(aStr[:-1]) 

#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if len(x) == 0:
        return True
    elif x[0] in word:
        idx = word.find(x[0])
        return x_ian(x[1:], word[idx:])
    else:
        return False 
        

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    if len(text) > lineLength:
        for idx in range(len(text[lineLength:])):
            if text[idx] == ' ':
                return text[:idx] + '\n' + str(insertNewlines(text[idx+1:], lineLength))
        return insertNewlines(text[idx:], lineLength)
    else:
        return text
   
   
print reverseString('simon')
print x_ian('eric', 'meritocracy')
print x_ian('john', 'mahjong')
print insertNewlines('Somewhere over the rainbow, there is a pot of gold.', 5)