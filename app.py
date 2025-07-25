from fastapi import FastAPI
from typing import Optional
import json
import os

app = FastAPI()

# ====== JSON 파일 로드 ======
DATA_PATH = r"C:\Users\k\workspace\project\crawling\data\tiger_etf_top10.json"
with open(DATA_PATH, "r", encoding="utf-8") as f:
    etf_data = json.load(f)

# ====== ETF 리스트 API ======
@app.get("/etf")
def get_all_etf(etf: Optional[str] = None):
    """
    전체 ETF 목록 반환
    - etf 쿼리파라미터로 이름 일부 검색 가능
    """
    results = etf_data
    if etf:
        results = [e for e in results if etf.lower() in e["ETF"].lower()]
    return results

# ====== 특정 ETF API ======
@app.get("/etf/{etf_name}")
def get_etf(etf_name: str):
    """
    ETF 이름으로 특정 ETF의 Top10 종목 반환
    """
    for e in etf_data:
        if e["ETF"].lower() == etf_name.lower():
            return e
    return {"error": "ETF not found"}


#cd C:\Users\k\workspace\project\fastapi
#uvicorn app:app --reload
# ngrok config add-authtoken <너의_토큰>

# ngrok http 8000
