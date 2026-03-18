
import os

# ── requirements.txt ─────────────────────────────────────────────────────────
req = """\
streamlit==1.43.0
streamlit-autorefresh==1.0.1
yfinance==0.2.54
pandas==2.2.3
numpy==1.26.4
plotly==5.24.1
requests==2.32.3
"""
with open("requirements.txt", "w") as f:
    f.write(req)

# ── .streamlit/config.toml  (dark theme for cloud) ───────────────────────────
os.makedirs(".streamlit", exist_ok=True)
config = """\
[theme]
base              = "dark"
primaryColor      = "#58a6ff"
backgroundColor   = "#0d1117"
secondaryBackgroundColor = "#161b22"
textColor         = "#e6edf3"

[server]
headless          = true
enableCORS        = false
enableXsrfProtection = true

[browser]
gatherUsageStats  = false
"""
with open(".streamlit/config.toml", "w") as f:
    f.write(config)

# ── README.md ────────────────────────────────────────────────────────────────
readme = """\
# 🇮🇳 India Macro Intelligence Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

> Real-time, auto-refreshing dashboard tracking **24 macro indicators** that
> drive the Indian stock market (Nifty 50 / BSE Sensex).

---

## 🚀 Deploy on Streamlit Cloud (5 minutes)

### Step 1 — Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit: India Macro Dashboard"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/india-macro-dashboard.git
git push -u origin main
```

### Step 2 — Deploy on Streamlit Cloud
1. Go to **https://share.streamlit.io**
2. Sign in with GitHub
3. Click **"New app"**
4. Fill in:
   - **Repository:** `YOUR_USERNAME/india-macro-dashboard`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click **Deploy!** 🎉

Your dashboard will be live at:
`https://YOUR_USERNAME-india-macro-dashboard-app-XXXXX.streamlit.app`

---

## 📁 Repository Structure

```
india-macro-dashboard/
├── app.py                    ← Main Streamlit app
├── requirements.txt          ← Python dependencies
├── .streamlit/
│   └── config.toml           ← Dark theme + server config
└── README.md
```

---

## 📊 Dashboard Sections

| # | Section | Content | Refresh |
|---|---------|---------|---------|
| 1 | **Market Pulse** | Nifty, Sensex, VIX, INR, Crude, Gold, DXY, US10Y, S&P500, MSCI EM | Every 5 min |
| 2 | **Macro Signal Scorecard** | 🟢/🔴/⚪ signal per indicator based on daily move | Every 5 min |
| 3 | **NSE Sector Heatmap** | Bank, IT, Auto, FMCG, Metal, Pharma, Realty, Energy | Every 5 min |
| 4 | **Correlation Charts** | Dual-axis Nifty vs 6 indicators + Pearson r value | On load |
| 5 | **World Bank Data** | GDP, CPI, CAD, Unemployment, FDI + 30Y GDP chart | Daily |
| 6 | **Reference Table** | All 24 indicators: relation + strength + rationale | Static |

---

## 🔑 Key Features

- ✅ **Zero API keys required** — uses Yahoo Finance + World Bank (both free)
- ✅ **Auto-refresh every 5 minutes** via `streamlit-autorefresh`
- ✅ **Dark theme** matching TradingView/GitHub aesthetic
- ✅ **Color-coded signals** — 🟢 Bullish / 🔴 Bearish / ⚪ Neutral
- ✅ **Pearson correlation r** shown per chart with expectation match
- ✅ **Sidebar controls** — toggle sections, change chart period (6mo–Max)

---

## 📡 Data Sources

| Data | Source | API Key? | Frequency |
|------|--------|----------|-----------|
| Market prices | Yahoo Finance (yfinance) | ❌ None | Every 5 min |
| Sector indices | Yahoo Finance (yfinance) | ❌ None | Every 5 min |
| GDP, CPI, CAD, FDI | World Bank Open API | ❌ None | Daily cache |

---

## ⚡ Optional Future Additions

| Feature | How to add |
|---------|-----------|
| Live FII/DII flows | `pip install nsetools` or NSE India API |
| RBI Repo Rate | RBI DBIE API → `https://rbi.org.in/dbie` |
| GST Monthly Collections | `https://www.gst.gov.in` |
| US Fed Rate | FRED API (free key at `fred.stlouisfed.org`) |

---

## 📬 Contact

Built by **Pawan Chaturvedi** | Surat, Gujarat, India
"""

with open("README.md", "w") as f:
    f.write(readme)

# ── .gitignore ────────────────────────────────────────────────────────────────
gitignore = """\
__pycache__/
*.py[cod]
.env
.venv/
venv/
*.egg-info/
.DS_Store
"""
with open(".gitignore", "w") as f:
    f.write(gitignore)

print("All files created:")
for fname in ["app.py", "requirements.txt", ".streamlit/config.toml", "README.md", ".gitignore"]:
    size = os.path.getsize(fname)
    print(f"  ✅ {fname:<35} ({size:,} bytes)")
