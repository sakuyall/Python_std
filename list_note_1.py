# -the_list-1/7/25--------------------------------------------------------
rhyme = [1,2,3,4,5,"tiger"]
print(rhyme)
for a in rhyme:
    print(a)
print(rhyme[5])                  # from 0 to n
print(rhyme[::-1])               # fron n to 0  //or use rhyme.reverse()

rhyme.append()                   # to add one n+1
rhyme.extend()                   # to add several n+1,n+2,...
rhyme[len(s):] = [etc...]        # a easier way to SLICE

rhyme.insert(address,feature)    # to add a feature in position
rhyme.remove(feature)            # to remove a feature

rhyme[address] = feature         # to replace a feature
rhyme[0:1] = [feature0,feature1] # use the slice to replace features

rhyme.pop(address)               # to kick a feature
rhyme.clear                      # clear the list

rythme.sort()                    # auto arrangement
rhyme.reverse()                  # reverse features

rhyme.index(feature,st,ed)       # find the address of a certain feature
rhyme[rhyme.index(feature)] = feature0  # replace the last feature in a same address

rhyme1 = rhyme.copy()            # copy to another list or//
rhyme1 = rhyme[:]                # such methods are shallow copy
