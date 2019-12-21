# Вам даны текущие цены на акции. Вам необходимо выяснить за какие акции дают большую цену.
# Input: Словарь (dict), в котором ключи - это рыночный код, а значение - это цена за акцию(float)
# Output: Строка, рыночный код

def stock_best_price(a):
    cena = list(a.items())
    cena.sort(key=lambda i: i[1])
    return cena[-1][0]


if __name__ == '__main__':
    print("Example:")
    print(stock_best_price({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert stock_best_price({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert stock_best_price({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
    print("Coo!")