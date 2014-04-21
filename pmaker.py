#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        pmaker
# Purpose:
#
# Author:      casa
#
# Created:     14/10/2012
# Copyright:   (c) casa 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import gtk
import os
import platform
from password_maker import password_maker
from decimal import Decimal
from decimal import getcontext
from populate import *

class main:
    def __init__(self):
        ui_path=os.path.join(sys.path[0],"gui/main.glade")
        self.builder = gtk.Builder()
        self.builder.add_from_file(ui_path)
        window = self.builder.get_object("window1")
        #window.set_icon_from_file(os.path.join(sys.path[0],"widgets/navigate/nav_uninstall.png"))
        self.builder.connect_signals(self)
        window.connect("destroy", self.quit)
        #window.connect("row-activated", self.new_package_selected)
        window.show_all()

    def quit(self, widget):
        if platform.system() == "Linux":
            t2 = os.getpid()
            os.popen("kill -9 "+str(t2))
        gtk.main_quit()

    def on_radiobutton2_toggled(self, widget):
        hbox1 = self.get_widget("hbox1")
        hbox1.set_sensitive(False)
        hbox2 = self.get_widget("hbox2")
        hbox2.set_sensitive(True)


    def on_radiobutton1_toggled(self, widget):
        hbox2 = self.get_widget("hbox2")
        hbox2.set_sensitive(False)
        hbox1 = self.get_widget("hbox1")
        hbox1.set_sensitive(True)


    def get_widget(self, widget):
        return self.builder.get_object(widget)

    def on_button1_clicked(self, widget):
        if self.get_widget("radiobutton1").get_active():
            entry1 = self.get_widget("entry1")
            user_input = entry1.get_text()
            if user_input:
                code = password_maker.encode_word(user_input)
                entry2 = self.get_widget("entry2")
                entry2.set_text(code)
        elif self.get_widget("radiobutton2").get_active():
            ell = Learner()
            ell.loadd(IUP)
            spin = self.get_widget("spinbutton1")
            word_number = spin.get_value_as_int()
            if word_number:
                words = ell.generate(word_number-1, prefix=None)[:-1]
                words = words.replace(".","")
                words = words.replace("\n","")
                code = password_maker.encode_word(words)
                entry2 = self.get_widget("entry2")
                entry2.set_text(code)

    def on_entry1_changed(self, widget):
        progress = self.get_widget("progressbar1")
        #print widget.get_text()
        fraction = password_maker.how_secure(widget.get_text())
        #print fraction
        #getcontext().prec = 3
        #print fraction/100
        progress.set_fraction(fraction/100)
        if fraction <= 35:
            progress.set_text("Muy Débil")
        elif fraction > 35 and fraction < 75:
            progress.set_text("Débil")
        elif fraction >= 75 and fraction < 100:
            progress.set_text("Media")
        elif fraction >= 100:
            progress.set_text("Fuerte")

    def on_entry2_changed(self, widget):
        progress = self.get_widget("progressbar2")
        fraction = password_maker.how_secure(widget.get_text())
        progress.set_fraction(fraction/100)
        if fraction <= 35:
            progress.set_text("Muy Débil")
        elif fraction > 35 and fraction < 75:
            progress.set_text("Débil")
        elif fraction >= 75 and fraction < 100:
            progress.set_text("Media")
        elif fraction >= 100:
            progress.set_text("Fuerte")


#if __name__ == '__main__':
main()
gtk.main()

