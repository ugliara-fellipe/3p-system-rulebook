import pandas as pd
from tabulate import tabulate

selected_dice = 8
max_aspect = 8

#df = pd.DataFrame(columns=('a', 'b', 'dice', 'init_a', 'exit_a', 'init_b', 'exit_b'))
mdf = pd.DataFrame(index=range(1,max_aspect+1), columns=range(1,max_aspect+1))
#tdf = pd.DataFrame(columns=('dice', 'init_a', 'exit_a', 'init_b', 'exit_b'))

#dices = [4,6,8,10,12,20]
#count = 0



for a in range(1,max_aspect+1):
    for b in range(1,max_aspect+1):
        #if b < a:
        #    continue
        #selected_dice = 20
        #sum_a_b = a + b
        #selected_dice = dices[0]
        #for dice in dices:
        #    selected_dice = dice
        #    if sum_a_b <= dice:
        #        break
        #formated_a = 'a(' + '{0: >2}'.format(str(a)) + ')'
        #formated_b = 'b(' + '{0: >2}'.format(str(b)) + ')'
        #formated_c = 'd' + '{0: <2}'.format(str(selected_dice))

        init_a = 0
        exit_a = 0
        
        init_b = 0
        exit_b = 0


        if a==b:#sum_a_b == selected_dice:
            init_a = 1
            exit_a = int(selected_dice/2)

            init_b = int(selected_dice/2) + 1
            exit_b = selected_dice
        else:
            a_b = a+b
            a_p = a/a_b
            b_p = b/a_b

            resto = selected_dice-a_b

            r_a_p = a_p * resto
            r_b_p = b_p * resto

            r_a_p = int(round(r_a_p))
            r_b_p = int(round(r_b_p))

            init_a = 1
            exit_a = a + r_a_p
            
            init_b = exit_a + 1
            exit_b = exit_a + b + r_b_p

        #number_of_a = 'a[' + '{0: >2}'.format(str(init_a)) + ' ~ ' + '{0: <2}'.format(str(exit_a)) + ']'
        #number_of_b = 'b[' + '{0: >2}'.format(str(init_b)) + ' ~ ' + '{0: <2}'.format(str(exit_b)) + ']'

        #print(formated_a, formated_b, '   ', formated_c, '   ', number_of_a, number_of_b)
        #value = tdf.loc[(tdf['dice'] == selected_dice) & (tdf['init_a'] == init_a) & (tdf['exit_a'] == exit_a) & (tdf['init_b'] == init_b) & (df['exit_b'] == exit_b)]
        #print(value)
        #if not value.empty:
        #    index = value.index.item()
        #    #print(index)
        #    mdf.iloc[a - 1, b - 1] = index
        #else:
        #    mdf.iloc[a - 1, b - 1] = len(tdf.index)
        #    tdf.loc[len(tdf.index)] = [selected_dice, init_a, exit_a, init_b, exit_b]

        #mdf.iloc[a - 1, b - 1] = len(tdf.index)
        #tdf.loc[len(tdf.index)] = [selected_dice, init_a, exit_a, init_b, exit_b]
        #mdf.iloc[a - 1, b - 1] = [selected_dice, init_a, exit_a, init_b, exit_b]
        value_a = '< ' + '{0: >2}'.format(str(init_a)) + ':' + '{0: <2}'.format(str(exit_a)) if init_a != exit_a else '< ' + '{0: <5}'.format('{0: >3}'.format(init_a))
        value_b = '^ ' + '{0: >2}'.format(str(init_b)) + ':' + '{0: <2}'.format(str(exit_b)) if init_b != exit_b else '^ ' + '{0: <5}'.format('{0: >3}'.format(init_b))
        mdf.iloc[a - 1, b - 1] = value_a + '<br/>'  + value_b


        #df.loc[len(df.index)] = [a, b, selected_dice, init_a, exit_a, init_b, exit_b]
        #count = count + 1

#print('')
#print('Total: ', count)
#print('')

#print(df.to_string())
#print('')
#print(mdf.to_string())
print(mdf.to_markdown())
#print('')
#print(tdf.to_string())

#dfg = df.groupby(['a', 'b']).first()
#print(dfg.to_string())

#print(tabulate(dfg, headers='keys', tablefmt='psql'))
