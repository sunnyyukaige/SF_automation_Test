# SF_automation_Test

## UI automated testing

### Setting up the environment

1. Install [pyenv](https://github.com/pyenv/pyenv).
2. Install Python 3.6 running `pyenv install 3.6.1`.
3. Set the newly installed Python to be used globally running `pyenv global 3.6.1`.
4. Install Selenium running `pip install selenium`.
5. Install the [Chrome driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) for Selenium and add it to your PATH.  
If you use macOS, you can do this via [Homebrew](https://brew.sh/) running `brew install chromedriver`.
7. Install Behave running `pip install behave`.

### Run the tests

1. Go to the directory `UI automation/OMNI_UI_automation`.
2. Run `behave -D env=qa`.

## Performance testing

### Setting up the environment

1. Install the JDK environment.
2. Download the latest version of JMeter.
3. Install tool management and install useful plugins.

## API testing

### Setting up the environment

1. Download and install the latest version of postman.
