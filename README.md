# Julius-local
A lightweight local alternative to Julius AI for exploratory data analysis (EDA), charting, and quick natural-language insights.

Features:
- Upload CSV / Excel files
- Automatic EDA (using pandas + simple heuristics)
- Interactive charts (plotly)
- Data filtering and column selection
- Generate a written summary (offline heuristics) or use OpenAI if you provide an API key
- Export charts and reports

Quick Start:
1. python -m venv venv
2. source venv/bin/activate   (or venv\Scripts\activate on Windows)
3. pip install -r requirements.txt
4. streamlit run app.py
