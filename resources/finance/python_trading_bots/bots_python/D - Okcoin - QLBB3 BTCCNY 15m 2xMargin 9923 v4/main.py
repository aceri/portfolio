#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8

import json
import shared
import common
import talib
import math
import random
import numpy as np

import csv
import datetime
import time

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture

apikey='e53fd45f-6d08-49c8-8172-7f3251cc929d'
secretkey='E019CE2DFDAEFECF693A93FB61FC8E8E'

okcoinRESTURL = 'www.okcoin.cn'   #请求注意：国内账号需要 修改为 www.okcoin.cn  

okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)

running=True

def broker_update():
    print("-------------------------------------------")
    data=okcoinSpot.ticker('btc_cny')
    
#DateOCHLV > es lo que tengo en mi excel    
    
    f=csv.writer(open("/home/CSV/Tickers/okcoin_btccny_15m.csv","a+"))
    x=1

    f.writerow([datetime.datetime.fromtimestamp(float(data['date'])).strftime('%Y-%m-%d %H:%M:%S'),
                                                      data['ticker']['last'],
                                                      data['ticker']['buy'],
                                                      data['ticker']['high'],
                                                      data['ticker']['low'],
                                                      data['ticker']['vol']])
            
#f.writerow([datetime.datetime.fromtimestamp(float(bars['response'][-x]['time'])).strftime('%Y-%m-%d %H:%M:%S')
#,bars['response'][-x]['h'],bars['response'][-x]['c'],bars['response'][-x]['o'],bars['response'][-x]['l']])            

def main_thread():
    print ("Initializing main daemon.")
    while running == True:
        broker_update()
        time.sleep(900)

if __name__ == "__main__":
    main_thread()