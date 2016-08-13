##          BUILD 2B
##CLEAN UP AND PUT IN WITH STATEMENT SO FILE CLOSES

import re


class Powerball:
    '''
    create specified lists for use in further comparisons and manipulations
    '''

    def __init__(self):
        d = dict()
        self.d = d

    def histogram_get(self, s, z=1):
        '''
        run the numbers and create dictionary counting the number of occurrences
        for each
        :param s: the list to be indexed and counted
        :return: the resulting dictionary
        '''

        if z == 0:
            for c in s: ## for powerball_nums
                self.d[c] = self.d.get(c,0) +1
        else: ## for powerball_pb
            self.d[s] = self.d.get(s,0) + 1
        return self.d

    def powerball_nums(self, z=None):
        '''
        :param z: limit to iterations if wanted, else read whole file
        also need to convert numbers to list so they are indexed correctly
        '''
        with open('powerball_numbers.txt') as x:
            count = 0
            for y in x:
                count +=1
                if count == z: ##using '>' breaks with no arg for z
                    break
                pbnums = re.search(r'\d+-\d+-\d+-\d+-\d+',y)
                pbnum_list = (pbnums.group()).split('-')
                self.histogram_get(pbnum_list, 0)

        return self.d

    def powerball_pb(self,z=None):
        '''
        return list of powerballs only
        :param z:
        :return:
        '''
        print('REMEMBER PB CHANGED RULES, NOW PB IS < 26\n')
        with open('powerball_numbers.txt') as x:
            count = 0
            for y in x:
                count += 1
                if count == z:
                    break
                pbonly = re.search(r'\d+$',y) ## powerball only
                pb_list = (pbonly.group())
                self.histogram_get(pb_list)

        return self.d

a = Powerball()
powerball = a.powerball_nums(10)
print(powerball)
print('total numbers in list: ',len(powerball))
print('\nnumbers that have n or more hits:')
for c in powerball:
    if a.d[c] >= 2:
        print('{0:4}-{1:4}'.format(c,a.d[c]))

print('\n','*'*8,'\n')

b = Powerball()
powerball2 = b.powerball_pb(10)
print(powerball2)
print('total numbers in list: ',len(powerball2))
print('\nnumbers that have n or more hits:')
for c in powerball2:
    if b.d[c] >= 2:
        print('{0:4}-{1:4}'.format(c,b.d[c]))