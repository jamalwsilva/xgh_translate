import sublime, sublime_plugin
import unicodedata


class XghTranslateCommand(sublime_plugin.TextCommand):
    """
    Translate latin1 words to ascii
    """

    def run(self, edit):
        view = self.view
        last = None

        for index, region in enumerate(view.sel()):
            text = view.substr(region)

            normalized = unicodedata.normalize('NFKD', text)
            text = normalized.encode('ASCII', 'ignore')

            view.replace(edit, region, text.decode("utf-8"))
