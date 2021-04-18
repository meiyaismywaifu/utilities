import os
import sys
import win32con
import win32api
import win32gui
import win32com.client
import pythoncom
from win32com.shell import shell, shellcon

from urllib.parse import unquote ### ### ###

# retrieves all selected files in all explorer windows

# original from "zett42" at [https://stackoverflow.com/questions/43949747/return-a-list-of-all-files-from-the-selected-explorer-window-with-pywin32], duplicated in [/ref/cppman.py].
# tripe ###'s denote additions. deletions not marked. only logic has changed.
# original had selections for all windows / active windows, and all files / selected files, and if a selected folder had no selected file an error appeared.
# the following modified version returns a list of all files selected in all windows. if there are no windows or no selected files, the return is a list of size 0.

# Get list of paths from given Explorer window or from all Explorer windows.
def get_explorer_files():
   files = []
   paths = []

   CLSID_IShellWindows = "{9BA05972-F6A8-11CF-A442-00A0C90A8F39}"
   shellwindows = win32com.client.Dispatch(CLSID_IShellWindows)

   # Loop over all currently open Explorer windows
   for window in shellwindows:

      items = "" ### ### ###

      # Get IServiceProvider interface
      sp = window._oleobj_.QueryInterface( pythoncom.IID_IServiceProvider )
      # Query the IServiceProvider for IShellBrowser
      shBrowser = sp.QueryService( shell.SID_STopLevelBrowser, shell.IID_IShellBrowser )
      # Get the active IShellView object
      shView = shBrowser.QueryActiveShellView()

      # Get an IDataObject that contains the items of the view (either only selected or all). 
      aspect = shellcon.SVGIO_SELECTION

      ### ### ###
      try:
         items = shView.GetItemObject( aspect, pythoncom.IID_IDataObject )
      except:
         'no selected file, will be filled with path at [else]'
      ### ### ###

      # Get the paths in drag-n-drop clipboard format. We don't actually use 
      # the clipboard, but this format makes it easy to extract the file paths.
      # Use CFSTR_SHELLIDLIST instead of CF_HDROP if you want to get ITEMIDLIST 
      # (aka PIDL) format, but you can't use the simple DragQueryFileW() API then.
      if items != "": ### if a file is selected, record file path
         data = items.GetData(( win32con.CF_HDROP, None, pythoncom.DVASPECT_CONTENT, -1, pythoncom.TYMED_HGLOBAL ))

         # Use drag-n-drop API to extract the individual paths.
         numPaths = shell.DragQueryFileW( data.data_handle, -1 )

         files.extend([
            shell.DragQueryFileW( data.data_handle, i ) \
                  for i in range( numPaths )
         ])
      ###
      else: ### otherwise, record folder path [/ref/artifact_of_great_power.py]
         LURL = window.LocationURL
         paths.append(unquote(LURL[8:])) ### first 8 characters are "file:///"
      ###

   return paths, files

