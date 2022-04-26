# count the number of ways a given word can be constructed from a list of words

def count_construct(target_word, word_list):
    #base case
    if(target_word == ''): return 1
    count = 0
    for word in word_list :
        if(target_word.find(word) == 0):
            suffix = target_word[len(word):]
            print(word,suffix)
            num_of_ways_to_return = count_construct(suffix, word_list)
            count += num_of_ways_to_return
    return count


print(count_construct('abcdef',['ab','abc', 'c','def','abcd', 'ef']))
#print(count_construct('aaaaaaaaaaaaaab',['a','aa', 'aaa','aaaa','aaaaa','aaaaaa']))


def count_construct_with_memo(target_word, word_list,memo={}):
    #base case
    if(target_word in memo): return memo[target_word]
    if(target_word == ''): return 1
    count = 0
    for word in word_list :
        if(target_word.find(word) == 0):
            suffix = target_word[len(word):]
            print(word,suffix)
            num_of_ways_to_return = count_construct_with_memo(suffix, word_list,memo)
            count += num_of_ways_to_return
    memo[target_word] = count
    return memo[target_word]


print(count_construct_with_memo('abcdef',['ab','abc', 'c','def','abcd', 'ef'],{}))
print(count_construct_with_memo('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab',['a','aa', 'aaa','aaaa','aaaaa','aaaaaa'],{}))
