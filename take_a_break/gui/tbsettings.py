import tkinter as tk

from take_a_break.configuration import CONFIG


class TBSettings(object):
    def __init__(self, parent):
        self._parent = parent
        self._dialog = tk.Tk()
        self._dialog.title("Settings (<ESC> will close it)")
        self._dialog.bind('<Escape>', self.close)
        # self._dialog.minsize(400, 100)
        self._dialog.focus_force()

        canvas1 = tk.Canvas(self._dialog, width=400, height=150)
        canvas1.pack()

        label1 = tk.Label(self._dialog, text="Unsplash Random URL:")
        canvas1.create_window(72, 30, window=label1)

        self.unsplash_provider = tk.Entry(self._dialog, cnf={"width": 63})
        self.unsplash_provider.insert(0, CONFIG.data["unsplash.com"]["url"])
        canvas1.create_window(202, 50, window=self.unsplash_provider)

        label2 = tk.Label(self._dialog, text="Remind me to take a break in (minutes):")
        canvas1.create_window(115, 80, window=label2)

        self.reminder = tk.Entry(self._dialog, cnf={"width": 20})
        self.reminder.insert(0, CONFIG.data["default"]["remind_me_after_these_minutes"])
        canvas1.create_window(73, 100, window=self.reminder)

        button1 = tk.Button(master=self._dialog, text='Save', command=self._save_settings)
        canvas1.create_window(28, 130, window=button1)

    def _save_settings(self):
        CONFIG.data["default"]["remind_me_after_these_minutes"] = self.reminder.get()
        CONFIG.data["unsplash.com"]["url"] = self.unsplash_provider.get()
        CONFIG.save()
        self.close()

    def show(self):
        self._parent.wm_attributes("-disabled", True)
        self._parent.toplevel_dialog = self._dialog
        self._parent.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.close)
        self._dialog.mainloop()

    def close(self, event=None):
        self._parent.wm_attributes("-disabled", False)  # IMPORTANT!
        self._parent.toplevel_dialog.destroy()
