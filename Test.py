import akshare as ak

if __name__ == '__main__':
    param = {'fund': '710001', 'indicator': '累计收益率走势'}

    method = getattr(ak, 'fund_em_open_fund_info')(**param)
    fund_em_open_fund_info = ak.fund_em_open_fund_info(fund = "710001", indicator = "单位净值走势")
    # stock_zh_a_new = ak.stock_zh_a_new(fund = "013525", indicator = "单位净值走势")
    # print(fund_em_open_fund_info)
    print(method)
