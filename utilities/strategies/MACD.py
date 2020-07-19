import requests
import time


class MACD:
    def __init__(self, required_bars=26, time_frame, insturment):
        self.time_frame = time_frame
        self.insturment = insturment
        key = [kjhfdskhvcmnjslkjjfelkjsldijielfjl]
        self.get_candles = request.get(http: // polygon.com/{key}/{insturment}/{time_frame}/{required_bars}).jason()

    def Running(self):
        close_prices = []
        position_size = []
        position_direction = []
        # entry_pirce = []

        for candles in self.get_candles:
            if candles == 'values':
                for i in candles:
                    if i == 'close':
                        close_prices.append(i)
            return close_prices

            self.current_position = requests.get(http: // alpaka/{self.insturment}/position).Jason()

            for position in self.current_position:
                if position == values:
                    for i in position:
                        if i == 'size':
                            position_size.append(i)
                            return position_size
                        if i == 'direction':
                            position_direction.append(i)
                            return position_direction
                        # if i == "entry_pirce":
                        #     entry_price.append(i)
                        #     return entry_price
        nine_ema = sum(del close_prices[0:16])/9
        twentyone_ema = sum(del close_prices[0:4])/21
        twelve_ema = sum(del close_prices[0:13])/12
        twentysix_ema = sum(close_prices)/26
        last_close = close_prices.pop()
        MACD_indicator = twelve_ema - twentysix_ema

        def countdown(self.time_frame):
            while t:
                    mins, secs = divmod(t, 60)
                    timer = '{:02d}:{:02d}'.format(mins, secs)
                    print(timer, end="\r")
                    time.sleep(1)
                    t -= 1
                print('Blast Off!!!')
            t = input("Enter the time in seconds: ") 
            countdown(int(t))

        while(position_size == 0 and countdown(t)==0):
            if MACD_indicator > nine_ema and last_close > twentyone_ema:
                return "buy 5 shares now"
            if MACD_indicator < nine_ema and last_close < twentyone_ema:
                return "sell 5 shares now"
        else:
            while(position_direction== short and countdown(t)== 0):
                if MACD_indicator > nine_ema or last_close > twentyone_ema:
                    return "close position now"
            while(position_direction=='long' and countdown(t)== 0):
                if MACD_indicator < nine_ema or last_close < twentyone_ema:
                    return "close position now"
        continue

