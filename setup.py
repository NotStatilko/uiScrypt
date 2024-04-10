from setuptools import setup

setup(
    name             = 'uiScrypt',
    version          =  '2.0',
    packages         =  ['uiScrypt'],
    license          =  'MIT',
    description      =  'A simple GUI app for generating Scrypt keys',
    long_description = open('README.md', encoding='utf-8').read(),
    author_email     =  'thenonproton@pm.me',
    url              =  'https://github.com/NotStatilko/uiScrypt',
    download_url     =  'https://github.com/NotStatilko/uiScrypt/archive/refs/tags/v2.0.tar.gz',

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
