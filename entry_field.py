import customtkinter as ctk

class EntryField(ctk.CTkFrame):
    def __init__(self, parent, entry_string,save_func):
        super().__init__(master=parent,corner_radius=20,fg_color="#17153B")
        self.place(relx=0.5,rely=1,relwidth=1,relheight=0.4,anchor="center")

        #
        self.rowconfigure((0,1),weight = 1, uniform="a")
        self.columnconfigure(0,weight = 1, uniform="a")

        self.frame = ctk.CTkFrame(self, fg_color="transparent")
        self.frame.columnconfigure(0, weight = 1,uniform="b")
        self.frame.columnconfigure(1, weight = 4,uniform="b")
        self.frame.columnconfigure(2, weight = 2,uniform="b")
        self.frame.columnconfigure(3, weight = 1,uniform="b")
        self.frame.grid(row=0,column=0)

        entry = ctk.CTkEntry(self.frame,
                             textvariable=entry_string,
                             border_color="#433D8B",
                             fg_color="#2E236C",
                             text_color="white")
        entry.grid(row=0,column=1, sticky="nsew")

        button = ctk.CTkButton(self.frame, text="Save",fg_color="#2E236C",hover_color="#5a52bf",command=lambda :save_func(""))
        button.grid(row=0,column=2, sticky="nsew",padx=10)