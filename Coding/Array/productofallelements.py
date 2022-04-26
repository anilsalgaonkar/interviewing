def find_product(lst):
    # get product start from left
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele
    # get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1): 
        product[i] = product[i] * right
        right = right * lst[i]

    return product


print(find_product([4, 5, 2, 3]))