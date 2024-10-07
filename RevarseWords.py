def reverseWords( s):
    """
    :type s: str
    :rtype: str
    """
    words = s.split()
    word = ''

    for i in words[:0:-1]:
        word = word + i + " "
    word += words[0]

    return word
