from setuptools import setup
from ast import literal_eval

with open('uiScrypt/version.py', encoding='utf-8') as f:
    version = literal_eval(f.read().split('=',1)[1].strip())

setup(
    name             = 'uiScrypt',
    version          =  version,
    packages         =  ['uiScrypt'],
    license          =  'MIT',
    description      =  'A simple GUI app for generating Scrypt keys',
    long_description = open('README.md', encoding='utf-8').read(),
    author_email     =  'thenonproton@pm.me',
    url              =  'https://github.com/NotStatilko/uiScrypt',
    download_url     =  f'https://github.com/NotStatilko/uiScrypt/archive/refs/tags/v{version}.tar.gz',

    install_requires = [
        'pyqt5==5.15.9',
        'qrcode==6.1',
        'pillow==9.5.0'
    ],
    long_description_content_type='text/markdown',

    package_data = {
        'uiScrypt': ['uiScrypt/data'],
    },

    entry_points = '''
        [console_scripts]
        uiScrypt=uiScrypt.uiScrypt:main
    ''',
)
