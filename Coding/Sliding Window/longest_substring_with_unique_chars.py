'''
This solution finds the longest word for each start pointer.
start pointer points to the next character once the longest word has been found for that pointer.
longest_str keeps track of the longest word found so far and gets returned once we reach to the end of the string.

This has time complexity of O(n(n+1)/2) ~ n^2
'''
def longest_str_with_unique_chars(input):
    longest_str = ""
    temp_str = ""
    for start_pointer in range(len(input)):
        i = start_pointer
        while i < len(input) and input[i] not in temp_str:
                temp_str += input[i]
                i +=1
        longest_str = longest_str if len(longest_str)>len(temp_str) else temp_str
        temp_str = ""
    return longest_str

print(longest_str_with_unique_chars("abcabcbb"))

'''
This is a sliding window solution
we maintain 2 pointers left and right
move right pointer until the non unique condition is true
move left pointer until the non unique condition is false
for each right move store the longest unique string so far between left and right pointers 

'''
def longest_str_with_unique_chars_sliding(input):
    left,right = 0,0
    temp_map={}
    temp_window = ""
    longest_str=""
    while right < len(input):
        char = input[right]
        temp_window += char
        if char not in temp_map:
            temp_map[char] = 1
        else:
            temp_map[char] += 1
        
        while (left <= right and temp_map[char] > 1):
            if input[left] == char:
                temp_map[char] -= 1
            temp_window = temp_window[1:]
            left += 1
        right += 1
        longest_str = longest_str if len(longest_str)>len(temp_window) else temp_window
    return longest_str

while True:
    input_string = input("Enter input string:")
    print(longest_str_with_unique_chars_sliding(input_string))