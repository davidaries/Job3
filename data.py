
from tkinter import font as tk_font
medium_font = None
larger_font = None


session_owner = ('boss', '~101')
#staffers = [['Joe', 2, True, '~101'], ['Jose', 2, False, '~102'], ['Maria', 12, True, '~101'],
#            ['Mary', 17, False, '~102']]
persons = [['Adam', '~5'], ['Beth', '~5'], ['Cory', '~5'], ['Debi', '~5']]
# NEW DATA
# staffers to replace staffers above -- 2nd item in the list is their role.
staffers = [['Joe', '~24', '~101'], ['Jose', '~25', '~102'], ['Maria', '~26', '~101'],  ['Mary', '~27', '~102']]
# pdata to replace per persons above
pdata = [(101, 1, 11, None, 1, None, None, None, 101, '~1', 4, 'Tina', None, None, None, None, None, 1603824276.5, None,
          None, None, None, None, None),
         (102, 1, 11, None, 1, None, None, None, 101, '~14', 0, '~22', None, None, None, None, None, 1603824276.5,
          None, None, None, None, None, None),
         (103, 1, 11, None, 1, None, None, None, 101, '~15', 1, 40, None, None, None, None, None, 1603824276.5, None,
          None, None, None, None, None),
         (104, 1, 11, None, 1, None, None, None, 101, '~16', 4, '202-5431', None, None, None, None, None, 1603824276.5,
          None, None, None, None, None, None),
         (105, 1, 12, None, 2, None, None, None, 102, '~1', 4, 'Tony', None, None, None, None, None, 1603824276.5, None,
          None, None, None, None, None),
         (106, 1, 12, None, 2, None, None, None, 102, '~14', 0, '~21', None, None, None, None, None, 1603824276.5, None,
          None, None, None, None, None),
         (107, 1, 12, None, 2, None, None, None, 102, '~15', 1, 35, None, None, None, None, None, 1603824276.5, None,
          None, None, None, None, None),
         (108, 1, 12, None, 2, None, None, None, 102, '~16', 4, '703-3341', None, None, None, None, None, 1603824276.5,
          None, None, None, None, None, None)]
# to populate dropboxes or checkboxes
list_17 = ['~28', '~29']
list_2 = ['~5', '~30']
list_18 = ['~31', '~32']

"""data.py is in charge of managing and returning the data used in this program
    :param medium_font: creates a medium sized font used in the GUI
    :type medium_font: Font
    :param larger_font: creates a larger sized font used in the GUI
    :type larger_font: Font
    :param root: a reference to the main program window needed to create fonts
    :type root: tkinter class reference
    :param session_owner: is a tuple that contains the name and the language preference of the person in charge
        of the current session of the program (~101 for english) (~102 for spanish)
    :type session_owner: tuple (str, str)
    :param staffers: staffers is a nested list of staff members where each staff member (in staff_members list) 
        contains the following variables:
        [name(str), entrance_time(int), laggard_status(bool), language_preference(str)]
    :type staffers: list
    :param persons: persons is a nested list of people where each person (in persons list) contains the following
        variables:
        [name(str), ailment(str)]
    :type persons: list
"""
def create_fonts(master):
    """This function generates and stores the fonts to be used in the program so they do not need to be created
        multiple times throughout the program
        :param master: takes in the reference to the main program window, which is needed to create the following fonts
        :type master: tkinter class window reference
        """
    global medium_font, larger_font
    root = master
    medium_font = tk_font.Font(root=root.master, family='Helvetica', size=10, weight=tk_font.BOLD)
    larger_font = tk_font.Font(root=root.master, family='Helvetica', size=12, weight=tk_font.BOLD)


def language_preference():
    """returns the language preference of the session owner
        :returns: returns the key value of language preference (~101 for english) (~102 for spanish)
        :rtype: str """
    return session_owner.__getitem__(1)


def get_staffers_list():
    """returns the full list of staffers
        :return: returns the list of staffers to be used in other classes
        :rtype: list"""
    return staffers


def get_next_person():
    """method in charge of returning the next person to be treated.  This person popped from the list persons
        :returns: list of a particular person in the persons nested list
        :rtype: list"""
    return persons.pop()


def get_large_font():
    """method to return the larger font to be used in other classes
        :returns: the layout for the larger font size
        :rtype: Font """
    return larger_font


def get_medium_font():
    """method to return the medium font to be used in other classes
        :returns: the layout for the medium font size
        :rtype: Font """
    return medium_font

def get_staff_member(staff_type):
    for member in staffers:
        if member[1]== staff_type:
            return member
