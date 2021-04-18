import psutil
import win32com.client
import time
from datetime import datetime
from urllib.parse import unquote

import windows2

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
             "   try: subprocess.run(f'explorer /select, \"{file}\"'); time.sleep(3)\n"
             "   except: print(f'failed to open explorer on: {file}')\n\n"
 
             "def stdopen(filelist):\n"
             "   for file in filelist:\n"
             "      try: os.startfile(file)\n"
             "      except: print(f'failed to open: {file}')\n"
             "stdopen(wls)\n"
             "stdopen(fls)\n\n"

             'input("Execution complete. Press enter to exit.")\n')
   return script

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
window_list = efl[0]; selected_list = efl[1]
if len(window_list) == 0 and len(selected_list) == 0 and len(process_list) == 0:
   print("no explorer or honeyview windows detected. window will close shortly...")
   time.sleep(3)
else:
   file_list = files(process_list)
   readout(window_list, selected_list, file_list)
   output = script_generator3(window_list, selected_list, file_list)
   name = time_to_string()
   write(name, output)
   time.sleep(5)