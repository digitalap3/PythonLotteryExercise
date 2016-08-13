## BEGINNING OF 2.0 PROJECT.

import re

class ListCreator:

    def __init__(self,file):

        main_five = []
        main_one = []
        self.main_five = main_five
        self.main_one = main_one
        self.file = file
        #count = 0

    def results_five(self, z=None):

        f = 0
        with open(self.file) as x:
            count = 0
            for y in x:
                count += 1
                if count == z:  ##using '>' breaks with no arg for z
                    break
                lot_nums = re.search(r'\d+-\d+-\d+-\d+-\d+', y)
                num_list = (lot_nums.group()).split('-')
                self.main_five.append(num_list)

        return count, self.main_five, f

    def results_one(self, z=None): ##Not sure I need the z here since this is only for building a full list
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
                one_num = re.search(r'\d+$', y)  ## mega or pb only
                single_list = (one_num.group())
                self.main_one.append(single_list)

        return self.main_one

    def combo_test(self, z=None):

        with open(self.file) as x:
            count = 0
            for y in x:
                count +=1
                if count == z:
                    break
                lot_nums = re.search(r'\d+-\d+-\d+-\d+-\d+', y)
                num_list = (lot_nums.group()).split('-')
                self.main_five.append(num_list)
                one_num = re.search(r'\d+$', y)  ## mega or pb only
                single_list = (one_num.group())
                self.main_one.append(single_list)

        return count, self.main_five, self.main_one

class Histogram:

    def __init__(self, l=None): # l=None so invert_dict can run

        d = dict()  ## MAYBE CREATE NEW DICT IN run?? - SO SAME INSTANCE CAN BE REUSED / WHY??
        self.d = d
        self.l = l

    def histogram_run(self, f=1):

        if f == 0:
            for x in self.l:
                self.histogram_get(x)
        else:
            for x in self.l:
                self.histogram_get(x,0)

        return self.d


    def histogram_get(self, s, f=1):

        if f == 0:
            for c in s:  ## for lottery_nums
                self.d[c] = self.d.get(c, 0) + 1
        else:  ## for single mega/pb
            self.d[s] = self.d.get(s, 0) + 1
        return self.d

    def invert_dict(self, dic):
        self.dic = dic
        inverse = dict()
        for key in self.dic:
            val = self.dic[key]
            if val not in inverse:
                inverse[val] = [key]
            else:
                inverse[val].append(key)
        return inverse


if __name__ == '__main__':
    '''
    put code for testing here
    '''
    print('this will be the area for test code')

    #x = ListCreator('megaball_numbers.txt')
    #y = x.results_five(100) ## MASTER LIST - NO ITERATION LIMIT WILL BE NEEDED OTHER THAN THESE INITIAL TESTS
                            ## LIST WILL BE SLICED TO PRODUCE ITERATIONS
    #print(y)
    #z = x.results_one(100) ## MASTER SINGLE RESULT LIST, SEE ABOVE
    #print(z)
    #a = Histogram(y[1]).histogram_run()
    #print(a)
    #b = Histogram(z).histogram_run(0)  ## NOTE THE ZERO FOR SINGLE RESULT RUNS
    #print(b)
    # m = ListCreator('megaball_numbers.txt')
    # n = m.combo_test(10)
    # #print(n)
    # o = Histogram(n[1]).histogram_run()
    # p = Histogram(n[2]).histogram_run(0)
    # print(o,'\n',p)
    # q = (n[1])[0]
    # print(q)
    # print('this is the value (number of ocurrence) for key (result) {0} : {1}'.format(q[0],o[q[0]]))
    # r = Histogram().invert_dict(o)
    # print(r)
    # for x in r:
    #     print(x,r[x])
