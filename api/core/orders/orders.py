def make_order_like_zhongli(session, symbol, qty, side, takeProfit, stopLoss):
    market_order = session.place_order(
        category="linear",
        symbol=symbol,
        side=side,
        orderType="MARKET",
        qty=qty,
        takeProfit=takeProfit,
        stopLoss=stopLoss,
        marketUnit="quoteCoin",
        timeInForce="PostOnly",
        orderFilter="Order"
    )
    print(market_order)
