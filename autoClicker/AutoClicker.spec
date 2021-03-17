# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['AutoClicker.py'],
             pathex=['C:\\desktop2\\2021\\scripts\\python\\PyCharmProjects\\SuperClickerUtility\\venv\\Lib\\site-packages', 'C:\\desktop2\\2021\\scripts\\python\\PyCharmProjects\\SuperClickerUtility'],
             binaries=[],
             datas=[('images', 'images')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['tkinter', 'test', 'sqlite3', 'numpy'],
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
