import pandas as pd

class Test_sot(object):
    def __init__(self):
        starter_budget = {'uA':['a','d','e','z'],
              'uB':[3,4,5,6],
              'uk1':[33,44,66,99]}
        starter_bank = {'aA':['b','d','e', 'l'],
                      'aB':[3,4,6,9],
                      'ak1':[33,44,77,88]}

        budget_df = pd.DataFrame(data=starter_budget)
        bank_df = pd.DataFrame(data=starter_bank)
        self.starter_df = pd.merge(bank_df, budget_df, how='outer', left_on='ak1',right_on='uk1')

    def update_bank(self):
        updated_df = self.starter_df
        second_bank = {'aA':['b','d','e','z'],
              'aB':[3,4,5,6],
              'ak1':[33,66,77,111]}
        second_bank_df = pd.DataFrame(data=second_bank)

        print(self.starter_df)
        print('####')
        bank_cols = second_bank_df.columns
        for n, (a,b,key) in second_bank_df.iterrows():
            print('looking for {}'.format(key))
            match_bank_cols = updated_df['ak1'] == key
            matched_bank = match_bank_cols.sum()
            assert matched_bank < 2, 'multiple match for bank - check function to match bank with bank'
            if not matched_bank:
                # New bank entry...
                matched_budget = (updated_df['uk1'] == key)
                number_budget_matches = matched_budget.sum()
                if number_budget_matches:
                    # Matches
                    if number_budget_matches == 1:
                        # found unique match
                        pass
                    elif number_budget_matches > 1:
                        # found multiple matches
                        pass
                else:
                    # Need to make new row
                    new_row = pd.DataFrame([a,b,key], index=bank_cols).transpose()
                    updated_df = pd.merge(updated_df, new_row,how='outer')
            else:
                # Entry already found in bank section, no need to do anything
                continue

        return updated_df


t = Test_sot()

print(t.update_bank())