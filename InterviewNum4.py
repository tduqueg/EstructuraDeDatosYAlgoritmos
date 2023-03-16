def anagram(word1,word2):
    word1 = sorted(word1)
    word2 = sorted(word2)

    if word2 == word1:
        return True
    return False

if __name__ == '__main__':
    print(anagram("banano","anonba"))
