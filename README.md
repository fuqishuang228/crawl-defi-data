# dex-asset-pricing
Repository for the study of network risk factor in DEX

## 
Clone this repository

```bash
git clone https://github.com/lyc0603/dex-asset-pricing.git
```

Navigate to the directory of the cloned repo

```bash
cd dex-asset-pricing
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
