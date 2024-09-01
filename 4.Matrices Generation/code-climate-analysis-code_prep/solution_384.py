import decimal
print("Configure the rounding to round to the nearest, with ties going towards 0:")
decimal.getcontext().prec = 1
decimal.getcontext().rounding = decimal.ROUND_HALF_DOWN
print(decimal.Decimal(10) / decimal.Decimal(4))
print("\nConfigure the rounding to round to the nearest, with ties going away from 0:")
decimal.getcontext().prec = 1
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
print(decimal.Decimal(10) / decimal.Decimal(4))
