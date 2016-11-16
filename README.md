# behave-generator

CLI to setup Python Projects to use Behave BDD

## Install
```
pip install behave-generator
```

## Usage
CLI command "behave-generator" will create:
* `features/` directory
* `features/steps` directory
* `features/environment.py` 

There is one command option `--browser` which configures the Behave setup to
use Selenium Webdriver for integration/functional testing.

```
$ behave-generator --browser=chrome
```
