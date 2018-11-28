
'use strict';

const log  = require ('ololog').configure ({ locate: false })
const ccxt = require('../../ccxt')

async function main() {
    const exchange = new ccxt.btctradeim()
    let markets = await exchange.loadMarkets ()
    console.log(markets);

    const ticker = await exchange.fetchTicker ('BTC/USDT');
    console.log(ticker);
}

main()
