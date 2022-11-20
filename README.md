# plotKelly

This shell tool is based on the [PyManifold](https://github.com/bcongdon/PyManifold) project.
Displays a plot on how much you should bet on a manifold market given a subjective crecedence range. The betsize is calculated through the kelly criterion. 
Quickly hacked together. If I am still using this in the future I might merge pull requests. 

## install
Only works on linux. 

run: 

``` bash
git clone --depth 1 --recurse-submodules https://github.com/sonofhypnos/PlotKelly
cd PlotKelly
chmod +x install.sh
./install.sh
```

./install creates a virtualenvironment and uses poetry to install dependencies. Should work with python3.8 or greater.

## Usage
run plot_kelly.sh and supply url, your bankroll on Manifold, upper and lower bounds crecedence percentages. 

Example:
```python
./plot_kelly.sh https://manifold.markets/IsaacKing/will-systemic-poverty-be-eliminated 800 1 100
```

![example](https://github.com/sonofhypnos/PyManifold/blob/main/pymanifold/readme-kelly.png)

## TODO

- [ ] Add different markets?
- [ ] add plot for regular kelly formula

## Running Tests

```sh
$ poetry run pytest
```
