#!/usr/bin/env python
# -*- coding: utf-8 -*-

import msvcrt
import sys
import ConfigParser
import TradeX
# 一定要最后import tradex
TradeX.OpenTdx()



class QA_Stock():
    TradeX.OpenTdx()
    print('stock')
    def get_config(self):
        config=ConfigParser.ConfigParser()
        try:
            with open("./setting.cfg","rw") as cfgfile: 
                config.readfp(cfgfile)
                self.sHost =config.get("trade","host")
                self.nPort =config. get("trade","port")
                self.sVersion =config.get("trade","version")
                self.sBranchID =config.get("trade","branchID")
                self.sAccountNo =config.get("trade","accountNo")
                self.sTradeAccountNo =config.get("trade","tradeAccountNo")
                self.sPassword=config.get("trade","password")
                self.sTxPassword =config.get("trade","txPassword")

                print(self.sHost)
        except:
            print('error with read setting files')
    def QA_trade_stock_login(self):
        try:
            client = TradeX.Logon(self.sHost, self.nPort, self.sVersion, self.sBranchID, self.sAccountNo,self.sTradeAccountNo, self.sPassword, self.sTxPassword)
            return client
        except TradeX.error as e:
            print ("error: " + e.message)
            sys.exit(-1)
    def QA_trade_stock_get_account(self,client):
        self.nCategory = 0

        errinfo, self.result = client.QueryData(self.nCategory)
        if errinfo != "":
            print (errinfo)
        else:
            print (self.result)
            return self.result
