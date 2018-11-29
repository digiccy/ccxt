"use strict";

// ----------------------------------------------------------------------------

const ccxt = require('../../ccxt.js')
    , log = require('ololog')
    , asTable = require('as-table').configure({ delimiter: ' | ' })

    // ----------------------------------------------------------------------------

    ; (async () => {

        const exchange = new ccxt.liqui({
            'timeout': 60000,
        })
        try {
            await exchange.loadMarkets()
            const response = await exchange.fetchTickers();
            log(JSON.stringify(response))

        } catch (e) {

            log(e.message)
        }

    })()