# -*- mode: python -*-

block_cipher = None


a = Analysis(['colorsearchan.py'],
             pathex=['/Users/hw17a114/colorsearchan'],
             binaries=[('/System/Library/Frameworks/Tk.framework/Tk', 'tk'),('/System/Library/Frameworks/Tcl.framework/Tcl', 'tcl')],
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
          name='colorsearchan',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='colorsearchan.app',
             icon=None,
             bundle_identifier=None
             info_plist={
                'NSHighResolutionCapable': 'True'
                },
             )
