#The dumbest way to solve josephus.py, you probably do not need this, 
#hell even I don't need this
def josephus(items,k):
    #Since we need only the order in which items are deleted,
    #it is better to create a new list which contains the indices of all items
    item = []
    for index, _ in enumerate(items):
        item.append(index)
    deleted_var = []
    start = k
    #Due to the zero formatting, in this code you encounter many instances of using "smth - 1"
    while item:
        if len(item) >= k:
            del_val = item[start-1::k]
            #In each iteration del function starts from the indicated starting point,
            #but since we permutating as if the list of items were in circle, 
            #we should change the starting point in each iteration
            #Start_val is the starting value for our next iteration
            #in order to find that we should find out how many items are left until the last item
            #and we should subtract value from k in order to find which value should we delete next
            start_val = k - ((len(item)-1)  - item.index(del_val[-1]))  
            del item[start-1::k]
        else:
        #When k is bigger than the number of items, we delete only one item in each iteration
        #this value is equal to our "start", but sometimes our "start" is also bigger than
        #the number of items. Then we should subtract the number of items from start until start is
        #less than the number of items
            while start > len(item):
                start -=len(item)
            del_val = [item[start-1]]
            # 
            start_val = k - ((len(item)-1)  - item.index(del_val[-1])) 
            del item[start-1]
        start = start_val
        #lastly we extend our deleted_var list by the items in "items" list with indexes
        #similar to del_val values
        deleted_var.extend([items[i] for i in del_val])
        print(deleted_var)
        
    return deleted_var