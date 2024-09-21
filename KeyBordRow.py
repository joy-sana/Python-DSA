class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        q = 'qwertyuiopQWERTYUIOP'
        a = 'asdfghjklASDFGHJKL'
        z = 'zxcvbnmZXCVBNM'

        row = []

        for word in words:
            flag = False
            if word[0] in q:
                for char in word:
                    if char not in q:
                        flag = True

                if flag != True:
                    row.append(word)
                
            if word[0] in a:
                for char in word:
                    if char not in a:
                        flag = True
                 
                if flag != True:
                    row.append(word)

            if word[0] in z:
                for char in word:
                    if char not in z:
                        flag = True

                if flag != True:
                    row.append(word)

        return row
            
                    
                