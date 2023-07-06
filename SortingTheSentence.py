def sortSentence(self, s: str) -> str:
        words =  s.split(' ')
        sorted = [None] * len(words)
        for word in words:
           position =  int( word[-1] ) -1
           text = word[:-1] 
           sorted[position] = text
        return ' '.join(sorted)
