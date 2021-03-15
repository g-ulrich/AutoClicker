# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['AutoClicker.py'],
             pathex=['C:\\desktop2\\projects\\pyqt5\\AutoClickerGUI\\autoClicker'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['tkinter', 'numpy', 'flask', 'eel', 'colorama', 'func_timeout', 'get_all_tickers', 'itsdangerous', 'pandas', 'pyowm', 'PySide2', 'pytweening', 'requests', 'selenium', 'scipy', 'talib', 'tda', 'tda_api', 'tests', 'twilio', 'urllib3'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='AutoClicker',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='images\\mouse.ico')
