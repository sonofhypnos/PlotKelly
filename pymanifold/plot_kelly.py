#!/usr/bin/env python3
import sys
import os
from pymanifold import ManifoldClient
from pymanifold.utils import kelly_calc
import pandas as pd
import matplotlib.pyplot as plt

# Import the necessary module
from pymanifold import Market, Bet, Comment

# HACK: Patch
def new_from_dict(cls, env):
    # Provide default values for missing keys
    env.setdefault("tags", [])
    env.setdefault("volume7Days", 0.0)

    # Now, call the original from_dict logic
    # This is the existing logic you're replacing or extending
    market = super(Market, cls).from_dict(env)

    bets = env.get("bets", [])
    comments = env.get("comments", [])

    market.bets = [Bet.from_dict(bet) for bet in bets]
    market.comments = [Comment.from_dict(comment) for comment in comments]

    return market


# # Apply the monkey patch
Market.from_dict = classmethod(new_from_dict)


# parse command line arguments
if len(sys.argv) < 5:
    url, bankroll = sys.argv[1:]  # lower and upper in percent
    bankroll = int(bankroll)
    lower = 1
    upper = 99

else:
    url, bankroll, lower, upper = sys.argv[1:]  # lower and upper in percent
    bankroll = int(bankroll)
    lower = int(lower)
    upper = int(upper)


# Find optimal Kelly bet
client = ManifoldClient()

# market = client.get_market_by_url(url)
market = client.get_market_by_url(
    "https://api.manifold.markets/IsaacKing/will-systemic-poverty-be-eliminated"
)
transform = lambda bet: bet[0] if (bet[1] == "YES") else -1 * bet[0]
[]
pd.Series(
    [transform(kelly_calc(market, 0.01 * i, bankroll)) for i in range(lower, upper + 1)]
).plot()
plt.grid(visible=True)
plt.xlabel("Subjective Probability in %")
plt.ylabel("M$ to bet (negative means bet on NO)")
plt.title(f'Kelly bet on "{market.question}"')
plt.savefig("kelly.png")
os.system("xdg-open kelly.png")
