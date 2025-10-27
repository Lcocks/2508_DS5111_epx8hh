import os
import sys
sys.path.append('.')
from bin.gainers.base import GainerBase
import bin.my_normalizer as my_normalizer
import pandas as pd

class GainerWSJ(GainerBase):
    def __init__(self):
        pass

    def download_html(self):
        print("WSJ html download")
        os.system("sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=500 https://www.wsj.com/market-data/stocks/us/movers > wsjgainers.html")

    def extract_csv(self):
        print("WSJ csv create")
        raw = pd.read_html('wsjgainers.html')
        raw[0].to_csv('wsjgainers.csv')

    def normalize_data(self):
        print("WSJ normalize csv")
        my_normalizer.normalize_yahoo(pd.read_csv("./wsjgainers.csv", index_col = 0))

if __name__=="__main__":
    import sys
    assert len(sys.argv) == 2, "Please pass in one of 'html', 'csv', 'normalize'"
    function = sys.argv[1]
    valid_functions = ['html', 'csv', 'normalize']
    assert function in valid_functions, f"Expected one of {valid_functions} but got {function}"

    gainer = GainerWSJ()

    if function == 'html':
        gainer.download_html()
    elif function == 'csv':
        gainer.extract_csv()
    elif function == 'normalize':
        gainer.normalize_data()
