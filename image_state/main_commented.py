import psutil
import win32com.client
import time
from datetime import datetime
from urllib.parse import unquote

import windows2

# retrieves all open explorer windows and all open files in Honeyview, creates script that opens said files upon execution.

# retrieve all processes
# string input, list (array) of [Process]es output.
# copy of [find_procs_by_name] example from psutil docs
def processes(name):
   ls = []
   for p in psutil.process_iter(['name']):
      if p.info['name'] == name:
         ls.append(p)
   return ls

# retrieve all files
# list of [Process]es input, list of strings output.
def files(process_list):
   ls = []
   for process in process_list:
      fn = retrieve_filename(process)
      ls.append(fn)
   return ls

# retrieve filename
# [Process] input, string output.
def retrieve_filename(process):
   fp = process.cmdline()[1] # honeyview gives [exe, file] here
   return fp

# current time
# no input, string output.
def time_to_string():
   time = datetime.now().strftime("%Y_%m_%d-%H.%M.%S")
   return time

# creates file
# input two strings, no output.
def write(filename, string):
   f = open(f"{filename}.py", "w", encoding="utf-8") # set encoding for japanese characters. requires designating encoding in first line of second string to be re-opened.
   f.write(string)
   f.close()
   return

# retrieves all explorer windows. superseded by windows2().
# reference [ancient_artifact_of_great_power.py], written in 2003 and in python 2.
# no input, list of strings output.
def windows():
   clsid='{9BA05972-F6A8-11CF-A442-00A0C90A8F39}' # explorer's designation in COM or something
   ShellWindows=win32com.client.Dispatch(clsid)
   ls = []
   for i in range(ShellWindows.Count):
      LURL = ShellWindows[i].LocationURL
      location = unquote(LURL[8:]) # first 8 characters are "file:///", unnec
      ls.append(location)
   return ls

# removes self from list. for use on [selected_list].
# list input, list output.
def filter_self(list):
    list = [i for i in list if not i == __file__]
    return list

# creates opener script. here for record purposes only.
# list of strings input, string output
# desire one with error catcher
def script_generator1(filelist):
   text = "import os \n\n"
   for file in filelist:
      line = f'os.startfile(r"{file}") \n'
      text += line
   return text

# creates opener script. here for record purposes only.
# list of strings input, string output.
def script_generator2(filelist):
   script = ("# -*- coding: UTF-8 -*-\n"
             "import os\n\n"
             f"filelist = {filelist}\n\n"
             "print('Opening the following files:')\n"
             "for file in filelist:\n"
             "   print(file)\n"
             "print('--- --- --- --- --- ---')\n\n"
             "for file in filelist:\n"
             "   try:\n"
             "      os.startfile(file)\n"
             "   except:\n"
             "      print(f'failed to open: {file}')\n"
             'input("Execution complete. Press enter to exit.")')
   return script

# creates opener script. here for record purposes only.
# three lists as input, string output.
def script_generator3(window_list, selected_list, file_list):
   script = ("# -*- coding: UTF-8 -*-\n"
             "import os\n"
             "import subprocess\n"
             "import time\n\n"

             f'wls = {window_list}\n'
             f'sls = {selected_list}\n'
             f"fls = {file_list}\n\n"

             "print('Opening')\n"
             "print('in explorer: --- --- ---')\n"
             "for f in wls: print(f)\n"
             "print('selected in explorer: --- --- ---')\n"
             "for f in sls: print(f)\n"
             "print('in Honeyview: --- --- ---')\n"
             "for f in fls: print(f)\n"
             "print('--- --- --- --- --- ---')\n\n"

             "for file in sls:\n"
             "   try: subprocess.run(f'explorer /select, \"{file}\"'); time.sleep(3)\n" # without a forced delay it opens correct directories but fails to select the files at a high rate. [run] is supposedly already a block and does not execute the next command until it's complete. 3s seems to be the right delay.
             "   except: print(f'failed to open explorer on: {file}')\n\n"
 
             "def stdopen(filelist):\n"
             "   for file in filelist:\n"
             "      try: os.startfile(file)\n"
             "      except: print(f'failed to open: {file}')\n"
             "stdopen(wls)\n"
             "stdopen(fls)\n\n"

             'input("Execution complete. Press enter to exit.")\n')
   return script

# console output during creation
# two strings as input, no output.
def readout(window_list, selected_list, file_list):
   print("detected empty windows:\n--- --- ---")
   print("\n".join(window_list) + "\n--- --- ---")
   print("detected selected files:\n--- --- ---")
   print( "\n".join(selected_list) + "\n--- --- ---")
   print("detected honeyview files:\n--- --- ---")
   print("\n".join(file_list) + "\n--- --- ---")
   print("window will close shortly...")
   return

# execution
process_list = processes("Honeyview.exe")
efl = windows2.get_explorer_files()
window_list = efl[0]; selected_list = filter_self(efl[1])
if len(window_list) == 0 and len(selected_list) == 0 and len(process_list) == 0:
   print("no explorer or honeyview windows detected. window will close shortly...")
   time.sleep(3)
   # if empty, have to put a string or something in it, python doesn't allow comment-only conditions
else:
   file_list = files(process_list)
   readout(window_list, selected_list, file_list)
   output = script_generator3(window_list, selected_list, file_list)
   name = time_to_string()
   write(name, output)
   time.sleep(5)