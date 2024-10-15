import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

class chartink():
  def __init__(self , condition):
    '''
    pass condition in init from payload in dictionary format
    {'scan_clause':'sample payload enter here'}
    '''
    self.condition = condition
  def stock_screener(self):

    with requests.Session() as s:
        r = s.get('https://chartink.com/screener/time-pass-48')
        soup = bs(r.content, 'lxml')
        s.headers['X-CSRF-TOKEN'] = soup.select_one('[name=csrf-token]')['content']
        r = s.post('https://chartink.com/screener/process', data=self.condition).json()
        #print(r.json())
        df = pd.DataFrame(r['data'])
        return df
