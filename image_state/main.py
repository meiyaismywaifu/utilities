import os
import psutil
from datetime import datetime

# retrieves all open files in Honeyview, creates script that opens said files upon execution.

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
   f = open(f"{filename}.py", "w")
   f.write(string)
   f.close()
   return

def script_generator2(filelist):
   script = ("import os\n\n"
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

# execution
process_list = processes("Honeyview.exe")
if len(process_list) == 0:
   "do nothing"
else:
   file_list = files(process_list)
   time = time_to_string()
   output = script_generator2(file_list)
   write(time, output)