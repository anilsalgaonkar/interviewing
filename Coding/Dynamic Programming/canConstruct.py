# find if you can construct a given word using a list of word array.

#solution using recursion
def canConstruct(target_word, word_arr):
    #print("Hello")
    if(target_word ==''): return True
    for word in word_arr:
        print(target_word, word)
        if(target_word.find(word) == 0):
            if(canConstruct(target_word[len(word):],word_arr)): return True
        
    return False

#print(canConstruct('abcdef',['ab','abc', 'cd','def','abcd']))

# solution using memoization
def canConstructMemo(target_word, word_arr, memo = {}):
    if (target_word in memo): return memo[target_word]
    if(target_word ==''): return True

    for word in word_arr:
        print(target_word, word)
        if(target_word.find(word) == 0):
            suffix = target_word[len(word):]

            if(canConstructMemo(suffix,word_arr,memo)):
                memo[suffix] = True 
                return memo[suffix]        
    memo[target_word] = False
    return False

print(canConstructMemo('abcdef',['ab','abc', 'cd','eef','abcd'],{}))