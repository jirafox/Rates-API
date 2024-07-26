from fastapi import FastAPI
from rates import get_exchange_rates, get_crypto_rates, get_gold_rates

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

@app.get("/api/exchange-rates")
def read_rates_curr():
    exchange_rates = get_exchange_rates()
    return exchange_rates

@app.get("/api/gold-rates")
def read_rates_gold():
    gold = get_gold_rates()
    return gold

@app.get("/api/crypto-rates")
def read_rates_crypto():
    crypto = get_crypto_rates()
    return crypto