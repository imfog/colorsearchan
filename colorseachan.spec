# -*- mode: python -*-

block_cipher = None


a = Analysis(['colorseachan.py'],
             pathex=['/Users/hw17a114/Desktop'],
             binaries=[('/Library/Frameworks/Python.framework/Versions/3.6/lib/libtk8.6.dylib', 'tk'),('/Library/Frameworks/Python.framework/Versions/3.6/lib/libtcl8.6.dylib', 'tcl')],
             datas=[],
             hiddenimports=[],
             hookspath=['.'],
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
          name='colorseachan',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='colorseachan.app',
             icon=None,
             bundle_identifier=None)
