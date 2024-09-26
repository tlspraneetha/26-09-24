import os
import pandas as pd
import matplotlib.pyplot as plt
market_caps={
    'AAPL':2300,
    'MSFT':210,
    'GOOGL':1600,
    'AMZN':1700,
    'TSLA':900,
    'BRK-B':600,
    'NVDA':500,
    'META':700, 
    'JNJ':400,
    'V':500,
}
top_10_companies={
    'AAPL':'Apple Inc.',
    'MSFT':'Microsoft corporation',
    'GOOGL':'Alphabet Inc.',
    'AMZN':'Amazon.com,Inc.',
    'TSLA':'Tesla,Inc.',
    'BRK-B':'Berkshiire hathway Inc.',
    'NVDA':'NVIDIA corporation',
    'META':'Meta platform ,Inc.',
    'JNJ':'Johnson &johnson.',
    'v':'Visa Inc.',
}
current_directory=os.path.dirname(os.path.abspath(__file__))
csv_file_path=os.path.join(current_directory,'top_10_stocks_sample_2013_2023.CSV',)
df=pd.read_csv(csv_file_path)
df['Date']=pd.to_datetime(df['Date'])
df['year']=df['date'].dt.year
stock_columns=['APPL-close','MSFT-close','GOOGL-close','AMZN-close','TSLA-close','BAK-B-close','NVDA-close','META-close','JNJ-close,']
average_prices=df.groupby('year')[stock_columns].means().rest_index()
plt.figure(figsize=(20,10))
bar_width=0.1
years=average_prices['year']
positions=[years+i*bar_width for i in range[len(stock_columns)]]
for i,column in enumerate(stock_columns):
    plt.bar(positions[i],average_prices[column], width=bar_width,label=column.split('_')[0]) 
plt.xlabe('year')
plt.ylabel('average closing price')
plt.title('average closing price of top 10 stocks(2013-2023)')
plt.xticks(years+bar_width*4.5,years)
plt.lengent()
plt.tight_layout()
plt.show()