# 🐦 Twitter Sentiment Analysis

> Classifying financial market sentiment from tweets using NLP — turning social chatter into a market signal.

---

## 📌 Objective

Social media platforms like Twitter are increasingly used by retail and institutional investors to gauge market mood. This project builds a **sentiment classification pipeline** that processes tweets mentioning financial assets and categorises them as **Positive**, **Negative**, or **Neutral** — with the goal of exploring whether sentiment precedes price movement.

---

## 🛠️ Tools & Libraries

| Category | Tools |
|----------|-------|
| Language | Python 3.x |
| NLP | VADER (NLTK), TextBlob |
| Data | pandas, NumPy |
| Visualisation | matplotlib, seaborn, WordCloud |
| Dataset | See `/Datasets` folder |

---

## 📁 Project Structure

```
Twitter Sentiment Analysis/
│
├── Datasets/               # Raw and cleaned tweet data
├── Sentiment_Analysis.py   # Main analysis script
└── README.md
```

---

## 🔍 Methodology

1. **Data Collection** — Dataset of tweets filtered by financial keywords/tickers
2. **Preprocessing** — Remove URLs, mentions, hashtags; tokenise and clean text
3. **Sentiment Scoring** — VADER compound score → classified into Positive / Negative / Neutral
4. **Analysis** — Sentiment distribution, time-series sentiment trend, comparison with price data
5. **Visualisation** — Word clouds per sentiment class, sentiment over time charts

---

## 📊 Key Findings

- Negative sentiment spikes were observed **1–2 days before** notable price declines in tracked assets
- VADER outperformed TextBlob in financial tweet classification due to slang and abbreviation handling
- ~65% of tweets in the dataset were classified as Neutral, with clear spikes in Negative sentiment during earnings seasons

---

## 🚀 How to Run

```bash
# Install dependencies
pip install nltk textblob pandas matplotlib seaborn wordcloud

# Run analysis
python Sentiment_Analysis.py
```

---

## 💡 Extensions & Next Steps

- [ ] Integrate live Twitter/X API stream for real-time sentiment
- [ ] Train a fine-tuned FinBERT model for finance-specific NLP
- [ ] Backtest a simple long/short strategy based on sentiment signals
- [ ] Add ticker-level sentiment breakdown (AAPL, TSLA, etc.)

---

*Part of [xaulok/Projects](https://github.com/xaulok/Projects) · B.Sc Economics, CUAP '27*
