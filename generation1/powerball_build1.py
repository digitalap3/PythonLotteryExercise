import re

d = dict() ##this is a problem until I use a class and can create instances
            #since it's being used by both functions and won't be cleared automatically like here
e = dict()

def histogram_get(s, z=1):
    '''
    run the numbers and create dictionary counting the number of occurrences
    for each
    :param s: the list to be indexed and counted
    :return: the resulting dictionary
    '''
    #print(s)
    global d
    if z == 0:
        for c in s:
            d[c] = d.get(c,0) +1
    else:
        d[s] = d.get(s,0) + 1
    return d

def powerball_nums(z=None):
    '''
    :param z: limit to iterations if wanted, else read whole file
    also need to convert numbers to list so they are indexed correctly
    '''
    x = open('powerball_numbers.txt')
    count = 0
    for y in x:

        #print(y)
        count +=1
        if count == z: ##using '>' breaks with no arg for z
            break
        pbnums = re.search(r'\d+-\d+-\d+-\d+-\d+',y)
        #print(pbnums.group())
        #print(nums.group())
        pbnum_list = (pbnums.group()).split('-')
        histogram_get(pbnum_list, 0)

    global d
    return d

def powerball_pb(z=None):
    '''
    return list of powerballs only
    :param z:
    :return:
    '''
    x = open('powerball_numbers.txt')
    count = 0
    for y in x:
        count += 1
        #print(y) #debug - make sure correct lines being referenced
        if count == z:
            break
        pbonly = re.search(r'\d+$',y) ## powerball only
        #print(pbonly.group())
        pb_list = (pbonly.group())
        histogram_get(pb_list)
    x.close()
    if x.closed:
        print('closed')
    global d
    return d

#powerball = powerball_nums(10)
powerball = powerball_pb(10)
print(powerball)
print('total numbers in list: ',len(powerball))
print('\nnumbers that have n or more hits:')
for c in powerball:
    if d[c] >= 2:
        print('{0:4}-{1:4}'.format(c,d[c]))