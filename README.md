# fabletics-skip
script to log into fabletics and skip the month so you don't get charged

## Background
- python3 and selenium based
- credentials are not stored in this repo, must create a credentials file and fill in with your own
- future scope: scheduling this job to occur on the first of each month


## Initial Set Up
- Before you begin, ensure you have a preferred virtual environment (venv, pyenv), python3, and geckodriver available
`brew install python3` -- via homebrew
`pip3 install virtualenv`
`brew install geckodriver` -- via homebrew

- set up virtual env (create, initialize) -- from main repo or venv storage, feel free to replace "fab" with other name for venv for this project
`python3 -m venv fab` 
`source fab/bin/activate`

- set up dependences - from your virtual environment, inside your repo, run:
` pip install -r requirements.txt `

- create credentials file -- from inside main repo, run
`touch credentials.py`
add in your username and password
```
username = "[insert email here]"
password = "[insert password here]"
```

## Running the Script
- `./run.py`

