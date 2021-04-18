import psutil
import win32com.client
import time
from datetime import datetime
from urllib.parse import unquote

# retrieves all open explorer windows and all open files in Honeyview, creates script that opens said files upon execution.

def processes(name):
   ls = []
   for p in psutil.process_iter(['name']):
      if p.info['name'] == name:
         ls.append(p)
   return ls

def files(process_list):
   ls = []
   for process in process_list:
      fn = retrieve_filename(process)
      ls.append(fn)
   return ls

def retrieve_filename(process):
   fp = process.cmdline()[1]
   return fp

def time_to_string():
   time = datetime.now().strftime("%Y_%m_%d-%H.%M.%S")
   return time

def write(filename, string):
   f = open(f"{filename}.py", "w", encoding="utf-8")
   f.write(string)
   f.close()
   return

def windows():
   clsid='{9BA05972-F6A8-11CF-A442-00A0C90A8F39}'
   ShellWindows=win32com.client.Dispatch(clsid)
   ls = []
   for i in range(ShellWindows.Count):
      LURL = ShellWindows[i].LocationURL
      location = unquote(LURL[8:])
      ls.append(location)
   return ls

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

def readout(explorer_list,file_list):
   console = "detected explorer windows:\n--- --- ---\n"
   console += "\n".join(explorer_list) + "\n--- --- ---\n"
   console += "detected honeyview files:\n--- --- ---\n"
   console += "\n".join(file_list) + "\n--- --- ---\n"
   console += "window will close shortly..."
   return console

# execution
process_list = processes("Honeyview.exe")
explorer_list = windows()
if len(explorer_list) == 0 & len(process_list) == 0:
   print("no explorer or honeyview windows detected. window will close shortly...")
   time.sleep(3)
else:
   file_list = files(process_list)
   print(readout(explorer_list,file_list))
   # save_list = explorer_list + file_list
   # name = time_to_string()
   # output = script_generator2(save_list)
   # write(name, output)
   time.sleep(5)