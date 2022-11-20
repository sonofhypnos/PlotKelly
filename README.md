# plotKelly

This is just quick shell tool based on the hard work of the [PyManifold](https://github.com/bcongdon/PyManifold) project.
Displays a plot on how much you should bet on a manifold market given a subjective crecedence range. The betsize is calculated through the kelly criterion. 
Quickly hacked together. If I am still using this in the future I might merge pull requests. 

## install
Only probably only works on linux. 

run: 

``` bash
.git clone --depth 1 --recurse-submodules https://github.com/sonofhypnos/plot-kelly
cd plot-kelly
chmod +x install.sh
./install.sh
```

./install creates a virtualenvironment for this repo using poetry.
Create a virtualenvironment to run 
```
git clone 
python3 -m venv .venv
source .venv/
```

## Usage

```python
./plot_kelly.sh https://manifold.markets/IsaacKing/will-systemic-poverty-be-eliminated 800 1 100
```

![example](https://github.com/sonofhypnos/PyManifold/blob/main/pymanifold/readme-kelly.png)

## TODO

- [ ] Add different markets?

## Running Tests

```sh
$ poetry run pytest
```
