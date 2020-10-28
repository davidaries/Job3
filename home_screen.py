from tkinter import *
import data
import language_dictionary as ld


class home_screen:

    def __init__(self, master, log_window):
        self.main_program = master
        self.horizontal_spacing = 0
        self.log_window_pointer = log_window
        self.column_padding= 75
        self.row_padding =10
        self.reception_home = self.create_home_screen()
        self.assistant_home = self.create_home_screen()
        self.provider_home = self.create_home_screen()
        self.lab_tech_home = self.create_home_screen()

    def create_home_screen(self):
        home = Toplevel(self.main_program)
        home.geometry("250x300+" + self.horizontal_spacing.__str__() + "+200")
        self.horizontal_spacing += 260
        return home

    def populate_reception_home(self, staff_id):
        receptionist = data.get_staff_member(staff_id)
        language = receptionist[2]
        self.reception_home.title(ld.get_text_from_dict(language, staff_id))
        staff_name = Label(self.reception_home, text=receptionist[0], font=data.get_large_font())
        staff_name.grid(column=0, row=0)
        self.add_column_headers(language, self.reception_home)
        """btn_exit = Button(self.reception_home, text=ld.get_text_from_dict(language, '~20'), fg="black", bg="gray",
                          height=1, width=10)
        btn_exit.pack(side=BOTTOM)"""

    def populate_assistant_home(self, staff_id):
        assistant = data.get_staff_member(staff_id)
        language = assistant[2]
        self.assistant_home.title(ld.get_text_from_dict(language, staff_id))
        staff_name = Label(self.assistant_home, text=assistant[0], font=data.get_large_font())
        staff_name.grid(column=0, row=0)
        self.add_column_headers(language,self.assistant_home)
        """btn_exit = Button(self.assistant_home, text=ld.get_text_from_dict(language, '~20'), fg="black", bg="gray",
                          height=1, width=10)
        btn_exit.pack(side=BOTTOM)"""

    def populate_provider_home(self, staff_id):
        provider = data.get_staff_member(staff_id)
        language = provider[2]
        self.provider_home.title(ld.get_text_from_dict(language, staff_id))
        staff_name = Label(self.provider_home, text=provider[0], font=data.get_large_font())
        staff_name.grid(column=0, row=0)
        self.add_column_headers(language, self.provider_home)
        """btn_exit = Button(self.provider_home, text=ld.get_text_from_dict(language, '~20'), fg="black", bg="gray",
                          height=1, width=10)
        btn_exit.pack(side=BOTTOM)"""

    def populate_lab_tech_home(self, staff_id):
        lab_tech = data.get_staff_member(staff_id)
        language = lab_tech[2]
        self.lab_tech_home.title(ld.get_text_from_dict(language, staff_id))
        staff_name = Label(self.lab_tech_home, text=lab_tech[0], font=data.get_large_font())
        staff_name.grid(column=0, row=0)
        self.add_column_headers(language, self.lab_tech_home)
        """btn_exit = Button(self.lab_tech_home, text=ld.get_text_from_dict(language, '~20'), fg="black", bg="gray",
                          height=1, width=10)
        btn_exit.pack(side=BOTTOM)"""

    def manage_staff_main_screen(self):
        self.populate_reception_home('~24')
        self.populate_assistant_home('~25')
        self.populate_provider_home('~26')
        self.populate_lab_tech_home('~27')

    def add_column_headers(self, lang, window):
        label_name = Label(window, text=ld.get_text_from_dict(lang, '~1'), font=data.medium_font)
        label_name.grid(column=1, row=2, ipady=self.row_padding)
        label_event = Label(window, text=ld.get_text_from_dict(lang, '~33'), font=data.get_medium_font())
        label_event.grid(column=2, row=2, ipadx=self.column_padding, ipady=self.row_padding)