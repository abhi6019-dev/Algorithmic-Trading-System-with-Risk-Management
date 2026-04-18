# 📊 Algorithmic Trading System with Risk Management

A modular algorithmic trading system built using Python that combines multiple trading strategies, risk management, and a backtesting engine to evaluate systematic trading performance on historical market data.

---

## 🚀 Project Overview

This project implements a quantitative trading framework inspired by real-world hedge fund systems. It focuses on:

- Signal generation using multiple strategies  
- Portfolio signal aggregation  
- Risk management and drawdown control  
- Backtesting using historical data (via yfinance)  
- Performance evaluation using key financial metrics  

---

## 🧠 Key Features

### 📈 Trading Strategies
- Momentum-based strategy (trend following)
- Mean reversion strategy (z-score based)
- Ensemble signal combination

### ⚖️ Risk Management
- Volatility-based position sizing
- Drawdown monitoring
- Exposure control framework

### 🧪 Backtesting Engine
- Historical simulation of strategy performance
- Strategy returns computation
- Equity curve generation

### 📊 Performance Metrics
- Sharpe Ratio
- Maximum Drawdown
- CAGR (Compound Annual Growth Rate)

---

## 🏗️ Project Structure

```
algorithmic-trading-system-with-risk-management/
│
├── data/
├── strategies/
├── backtest/
├── portfolio/
├── risk/
├── metrics/
├── main.py
└── requirements.txt
```

---

## ⚙️ Installation

```bash
git clone https://github.com/abhi6019-dev/algorithmic-trading-system-with-risk-management
cd algorithmic-trading-system-with-risk-management
pip install -r requirements.txt
```

---

## 📦 Requirements

```
pandas
numpy
yfinance
matplotlib
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 📊 Output

- Equity curve
- Sharpe ratio
- Max drawdown
- CAGR
- Strategy performance summary

---

## 📉 Metrics

Sharpe:
Sharpe = (Rp - Rf) / sigma_p

Max Drawdown:
Drawdown = (Peak - Trough) / Peak

CAGR:
CAGR = (Ending / Beginning)^(1/n) - 1

---

## 🚀 Future Improvements

- ML-based alpha models
- Portfolio optimization
- Transaction costs + slippage
- Walk-forward validation
- Live trading integration

---

## ⚠️ Disclaimer

Educational use only. Not financial advice.

---

## 👨‍💻 Author

Abhi (abhi6019-dev)
