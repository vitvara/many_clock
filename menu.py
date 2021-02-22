import tkinter as tk
from clock import AnalogClock
from tkinter import ttk
import time


class menu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.choices = ["Thailand", "US", "Japan", "UK"]
        self.contry = tk.StringVar(value=self.choices)
        self.grid(row=0, column=0, sticky="NSWE")
        self.box = tk.Listbox(self, height=4, listvariable=self.contry)
        self.box.grid(row=0, column=0, padx=5, pady=5)
        self.box.bind("<<ListboxSelect>>", self.add_clock)
        self.text1 = tk.StringVar()
        self.label1 = tk.Label(self, textvariable=self.text1)
        self.label1.grid(row=0, column=1)
        self.button = tk.Button(self, text="Add", width=8,
                                command=self.create_clock)
        self.button.grid(row=1, column=1)
        self.root = tk.Tk()
        self.root.geometry("300x300")
        self.clock_list = []

    def add_clock(self, *args):
        idxs = self.box.curselection()
        self.text1.set("Do you want to add \n" +
                       self.choices[idxs[0]]+" clock?")

    def create_clock(self, timedif=0):
        idxs = self.box.curselection()
        if self.choices[idxs[0]] == "Thailand":
            self.loadingscreen()
            self.clock_list.append(AnalogClock(
                self.root, 0, len(self.clock_list), 0))
        elif self.choices[idxs[0]] == "US":
            self.loadingscreen()
            self.clock_list.append(AnalogClock(
                self.root, 0, len(self.clock_list), -12))
        elif self.choices[idxs[0]] == "UK":
            self.loadingscreen()
            self.clock_list.append(AnalogClock(
                self.root, 0, len(self.clock_list), -7))
        elif self.choices[idxs[0]] == "Japan":
            self.loadingscreen()
            self.clock_list.append(AnalogClock(
                self.root, 0, len(self.clock_list), 2))

    def loadingscreen(self):
        self.percent = tk.IntVar()
        self.loading_frame = tk.Frame(self.root)
        self.loading_frame.grid(row=0, column=0, sticky="NEWS")
        self.p = ttk.Progressbar(
            self.loading_frame, length=200, mode='determinate', variable=self.percent)
        self.p.grid(row=1, column=0)
        self.root.update()
        for i in range(51):
            time.sleep(0.1)
            self.percent.set(i)
            self.root.update()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    root.title("menu")
    menu = menu(root)
    root.mainloop()
