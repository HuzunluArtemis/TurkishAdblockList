list1 = []
list2 = []
list_diff = []

with open("HostsList.txt") as f:
    list1 = f.readlines()

with open("new.txt") as f:
    list2 = f.readlines()
    
def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]



with open('diff.txt', 'w') as f:
    for item in diff(list1,list2):
        f.write("%s" % item)