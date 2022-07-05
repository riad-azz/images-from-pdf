from tkinter import Tk, filedialog, messagebox
from tkinter.ttk import Separator

from constants import *
from image_extractor import ImageExtractor
from interface.my_button import MyButton
from interface.my_label import MyLabel


class MyApp(Tk):
    def __init__(self):
        super().__init__()
        # ----- App Settings -----
        self.title('Images from PDF')
        self['bg'] = BG_COLOR
        self.resizable(False, False)
        self.geometry(f"{WIDTH}x{HEIGHT}")
        # ----- App Vars -----
        self.__extractor = ImageExtractor(self)
        self.file_path = None
        self.save_path = None
        # ----- App Widgets -----
        # -- Getting the pdf file path --
        # instruction label
        self.l_file_path = MyLabel(self, text='Select the PDF file you would like to extract from')
        self.l_file_path.position(x=4, y=20)
        # path label
        self.l_file_path_display = MyLabel(self, text="File path not selected", wrap=True, font=PATH_FONT, fg=BG_COLOR,
                                           bg=FG_COLOR)
        self.l_file_path_display.bind("<Button-1>", self.get_file_path)
        self.l_file_path_display.position(x=0, y=60, width=490, height=40)
        # select file dir button
        self.b_file_path = MyButton(self, text="Select", command=self.get_file_path)
        self.b_file_path.position(x=545, y=60, anchor='center')
        # Separate Sections
        Separator(self).place(x=0, y=90, height=4, width=WIDTH)
        # -- Getting the save path --
        # instruction label
        self.l_save_path = MyLabel(self, text='Select where you would like to save the images')
        self.l_save_path.position(x=4, y=120)
        # path label
        self.l_save_path_display = MyLabel(self, text="Save path not selected", wrap=True, font=PATH_FONT, fg=BG_COLOR,
                                           bg=FG_COLOR)
        self.l_save_path_display.bind("<Button-1>", self.get_save_path)
        self.l_save_path_display.position(x=0, y=160, width=490, height=40)
        # select save dir button
        self.b_save_path = MyButton(self, text="Select", command=self.get_save_path)
        self.b_save_path.position(x=545, y=160, anchor='center')
        # Separate Sections
        Separator(self).place(x=0, y=190, height=4, width=WIDTH)
        # -- Extract Button --
        self.b_extract = MyButton(self, text='Extract Images', command=self.extract)
        self.b_extract.position(x=CENTER_X, y=235, width=250)

    def extract(self):
        # Check if file path is selected
        if not self.file_path:
            messagebox.showwarning('Error', 'Please Select the pdf file path')
            return

        # Check if save path is selected
        if not self.save_path:
            messagebox.showwarning('Error', 'Please Select the save path')
            return

        try:
            # Disabled user inputs
            self.disabled_all()
            self.__extractor.extract(self.file_path, self.save_path)
        except Exception as e:
            self.enable_all(error=str(e))

    def get_file_path(self, event=None):
        title = 'Select PDF file'
        initial_dir = './'
        file_types = (('PDF files', '*.pdf'),)
        file = filedialog.askopenfilename(title=title, initialdir=initial_dir, filetypes=file_types)
        if file:
            self.file_path = file
            self.l_file_path_display.configure(text=file)

    def get_save_path(self, event=None):
        title = 'Select save path'
        initial_dir = './'
        file = filedialog.askdirectory(title=title, initialdir=initial_dir)
        if file:
            self.save_path = file
            self.l_save_path_display.configure(text=file)

    def update_progress(self, count, curr):
        self.b_extract.configure(text=f"Extracting {curr}/{count}")

    def enable_all(self, done=False, error=""):
        if done:
            messagebox.showinfo('Success', f'Images were successfully saved to\n\n{self.save_path}')
        else:
            messagebox.showerror('Error', f'{error}')
        self.b_file_path['state'] = 'normal'
        self.b_save_path['state'] = 'normal'
        self.l_file_path_display['state'] = 'normal'
        self.l_save_path_display['state'] = 'normal'
        self.b_extract['state'] = 'normal'
        self.b_extract.configure(text="Extract Images")

    def disabled_all(self):
        self.b_file_path['state'] = 'disabled'
        self.b_save_path['state'] = 'disabled'
        self.l_file_path_display['state'] = 'disabled'
        self.l_save_path_display['state'] = 'disabled'
        self.b_extract['state'] = 'disabled'
