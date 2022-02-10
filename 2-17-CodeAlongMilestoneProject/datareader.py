import pandas_datareader as pdr
import pandas as pd
import os

start = '2020-01-01'
end = '2020-01-31'

# columns: ['adjClose', 'adjHigh', 'adjLow', 'adjOpen', 'adjVolume', 'close',
#           'divCash', 'high', 'low', 'open', 'splitFactor', 'volume']

def get_prices(ticker_list, start, end):
    df = pdr.tiingo.TiingoDailyReader(ticker_list,
                                        start=start,
                                        end=end,
                                        api_key='fa7df24832043c834d91324b77a0f73e5fa99aac').read()
    df = df.reset_index(level=['date', 'symbol']) # reset multi-index to new single-index
    # figure = {'data': [go.Scatter(x=df['date'],
    #                                 y=df['adjClose'],
    #                                 mode='lines')],
    #             'layout': go.Layout(title=f"{ticker} Prices",
    #                                 hovermode='closest')}
    return df

key = os.environ['TIINGO_KEY']
print(key)
print(type(key))
