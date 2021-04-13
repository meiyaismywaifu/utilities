import os
import psutil
import win32api
import win32process
# import win32com # unclear

print("Hello world")

#    p = psutil.Process(os.getpid()) # or PID of process
#    p.open_files()
# os.getpid() appears to refer to this script.
# having pointed it at a few honeyviews, this doesn't return any jpg's. doesn't return a consistent list either. did return something saying honeyview once.

    # print(os.getcwd())
# filler.

    # path = os.path.normpath(r"A:\Users\path\redacted\1618199225104.jpg")
    # path = os.path.normpath(r"A:\Users\path\redacted")
    # print(path)
    # os.startfile(path)
# [\U] "starts an eight-character Unicode escape" [...] You either need to duplicate all backslashes [..] Or prefix the string with r (to produce a raw string)""
# above open file and folder.
# python whitespace is read, have to un-indent.

# p = win32api.GetUserName()
    # pywin32 is apparently imported as whatever module you're using.
    # need to call module.method. apparently i forgot this.

# p = psutil.Process(13280)
# print(p.cwd())
# print(p.as_dict())
    # former does actually retrieve honeyview filepath.
    # latter retrieves all public information, which does actually include the filename. just not under open_files, apparently.
    # does not work for explorer. somewhere else says has to be done via "COM", which looks like a hellhole. is there another way?

# well, we'll put aside explorer for the time being.

# def find_procs_by_name(name):
#     "Return a list of processes matching 'name'."
#     ls = []
#     for p in psutil.process_iter(['name']):
#         if p.info['name'] == name:
#             ls.append(p)
#     return ls
# f = find_procs_by_name("Honeyview.exe")
# print(f)
    # given example in psutil docs
    # name must be exact match. name can be retrieved like so:
# p = psutil.Process(13280)
# print(p.name())

# what do we want? we want on run to record all open files so they can be re-opened at later date.
    # - find all desired things to record
    # - record things
    # - name the set according to time
    # - ability to re-open set
# i think that's the basic idea. interface etc. not a big deal; inherent function isn't much bigger than double-clicking script.

# "find all desired things to record"
    # in some magic land it'd be the entire state of the computer but the basics are just images.
    # the above given function finds processes by name and returns... an array of Process instances. ok, that's what we want. then we retrieve the file/path out of each instance, which we know exists for honeyview in as_dict() somewhere, just need to find out where
# "record things" / "ability to re-open set"
    # either as a script, or as a folder of shortcuts.
    # script: thought problem would be lack of error message if failed, but it does actually give error. what it doesn't, is continue to try to open every other file.
    # shortcuts: shortcuts are a couple kb each. this is fairly large compared to a script, but seem like a trivially correct path otherwise. would need to find how to make shortcuts with python.
# "name the set according to time"
    # both: retrieve system time, parse, etc.
    # shortcuts only: create directory
# that seems to be it.
# i don't have a particular preference for saving a script vs saving a folder of shortcuts. i prefer robustness but it's not like i can't manually retrieve filenames from a script via N++.

# path = os.path.normpath(r"A:\Users\path\redacted\1618.jpg")
# try:
#     os.startfile(path)
# except:
#     print(f"could not open:{path}")
    # this continues after error.
    # [f""]/[f''] is the interpolater. no space after f.

# big_value = "big"
    # inner scope can read but not write to outer scope.
    # instance variables are not marked by anything, just put them outside methods.

# def retrieve_processes():
#    return print("test1")
# def retrieve_filenames():
#    print("test2")
#    return
# def write():
#    print("test3")
    # none of these print...
    # oh i need to call [write()], not [write]; [()]s are req.

# os.chdir(r".\thing")
# print(os.getcwd())
    # chdir returns error if it doesn't exist.

# string = '\n'.join(map(str, file_list))
    # don't get syntax but this is the desired concept, where [file_list] is list input.

# print(type(file_list))
    # not file_list.type(), apparently.

# def opener(filelist):
#    for file in filelist:
#       try:
#          os.startfile(file)
#       except:
#          print(f"failed to open {file}")
#    return
   # this is the model.

# # from datetime import datetime
# import datetime
# # now = datetime.now()
# # current_time = now.strftime("%H:%M:%S")
# # print("Current Time =", current_time)
# print(datetime.datetime.now())
    # ...
    # apparently these two are equivalent:
# import datettime
# print(datetime.datetime.now())
    # and
# from datetime import datetime
# print(datetime.now())

# thing = """ testing testing one two three
#    does this work?
#       would be interesting if it does """
    # it does work. don't really like though.
# thing = ("testing testing one two three\n"
#          "  does this work?\n"
#          "     would be interesting if it does\n")
    # that's better.
