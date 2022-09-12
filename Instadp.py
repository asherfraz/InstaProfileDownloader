import kivy

kivy.require("2.1.0")  # replace with your current kivy version !

from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.snackbar import Snackbar
from kivy.lang import Builder
from kivy.core.window import Window
import webbrowser

Window.size = (865, 638)


class instaDpDownloader(Screen):
    def __init__(self, **kw):
        super(instaDpDownloader, self).__init__(**kw)

    def sociallinks(self, num):
        if num == "1":
            webbrowser.open("https://github.com/asherfraz")
        elif num == "2":
            webbrowser.open("https://instagram.com/ash3rfraz")
        elif num == "3":
            webbrowser.open_new_tab(
                "https://github.com/asherfraz/InstaProfileDownloader"
            )
        else:
            pass

    def Profile_downloader(self, usrname):
        import instaloader

        loader = instaloader.Instaloader()
        # profile = instaloader.Profile.from_username(loader.context, usrname)
        usrname = usrname.lower()
        if usrname != "":
            try:
                loader.download_profile(usrname, profile_pic_only=True)
                Snackbar(
                    text="[b]Profile Downloaded Successfully![/b]",
                    bg_color=(0, 1, 0, 0.5),
                ).open()
                raise instaloader.exceptions.ProfileNotExistsException
            except instaloader.exceptions.ProfileNotExistsException as e:
                Snackbar(
                    text=f"[b] Profile {usrname} does not exist![/b]",
                    bg_color=(255, 240, 0, 1),
                ).open()

        else:
            Snackbar(text="[b]Please Enter Username[/b]", bg_color=(1, 0, 0, 1)).open()


sm = ScreenManager()
sm.add_widget(instaDpDownloader(name="InstaDPdownloader"))


class InstaDPApp(MDApp):
    def build(self):
        self.title = "Insta Profile Downloader"
        self.icon = ".\\assets\\images\\insta.png"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file("Instadp.kv")


if __name__ == "__main__":
    InstaDPApp().run()
