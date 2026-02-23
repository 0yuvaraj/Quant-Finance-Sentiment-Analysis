import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# 1. Configuration - Let's look at NVIDIA (NVDA) or NIFTY 50
ticker = "NVDA"
analyzer = SentimentIntensityAnalyzer()

# 2. Mock News Data (In a real scenario, you'd use NewsAPI or Scrapy)
news_headlines = [
    "NVIDIA beats earnings expectations with record revenue",
    "Tech stocks tumble as inflation fears rise",
    "NVDA announces new high-performance AI chips",
    "Regulatory concerns hit semiconductor industry hard",
    "Analyst upgrades NVIDIA to Buy rating after strong quarter"
]

# 3. Analyze Sentiment
print(f"--- Sentiment Analysis for {ticker} ---")
scores = []
for text in news_headlines:
    vs = analyzer.polarity_scores(text)
    scores.append(vs['compound'])
    print(f"Score: {vs['compound']} | Headline: {text[:50]}...")

avg_sentiment = sum(scores) / len(scores)
print(f"\nAverage Market Sentiment: {avg_sentiment:.2f}")

# 4. Fetch Historical Market Data
data = yf.download(ticker, start="2024-01-01", end="2024-12-31")
data['MA20'] = data['Close'].rolling(window=20).mean() # 20-day Moving Average

# 5. Visualization
plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='Close Price', color='blue', alpha=0.5)
plt.plot(data['MA20'], label='20-Day Moving Average', color='orange')
plt.title(f"{ticker} Price Trend vs Moving Average")
plt.legend()
plt.show()
