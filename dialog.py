#!/usr/bin/python

import gtk
from os import system

class MyDialog():
    
    # Delete event handler
    def delete_event(self, widget, event, data=None):
        return False
    
    # destroy handler
    def destroy(self, widget, data=None):
        gtk.main_quit()

    ##actions 
    
    def reboot_action(self, btn):
        system("dbus-send --print-reply --system --dest=org.freedesktop.Hal /org/freedesktop/Hal/devices/computer org.freedesktop.Hal.Device.SystemPowerManagement.Reboot")

    def hibernate_action(self, btn):
        system("cb-lock")
        system("dbus-send --print-reply --system --dest=org.freedesktop.Hal /org/freedesktop/Hal/devices/computer org.freedesktop.Hal.Device.SystemPowerManagement.Hibernate")
        gtk.main_quit()

    def shutdown_action(self, btn):
        system("dbus-send --print-reply --system --dest=org.freedesktop.Hal /org/freedesktop/Hal/devices/computer org.freedesktop.Hal.Device.SystemPowerManagement.Shutdown")

    def suspend_action(self, btn):
        system("dbus-send --system --print-reply --dest=org.freedesktop.UPower /org/freedesktop/UPower org.freedesktop.UPower.Suspend")
        gtk.main_quit()

    def __init__(self):
        # create the new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        
        # conects events
        window.connect("delete_event", self.delete_event)
        window.connect("destroy", self.destroy)
        
        # config window
        window.set_title("w?")
        window.set_border_width(0)
        window.set_size_request(500, 100)
       
        # main container
        self.vertical_box = gtk.VBox()
          
        ## button box
        self.button_box = gtk.HBox()
        
        ## Buttons
        
        # hibernate button
        self.hibernate_button = gtk.Button("_Hibernate")
        self.hibernate_button.set_border_width(0)
        self.hibernate_button.connect("clicked", self.hibernate_action)
        self.button_box.pack_start(self.hibernate_button)

        # suspend button
        self.suspend_button = gtk.Button("_Suspend")
        self.suspend_button.set_border_width(0)
        self.suspend_button.connect("clicked", self.suspend_action)
        self.button_box.pack_start(self.suspend_button)

        # reboot button
        self.reboot_button = gtk.Button("_Reboot")
        self.reboot_button.set_border_width(0)
        self.reboot_button.connect("clicked", self.reboot_action)
        self.button_box.pack_start(self.reboot_button)

        # shutdown button
        self.shutdown_button = gtk.Button("_Shutdown")
        self.shutdown_button.set_border_width(0)
        self.shutdown_button.connect("clicked", self.shutdown_action)
        self.button_box.pack_start(self.shutdown_button)    

        self.vertical_box.add(self.button_box)
        
        window.add(self.vertical_box)
        
        window.show_all()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    app = MyDialog()
    app.main()
