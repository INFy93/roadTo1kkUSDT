from flask import Flask, jsonify
from flask_cors import CORS
from api.account import account
from api.core import coin_data

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


# sanity check route
@app.route('/api/account/balance', methods=['GET'])
def getMoney():
    return jsonify(account.get_wallet_balance())


@app.route('/api/core/coin/<coin>/<period>', methods=['GET'])
def getCoinInfo(coin, period):
    return jsonify(coin_data.getKlineData(coin, period))


if __name__ == '__main__':
    app.run()
