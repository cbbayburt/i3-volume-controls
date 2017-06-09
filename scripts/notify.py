#!/usr/bin/env python

# Usage: notify app_name id title body icon timeout_in_ms

import sys
import dbus


def notify(*argv):
    notify = dbus.Interface(dbus.SessionBus()
                            .get_object("org.freedesktop.Notifications",
                                        "/org/freedesktop/Notifications"),
                            "org.freedesktop.Notifications")

    print(argv)
    id = notify.Notify(argv[0], int(argv[1]), argv[4], argv[2], argv[3], "",
                       "", int(argv[5]))

    return id

if __name__ == '__main__':
    print notify(sys.argv[1:])
