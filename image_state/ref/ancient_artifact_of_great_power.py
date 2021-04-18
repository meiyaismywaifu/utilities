# [https://mail.python.org/pipermail/python-list/2003-August/175691.html]
# "FOUND! how to attach to running instances of Internet Explorer"
# gcash gcash at luncheonmeat.cfl.rr.com 
# Sat Aug 2 01:47:55 EDT 2003

# Most folks know you can start up an instance of Internet Explorer by
# saying "x=win32com.client.Dispatch('InternetExplorer.Application.1')"
# and you get a WIN32 object with a "Document" object that has arrays of
# "Link"/"Form"/"Frame" subobjects, and methods like "Navigate" where
# you can force the IE instance to browse to a new URL.

# What folks would like to do is to connect to an already running
# version of explorer, and this isn't so obvious.

# The MS KB article you usually find is 176792 which mentions using
# SHDocVw.ShellWindows to iterate through the instances.  However Mark
# Hammond sayes this is a "vtable interface" (whatever that is) and "not
# supported by python" in
# http://groups.google.com/groups?hl=en&lr=&ie=UTF-8&oe=UTF-8&newwindow=1&safe=off&selm=3D106564.4040602%40pretection.com

# HA! well, I happened to discover you can do:

import win32com.client
# look in the makepy output for IE for the "CLSIDToClassMap"
# dictionary, and find the entry for "ShellWindows"
clsid='{9BA05972-F6A8-11CF-A442-00A0C90A8F39}'
ShellWindows=win32com.client.Dispatch(clsid)
for i in range(ShellWindows.Count):
    print i
    # this is the titlebar value
    print ShellWindows[i].LocationName
    # this is the current URL
    print ShellWindows[i].LocationURL
    print

# and the object returned by ShellWindows[n] is the exact same as the
# one returned by Dispatch('InternetExplorer.Application.1')

# I'm posting this here for future generations of Googlers.

# So I'm running Win2K Pro... and I'm curious about what versions this
# works under.  I'm pretty sure you have to have IE 5.0 or newer, but
# could folks try this code on 95/98 and tell me (gcash-at-cfl.rr.com)
# if it works??

# Also, I haven't been able to determine if there's a better name of the
# form 'InternetExplorer.Application.1' instead of using the horrid
# class-id.  How do you do that?  The makepy output for explorer doesn't
# list one.

# Thanks to Mark Hammond for win32all, it is a true work of art, and is
# teaching an old UNIX hack lots of Windows stuff.

# -gc

# -- 
# I've never tried emacs because I already _have_ an OS on this peecee.
# -- mikea at mikea.ath.cx (Mike Andrews)