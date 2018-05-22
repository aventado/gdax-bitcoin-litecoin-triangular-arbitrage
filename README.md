# gdax-triangular-arbitrage
Automated trading bot for triangular arbitrage between USD -> BTC -> LTC -> USD on Gdax

Easily modified for the currencies of your choice

Change line 30 for your API information, change line 33 for the amount of capital in USD to run the arbitrage bot with.

Known Issues:
- Does not calculate max trade size based on each leg of the trade (must be in and out of each position seamlessly)
- Does not calculate alternative exit strategies (if caught in leg and selling is unprofitable because of a lag in execution, can we move to another pair and get back to USD?)
- Probably more

Tipjar -

Donate BTC: 3EYfd42eD5dZCWVBXYzrF5wMMR4ERLs68b

Donate ETH: 0x020FB5A3DfcA8a23c2D3a2d8fe37E277ce183011

Donate LTC: MD1kYZZALcZRRidE4E4ey4LhnT5C5eEfWU (Segwit)
