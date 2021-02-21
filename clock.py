import tkinter as tk
import tkinter.ttk as ttk
from time import strftime


class Application:
    def __init__(self, parent):
        super().__init__()
        self.geometry("400x100")
        self.time = tk.StringVar()
        self.date = tk.StringVar()
        self.time.set("Current Time")
        self.date.set("Current Date")
        self.button = tk.Button(self, text="Quit", width=8, command=quit)
        self.time_label = tk.Label(self, textvariable=self.time)
        self.date_label = tk.Label(self, textvariable=self.date)
        self.date_label.pack()
        self.time_label.pack()
        self.button.pack()
        self.update_time()

    def update_time(self):
        self.time.set(strftime("%H:%M:%S"))
        self.date.set(strftime("%d %B %Y"))
        self.after(1000, self.update_time)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
