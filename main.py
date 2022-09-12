from kivy.factory import Factory
from kaki.app import App
from kivymd.app import MDApp


class Live(App, MDApp):
    CLASSES = {
        "InstaDPApp": "Instadp",
        "instaDpDownloader": "Instadp",
        "devProfile": "Instadp",
    }
    KV_FILES = ["Instadp.kv"]
    AUTORELOADER_PATHS = [(".", {"recursive": True})]

    def build_app(self, first=False):
        self.title = "Insta Profile Downloader"
        self.icon = ".\\assets\\images\\insta.png"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        # self.theme_cls.accent_palette = "Red"
        return Factory.instaDpDownloader()

    def theme_change(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"


if __name__ == "__main__":
    Live().run()
