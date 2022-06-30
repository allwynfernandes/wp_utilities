import datetime
import pandas as pd



def make_records(div, cuID, amt):
    amt_per_reward = 10000 
    if amt>0:
        recs = amt//amt_per_reward, amt%amt_per_reward  # equal_parts, remainder
        amt_bif = [amt_per_reward for row in range(recs[0]) ] 

        if recs[1] >0:
            amt_bif = amt_bif + [recs[1]]
        else:
            pass
        df = pd.DataFrame( amt_bif, columns=['Sub Division Amt'])
        df['Mobile'] = cuID
        df['Total Amt'] = amt
        df.index += 1 
        df = df.reset_index()
        df = df.rename(columns={'index':'Point Sr.'})
        df['Total Points'] = len(amt_bif)
        df['Card Number'] = ""
        df['Division'] = div
        df = df[['Division', 'Mobile', 'Total Points', 'Point Sr.', 'Total Amt', 'Sub Division Amt', 'Card Number']]
        return df
    else:
        return pd.DataFrame()



def main_logic(raw_data=None):
    if not(raw_data==None):
        df = pd.read_csv(raw_data)
        df.columns = ["Division", "Mobile", "Investment"]
        export_data = pd.concat([make_records(row[0], row[1], row[2]) for row in zip(df['Division'], df['Mobile'], df['Investment'])])
        return export_data

def get_upload_template():
    return pd.DataFrame(columns=['Division', 'Mobile', 'Investment'])


def get_timestamp():
    return str(datetime.datetime.now()).replace(":","").replace("-","").partition(".")[0]


def main():
    pass


if __name__ == '__main__':
        main()
