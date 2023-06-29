# crawl-defi-data
Repository for the study of crawling data on DeFi

## 
Clone this repository

```bash
git clone https://github.com/fuqishuang228/crawl-defi-data.git
```

Navigate to the directory of the cloned repo

```bash
cd crawl-defi-data
```

## Set up the repo

### Give execute permission to your script and then run `setup_repo.sh`

```
chmod +x setup_repo.sh
./setup_repo.sh
```

or follow the step-by-step instructions below

### Create a python virtual environment

- iOS

```zsh
python3 -m venv venv
```

- Windows

```
python -m venv venv
```

### Activate the virtual environment

- iOS

```zsh
. venv/bin/activate
```

- Windows (in Command Prompt, NOT Powershell)

```zsh
venv\Scripts\activate.bat
```

## Install the project in editable mode

```
pip install -e ".[dev]"
```
or 

```
pip install -e ".[dev]" -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```
## Question I met
Q1：ProxyError: HTTPSConnectionPool(host='coinmarketcap.com', port=443): Max retries exceeded with url: /exchanges/binance/ (Caused by ProxyError('Unable to connect to proxy', FileNotFoundError(2, 'No such file or directory')))\
A1: pip install urllib3==1.25.11 -- reduce the version of urllib3

Q2: locate context of Json\
A2： there is a useful tool called vscode-json,ctrl+alt+b