# uiScrypt

It's a UI implementation of [**Scrypt**](https://en.wikipedia.org/wiki/Scrypt) on PyQt5.

![uiScrypt preview](https://github.com/NotStatilko/uiScrypt/assets/43419673/ea1b6231-43aa-4a1b-8030-de4bb5d49fa4)

## Install

**uiScrypt** is available on **PyPI**, install with *pip*:
```bash
pip install uiScrypt
```

## Usage

### Run uiScrypt

Just type `uiScrypt` in your Terminal:
```bash
uiScrypt
```

### Configuration

You can set Scrypt configuration via **CMD args**
```bash
# python3 uiScrypt.py <N> <r> <p> <dklen> <hex|b64>
python3 uiScrypt.py 1048576 8 1 32 b64 # Default Configuration
```
