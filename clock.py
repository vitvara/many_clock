import tkinter as tk
from datetime import datetime
import math


class AnalogClock(tk.Frame):

    def __init__(self, parent, r, c, timediff):
        super().__init__(parent)
        self.timedif = timediff
        parent.rowconfigure(r, weight=1)
        parent.columnconfigure(c, weight=1)
        self.grid(row=r, column=c, sticky="NEWS")
        self.config(bg="brown")
        self.canvas = tk.Canvas(self, borderwidth=0,
                                highlightthickness=0, bg="yellow")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.canvas.grid(row=0, column=0, padx=10, pady=10, sticky="NEWS")
        self.prepare_items()
        self.canvas.bind("<Configure>", lambda x: self.update_clock())
        self.update_time()

    def prepare_items(self):
        self.clock_face = self.canvas.create_oval(
            0, 0, 0, 0, width=3, outline="blue")
        self.center_pin = self.canvas.create_oval(0, 0, 0, 0, fill="green")
        self.second_hand = self.canvas.create_line(
            0, 0, 0, 0, fill="gray", width=1)
        self.minute_hand = self.canvas.create_line(
            0, 0, 0, 0, fill="black", width=4)
        self.hour_hand = self.canvas.create_line(
            0, 0, 0, 0, fill="black", width=8)

    def center_coords(self):
        '''
        Return a tuple (x,y) representing the current center coordinates of the canvas
        '''
        return self.canvas.winfo_width()/2, self.canvas.winfo_height()/2

    def clock_radius(self):
        '''
        Return the desired clock's radius, which is set to be 90% of the canvas's shorter side
        '''
        cx, cy = self.center_coords()
        return min(cx, cy)*0.9

    def update_clock(self):
        cx, cy = self.center_coords()
        radius = self.clock_radius()

        # update the item self.clock_face so that it has the radius of self.clock_radius()
        # and is centered at coordinates (cx,cy)
        self.canvas.coords(self.clock_face, cx-radius,
                           cy-radius, cx+radius, cy+radius)

        # update the item self.center_pin so that it has the radius of 5 pixels and
        # is centered at coordinates (cx,cy)
        self.canvas.coords(self.center_pin, cx-5, cy-5, cx+5, cy+5)
        now = datetime.now()
        hour = now.hour + self.timedif
        if hour < 0:
            hour = hour * (-1)
        if hour > 24:
            hour = hour - 24
        sec_angle = now.second/60*360
        min_angle = now.minute/60*360 + now.second/10
        hour_angle = hour/12*360 + now.minute/6
        x, y = self.polar_to_canvas(radius*0.9, sec_angle)
        self.canvas.coords(self.second_hand, cx, cy, x, y)
        x, y = self.polar_to_canvas(radius*0.85, min_angle)
        self.canvas.coords(self.minute_hand, cx, cy, x, y)
        x, y = self.polar_to_canvas(radius*0.5, hour_angle)
        self.canvas.coords(self.hour_hand, cx, cy, x, y)

    def update_time(self):
        self.update_clock()
        self.after(1000, self.update_time)

    def polar_to_canvas(self, radius, theta):
        '''
        Take polar coordinates (radius,theta) and return a tuple (x,y)
        representing the Cartesian coordinates on the canvas, with respect to
        the canvas's center.
        '''
        cx, cy = self.center_coords()
        x = cx+radius*math.sin(math.radians(theta))
        y = cy-radius*math.cos(math.radians(theta))
        return x, y


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    root.title("Analog Clock")
    clock = AnalogClock(root, 0, 0)
    clock = AnalogClock(root, 0, 1)
    root.mainloop()
