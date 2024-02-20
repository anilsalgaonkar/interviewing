'''
# Synonym Lists

# Given a list of synomym word string pairs, determine if two strings of word sequences are synomym sequences. This requires words in the same positions in each sequence to be synonyms of each other.

# synonyms = [
#     ["Lebron", "James"],
#     [“wins”, “awarded”],
#.    ["James", "LBJ"]
# ]

#   Example queries:
#  1 "Lebron awarded mvp", “James wins mvp" -> True
#  2 "Lebron wins mvp", "Lebron granted mvp" -> False,  granted is not a synonym of wins
#  3 "Lebron James wins mvp", "LBJ wins mvp" -> False , different number of words
#  4 "LBJ awarded mvp", "James awarded mvp" -> True
#  5 "Lebron awarded mvp", "mvp awarded James" -> False, synonyms in different positions
#  6 "Lebron wins awarded mvp", "Lebron James wins mvp" -> False, different # of synonyms


boolean areSynonymSequences(List<List<String>> synonyms, String query1, String query2)

 */
'''

synonyms = [
    ['Lebron', 'James'],
    ['wins', 'awarded'],
    ['James', 'LBJ']
]

# {
#     'lebron': "james",
#     'james' : 'lebron',

# }


def evaluate(synonyms, first, second):
    first = first.strip()
    second = second.strip()
    
    first = first.split(" ")
    second = second.split(" ")
    if len(first) != len(second):
        return False
        
    syn_map= {}
    for f, s in synonyms:
        
        if f in syn_map :
            for key in syn_map[f]:
                syn_map[key] = syn_map.get(key, []) + [s]
                syn_map[s] = syn_map.get(key, []) + [key]
        
        
                
        syn_map[f] = syn_map.get(f, []) + [s]
        syn_map[s] = syn_map.get(s, []) + [f]

        
        
    print(syn_map)
    
    
    for i in range(len(first)):
        if first[i] != second[i]:
            if not check_synonym(first[i], second[i], syn_map):
                return False
    return True


def check_synonym(first, second, syn_map):
    if second in syn_map[first]:
        return True
    else:
        return False
       
            
print(evaluate(synonyms, 'Lebron awarded mvp', 'James wins mvp'))
print(evaluate(synonyms, "LBJ awarded mvp", "James awarded mvp"))
print(evaluate(synonyms, "Lebron wins mvp", "Lebron granted mvp"))
print(evaluate(synonyms, 'Lebron awarded mvp', 'LBJ awarded mvp')) # True
print(evaluate(synonyms, 'LBJ awarded mvp', 'Lebron awarded mvp')) # True
        





