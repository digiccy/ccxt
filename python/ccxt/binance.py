# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
import math
import json
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import DDoSProtection
from ccxt.base.errors import ExchangeNotAvailable
from ccxt.base.errors import InvalidNonce


class binance (Exchange):

    def describe(self):
        return self.deep_extend(super(binance, self).describe(), {
            'id': 'binance',
            'name': 'Binance',
            'countries': ['JP'],  # Japan
            'rateLimit': 500,
            'certified': True,
            # new metainfo interface
            'has': {
                'fetchDepositAddress': True,
                'CORS': False,
                'fetchBidsAsks': True,
                'fetchTickers': True,
                'fetchOHLCV': True,
                'fetchMyTrades': True,
                'fetchOrder': True,
                'fetchOrders': True,
                'fetchOpenOrders': True,
                'fetchClosedOrders': True,
                'withdraw': True,
                'fetchFundingFees': True,
            },
            'timeframes': {
                '1m': '1m',
                '3m': '3m',
                '5m': '5m',
                '15m': '15m',
                '30m': '30m',
                '1h': '1h',
                '2h': '2h',
                '4h': '4h',
                '6h': '6h',
                '8h': '8h',
                '12h': '12h',
                '1d': '1d',
                '3d': '3d',
                '1w': '1w',
                '1M': '1M',
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/29604020-d5483cdc-87ee-11e7-94c7-d1a8d9169293.jpg',
                'api': {
                    'web': 'https://www.binance.com',
                    'wapi': 'https://api.binance.com/wapi/v3',
                    'public': 'https://api.binance.com/api/v1',
                    'private': 'https://api.binance.com/api/v3',
                    'v3': 'https://api.binance.com/api/v3',
                    'v1': 'https://api.binance.com/api/v1',
                },
                'www': 'https://www.binance.com',
                'referral': 'https://www.binance.com/?ref=10205187',
                'doc': 'https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md',
                'fees': [
                    'https://binance.zendesk.com/hc/en-us/articles/115000429332',
                    'https://support.binance.com/hc/en-us/articles/115000583311',
                ],
            },
            'api': {
                'web': {
                    'get': [
                        'exchange/public/product',
                        'assetWithdraw/getAllAsset.html',
                    ],
                },
                'wapi': {
                    'post': [
                        'withdraw',
                    ],
                    'get': [
                        'getAllAsset',
                        'depositHistory',
                        'withdrawHistory',
                        'depositAddress',
                        'accountStatus',
                        'systemStatus',
                        'withdrawFee',
                    ],
                },
                'v3': {
                    'get': [
                        'ticker/price',
                        'ticker/bookTicker',
                    ],
                },
                'public': {
                    'get': [
                        'exchangeInfo',
                        'ping',
                        'time',
                        'depth',
                        'aggTrades',
                        'klines',
                        'ticker/24hr',
                        'ticker/allPrices',
                        'ticker/allBookTickers',
                        'ticker/price',
                        'ticker/bookTicker',
                        'exchangeInfo',
                    ],
                    'put': ['userDataStream'],
                    'post': ['userDataStream'],
                    'delete': ['userDataStream'],
                },
                'private': {
                    'get': [
                        'order',
                        'openOrders',
                        'allOrders',
                        'account',
                        'myTrades',
                    ],
                    'post': [
                        'order',
                        'order/test',
                    ],
                    'delete': [
                        'order',
                    ],
                },
            },
            'fees': {
                'trading': {
                    'tierBased': False,
                    'percentage': True,
                    'taker': 0.001,
                    'maker': 0.001,
                },
                # should be deleted, these are outdated and inaccurate
                'funding': {
                    'tierBased': False,
                    'percentage': False,
                    'withdraw': {
                        'ADA': 1.0,
                        'ADX': 4.7,
                        'AION': 1.9,
                        'AMB': 11.4,
                        'APPC': 6.5,
                        'ARK': 0.1,
                        'ARN': 3.1,
                        'AST': 10.0,
                        'BAT': 18.0,
                        'BCD': 1.0,
                        'BCH': 0.001,
                        'BCPT': 10.2,
                        'BCX': 1.0,
                        'BNB': 0.7,
                        'BNT': 1.5,
                        'BQX': 1.6,
                        'BRD': 6.4,
                        'BTC': 0.001,
                        'BTG': 0.001,
                        'BTM': 5.0,
                        'BTS': 1.0,
                        'CDT': 67.0,
                        'CMT': 37.0,
                        'CND': 47.0,
                        'CTR': 5.4,
                        'DASH': 0.002,
                        'DGD': 0.06,
                        'DLT': 11.7,
                        'DNT': 51.0,
                        'EDO': 2.5,
                        'ELF': 6.5,
                        'ENG': 2.1,
                        'ENJ': 42.0,
                        'EOS': 1.0,
                        'ETC': 0.01,
                        'ETF': 1.0,
                        'ETH': 0.01,
                        'EVX': 2.5,
                        'FUEL': 45.0,
                        'FUN': 85.0,
                        'GAS': 0,
                        'GTO': 20.0,
                        'GVT': 0.53,
                        'GXS': 0.3,
                        'HCC': 0.0005,
                        'HSR': 0.0001,
                        'ICN': 3.5,
                        'ICX': 1.3,
                        'INS': 1.5,
                        'IOTA': 0.5,
                        'KMD': 0.002,
                        'KNC': 2.6,
                        'LEND': 54.0,
                        'LINK': 12.8,
                        'LLT': 54.0,
                        'LRC': 9.1,
                        'LSK': 0.1,
                        'LTC': 0.01,
                        'LUN': 0.29,
                        'MANA': 74.0,
                        'MCO': 0.86,
                        'MDA': 4.7,
                        'MOD': 2.0,
                        'MTH': 34.0,
                        'MTL': 1.9,
                        'NAV': 0.2,
                        'NEBL': 0.01,
                        'NEO': 0.0,
                        'NULS': 2.1,
                        'OAX': 8.3,
                        'OMG': 0.57,
                        'OST': 17.0,
                        'POE': 88.0,
                        'POWR': 8.6,
                        'PPT': 0.25,
                        'QSP': 21.0,
                        'QTUM': 0.01,
                        'RCN': 35.0,
                        'RDN': 2.2,
                        'REQ': 18.1,
                        'RLC': 4.1,
                        'SALT': 1.3,
                        'SBTC': 1.0,
                        'SNGLS': 42,
                        'SNM': 29.0,
                        'SNT': 32.0,
                        'STORJ': 5.9,
                        'STRAT': 0.1,
                        'SUB': 7.4,
                        'TNB': 82.0,
                        'TNT': 47.0,
                        'TRIG': 6.7,
                        'TRX': 129.0,
                        'USDT': 23.0,
                        'VEN': 1.8,
                        'VIB': 28.0,
                        'VIBE': 7.2,
                        'WABI': 3.5,
                        'WAVES': 0.002,
                        'WINGS': 9.3,
                        'WTC': 0.5,
                        'XLM': 0.01,
                        'XMR': 0.04,
                        'XRP': 0.25,
                        'XVG': 0.1,
                        'XZC': 0.02,
                        'YOYOW': 39.0,
                        'ZEC': 0.005,
                        'ZRX': 5.7,
                    },
                    'deposit': {},
                },
            },
            'commonCurrencies': {
                'YOYO': 'YOYOW',
                'BCC': 'BCH',
            },
            # exchange-specific options
            'options': {
                'defaultTimeInForce': 'GTC',  # 'GTC' = Good To Cancel(default), 'IOC' = Immediate Or Cancel
                'defaultLimitOrderType': 'limit',  # or 'limit_maker'
                'hasAlreadyAuthenticatedSuccessfully': False,
                'warnOnFetchOpenOrdersWithoutSymbol': True,
                'recvWindow': 5 * 1000,  # 5 sec, binance default
                'timeDifference': 0,  # the difference between system clock and Binance clock
                'adjustForTimeDifference': False,  # controls the adjustment logic upon instantiation
                'parseOrderToPrecision': False,  # force amounts and costs in parseOrder to precision
                'newOrderRespType': 'RESULT',  # 'ACK' for order id, 'RESULT' for full order or 'FULL' for order with fills
            },
            'exceptions': {
                '-1000': ExchangeNotAvailable,  # {"code":-1000,"msg":"An unknown error occured while processing the request."}
                '-1013': InvalidOrder,  # createOrder -> 'invalid quantity'/'invalid price'/MIN_NOTIONAL
                '-1021': InvalidNonce,  # 'your time is ahead of server'
                '-1022': AuthenticationError,  # {"code":-1022,"msg":"Signature for self request is not valid."}
                '-1100': InvalidOrder,  # createOrder(symbol, 1, asdf) -> 'Illegal characters found in parameter 'price'
                '-1104': ExchangeError,  # Not all sent parameters were read, read 8 parameters but was sent 9
                '-1128': ExchangeError,  # {"code":-1128,"msg":"Combination of optional parameters invalid."}
                '-2010': ExchangeError,  # generic error code for createOrder -> 'Account has insufficient balance for requested action.', {"code":-2010,"msg":"Rest API trading is not enabled."}, etc...
                '-2011': OrderNotFound,  # cancelOrder(1, 'BTC/USDT') -> 'UNKNOWN_ORDER'
                '-2013': OrderNotFound,  # fetchOrder(1, 'BTC/USDT') -> 'Order does not exist'
                '-2014': AuthenticationError,  # {"code":-2014, "msg": "API-key format invalid."}
                '-2015': AuthenticationError,  # "Invalid API-key, IP, or permissions for action."
            },
        })

    def nonce(self):
        return self.milliseconds() - self.options['timeDifference']

    def load_time_difference(self):
        response = self.publicGetTime()
        after = self.milliseconds()
        self.options['timeDifference'] = int(after - response['serverTime'])
        return self.options['timeDifference']

    def fetch_markets(self):
        response = self.publicGetExchangeInfo()
        if self.options['adjustForTimeDifference']:
            self.load_time_difference()
        markets = response['symbols']
        result = []
        for i in range(0, len(markets)):
            market = markets[i]
            id = market['symbol']
            # "123456" is a "test symbol/market"
            if id == '123456':
                continue
            baseId = market['baseAsset']
            quoteId = market['quoteAsset']
            base = self.common_currency_code(baseId)
            quote = self.common_currency_code(quoteId)
            symbol = base + '/' + quote
            filters = self.index_by(market['filters'], 'filterType')
            precision = {
                'base': market['baseAssetPrecision'],
                'quote': market['quotePrecision'],
                'amount': market['baseAssetPrecision'],
                'price': market['quotePrecision'],
            }
            active = (market['status'] == 'TRADING')
            entry = {
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'info': market,
                'active': active,
                'precision': precision,
                'limits': {
                    'amount': {
                        'min': math.pow(10, -precision['amount']),
                        'max': None,
                    },
                    'price': {
                        'min': math.pow(10, -precision['price']),
                        'max': None,
                    },
                    'cost': {
                        'min': -1 * math.log10(precision['amount']),
                        'max': None,
                    },
                },
            }
            if 'PRICE_FILTER' in filters:
                filter = filters['PRICE_FILTER']
                entry['precision']['price'] = self.precision_from_string(filter['tickSize'])
                entry['limits']['price'] = {
                    'min': self.safe_float(filter, 'minPrice'),
                    'max': self.safe_float(filter, 'maxPrice'),
                }
            if 'LOT_SIZE' in filters:
                filter = filters['LOT_SIZE']
                entry['precision']['amount'] = self.precision_from_string(filter['stepSize'])
                entry['limits']['amount'] = {
                    'min': self.safe_float(filter, 'minQty'),
                    'max': self.safe_float(filter, 'maxQty'),
                }
            if 'MIN_NOTIONAL' in filters:
                entry['limits']['cost']['min'] = float(filters['MIN_NOTIONAL']['minNotional'])
            result.append(entry)
        return result

    def calculate_fee(self, symbol, type, side, amount, price, takerOrMaker='taker', params={}):
        market = self.markets[symbol]
        key = 'quote'
        rate = market[takerOrMaker]
        cost = float(self.cost_to_precision(symbol, amount * rate))
        if side == 'sell':
            cost *= price
        else:
            key = 'base'
        return {
            'type': takerOrMaker,
            'currency': market[key],
            'rate': rate,
            'cost': float(self.fee_to_precision(symbol, cost)),
        }

    def fetch_balance(self, params={}):
        self.load_markets()
        response = self.privateGetAccount(params)
        result = {'info': response}
        balances = response['balances']
        for i in range(0, len(balances)):
            balance = balances[i]
            currency = balance['asset']
            if currency in self.currencies_by_id:
                currency = self.currencies_by_id[currency]['code']
            account = {
                'free': float(balance['free']),
                'used': float(balance['locked']),
                'total': 0.0,
            }
            account['total'] = self.sum(account['free'], account['used'])
            result[currency] = account
        return self.parse_balance(result)

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        if limit is not None:
            request['limit'] = limit  # default = maximum = 100
        response = self.publicGetDepth(self.extend(request, params))
        orderbook = self.parse_order_book(response)
        orderbook['nonce'] = self.safe_integer(response, 'lastUpdateId')
        return orderbook

    def parse_ticker(self, ticker, market=None):
        timestamp = self.safe_integer(ticker, 'closeTime')
        iso8601 = None if (timestamp is None) else self.iso8601(timestamp)
        symbol = self.find_symbol(self.safe_string(ticker, 'symbol'), market)
        last = self.safe_float(ticker, 'lastPrice')
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': iso8601,
            'high': self.safe_float(ticker, 'highPrice'),
            'low': self.safe_float(ticker, 'lowPrice'),
            'bid': self.safe_float(ticker, 'bidPrice'),
            'bidVolume': self.safe_float(ticker, 'bidQty'),
            'ask': self.safe_float(ticker, 'askPrice'),
            'askVolume': self.safe_float(ticker, 'askQty'),
            'vwap': self.safe_float(ticker, 'weightedAvgPrice'),
            'open': self.safe_float(ticker, 'openPrice'),
            'close': last,
            'last': last,
            'previousClose': self.safe_float(ticker, 'prevClosePrice'),  # previous day close
            'change': self.safe_float(ticker, 'priceChange'),
            'percentage': self.safe_float(ticker, 'priceChangePercent'),
            'average': None,
            'baseVolume': self.safe_float(ticker, 'volume'),
            'quoteVolume': self.safe_float(ticker, 'quoteVolume'),
            'info': ticker,
        }

    def fetch_ticker(self, symbol, params={}):
        self.load_markets()
        market = self.market(symbol)
        response = self.publicGetTicker24hr(self.extend({
            'symbol': market['id'],
        }, params))
        return self.parse_ticker(response, market)

    def parse_tickers(self, rawTickers, symbols=None):
        tickers = []
        for i in range(0, len(rawTickers)):
            tickers.append(self.parse_ticker(rawTickers[i]))
        return self.filter_by_array(tickers, 'symbol', symbols)

    def fetch_bids_asks(self, symbols=None, params={}):
        self.load_markets()
        rawTickers = self.publicGetTickerBookTicker(params)
        return self.parse_tickers(rawTickers, symbols)

    def fetch_tickers(self, symbols=None, params={}):
        self.load_markets()
        rawTickers = self.publicGetTicker24hr(params)
        return self.parse_tickers(rawTickers, symbols)

    def parse_ohlcv(self, ohlcv, market=None, timeframe='1m', since=None, limit=None):
        return [
            ohlcv[0],
            float(ohlcv[1]),
            float(ohlcv[2]),
            float(ohlcv[3]),
            float(ohlcv[4]),
            float(ohlcv[5]),
        ]

    def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
            'interval': self.timeframes[timeframe],
        }
        if since is not None:
            request['startTime'] = since
        if limit is not None:
            request['limit'] = limit  # default == max == 500
        response = self.publicGetKlines(self.extend(request, params))
        return self.parse_ohlcvs(response, market, timeframe, since, limit)

    def parse_trade(self, trade, market=None):
        timestampField = 'T' if ('T' in list(trade.keys())) else 'time'
        timestamp = self.safe_integer(trade, timestampField)
        priceField = 'p' if ('p' in list(trade.keys())) else 'price'
        price = self.safe_float(trade, priceField)
        amountField = 'q' if ('q' in list(trade.keys())) else 'qty'
        amount = self.safe_float(trade, amountField)
        idField = 'a' if ('a' in list(trade.keys())) else 'id'
        id = self.safe_string(trade, idField)
        side = None
        order = None
        if 'orderId' in trade:
            order = self.safe_string(trade, 'orderId')
        if 'm' in trade:
            side = 'sell' if trade['m'] else 'buy'  # self is reversed intentionally
        else:
            if 'isBuyer' in trade:
                side = 'buy' if (trade['isBuyer']) else 'sell'  # self is a True side
        fee = None
        if 'commission' in trade:
            fee = {
                'cost': self.safe_float(trade, 'commission'),
                'currency': self.common_currency_code(trade['commissionAsset']),
            }
        takerOrMaker = None
        if 'isMaker' in trade:
            takerOrMaker = 'maker' if trade['isMaker'] else 'taker'
        return {
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': market['symbol'],
            'id': id,
            'order': order,
            'type': None,
            'takerOrMaker': takerOrMaker,
            'side': side,
            'price': price,
            'cost': price * amount,
            'amount': amount,
            'fee': fee,
        }

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        if since is not None:
            request['startTime'] = since
            request['endTime'] = since + 3600000
        if limit is not None:
            request['limit'] = limit
        # 'fromId': 123,    # ID to get aggregate trades from INCLUSIVE.
        # 'startTime': 456,  # Timestamp in ms to get aggregate trades from INCLUSIVE.
        # 'endTime': 789,   # Timestamp in ms to get aggregate trades until INCLUSIVE.
        # 'limit': 500,     # default = 500, maximum = 1000
        #
        # Caveats:
        # - default limit(500) applies only if no other parameters set, trades up
        #   to the maximum limit may be returned to satisfy other parameters
        # - if both limit and time window is set and time window contains more
        #   trades than the limit then the last trades from the window are returned
        # - 'tradeId' accepted and returned by self method is "aggregate" trade id
        #   which is different from actual trade id
        # - setting both fromId and time window results in error
        response = self.publicGetAggTrades(self.extend(request, params))
        return self.parse_trades(response, market, since, limit)

    def parse_order_status(self, status):
        statuses = {
            'NEW': 'open',
            'PARTIALLY_FILLED': 'open',
            'FILLED': 'closed',
            'CANCELED': 'canceled',
        }
        return statuses[status] if (status in list(statuses.keys())) else status.lower()

    def parse_order(self, order, market=None):
        status = self.safe_value(order, 'status')
        if status is not None:
            status = self.parse_order_status(status)
        symbol = self.find_symbol(self.safe_string(order, 'symbol'), market)
        timestamp = None
        if 'time' in order:
            timestamp = order['time']
        elif 'transactTime' in order:
            timestamp = order['transactTime']
        iso8601 = None
        if timestamp is not None:
            iso8601 = self.iso8601(timestamp)
        price = self.safe_float(order, 'price')
        amount = self.safe_float(order, 'origQty')
        filled = self.safe_float(order, 'executedQty')
        remaining = None
        cost = None
        if filled is not None:
            if amount is not None:
                remaining = amount - filled
                if self.options['parseOrderToPrecision']:
                    remaining = float(self.amount_to_precision(symbol, remaining))
                remaining = max(remaining, 0.0)
            if price is not None:
                cost = price * filled
        id = self.safe_string(order, 'orderId')
        type = self.safe_string(order, 'type')
        if type is not None:
            type = type.lower()
            if type == 'market':
                if price == 0.0:
                    quoteCost = self.safe_float(order, 'cummulativeQuoteQty')
                    if (quoteCost is not None) and(filled is not None):
                        if (quoteCost > 0) and(filled > 0):
                            price = quoteCost / filled
        side = self.safe_string(order, 'side')
        if side is not None:
            side = side.lower()
        fee = None
        trades = None
        fills = self.safe_value(order, 'fills')
        if fills is not None:
            trades = self.parse_trades(fills, market)
            numTrades = len(trades)
            if numTrades > 0:
                cost = trades[0]['cost']
                fee = {
                    'cost': trades[0]['fee']['cost'],
                    'currency': trades[0]['fee']['currency'],
                }
                for i in range(1, len(trades)):
                    cost = self.sum(cost, trades[i]['cost'])
                    fee['cost'] = self.sum(fee['cost'], trades[i]['fee']['cost'])
                if cost and filled:
                    price = cost / filled
        if cost is not None:
            if self.options['parseOrderToPrecision']:
                cost = float(self.cost_to_precision(symbol, cost))
        result = {
            'info': order,
            'id': id,
            'timestamp': timestamp,
            'datetime': iso8601,
            'lastTradeTimestamp': None,
            'symbol': symbol,
            'type': type,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': cost,
            'filled': filled,
            'remaining': remaining,
            'status': status,
            'fee': fee,
            'trades': trades,
        }
        return result

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        # the next 5 lines are added to support for testing orders
        method = 'privatePostOrder'
        test = self.safe_value(params, 'test', False)
        if test:
            method += 'Test'
            params = self.omit(params, 'test')
        uppercaseType = type.upper()
        order = {
            'symbol': market['id'],
            'quantity': self.amount_to_string(symbol, amount),
            'type': uppercaseType,
            'side': side.upper(),
            'newOrderRespType': self.options['newOrderRespType'],  # 'ACK' for order id, 'RESULT' for full order or 'FULL' for order with fills
        }
        timeInForceIsRequired = False
        priceIsRequired = False
        stopPriceIsRequired = False
        if uppercaseType == 'LIMIT':
            priceIsRequired = True
            timeInForceIsRequired = True
        elif (uppercaseType == 'STOP_LOSS') or (uppercaseType == 'TAKE_PROFIT'):
            stopPriceIsRequired = True
        elif (uppercaseType == 'STOP_LOSS_LIMIT') or (uppercaseType == 'TAKE_PROFIT_LIMIT'):
            stopPriceIsRequired = True
            priceIsRequired = True
            timeInForceIsRequired = True
        elif uppercaseType == 'LIMIT_MAKER':
            priceIsRequired = True
        if priceIsRequired:
            if price is None:
                raise InvalidOrder(self.id + ' createOrder method requires a price argument for a ' + type + ' order')
            order['price'] = self.price_to_precision(symbol, price)
        if timeInForceIsRequired:
            order['timeInForce'] = self.options['defaultTimeInForce']  # 'GTC' = Good To Cancel(default), 'IOC' = Immediate Or Cancel
        if stopPriceIsRequired:
            stopPrice = self.safe_float(params, 'stopPrice')
            if stopPrice is None:
                raise InvalidOrder(self.id + ' createOrder method requires a stopPrice extra param for a ' + type + ' order')
            else:
                order['stopPrice'] = self.price_to_precision(symbol, stopPrice)
        response = getattr(self, method)(self.extend(order, params))
        return self.parse_order(response, market)

    def fetch_order(self, id, symbol=None, params={}):
        if symbol is None:
            raise ExchangeError(self.id + ' fetchOrder requires a symbol argument')
        self.load_markets()
        market = self.market(symbol)
        origClientOrderId = self.safe_value(params, 'origClientOrderId')
        request = {
            'symbol': market['id'],
        }
        if origClientOrderId is not None:
            request['origClientOrderId'] = origClientOrderId
        else:
            request['orderId'] = int(id)
        response = self.privateGetOrder(self.extend(request, params))
        return self.parse_order(response, market)

    def fetch_orders(self, symbol=None, since=None, limit=None, params={}):
        if symbol is None:
            raise ExchangeError(self.id + ' fetchOrders requires a symbol argument')
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        if limit is not None:
            request['limit'] = limit
        response = self.privateGetAllOrders(self.extend(request, params))
        return self.parse_orders(response, market, since, limit)

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        market = None
        request = {}
        if symbol is not None:
            market = self.market(symbol)
            request['symbol'] = market['id']
        elif self.options['warnOnFetchOpenOrdersWithoutSymbol']:
            symbols = self.symbols
            numSymbols = len(symbols)
            fetchOpenOrdersRateLimit = int(numSymbols / 2)
            raise ExchangeError(self.id + ' fetchOpenOrders WARNING: fetching open orders without specifying a symbol is rate-limited to one call per ' + str(fetchOpenOrdersRateLimit) + ' seconds. Do not call self method frequently to avoid ban. Set ' + self.id + '.options["warnOnFetchOpenOrdersWithoutSymbol"] = False to suppress self warning message.')
        response = self.privateGetOpenOrders(self.extend(request, params))
        return self.parse_orders(response, market, since, limit)

    def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        orders = self.fetch_orders(symbol, since, limit, params)
        return self.filter_by(orders, 'status', 'closed')

    def cancel_order(self, id, symbol=None, params={}):
        if symbol is None:
            raise ExchangeError(self.id + ' cancelOrder requires a symbol argument')
        self.load_markets()
        market = self.market(symbol)
        response = self.privateDeleteOrder(self.extend({
            'symbol': market['id'],
            'orderId': int(id),
            # 'origClientOrderId': id,
        }, params))
        return self.parse_order(response)

    def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        if symbol is None:
            raise ExchangeError(self.id + ' fetchMyTrades requires a symbol argument')
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        if limit is not None:
            request['limit'] = limit
        response = self.privateGetMyTrades(self.extend(request, params))
        return self.parse_trades(response, market, since, limit)

    def fetch_deposit_address(self, code, params={}):
        self.load_markets()
        currency = self.currency(code)
        response = self.wapiGetDepositAddress(self.extend({
            'asset': currency['id'],
        }, params))
        if 'success' in response:
            if response['success']:
                address = self.safe_string(response, 'address')
                tag = self.safe_string(response, 'addressTag')
                return {
                    'currency': code,
                    'address': self.check_address(address),
                    'tag': tag,
                    'info': response,
                }

    def fetch_funding_fees(self, codes=None, params={}):
        #  by default it will try load withdrawal fees of all currencies(with separate requests)
        #  however if you define codes = ['ETH', 'BTC'] in args it will only load those
        self.load_markets()
        withdrawFees = {}
        info = {}
        if codes is None:
            codes = list(self.currencies.keys())
        for i in range(0, len(codes)):
            code = codes[i]
            currency = self.currency(code)
            response = self.wapiGetWithdrawFee({
                'asset': currency['id'],
            })
            withdrawFees[code] = self.safe_float(response, 'withdrawFee')
            info[code] = response
        return {
            'withdraw': withdrawFees,
            'deposit': {},
            'info': info,
        }

    def withdraw(self, code, amount, address, tag=None, params={}):
        self.check_address(address)
        self.load_markets()
        currency = self.currency(code)
        name = address[0:20]
        request = {
            'asset': currency['id'],
            'address': address,
            'amount': float(amount),
            'name': name,
        }
        if tag:
            request['addressTag'] = tag
        response = self.wapiPostWithdraw(self.extend(request, params))
        return {
            'info': response,
            'id': self.safe_string(response, 'id'),
        }

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'][api]
        url += '/' + path
        if api == 'wapi':
            url += '.html'
        # v1 special case for userDataStream
        if path == 'userDataStream':
            body = self.urlencode(params)
            headers = {
                'X-MBX-APIKEY': self.apiKey,
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        elif (api == 'private') or (api == 'wapi'):
            self.check_required_credentials()
            query = self.urlencode(self.extend({
                'timestamp': self.nonce(),
                'recvWindow': self.options['recvWindow'],
            }, params))
            signature = self.hmac(self.encode(query), self.encode(self.secret))
            query += '&' + 'signature=' + signature
            headers = {
                'X-MBX-APIKEY': self.apiKey,
            }
            if (method == 'GET') or (method == 'DELETE') or (api == 'wapi'):
                url += '?' + query
            else:
                body = query
                headers['Content-Type'] = 'application/x-www-form-urlencoded'
        else:
            if params:
                url += '?' + self.urlencode(params)
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, code, reason, url, method, headers, body):
        if (code == 418) or (code == 429):
            raise DDoSProtection(self.id + ' ' + str(code) + ' ' + reason + ' ' + body)
        # error response in a form: {"code": -1013, "msg": "Invalid quantity."}
        # following block cointains legacy checks against message patterns in "msg" property
        # will switch "code" checks eventually, when we know all of them
        if code >= 400:
            if body.find('Price * QTY is zero or less') >= 0:
                raise InvalidOrder(self.id + ' order cost = amount * price is zero or less ' + body)
            if body.find('LOT_SIZE') >= 0:
                raise InvalidOrder(self.id + ' order amount should be evenly divisible by lot size ' + body)
            if body.find('PRICE_FILTER') >= 0:
                raise InvalidOrder(self.id + ' order price exceeds allowed price precision or invalid, use self.price_to_precision(symbol, amount) ' + body)
        if len(body) > 0:
            if body[0] == '{':
                response = json.loads(body)
                # check success value for wapi endpoints
                # response in format {'msg': 'The coin does not exist.', 'success': True/false}
                success = self.safe_value(response, 'success', True)
                if not success:
                    if 'msg' in response:
                        try:
                            response = json.loads(response['msg'])
                        except Exception as e:
                            response = {}
                # checks against error codes
                error = self.safe_string(response, 'code')
                if error is not None:
                    exceptions = self.exceptions
                    if error in exceptions:
                        # a workaround for {"code":-2015,"msg":"Invalid API-key, IP, or permissions for action."}
                        # despite that their message is very confusing, it is raised by Binance
                        # on a temporary ban(the API key is valid, but disabled for a while)
                        if (error == '-2015') and self.options['hasAlreadyAuthenticatedSuccessfully']:
                            raise DDoSProtection(self.id + ' temporary banned: ' + body)
                        message = self.safe_string(response, 'msg')
                        if message == 'Order would trigger immediately.':
                            raise InvalidOrder(self.id + ' ' + body)
                        elif message == 'Account has insufficient balance for requested action.':
                            raise InsufficientFunds(self.id + ' ' + body)
                        elif message == 'Rest API trading is not enabled.':
                            raise ExchangeNotAvailable(self.id + ' ' + body)
                        raise exceptions[error](self.id + ' ' + body)
                    else:
                        raise ExchangeError(self.id + ' ' + body)
                if not success:
                    raise ExchangeError(self.id + ' ' + body)

    def request(self, path, api='public', method='GET', params={}, headers=None, body=None):
        response = self.fetch2(path, api, method, params, headers, body)
        # a workaround for {"code":-2015,"msg":"Invalid API-key, IP, or permissions for action."}
        if (api == 'private') or (api == 'wapi'):
            self.options['hasAlreadyAuthenticatedSuccessfully'] = True
        return response
