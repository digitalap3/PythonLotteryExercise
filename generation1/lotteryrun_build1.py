import lottery_build1 as lb

game = input('which game?(powerball or megaball):  ')

five_nums = lb.Lottery('{}_numbers.txt'.format(game))
one_num = lb.Lottery('{}_numbers.txt'.format(game))

## CREATE DICTIONARIES TO MANIPULATE

## FULL LIST
full_list_five = five_nums.lottery_nums()
full_list_one = five_nums.mega_or_pb()

## TOP HALF - REFER TO TESTCODE.PY - USING COUNT TO GET TXT LENGTH TO USE FOR THESE CALCULATIONS
## NEW SCRIPTS - ALL TO 2
#top_half_five = five_nums.lottery_nums(


powerball = five_nums.lottery_nums(10)
print(powerball)
print('total numbers in list: ',len(powerball[0]))
print('\nnumbers that have n or more hits:')
for c in powerball[0]:
    if five_nums.d[c] >= 2:  ## THIS COULD BE A PROBLEM - WOULD HAVE TO BE REWRITTEN FOR EACH LIST??  NO.
        print('{0:4}-{1:4}'.format(c,five_nums.d[c]))

print('\n','*'*8,'\n')

powerball2 = one_num.mega_or_pb(10)
print(powerball2)
print('total numbers in list: ',len(powerball2))
print('\nnumbers that have n or more hits:')
for c in powerball2:
    if one_num.d[c] >= 2:
        print('{0:4}-{1:4}'.format(c,one_num.d[c]))