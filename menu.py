import tkinter as tk
from clock import AnalogClock
from tkinter import ttk
from threading import Thread
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
        self.task_list = []

    def add_clock(self, *args):
        idxs = self.box.curselection()
        self.text1.set("Do you want to add \n" +
                       self.choices[idxs[0]]+" clock?")

    def create_clock(self):
        idxs = self.box.curselection()
        if self.choices[idxs[0]] == "Thailand":
            self.run_loading(0)
        elif self.choices[idxs[0]] == "US":
            self.run_loading(-12)
        elif self.choices[idxs[0]] == "UK":
            self.run_loading(-7)
        elif self.choices[idxs[0]] == "Japan":
            self.run_loading(2)

    def run_loading(self, timediff):
        self.thread_loading_screen(timediff)

    def thread_loading_screen(self, timediff):

        # self.loading_task = Thread(target=self.task1)
        # self.loading_task.start()
        thread = Thread(target=self.task1(timediff))
        thread.start()

        # self.after(10, self.check_loading)

    # def check_loading(self):
    #     if self.loading_task.is_alive():
    #         print('Not Done')
    #         self.after(10, self.check_loading)
    #     else:
    #         print("Done")
    #         self.loading_frame.destroy()

    def task1(self, timediff):
        self.task_list.append(0)
        loading_frame = tk.Frame(self.root)
        print(self.task_list)
        loading_frame.grid(row=0, column=len(self.task_list))
        p = ttk.Progressbar(
            loading_frame, length=200, mode="determinate")
        p.grid(row=4, column=0)
        for i in range(101):
            time.sleep(0.1)
            p['value'] = i
            self.update()
        p.destroy()
        self.clock_list.append(AnalogClock(
            loading_frame, 0, len(self.task_list), timediff))
        print("Loading new Clock")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    root.title("menu")
    menu = menu(root)
    root.mainloop()
