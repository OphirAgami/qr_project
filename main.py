from tkinter import filedialog
import customtkinter as ctk
from PIL import  ImageTk
import qrcode
from entry_field import EntryField
from qrImage import QrImage


class App(ctk.CTk):
    def __init__(self):
        #Set_up window
        super().__init__(fg_color="#FFFFFF")
        ctk.set_appearance_mode("light")
        #Custom the window
        self.minsize(width=400,height=400)
        self.title("")
        self.iconbitmap("images/empty.ico")

        #Entry field
        self.entry_string = ctk.StringVar()
        self.entry_string.trace("w", self.create_qr)
        EntryField(self, self.entry_string,self.save)

        self.bind("<Return>",lambda event: self.save(event))

        #QrImage
        self.tk_image = None
        self.raw_image = None
        self.qr_image = QrImage(self)

        self.mainloop()

    def create_qr(self, *args):
        current_text = self.entry_string.get()
        if current_text:
            self.raw_image = qrcode.make(current_text).resize((400,400))
            self.tk_image = ImageTk.PhotoImage(self.raw_image)
            self.qr_image.update_image(self.tk_image)
        else:
            self.qr_image.clear()
            self.raw_image=None
            self.tk_image=None
    def save(self, event):
        if self.raw_image:
            file_path = filedialog.asksaveasfilename()
            if file_path:
                self.raw_image.save(file_path+".png")

App()
