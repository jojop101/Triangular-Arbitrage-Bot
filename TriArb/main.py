import requests
import json
import func_arb
import time

""" Step 0 """
url = "https://poloniex.com/public?command=returnTicker"


def step_0():
    coin_json = func_arb.get_coin_tickers(url)
    coin_list = func_arb.collect_tradeables(coin_json)
    return coin_list

''' Step 1 '''

def step_1(coin_list):

    structured_list = func_arb.structure_triangular_pairs(coin_list)

    with open("structured_triangular_pairs.json", "w") as fp:
        json.dump(structured_list, fp)

""" Step 2: calculate surface rate"""

def step_2():
    with open("structured_triangular_pairs.json") as json_file:
        structured_pairs = json.load(json_file)

        prices_json = func_arb.get_coin_tickers(url)


        for t_pair in structured_pairs:
                    time.sleep(0.3)
                    prices_dict = func_arb.get_price_for_t_pair(t_pair, prices_json)
                    surface_arb = func_arb.calc_tri_arb_surface_rate(t_pair, prices_dict)
                    if len(surface_arb) > 0:
                        real_rate_arb = func_arb.get_depth_from_orderbook(surface_arb)
                        print(real_rate_arb)
                        time.sleep(1)


""" Main """

if __name__ == "__main__":
    #    coin_list = step_0()
    #    structured_pairs = step_1(coin_list)
       while True:
            step_2()

