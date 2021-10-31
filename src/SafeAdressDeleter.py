list1 = []
list2 = []

with open("HostsList.txt") as f:
    list1 = f.readlines()

with open("SafeDomains.txt") as f:
    list2 = f.readlines()

# https://raw.githubusercontent.com/EnergizedProtection/unblock/master/basic/formats/domains.txt

list_diff = list(set(list1) - set(list2))

with open('new.txt', 'w') as f:
    for item in list_diff:
        f.write("%s" % item)