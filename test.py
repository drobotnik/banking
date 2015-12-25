import pandas as pd
import itertools

dice_columns = list("""range	damage	surge	colour""".split())
dice_raw = """3	2	0	g
2	2	0	g
1	2	0	g
1	0	1	g
1	1	1	g
2	1	1	g
3	2	0	b
2	0	1	b
4	2	0	b
3	1	1	b
5	1	0	b
2	1	0	b
0	1	0	r
0	2	0	r
0	2	1	r
0	2	0	r
0	3	0	r
0	3	0	r
0	0	1	y
1	2	0	y
2	0	1	y
1	1	1	y
0	1	2	y
2	1	0	y"""

dice_rows = dice_raw.splitlines()
dice_rows = [row.split() for row in dice_rows]
new_dice_rows = []
for row in dice_rows:
    new_row = []
    for ent in row:
        try:
            new_row += [int(ent)]
        except ValueError:
            new_row += [ent]
    new_dice_rows += [new_row]

for _ in dice_rows:
    print('{'
          '},'.format(_))

df = pd.DataFrame(data=dice_rows, dtype=int)
df.columns = dice_columns

print(df)

class RandomRoller(object):
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def roll(self, cols):

        out = []
        for key in cols:
            dice_options = self.data_frame[self.data_frame['colour'] == lookup[key]]
            sample = dice_options.sample(n=1)
            out += [sample]

        return pd.concat(out)


roller = RandomRoller(df)

x = roller.roll('rb')


dicts = {}

for *row, col in new_dice_rows:
    if col in dicts:
        dicts[col] += [row]
    else:
        dicts[col] = [row]


r = dicts['r']


def calc_dice(rollers):
    dice = {'g': [[3, 2, 0], [2, 2, 0], [1, 2, 0], [1, 0, 1], [1, 1, 1], [2, 1, 1]],
            'r': [[0, 1, 0], [0, 2, 0], [0, 2, 1], [0, 2, 0], [0, 3, 0], [0, 3, 0]],
            'b': [[3, 2, 0], [2, 0, 1], [4, 2, 0], [3, 1, 1], [5, 1, 0], [2, 1, 0]],
            'y': [[0, 0, 1], [1, 2, 0], [2, 0, 1], [1, 1, 1], [0, 1, 2], [2, 1, 0]]}

    test = []
    for colour in rollers:
        test += [dice[colour]]

    combinations = itertools.product(*test)

    added_dice = []

    for combs in combinations:
        added_dice += [[sum(comb) for comb in zip(*combs)]]
    return added_dice


def calc_freqs(combinations):
    """

    :param combinations: list of all different combinations of outcomes of a number of die.
    :return: list of list of [frequency, range, damage, surge]
    """
    out = []
    for z in range(3):
        combinations.sort(key=lambda x: x[z])
    unique = -1
    for n, combo in enumerate(combinations):
        if combo == combinations[n-1]:
            out[unique][0] += 1
        else:
            unique += 1
            out += [[1, *combo]]
    return out




zz = calc_dice('bgy')

