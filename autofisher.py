import tkinter as tk
import tkinter.font as font
from turtle import width

class Functions():
    def start_thread():
        print("start")
    
    def stop_thread():
        print("stop")

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.configure(bg="#131417")
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        self.font = font.Font(family="calibri", size=20)

        # log box
        self.logFrame = tk.Frame(self, bg="#131417")
        self.logFrame.grid(row=0, column=0, rowspan=2)
        self.logBox = tk.Text(self.logFrame, state="disabled")
        self.logBox.pack(fill="both", expand=True)

        # gif box
        self.gifBox = tk.Button(self, text="Iniciar", command=lambda: Functions.start_thread(), relief="flat")
        self.gifBox.grid(row=0, column=1, columnspan=2)

        # setting button
        self.settingIcon = tk.PhotoImage(file="C:\\dev\\autofisher\\settings.png").subsample(14,14)
        self.settingButton = tk.Button(self, image=self.settingIcon, command=lambda: Functions.start_thread(), relief="flat")
        self.settingButton.grid(row=0, column=3)

        # stop button
        self.startButtonBorder = tk.Frame(self, highlightbackground="#8bed4f", highlightcolor="#8bed4f", highlightthickness=4, bd=0)
        self.startButtonBorder.grid(row=1, column=1)
        self.startButton = tk.Button(self.startButtonBorder, text="Iniciar", command=lambda: Functions.start_thread(), 
                                     relief="solid", bg="#131417", fg="#8bed4f", font=self.font)
        self.startButton.grid(row=1, column=1)

        # start button
        self.stopButtonBorder = tk.Frame(self, highlightbackground="#ff2626", highlightcolor="#ff2626", highlightthickness=4, bd=0)
        self.stopButtonBorder.grid(row=1, column=2)
        self.stopButton = tk.Button(self.stopButtonBorder, text="Parar", command=lambda: Functions.stop_thread(), 
                                    relief="solid", bg="#131417", fg="#ff2626", font=self.font)
        self.stopButton.grid(row=1, column=2)

if __name__ == "__main__":
    app = Application()
    app.master.title("AutoFisher")
    app.master.geometry("720x360")
    app.master.configure(bg="#131417")

    app.mainloop()