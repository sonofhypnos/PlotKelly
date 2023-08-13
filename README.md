# plotKelly

This shell tool is based on the [PyManifold](https://github.com/bcongdon/PyManifold) project.
Displays a plot on how much you should bet on a manifold market given a subjective crecedence range. The betsize is calculated through the kelly criterion. If you have never heard about it, I recommend learning more about it. [Here's some random article on it I enjoyed](https://www.lesswrong.com/posts/3pjv6uDvY9sqmsnvY/kelly-bet-on-everything).
Quickly hacked together. If I am still using this in the future I might merge pull requests.

## install
Should work on linux and possibly macOS as long as git and python>=3.8 (including virtualenvironment for your python) are installed.

run: 

``` bash
git clone --depth 1 --recurse-submodules https://github.com/sonofhypnos/PlotKelly
cd PlotKelly
chmod +x install.sh
./install.sh
```

./install creates a virtualenvironment and uses poetry to install dependencies.

## Usage
run plot_kelly.sh and supply url, your bankroll on Manifold, upper, lower %-bounds for the plot and crecedence percentages. 

Example:
```python
./plot_kelly.sh https://manifold.markets/IsaacKing/will-systemic-poverty-be-eliminated 800 1 100
```

![example](https://github.com/sonofhypnos/PyManifold/blob/main/pymanifold/readme-kelly.png)

## TODO

- [ ] Add different markets?
- [ ] add plot for regular kelly formulam (even though is boring/linear)
- [ ] figure out implications that lending has on this.
- [ ] better explanation in the readme

## Running Tests

```sh
$ poetry run pytest
```
