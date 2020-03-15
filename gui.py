import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

import os

class LabelWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ZCTL GUI")

        hbox = Gtk.Box(spacing=10)
        hbox.set_homogeneous(False)
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_right.set_homogeneous(False)

        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        self.label = Gtk.Label()
        self.passthrough(0)
        self.label.set_line_wrap(True)
        vbox_left.pack_start(self.label, True, True, 0)

        self.passthrough_button = Gtk.Button.new_with_mnemonic("_Passthrough")
        self.passthrough_button.connect("clicked", self.passthrough)
        vbox_right.pack_start(self.passthrough_button, True, False, 0)

        self.video_idle_button = Gtk.Button.new_with_mnemonic("_Video")
        self.video_idle_button.connect("clicked", self.video_idle)
        vbox_right.pack_start(self.video_idle_button, True, False, 0)

        self.image_button = Gtk.Button.new_with_mnemonic("_Image")
        self.image_button.connect("clicked", self.image)
        vbox_right.pack_start(self.image_button, True, False, 0)

        self.quit_button = Gtk.Button.new_with_mnemonic("_Quit")
        self.quit_button.connect("clicked", self.quit)
        vbox_right.pack_start(self.quit_button, True, False, 0)

        self.add(hbox)


    def set(self, state):
        with open("status", "w") as statusfile:
            statusfile.write(str(state))

    def passthrough(self, button):
        self.label.set_text("Passthrough")
        self.set("PASSTHROUGH")

    def video_idle(self, button):
        self.label.set_text("Playing video")
        self.set("VIDEO")

    def image(self, button):
        self.label.set_text("Showing image")
        self.set("IMAGE")

    def quit(self, button):
        self.set("EXIT")
        exit(0)

window = LabelWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
