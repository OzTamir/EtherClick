import rumps
import webbrowser
import xerox

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

if __name__ == "__main__":
    EtherClick("EtherClick").run()