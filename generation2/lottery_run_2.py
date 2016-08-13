##Write results to a file, check if file exists
## next check to see if game has changed then delete lists if so
## MOVE THIS TO CODE AND MAKE A CLASS LIST_COUNTERS??

import lottery_code_1 as lc
import os
import json


# import demjson


def make_lists():
    if not os.path.exists('megaball/masterlist_{}' .format(game)):
        with open('megaball/masterlist_{}' .format(game), 'w') as f:
            master_list = lc.ListCreator('{}_numbers.txt' .format(game)).combo_test()
            json.dump(master_list, f)
    else:
        with open('megaball/masterlist_{}' .format(game)) as f:
            master_list = json.load(f)

    five_results = master_list[1]
    one_results = master_list[2]
    result_count = master_list[0]
    return master_list, five_results, one_results, result_count



def make_counters():

    #master_list, five_results, one_results, result_count = make_lists()
    if not os.path.exists('{0}/fivecountdict_{1}'.format(game,game)):
        with open('{0}/fivecountdict_{1}'.format(game,game), 'w') as f:
            full_five = lc.Histogram(five_results).histogram_run()
            json.dump(full_five, f, sort_keys=True)

    with open('{0}/fivecountdict_{1}'.format(game,game)) as f:
        full_five_count = json.load(f)

    if not os.path.exists('{0}/onecountdict_{1}' .format(game,game)):
        with open('{0}/onecountdict_{1}' .format(game,game), 'w') as f:
            full_one = lc.Histogram(one_results).histogram_run(0)
            json.dump(full_one, f, sort_keys=True)

    with open('{0}/onecountdict_{1}' .format(game,game)) as f:
        full_one_count = json.load(f)

    if not os.path.exists('{0}/invertfivedict_{1}' .format(game,game)):
        with open('{0}/invertfivedict_{1}' .format(game,game), 'w') as f:
            inv_five = lc.Histogram().invert_dict(full_five_count)
            json.dump(inv_five, f, sort_keys=True)  # well shit that works!!!

    with open('{0}/invertfivedict_{1}' .format(game,game)) as f:
        inv_five = json.load(f)

    if not os.path.exists('{0}/invertonedict_{1}' .format(game,game)):
        with open('{0}/invertonedict_{1}' .format(game,game), 'w') as f:
            inv_one = lc.Histogram().invert_dict(full_one_count)
            json.dump(inv_one, f, sort_keys=True)

    with open('{0}/invertonedict_{1}' .format(game,game)) as f:
        inv_one = json.load(f)

    return full_five_count, full_one_count, inv_five, inv_one

    # if not os.path.exists('{0}/nvertfivedict_{}'%game):
    #     inv_five_dict = lc.Histogram().invert_dict(full_five_count)
    #     demjson.encode_to_file('{0}/nvertfivedict_{}'%game,inv_five_dict, strict=False)
    # else:
    #     inv_five_dict = demjson.decode_file('{0}/nvertfivedict_{}'%game,encoding=None,strict=False)

def percent_to_file():

    with open('{0}/percentfile_{1}'.format(game,game),'w') as g:
        g.write('total results : {}\n'.format(result_count))
        for x in range(50):
            recent = five_results[x]
            rec_one = one_results[x]
            g.write('---{}---\n\n'.format(x))
            for y in recent:
                m = full_five_count[y]
                n = (m/result_count)*100
                g.write('{0} : {1:.2f} prcnt\n'.format(y, n))
            o = full_one_count[rec_one]
            p = (o/result_count)*100
            g.write('{0} {1} : {2:.2f} prcnt\n\n'.format(game,rec_one,p))
            g.write('*'*10)
            g.write('\n\n')
        print('done')


# game = input('which game?(powerball or megaball):  ')
game = 'megaball'  ##SO I DON'T HAVE TO KEEP PUTTING IT IN!!
master_list, five_results, one_results, result_count = make_lists()

full_five_count, full_one_count, inv_five, inv_one = make_counters()

percent_to_file()
