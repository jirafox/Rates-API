from fastapi import FastAPI
from rates import get_exchange_rates

app = FastAPI()

@app.get("/api/rates")
def read_rates():
    exchange_rates = get_exchange_rates()
    return exchange_rates
