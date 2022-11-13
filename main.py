import rumps
import webbrowser
import xerox
import sha3

CHROME_PATH = 'open -a /Applications/Google\ Chrome.app %s'

class EtherClick(rumps.App):
    @rumps.clicked("Etherscan")
    def prefs(self, _):
        address = xerox.paste()
        if not address.startswith('0x'):
            rumps.notification(title='EtherClick', subtitle='Clipboard does not contain a valid ethereum address', message='')
            return
        url = 'https://etherscan.io/address/' + xerox.paste()
        webbrowser.get(CHROME_PATH).open_new_tab(url)
    
    @rumps.clicked("keccak256")
    def prefs(self, _):
        src = xerox.paste()
        k = sha3.keccak_256()
        k.update(src.encode('utf-8'))
        result = k.hexdigest()
        xerox.copy(result)
        rumps.notification(title='EtherClick', subtitle=f'keccak256({src}) was copied to clipboard', message=f'Hash: {result}')

if __name__ == "__main__":
    EtherClick("Ξ").run()