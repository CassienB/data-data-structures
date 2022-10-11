# pylint: disable=missing-docstring


RATES = {
    'USDEUR':0.85,
    'GBPEUR':1.13,
    "CHFEUR":0.86,
    'EURUSD': 1 / 0.85,
    'EURGBP': 1 / 1.13,
    'EURCHF': 1 / 0.86}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    if RATES.get(amount[1] + currency):
        return round(amount[0] * RATES[amount[1] + currency])
    return None
