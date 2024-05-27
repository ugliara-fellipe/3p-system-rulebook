import pandas as pd

def generate_dice_table(selected_dice, max_aspect):
    mdf = pd.DataFrame(index=range(1,max_aspect+1), columns=range(1,max_aspect+1))

    for a in range(1,max_aspect+1):
        for b in range(1,max_aspect+1):
            init_a = 0
            exit_a = 0

            init_b = 0
            exit_b = 0


            if a==b:
                init_a = 1
                exit_a = int(selected_dice/2)

                init_b = int(selected_dice/2) + 1
                exit_b = selected_dice
            elif a > b:
                a_b = a - b
                pivot = int(selected_dice/2) + a_b
                if pivot > selected_dice - 1:
                    pivot = selected_dice - 1

                init_a = 1
                exit_a = pivot

                init_b = exit_a + 1
                exit_b = selected_dice
            elif b > a:
                b_a = b - a
                pivot = int(selected_dice/2) - b_a
                if pivot < 1:
                    pivot = 1

                init_a = 1
                exit_a = pivot

                init_b = exit_a + 1
                exit_b = selected_dice

            value_a = '< ' + '{0: >2}'.format(str(init_a)) + ':' + '{0: <2}'.format(str(exit_a)) if init_a != exit_a else '< ' + '{0: <5}'.format('{0: >3}'.format(init_a))
            value_b = '^ ' + '{0: >2}'.format(str(init_b)) + ':' + '{0: <2}'.format(str(exit_b)) if init_b != exit_b else '^ ' + '{0: <5}'.format('{0: >3}'.format(init_b))
            mdf.iloc[a - 1, b - 1] = value_a + '<br/>'  + value_b

    return mdf

print(generate_dice_table(6, 5).to_markdown())
print('')
print(generate_dice_table(6, 6).to_markdown())
print('')
print(generate_dice_table(6, 8).to_markdown())
print('')
print(generate_dice_table(8, 5).to_markdown())
print('')
print(generate_dice_table(8, 6).to_markdown())
print('')
print(generate_dice_table(8, 8).to_markdown())
print('')
print(generate_dice_table(12, 6).to_markdown())
print('')
print(generate_dice_table(12, 7).to_markdown())
print('')
print(generate_dice_table(12, 8).to_markdown())
print('')
print(generate_dice_table(12, 10).to_markdown())
print('')
print(generate_dice_table(20, 8).to_markdown())
print('')
print(generate_dice_table(20, 10).to_markdown())
print('')
print(generate_dice_table(20, 12).to_markdown())
print('')
print(generate_dice_table(20, 15).to_markdown())

