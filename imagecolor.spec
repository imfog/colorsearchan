# -*- mode: python -*-

block_cipher = None


a = Analysis(['imagecolor.py'],
             pathex=['/Users/hw17a114/Desktop'],
             binaries=[],
             datas=[],
             hiddenimports=['scipy._lib.messagestream', 'sklearn.neighbors.typedefs'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='imagecolor',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='imagecolor.app',
             icon=None,
             bundle_identifier=None)
