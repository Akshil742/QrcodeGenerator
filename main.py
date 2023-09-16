import customtkinter as ctk
import qrcode
from PIL import ImageTk
from tkinter import filedialog
from tkinter import messagebox

ctk.set_default_color_theme("dark-blue")

class upperframe(ctk.CTkFrame):
    path = ""
    def __init__(self, master):
        super().__init__(master, corner_radius=5, fg_color="lightgray")
        self.master = master
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        self.upperframe = ctk.CTkFrame(self, fg_color="transparent")
        self.upperframe.grid(row=0, column=0, sticky="nesw", padx=10, pady=5)
        
        self.frame1 = ctk.CTkFrame(self.upperframe, fg_color="transparent")
        self.frame1.pack(side="left", fill="both", expand=True)
        self.filetype_box_label = ctk.CTkLabel(self.frame1, text="File Extension", anchor="sw", padx=13, font=("Georgia", 14)).pack(side="top", fill="both", expand=True)
        self.filetype_box = ctk.CTkComboBox(self.frame1, values=[".png",".jpg",".webp"], state="readonly", command=self.showdata)
        self.filetype_box.pack(side="top", fill="both", expand=True, padx=10, pady=5)
        self.filetype_box.set(".png")  # Sets initial value

        self.frame2 = ctk.CTkFrame(self.upperframe, fg_color="transparent")
        self.frame2.pack(side="left", fill="both", expand=True)
        self.filetype_box_label = ctk.CTkLabel(self.frame2, text="Error Correction", anchor="sw", padx=13, font=("Georgia", 14)).pack(side="top", fill="both", expand=True)
        self.error_corection_box = ctk.CTkComboBox(self.frame2, values=["L (7%)","M (15%)","Q (25%)","H (30%)"], state="readonly", command=self.showdata)
        self.error_corection_box.pack(side="top", fill="both", expand=True, padx=10, pady=5)
        self.error_corection_box.set("M (15%)")  # Sets initial value

        self.frame3 = ctk.CTkFrame(self.upperframe, fg_color="transparent")
        self.frame3.pack(side="left", fill="both", expand=True)
        self.filetype_box_label = ctk.CTkLabel(self.frame3, text="Color", anchor="sw", padx=13, font=("Georgia", 14)).pack(side="top", fill="both", expand=True)
        self.fill_color_box = ctk.CTkComboBox(self.frame3, values=["black","white","red","green", "blue", "yellow", "orange", "pink", "purple"], state="readonly", command=self.showdata)
        self.fill_color_box.pack(side="top", fill="both", expand=True, padx=10, pady=5)
        self.fill_color_box.set("black")  # Sets initial value

        self.frame4 = ctk.CTkFrame(self.upperframe, fg_color="transparent")
        self.frame4.pack(side="left", fill="both", expand=True)
        self.filetype_box_label = ctk.CTkLabel(self.frame4, text="Background Color", anchor="sw", padx=13, font=("Georgia", 14)).pack(side="top", fill="both", expand=True)
        self.background_color_box = ctk.CTkComboBox(self.frame4, values=["transparent","black","white","red","green", "blue", "yellow", "orange", "pink", "purple"], state="readonly", command=self.showdata)
        self.background_color_box.pack(side="top", fill="both", expand=True, padx=10, pady=5)
        self.background_color_box.set("white")  # Sets initial value
        
        self.downframe = ctk.CTkFrame(self, fg_color="transparent")
        self.downframe.grid(row=1, column=0, sticky="nesw", padx=10)
        
        self.filetype_box_lbl1 = ctk.CTkLabel(self.downframe, text="Version 1", anchor="sw", font=("Georgia", 14))
        self.filetype_box_lbl1.pack(side="top", fill="x", expand=True, padx=20)
        self.version_slider = ctk.CTkSlider(self.downframe, from_=1, to=40, number_of_steps=40, command=self.showdata)
        self.version_slider.pack(side="top", fill="x", expand=True, padx=20)
        self.version_slider.set(1) # Sets initial value
        
        self.filetype_box_lbl2 = ctk.CTkLabel(self.downframe, text="Border size 10", anchor="sw", font=("Georgia", 14))
        self.filetype_box_lbl2.pack(side="top", fill="x", expand=True, padx=20)
        self.border_slider = ctk.CTkSlider(self.downframe, from_=1, to=50, number_of_steps=50, command=self.showdata)
        self.border_slider.pack(side="top", fill="x", expand=True, padx=20)
        self.border_slider.set(10) # Sets initial value
        
        self.filetype_box_lbl3 = ctk.CTkLabel(self.downframe, text="Box size 4", anchor="sw", font=("Georgia", 14))
        self.filetype_box_lbl3.pack(side="top", fill="x", expand=True, padx=20)
        self.boxsize_slider = ctk.CTkSlider(self.downframe, from_=1, to=50, number_of_steps=50, command=self.showdata)
        self.boxsize_slider.pack(side="top", fill="x", expand=True, padx=20)
        self.boxsize_slider.set(4) # Sets initial value
        
        self.fileframe = ctk.CTkFrame(self, fg_color="transparent")
        self.fileframe.grid(row=2, column=0, sticky="nesw", padx=10, pady=5)
        self.pathlbl = ctk.CTkLabel(self.fileframe, anchor="w", text="path", font=("Georgia", 14))
        self.pathlbl.pack(side="left", fill="x", expand=True, padx=10)
        self.openfilebtn = ctk.CTkButton(self.fileframe, text="Open Folder", command=self.open_file, font=("Algerian", 16))
        self.openfilebtn.pack(side="left", fill="y", padx=10)
        
    def open_file(self):
        file_path = filedialog.askdirectory()
        self.pathlbl.configure(text=file_path)
        self.path = file_path
        
    def showdata(self, value):
        self.filetype_box_lbl1.configure(text=f"Version {int(self.version_slider.get())}")
        self.filetype_box_lbl2.configure(text=f"Border size {int(self.border_slider.get())}")
        self.filetype_box_lbl3.configure(text=f"Boxsize size {int(self.boxsize_slider.get())}")
        self.master.show_qrcode()
        
class downframe(ctk.CTkFrame):
    qr_img = None
    def __init__(self, master):
        super().__init__(master, corner_radius=0)
        self.master = master
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        
        self.generate_frame = ctk.CTkFrame(self)
        self.generate_frame.grid(row=0, column=0, sticky="nesw", padx=10, pady=10)
        
        self.filename = ctk.CTkEntry(self.generate_frame, font=("Georgia", 16))
        self.filename.pack(side="top", fill="x", expand=True, padx=10, pady=5)
        
        self.textbox = ctk.CTkTextbox(self.generate_frame, font=("Georgia", 18))
        self.textbox.pack(side="top", fill="both", expand=True, padx=8, pady=(5,5))
        self.textbox.insert("0.0", "welcome")
        self.textbox.bind("<KeyRelease>", self.update_on_keyevent)
        
        self.generate_btn = ctk.CTkButton(self.generate_frame, text="GENERATE QR CODE", command=self.save_qrcode, font=("Algerian", 20))
        self.generate_btn.pack(side="top", fill="x", expand=True, padx=8, pady=(0,10))
        
        self.qrcode_frame = ctk.CTkFrame(self, corner_radius=5)
        self.qrcode_frame.grid(row=0, column=1, sticky="nesw", padx=10, pady=10)
        
        self.qrlbl = ctk.CTkLabel(self.qrcode_frame, text="")
        self.qrlbl.pack(side="top", fill="both", expand=True)
        
    def update_on_keyevent(self, event):
        self.master.show_qrcode()
        
    def update(self, ver, err, box, border, fg, bg):
        qr = qrcode.QRCode(version=ver, error_correction=err, box_size=box, border=border)
        qr.add_data(self.textbox.get("0.0", "end"))
        qr.make(fit=True)
        self.img = qr.make_image(fill_color=fg, back_color=bg).convert("RGB")
        self.qr_img = ImageTk.PhotoImage(self.img)
        self.qrlbl.configure(image=self.qr_img)
        self.qrlbl.image = self.qr_img
        
    def save_qrcode(self):
        if self.master.upperframe.path == "":
            messagebox.showwarning("Warning", "Select path.")
        elif self.filename.get() == "":
            messagebox.showwarning("Warning", "Give file name.")
        elif self.master.upperframe.filetype_box.get() == "":
            messagebox.showwarning("Warning", "Select extention.")
        else:
            try:
                self.img.save(f"{self.master.upperframe.path}/{self.filename.get()}{self.master.upperframe.filetype_box.get()}")
                messagebox.showinfo("Success", "Image added successfully!")
            except Exception as e:
                messagebox.showerror("Error", str(e))

class qrgenerator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("QR-code Generator")
        self.geometry("800x550")
        self.minsize(800, 550)
        self.iconbitmap("icon.ico")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1,2), weight=2)
        
        self.upperframe = upperframe(self)
        self.upperframe.grid(row=0, column=0, sticky="nesw")
        
        self.downframe = downframe(self)
        self.downframe.grid(row=1, column=0, rowspan=2, sticky="nesw")
        
        self.show_qrcode()
        
    def show_qrcode(self):
        ver = int(self.upperframe.version_slider.get())
        if self.upperframe.error_corection_box.get()=="L (7%)":
            err = qrcode.constants.ERROR_CORRECT_L
        elif self.upperframe.error_corection_box.get()=="M (15%)":
            err = qrcode.constants.ERROR_CORRECT_M
        elif self.upperframe.error_corection_box.get()=="Q (25%)":
            err = qrcode.constants.ERROR_CORRECT_Q
        elif self.upperframe.error_corection_box.get()=="H (30%)":
            err = qrcode.constants.ERROR_CORRECT_H
        else: err = qrcode.constants.ERROR_CORRECT_M
        box = int(self.upperframe.border_slider.get())
        border = int(self.upperframe.boxsize_slider.get())
        fg = self.upperframe.fill_color_box.get()
        bg = self.upperframe.background_color_box.get()
        self.downframe.update(ver, err, box, border, fg, bg)

app = qrgenerator()
app.mainloop()
