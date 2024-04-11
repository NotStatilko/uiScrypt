from pathlib import Path


if Path.cwd().name != 'pyinstaller':
    raise RuntimeError('You should build App inside the "pyinstaller" folder.')

MAIN_SCRIPT = '.uiScrypt_wrapper.py'
SCRIPT_LOGO = Path.cwd() / 'logo/logo.ico'


a = Analysis(
    [str(MAIN_SCRIPT)],
    pathex = [str(Path.cwd().parent)],
    binaries = [],
    datas = [],
    hiddenimports = [],
    hookspath = [],
    hooksconfig = {},
    runtime_hooks = [],
    excludes = [],
    win_no_prefer_redirects = False,
    win_private_assemblies = False,
    cipher = None,
    noarchive = False
)
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher = None
)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas, [],
    name = 'uiScrypt',
    icon = str(SCRIPT_LOGO),
    debug = False,
    bootloader_ignore_signals = False,
    strip = False,
    upx = True,
    upx_exclude = [],
    runtime_tmpdir = None,
    console = False,
    disable_windowed_traceback = False,
    target_arch = None,
    codesign_identity = None,
    entitlements_file = None
)
