def make_order_like_zhongli(session, symbol, qty, side, takeProfit, stopLoss):
    market_order = session.place_order(
        category="linear",
        symbol=symbol,
        side=side,
        orderType="MARKET",
        qty=qty,
        takeProfit=takeProfit,
        stopLoss=stopLoss,
        isLeverage=1,
        positionIdx=1 if side == "Buy" else 2,
        timeInForce="PostOnly",
        orderFilter="Order"
    )
    print(market_order)
