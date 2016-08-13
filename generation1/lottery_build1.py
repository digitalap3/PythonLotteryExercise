##              LOTTERY BUILD 1
## TAKE CODE FROM POWERBALL BUILDS AND APPLY IT TO A GENERAL SCRIPT
## THAT WILL OPEN A FILE BASED ON USER INPUT: MEGA, PB, OR LOTTO
## AND GENERATE THE SPECIFIED DICTIONARIES/LISTS

import re


class Lottery:
    '''
    create specified lists for use in further comparisons and manipulations
    file is the file to open as a class arg
    '''

    def __init__(self,file):
        d = dict()
        self.d = d
        self.file = file

    def histogram_get(self, s, z=1):
        '''
        run the numbers and create dictionary counting the number of occurrences
        for each
        :param s: the list to be indexed and counted
        :return: the resulting dictionary
        '''

        if z == 0:
            for c in s: ## for lottery_nums
                self.d[c] = self.d.get(c,0) +1
        else: ## for single mega/pb
            self.d[s] = self.d.get(s,0) + 1
        return self.d

    def lottery_nums(self, z=None):
        '''
        :param z: limit to iterations if wanted, else read whole file
        also need to convert numbers to list so they are indexed correctly
        '''
        with open(self.file) as x:
            count = 0
            for y in x:
                count +=1
                if count == z: ##using '>' breaks with no arg for z
                    break
                lot_nums = re.search(r'\d+-\d+-\d+-\d+-\d+',y)
                num_list = (lot_nums.group()).split('-')
                self.histogram_get(num_list, 0)

        return self.d

    def mega_or_pb(self,z=None):
        '''
        return list of single mega or pb only
        :param z: limit to iterations through list if user wants
        :return:
        '''
        print('REMEMBER PB CHANGED RULES, NOW PB IS < 26\n')
        with open(self.file) as x:
            count = 0
            for y in x:
                count += 1
                if count == z:
                    break
                one_num_only = re.search(r'\d+$',y) ## mega or pb only
                single_list = (one_num_only.group())
                self.histogram_get(single_list)

        return self.d

# a = Lottery('megaball_numbers.txt')
# powerball = a.lottery_nums(10)
# print(powerball)
# print('total numbers in list: ',len(powerball))
# print('\nnumbers that have n or more hits:')
# for c in powerball:
#     if a.d[c] >= 2:
#         print('{0:4}-{1:4}'.format(c,a.d[c]))
#
# print('\n','*'*8,'\n')
#
# b = Lottery('megaball_numbers.txt')
# powerball2 = b.mega_or_pb(10)
# print(powerball2)
# print('total numbers in list: ',len(powerball2))
# print('\nnumbers that have n or more hits:')
# for c in powerball2:
#     if b.d[c] >= 2:
#         print('{0:4}-{1:4}'.format(c,b.d[c]))