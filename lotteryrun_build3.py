import lottery_build3 as lb  ##BE SURE THIS IMPORT IS CURRENT!!!!!!!!!!
## SEE STRATEGIES2.TXT - MATURING ALGORITHM, USING NUMLIST TO GENERATE DIFFERENT DICTIONARIES/LISTS
## CHANGE NAMES FROM LISTS TO DICTS WHERE APPLICABLE TO AVOID CONFUSION

def newfulllist(testlist): ## clear testerlist dict each use
    testerlist = lb.Lottery('megaball_numbers.txt')
    #testlistfive = testerlist.lottery_nums()
    for y in testlist:
        testerlist.histogram_get(y,0)
    return testerlist.d

#game = input('which game?(powerball or megaball):  ')
game = 'megaball' ##SO I DON'T HAVE TO KEEP PUTTING IT IN!!

##CAN ONLY USE ONE INSTANCE PER LIST SO DICT d RESETS!!!!!

##               FIVE NUM LISTS/DICTS

## FULL LIST - CREATE A LIST OF THE LISTS OF ALL THE RESULTS AND A COUNTER DICT OF ALL THE RESULTS
full_list = lb.Lottery('{}_numbers.txt'.format(game))
full_list_five = full_list.lottery_nums()  #returns line count[1], count dict[0], and list of lists[2]

## TOP HALF
count = full_list_five[1]
half_count = int(count/2)
top_half = (full_list_five[2])[:half_count]
#print(top_half[0])
#print(top_half[-1])
#top_count_c = lb.Lottery('{}_numbers.txt'.format(game))
#top_count_d = top_count_c.lottery_nums()
#tcd = newfulllist(top_count_d[2])
#print(tcd)
top_count_d = newfulllist(top_half)
print(top_count_d)



##BOTTOM HALF - combine with above into one line like below
bott_half = (full_list_five[2])[half_count:]
#print(bott_half[0])
#print(bott_half[-1])

##PREVIOUS 100, 50, 10 - tuple form?
prev_100, prev_50, prev_10 = (full_list_five[2])[:100],(full_list_five[2])[:50],(full_list_five[2])[:10]
print(prev_10)

##PERCENTAGE OF LAST RESULTS
last_res = (full_list_five[2])[1]
for x in last_res:
    res = (int(x)/count)*100
    #print('%3.2f'%res)
    print(res)

## INITIAL TESTING OF USING NUMLIST TO FEED BACK INTO HISTOGRAM_GET  REVEALED LISTFIVE AND LISTONE COMBO FLAW!!!!
#testerlist = lb.Lottery('megaball_numbers.txt')
#testlistfive = testerlist.lottery_nums()

#print(testlistfive[0])
#print(len(testlistfive[2]))
#a = newfulllist(testlistfive[2])
#print(a)


##  MOVE TO 3A - CLEAN IT UP
##  WHAT TO DO WITH NEWFULLLIST FUNCTION?  ADD TO LOTTERY CLASS? CHANGE NAME
## IF MOVE TO CLASS THEN HAVE TO MAKE NEW INSTANCE EACH LIST/DICT - UNLESS CREATE A CHILD CLASS?