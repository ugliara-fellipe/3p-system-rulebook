import pandas as pd
from tabulate import tabulate

df = pd.DataFrame(columns=('a', 'b', 'dice', 'init_a', 'exit_a', 'init_b', 'exit_b'))
mdf = pd.DataFrame(index=range(1,11), columns=range(1,11))
tdf = pd.DataFrame(columns=('dice', 'init_a', 'exit_a', 'init_b', 'exit_b'))

dices = [4,6,8,10,12,20]
count = 0

for a in range(1,11):
    for b in range(1,11):
        #if b < a:
        #    continue
        sum_a_b = a + b
        selected_dice = dices[0]
        for dice in dices:
            selected_dice = dice
            if sum_a_b <= dice:
                break
        formated_a = 'a(' + '{0: >2}'.format(str(a)) + ')'
        formated_b = 'b(' + '{0: >2}'.format(str(b)) + ')'
        formated_c = 'd' + '{0: <2}'.format(str(selected_dice))

        init_a = 0
        exit_a = 0
        
        init_b = 0
        exit_b = 0

        if sum_a_b == selected_dice:
            init_a = 1
            exit_a = a
            
            init_b = exit_a + 1
            exit_b = exit_a + b
        elif sum_a_b % 2 == 0:
            ajust = int((dice - sum_a_b) / 2)

            init_a = 1
            exit_a = a + ajust
            
            init_b = exit_a + 1
            exit_b = exit_a + b + ajust
        else:
            ajust = int((dice - sum_a_b - 1) / 2)

            fix_a = 1 if a > b else 0
            fix_b = 1 if b > a else 0

            init_a = 1
            exit_a = a + ajust + fix_a
            
            init_b = exit_a + 1
            exit_b = exit_a + b + ajust + fix_b

        number_of_a = 'a[' + '{0: >2}'.format(str(init_a)) + ' ~ ' + '{0: <2}'.format(str(exit_a)) + ']'
        number_of_b = 'b[' + '{0: >2}'.format(str(init_b)) + ' ~ ' + '{0: <2}'.format(str(exit_b)) + ']'

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
        mdf.iloc[a - 1, b - 1] = '{0: <3}'.format('d' + str(selected_dice)) + '<br/>' + value_a + '<br/>'  + value_b


        df.loc[len(df.index)] = [a, b, selected_dice, init_a, exit_a, init_b, exit_b]
        count = count + 1

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
