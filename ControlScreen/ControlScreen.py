from tkinter import *
import socket
import time

UDP_IP = "192.168.10.42"
UDP_PORT = 1500

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP


class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master
        self.image_lammitinon = PhotoImage(file="Lammitin_small.png")
        self.image_lammitinoff = PhotoImage(file="Lammitinoff_small.png")
        self.image_lightnon = PhotoImage(file="lightbulb_on_small.png")
        self.image_lighnoff = PhotoImage(file="lightbulb_off_small.png")

        filename = PhotoImage(file="House_small.png")
        background_label = Label(self, image=filename)
        background_label.image = filename
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.pack()

        self.init_window()


    def init_window(self):
        self.master.title("Control screen")
        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text = "Close program", command=self.client_exit, bg="grey")
        quitButton.place(x=5, y=5, height = 25, width = 90)

        LightsOnButton = Button(self, command=self.light_on, bg="green")
        LightsOnButton.place(x = 10, y = 40, height = 150, width = 150)
        LightsOnButton.config(image=self.image_lightnon)

        LightsOffButton = Button(self, command=self.light_off, bg = "red")
        LightsOffButton.place(x = 516, y = 40, height = 150, width = 150)
        LightsOffButton.config(image=self.image_lighnoff)

        HeatingOnButton = Button(self, command=self.heating_on, bg = "green")
        HeatingOnButton.place(x = 10, y = 220, height = 150, width = 150)
        HeatingOnButton.config(image=self.image_lammitinon)

        HeatingOffButton = Button(self, command=self.heating_off, bg = "red")
        HeatingOffButton.place(x = 516, y = 220, height = 150, width = 150)
        HeatingOffButton.config(image=self.image_lammitinoff)

    def client_exit(self):
        exit()

    def light_on(self):
        sock.sendto("light_on".encode(), (UDP_IP, UDP_PORT))
        time.sleep(0.5)

    def light_off(self):
        sock.sendto("light_off".encode(), (UDP_IP, UDP_PORT))
        time.sleep(0.5)

    def heating_on(self):
        sock.sendto("heating_on".encode(), (UDP_IP, UDP_PORT))
        time.sleep(0.5)

    def heating_off(self):
        sock.sendto("heating_off".encode(), (UDP_IP, UDP_PORT))
        time.sleep(0.5)

root = Tk()
root.geometry("676x380")


app = Window(root)
root.mainloop()