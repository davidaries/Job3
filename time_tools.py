

class time_tools:
    def __init__(self, simulation,time_lbl, root):
        self.sim = simulation
        self.start_time = self.sim.get_start_time()
        self.time_lbl = time_lbl
        self.time_lbl.config(text=self.convert_time(self.start_time))
        self.root = root
        self.loop_count = 0
        self.inc_value = 30
    def convert_time(self, seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        minutes = seconds // 60 - (hour * 60)
        seconds %= 60
        return "%d:%02d:%02d" % (hour, minutes, seconds)
    def get_time(self):
        return self.convert_time(self.start_time+(self.loop_count*self.inc_value))

    def update_time(self):
        self.loop_count +=1
        self.time_lbl.config(text=self.convert_time(self.start_time + (self.loop_count*self.inc_value)))
        self.root.after(1000, self.update_time)