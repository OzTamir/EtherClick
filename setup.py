from setuptools import setup
APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'ether.icns',
    'plist': {
        'CFBundleShortVersionString': '1.0.0',
        'LSUIElement': True,
    },
    'packages': ['rumps', 'xerox'],
}
setup(
    app=APP,
    name='EtherClick',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['rumps', 'xerox']
)