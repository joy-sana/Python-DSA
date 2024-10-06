
def mergeAlternately( word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    i = 0
    word3 = ''
    while (i < len(word1) and i < len(word2)):
        word3 += word1[i]
        word3 += word2[i]
        i+=1
    while i < len(word2):
        word3 += word2[i]
        i+=1
    while i < len(word1) :
        word3 += word1[i]
        i+=1

    return word3