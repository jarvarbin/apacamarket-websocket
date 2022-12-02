import asyncio
from alpaca_trade_api import StreamConn

async def on_ticker(conn, channel, data):
    # process the incoming data from the websocket
    print(data)

async def main():
    # create a StreamConn instance
    conn = StreamConn()

    # start a websocket connection to the Alpaca Markets API
    await conn.subscribe(['T.AAPL'], on_ticker)

    # wait for the data to be processed
    await asyncio.sleep(300)

    # close the websocket connection
    await conn.close()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
