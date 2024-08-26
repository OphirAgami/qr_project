import tkinter as tk


class QrImage(tk.Canvas):
    def __init__(self,parent):
        super().__init__(master=parent,background="#FFFFFF",bd=0,highlightthickness=0,relief="ridge")
        self.place(relx=0.5,rely=0.4,width=400,height=400,anchor="center")

    def update_image(self, image_tk):
        self.clear()
        self.create_image(0,0, image=image_tk,anchor="nw")

    def clear(self):
        self.delete("all")
