##              LOTTERY BUILD 3
## MAINLY TO KEEP IN LINE WITH RUN SCRIPT.  CLEAN UP CODE AND ADD NUMLIST TO MEGAPB FUNCTION

import re


class Lottery:
    '''
    create specified lists for use in further comparisons and manipulations
    file is the file to open as a class arg
    '''

    def __init__(self,file):
        d = dict()
        numlist = []
        self.d = d
        self.file = file
        self.numlist = numlist

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
        :param self.d: dict counter of frequency of numbers
        :param count: number of iterations = number of results/length of list
        :param self.numlist: ordered list of all number sequences
        '''
        with open(self.file) as x:
            count = 0
            for y in x:
                count +=1
                if count == z: ##using '>' breaks with no arg for z
                    break
                lot_nums = re.search(r'\d+-\d+-\d+-\d+-\d+',y)
                num_list = (lot_nums.group()).split('-')
                self.numlist.append(num_list)
                self.histogram_get(num_list, 0)

        return self.d, count, self.numlist

    def mega_or_pb(self,z=None):
        '''
        return list of single mega or pb only
        :param z: limit to iterations through list if user wants
        :return:
        '''

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
