from flask import Flask, jsonify
import rates

app = Flask(__name__)

@app.route('/api/rates', methods=['GET'])
def rates():
    exchange_rates = rates.get_exchange_rates()
    return jsonify(exchange_rates)

if __name__ == '__main__':
    app.run(debug=True)
