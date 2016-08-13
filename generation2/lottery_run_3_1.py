

import lottery_code_3_2 as lc

# game = input('which game?(powerball or megaball):  ')
game = 'powerball'  ##SO I DON'T HAVE TO KEEP PUTTING IT IN!!

action_lists = lc.Action_Lists(game)
#
# action_lists.percent_to_file()
action_lists.numcount_to_file()
action_lists.ballcount_to_file()

winners = lc.Winning(game) ## the user could input a name for this instance or it could be printed to a file with the
                            # date and time

x,y,z = (winners.winnerballs())

a, b, c = winners.winnerlo(), winners.winner4lo(), winners.winner3lo()

print(a,x)
print(b,y)
print(c,z)

x, y= winners.not_recent(17)
print(x)
print(y)