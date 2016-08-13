##   AUTOMATE BESTNUMS SELECTION
## UNABLE TO AUTOMATE BECAUSE OF RULE CHANGE!!  NEED TO FIND A WAY TO DEAL WITH THAT.
## MADE IF STATEMENTS BASED ON SELF.GAME FOR NOW
## ADD ANOTHER WINNING CLASS FOR PICKING NUMBERS THAT HAVEN'T COME UP LATELY

import re
import os
import json
from random import sample
from sortedcontainers import SortedDict


class Histogram:
    def __init__(self, l=None):  # l=None so invert_dict can run

        d = dict()
        self.d = d
        self.l = l

    def histogram_run(self, f=1):

        if f == 0:
            for x in self.l:
                self.histogram_get(x)
        else:
            for x in self.l:
                self.histogram_get(x, 0)

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


class MakeLists_Counters:
    def __init__(self, game, file):  ##TODO: check for folders 'game' and mkdir if not

        self.main_five = []
        self.main_one = []
        self.game = game
        self.file = file

    def list_creator(self, file, z=None):

        with open(self.file) as x:
            count = 0
            for y in x:
                count += 1
                if count == z:
                    break
                lot_nums = re.search(r'\d+-\d+-\d+-\d+-\d+', y)
                num_list = (lot_nums.group()).split('-')
                self.main_five.append(num_list)
                one_num = re.search(r'\d+$', y)  ## mega or pb only
                single_list = (one_num.group())
                self.main_one.append(single_list)

        return count, self.main_five, self.main_one

    def make_lists(self):

        if not os.path.exists('{0}/masterlist_{1}'.format(self.game, self.game)):
            with open('{0}/masterlist_{1}'.format(self.game, self.game), 'w') as f:
                master_list = self.list_creator(self.file)  ##'{}_numbers.txt'.format(self.game)
                json.dump(master_list, f)
        else:
            with open('{0}/masterlist_{1}'.format(self.game, self.game)) as f:
                master_list = json.load(f)

        five_results = master_list[1]
        one_results = master_list[2]
        result_count = master_list[0]

        return master_list, five_results, one_results, result_count

    def make_counters(self):

        master_list, five_results, one_results, result_count = self.make_lists()

        if not os.path.exists('{0}/fivecountdict_{1}'.format(self.game, self.game)):
            with open('{0}/fivecountdict_{1}'.format(self.game, self.game), 'w') as f:
                full_five = Histogram(five_results).histogram_run()
                json.dump(full_five, f, sort_keys=True)

        with open('{0}/fivecountdict_{1}'.format(self.game, self.game)) as f:
            full_five_count = json.load(f)

        if not os.path.exists('{0}/shortfivecountdict_{1}'.format(self.game, self.game)):
            with open('{0}/shortfivecountdict_{1}'.format(self.game, self.game), 'w') as f:
                short_results = five_results[:290]
                short_five = Histogram(short_results).histogram_run()
                if self.game == 'powerball':
                    short_five = {x: short_five[x] for x in short_five.keys() if int(x) > 59}
                if self.game == 'megaball':
                    short_five = {x: short_five[x] for x in short_five.keys() if int(x) > 56}
                json.dump(short_five, f, sort_keys=True)

        with open('{0}/shortfivecountdict_{1}'.format(self.game, self.game)) as f:
            short_five_count = json.load(f)


        if not os.path.exists('{0}/onecountdict_{1}'.format(self.game, self.game)):
            with open('{0}/onecountdict_{1}'.format(self.game, self.game), 'w') as f:
                full_one = Histogram(one_results).histogram_run(0)
                json.dump(full_one, f, sort_keys=True)

        with open('{0}/onecountdict_{1}'.format(self.game, self.game)) as f:
            full_one_count = json.load(f)

        if not os.path.exists('{0}/invertfivedict_{1}'.format(self.game, self.game)):
            with open('{0}/invertfivedict_{1}'.format(self.game, self.game), 'w') as f:
                inv_five = Histogram().invert_dict(full_five_count)
                json.dump(inv_five, f, sort_keys=True)  # well shit that works!!!

        with open('{0}/invertfivedict_{1}'.format(self.game, self.game)) as f:
            inv_five = json.load(f)

        if not os.path.exists('{0}/invertshort_{1}'.format(self.game, self.game)):
            with open('{0}/invertshort_{1}'.format(self.game, self.game), 'w') as f:
                pass

        if not os.path.exists('{0}/invertonedict_{1}'.format(self.game, self.game)):
            with open('{0}/invertonedict_{1}'.format(self.game, self.game), 'w') as f:
                inv_one = Histogram().invert_dict(full_one_count)
                json.dump(inv_one, f, sort_keys=True)

        with open('{0}/invertonedict_{1}'.format(self.game, self.game)) as f:
            inv_one = json.load(f)

        return full_five_count, short_five_count, full_one_count, inv_five, inv_one


class Action_Lists:

    def __init__(self, game):

        self.game = game
        self.file = '{}_numbers.txt'.format(self.game)

        self.master_list, self.five_results, self.one_results, self.result_count = \
            MakeLists_Counters(self.game, self.file).make_lists()

        self.full_five_count, self.short_five_count, self.full_one_count, self.inv_five, self.inv_one = \
            MakeLists_Counters(self.game, self.file).make_counters()

    def percent_to_file(self):
        '''
        PATTERN FINDER
        SHOWING PERCENTAGES OF LAST 50 RESULTS
        THIS NEEDS TO BE REDONE TO REFLECT DIFFERENCES BASED ON RULE CHANGE
        PERCENTAGE PULLED FROM WHOLE LIST FOR LOW #'S AND SINCE RULE CHANGE FOR HIGHER
        :return:
        '''

        if not os.path.exists('{0}/percentfile_{1}'.format(self.game, self.game)):
            with open('{0}/percentfile_{1}'.format(self.game, self.game), 'w') as g:
                g.write('total results : {}\n'.format(self.result_count))
                for x in range(50):
                    recent = self.five_results[x]
                    rec_one = self.one_results[x]
                    g.write('---{}---\n\n'.format(x))
                    for y in recent:
                        m = self.full_five_count[y]
                        n = (m / self.result_count) * 100
                        g.write('{0} : {1:.2f} prcnt\n'.format(y, n))
                    o = self.full_one_count[rec_one]
                    p = (o / self.result_count) * 100
                    g.write('{0} {1} : {2:.2f} prcnt\n\n'.format(self.game, rec_one, p))
                    g.write('*' * 10)
                    g.write('\n\n')
            print('done')

    def count_to_file(self):
        '''
        PATTERN FINDER
        SHOWING OVERALL COUNTS OF LAST 50 RESULTS
        ?? NOT USEFUL WITHOUT TAKING INTO ACCOUNT RULE CHANGE ??
        :return:
        '''
        if not os.path.exists('{0}/countfile_{1}'.format(self.game, self.game)):
            with open('{0}/countfile_{1}'.format(self.game, self.game), 'w') as g:
                g.write('total results : {}\n'.format(self.result_count))
                for x in range(50):
                    recent = self.five_results[x]
                    rec_one = self.one_results[x]
                    g.write('---{}---\n\n'.format(x))
                    for y in recent:
                        m = self.full_five_count[y]
                        g.write('{0} : {1}\n'.format(y, m))
                    o = self.full_one_count[rec_one]
                    g.write('{0} {1} : {2}\n\n'.format(self.game, rec_one, o))
                    g.write('*' * 10)
                    g.write('\n\n')
            print('done')

    def numcount_to_file(self):  ## THE COUNT OF THE COUNTS FROM ABOVE (IE NUMBER OF TIMES 67COUNT HAPPENS
        '''
        used to generate 'bestnums' in result lists below
        :return:
        '''
        if not os.path.exists('{0}/numcountfile_{1}'.format(self.game, self.game)):
            numcountlst = []
            for x in range(600):  ## WHY NOT THE WHOLE LIST?
                recent = self.five_results[x]
                for y in recent:
                    m = self.full_five_count[y]
                    numcountlst.append(m)

            numcntdict = Histogram(numcountlst).histogram_run(0)

            with open('{0}/numcountfile_{1}'.format(self.game, self.game), 'w') as g:
                invnumcnt = Histogram().invert_dict(numcntdict)
                json.dump(invnumcnt, g, sort_keys=True)

    def ballcount_to_file(self):
        '''
        used to generate 'bestnums' for file below
        :return:
        '''
        if not os.path.exists('{0}/ballcountfile_{1}'.format(self.game, self.game)):
            numcountlst = []
            for x in range(600):
                rec_one = self.one_results[x]
                m = self.full_one_count[rec_one]
                numcountlst.append(m)

            ballcntdict = Histogram(numcountlst).histogram_run(0)

            with open('{0}/ballcountfile_{1}'.format(self.game, self.game), 'w') as g:
                invballcnt = Histogram().invert_dict(ballcntdict)
                json.dump(invballcnt, g, sort_keys=True)

    def best_nums_short(self):
        d = self.short_five_count
        best_nums_count = SortedDict({int(y): d[y] for y in d.keys()})
        a = len(best_nums_count)
        best_nums = []
        for z in range(a - 4, a):
            best_nums.append(best_nums_count.values()[z])
        return best_nums

    def list_of_balls(self):
        listoflist = []

        if self.game == 'megaball':
            #bestnums = [39, 34, 29, 24] ##megaball - picked from ballcount_to_file TODO: automate this
            bestnums = [40, 36, 35] ## for winning.not_recent
        else:
            bestnums = [21, 20, 19, 16]  ##powerbal
        #bestnums = self.best_nums()

        with open('{0}/invertonedict_{1}'.format(self.game, self.game)) as f:
            lstdict = json.load(f)
            for x in bestnums:
                if str(x) in lstdict:
                    listoflist.append(lstdict[str(x)])

        return listoflist

    def list_of_results2(self):
        '''
        best hits from full list all the way to beginning - before 57 to 72 were added
        these are the highest hits - ie no 57-72 results show in this list
        :return:
        '''
        listoflist = []

        if self.game == 'megaball':
            #bestnums = [72, 78, 80, 67]## megaball
            bestnums = [93, 87, 86, 85, 84, 83, 82, 81, 25, 21, 20] ## for winning.not_recent
        else:
            bestnums = [50, 61, 57, 53]  ##powerball

        with open('{0}/invertfivedict_{1}'.format(self.game, self.game)) as f:
            lstdict = json.load(f)
            for x in bestnums:
                if str(x) in lstdict:
                    listoflist.append(lstdict[str(x)])

        return listoflist

    def list_of_results3(self):
        '''
        these are the highest hits for 57 -72 result range
        :return:
        '''
        listoflist = []

        if self.game == 'megaball':
            bestnums = [24, 20, 19]##megaball
        else:
            bestnums = [8, 4, 6]  ##powerball
        #bestnums = self.best_nums_short()
        with open('{0}/invertfivedict_{1}'.format(self.game, self.game)) as f:
            lstdict = json.load(f)
            for x in bestnums:
                if str(x) in lstdict:
                    listoflist.append(lstdict[str(x)])

        return listoflist


class Winning(Action_Lists):
    '''
    various actions to produce results from the dicts and lists generated
    '''

    def winnerballs(self):
        a = self.list_of_balls()
        finalball = [z for x in a for z in x]
        winnerball = sample(finalball, 3)
        return winnerball

    def winnerlo(self):
        a = self.list_of_results2()
        finallo = [z for x in a for z in x]
        winnerlo = sample(finallo, 5)
        return sorted(winnerlo)

    def winner4lo(self):
        a = self.list_of_results2()
        b = self.list_of_results3()
        final4lo = [z for x in a for z in x]
        final1hi = [z for x in b for z in x]
        winnerlo = sample(final4lo, 4)
        winnerhi = sample(final1hi, 1)
        winner = winnerlo + winnerhi
        return sorted(winner)

    def winner3lo(self):
        a = self.list_of_results2()
        b = self.list_of_results3()
        final4lo = [z for x in a for z in x]
        final1hi = [z for x in b for z in x]
        winnerlo = sample(final4lo, 3)
        winnerhi = sample(final1hi, 2)
        winner = winnerlo + winnerhi
        return sorted(winner)

    def not_recent(self, n):
        self.n = n
        res = []
        a = self.list_of_results2() ##take these and make them class attributes
        b = self.list_of_balls()
        #print(b)
        hires = [z for x in a for z in x]
        hiball = [z for x in b for z in x]
        print(hiball)
        print(hires)
        for lst in self.five_results[:n]:
            #print(lst)
            for x in lst:
                if x in hires:
                    hires.remove(x)
        for ball in self.one_results[:n]:
            #print(ball)
            if ball in hiball:
                hiball.remove(ball)
        return hires, hiball


if __name__ == '__main__':
    '''
    put code for testing here
    '''
    print('this will be the area for test code')


