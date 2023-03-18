# Installation

## Create Environment

```bash
# Create using environment file
# the sample below have used tensorflow as environment name
# * specific environment config file argument either in -f | --file

conda env create --file tax-calculator.yml --name tax-calculator
```

## OR

```bash
# Easy create environment at default folder (in anaconda installation location)
# * specific environment name with either argument -n | --name
conda create --name tax-calculator python=3.10
```

## OR

```bash
# Easy create environment at specific path
conda create --prefix ./venv python=3.10
```

# Common problems

1. WARNING!!! file_name cannot contain SPACE in projects
