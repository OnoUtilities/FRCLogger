# -*- mode: python -*-

block_cipher = None


a = Analysis(['zlogger.py'],
             pathex=['C:\\Users\\<name>\\PycharmProjects\\DriverLogger'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.datas += [('z.ico', 'z.ico', 'DATA')]
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
		  a.datas,
          name='ZLogger',
          debug=False,
          strip=False,
          upx=True,
		  icon='file.ico')