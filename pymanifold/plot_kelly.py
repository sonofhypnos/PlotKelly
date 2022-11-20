#!/usr/bin/env python3
import sys
import os
from pymanifold import ManifoldClient
import pandas as pd
import matplotlib.pyplot as plt


url, bankroll, lower, upper = sys.argv[1:]  # lower and upper in percent
bankroll = int(bankroll)
lower = int(lower)
upper = int(upper)

# TODO - remove stuff to get slug
# List markets
client = ManifoldClient()

# Find optimal Kelly bet
from pymanifold.utils import kelly_calc

market = client.get_market_by_url(url)
transform = lambda bet: bet[0] if (bet[1] == "YES") else -1 * bet[0]
[]
pd.Series(
    [transform(kelly_calc(market, 0.01 * i, bankroll)) for i in range(lower, upper)]
).plot()
# plt.vlines([0.01 * x for x in range(1, 100, 5)], -1000, 1000, linestyles="dashed")
plt.grid(visible=True)
plt.xlabel("Subjective Probability in %")
plt.ylabel("M$ to bet (negative means bet on NO)")
plt.savefig("kelly.png")
plt.title(f'Kelly bet on"{market.question}"')
os.system("xdg-open kelly.png")
