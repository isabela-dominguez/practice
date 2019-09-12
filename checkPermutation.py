def checkPermutation(word1, word2):
    if((len(word1) != len(word2))):
        return False

    word1 = ''.join(sorted(word1))
    word2 = ''.join(sorted(word2))

    #if(word1 == word2):
      #  return True
    #else:
     #   return False 

    return word1 == word2


print(checkPermutation("aabb", "bbab"))