from tkinter import *
import data
from manage_window import manage_window


class home_screen:
    """The home_screen class is in charge of creating and managing the home screens for the various staffers
    based on the different kinds of staff windows, the handling of the person populated on their task list
    will be done based on their job type
    :param self.main_program: reference to the main tk program used for the creation of additional windows
    :type self.main_program: tk class
    :param self.horizontal_spacing: value used to space the windows horizontally across the screen
    :type self.horizontal_spacing: int
    :param self.log_window_pointer: pointer to reference the log window which is needed to write data to the log window
    :type self.log_window_pointer: tk class
    :param self.column_padding: value used to space out values placed into a window
    :type self.column_padding: int
    :param self.row_padding: value used to pad rows to make the spacing between them larger
    :type self.row_padding: int
    :param self.row_current: value used to place values in the home screen in the appropriate rows
    :type self.row_current: int
    :param self.task_row: value used to increment the current row placement
    :type self.task_row: int
    :param self.reception_home: the window that holds a reference to the receptionist's window
    :type self.reception_home: tk Window
    :param self.assistant_home: the window that holds a reference to the assistant's window
    :type self.assistant_home: tk Window
    :param self.provider_home: the window that holds a reference to the provider's window
    :type self.provider_home: tk Window
    :param self.lab_tech_home: the window that holds a reference to the lab tech's window
    :type self.reception_home: tk Window"""

    def __init__(self, master, log_window):
        self.root = master
        self.horizontal_spacing = 0
        self.log_window_pointer = log_window
        self.column_padding = 80
        self.row_padding = 12
        self.row_current = 2
        self.task_row = 0
        self.staff_windows = []

    def create_home_screen(self, v):
        """In charge of the creation of a new window to be displayed on the screen
        :param v: is a value used for the vertical spacing of the staffers windows in the UI
        :type v: str
        :return: a reference to a window so it can be edited in the future
        :rtype: Window"""
        home = Toplevel(self.root)
        home.geometry("260x300+" + self.horizontal_spacing.__str__() + v)
        self.horizontal_spacing += 270
        return home

    def manage_staff_main_screen(self):
        """This method populates the various staff screens, in reference to NOTE 1 above I believe this can be
        simplified so there are not multiple methods to create the various home screen"""
        staff_window_ids = data.get_data('staff_device')
        staffers = data.get_data('staffers')
        for staff in staffers:
            for window in staff_window_ids:
                if not window.get(staff[0]) is None:
                    device_id = window.get(staff[0])
            self.staff_windows.append(manage_window(self.create_home_screen('+150'), staff, self.log_window_pointer,
                                                    device_id, self.root))

        for win in self.staff_windows: # makes a call to set the home windows for all of the staffers
            win.set_home()


