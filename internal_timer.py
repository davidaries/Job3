# """internal_timer.py is a class that manages an internal timer used in the application. The timer displays in the format
# HOURS:MINUTES:SECONDS starting at 0 seconds and continuing for as long as the program is being executed or until paused
#
# :param time_count: stores the current running time of the application
# :type time_count: int
# :param timer_running: says whether the timer is current paused or not
# :type timer_running: bool
# :param root: is an instance of tkinter creating the main window for program.  root holds the primary pause, unpause,
#     and end buttons to interact with the timer (pausing and unpausing) as well as ending the program
# :type root: tkinter class reference
# :param time_label: is a label inside packed inside of the time_window used to display current running time
# :type time_label: Label
# """
#
# import staff_manager as sm
#
# time_count = 0  # counter for the current time
# #wait_count = 0
# timer_running = True
# root = None
# time_label = None
#
#
# def __init__(master, timer):
#     """constructor method for internal timer class
#     :param master: establishes a pointer to the root of the program
#     :type master: Tk class
#     :param timer: timer is a reference to the label that displays the time in timer_window
#     :type timer: Label"""
#     global root, time_label
#     root = master
#     time_label = timer
#
#
# def pause_time():
#     """this method sets the bool value of timer_running to False, which is checked each second by the manage time function"""
#     global timer_running
#     timer_running = False
#
#
# def resume_time():
#     """this method sets the bool value of timer_running to True, which is checked each second by the manage time function"""
#     global timer_running
#     timer_running = True
#
#
# def convert_time(seconds):
#     """this method converts a given time count into the format HOURS:MINUTES:SECONDS
#     :param seconds: the number of seconds to be processed into the format
#     :type seconds: int
#     :return: a formatted string of the seconds given to the method
#     :rtype: str"""
#     seconds = seconds % (24 * 3600)
#     hour = seconds // 3600
#     minutes = seconds // 60 - (hour * 60)
#     seconds %= 60
#     return "%d:%02d:%02d" % (hour, minutes, seconds)
#
#
# def get_formatted_time():
#     """this method returns the formatted current time
#     :return: formatted version of current time HOURS:MINUTES:SECONDS
#     :rtype: str"""
#     return convert_time(time_count)
#
#
# def manage_time():
#     """This method manages the internal timer of the application it calls itself every second (1000 miliseconds)
#     updating the current time count if the clock is meant to be running.  This done by checking the if the timer_running
#     variable and only incrementing the current running time if that is true.
#     """
#     global time_count
#     sm.staff_entrance()
#     time_label.config(text="T: " + get_formatted_time())
#     if timer_running:
#         time_count += 1
#     root.after(1000, manage_time)
#
# """ Proposed function to handle the wait for a laggard.  This function does not function properly as listed
# def handle_wait():
#     global wait_count
#     print(wait_count)
#     if wait_count == 3:
#         wait_count = 0
#         return True
#     if timer_running:
#         wait_count += 1
#
#     root.after(1000, handle_wait)
# """