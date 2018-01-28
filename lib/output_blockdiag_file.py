# -*- coding:utf-8 -*-


class OutputBlockdiagFile:

    def __init__(self, conf):
        self.conf = conf
        self.f = open(self.conf.get_config_by_key('target', 'service_name') + '.diag', 'w')
        self.f.write("blockdiag {")

    def add_diagram(self, start_name, end_name_list):
        text = start_name + " -> "
        for end_name in end_name_list:
            text += end_name + ","
        text = text[:-1] + ";"
        self.f.write(text)

    def __del__(self):
        self.f.write("}")
        self.f.close()