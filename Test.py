import akshare as ak

if __name__ == '__main__':
    stock_zh_a_new = ak.fund_em_open_fund_info(fund = "013525", indicator = "累计收益率走势")
    print(stock_zh_a_new)
