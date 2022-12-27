# String utilities

def replaceAt(s, i, c):
    '''
    Replaces a portion of a string starting at the given index with another string

    Returns the new string
    
    s   - string to be replaced
    i   - index to start the replacement
    c   - replacement string 
    '''
    if i >= 0:
        out = s[:i] + c + s[i+len(c):]
    else:
        return s[:i] + c + s[len(s)+i+len(c):]
    return out
