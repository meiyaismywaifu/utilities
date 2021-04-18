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



### 21_04_17 (above was 21_04_13)
    # https://mail.python.org/pipermail/python-list/2003-August/175691.html
    # "FOUND! how to attach to running instances of Internet Explorer"
# import win32com.client
# # look in the makepy output for IE for the "CLSIDToClassMap"
# # dictionary, and find the entry for "ShellWindows"
# clsid='{9BA05972-F6A8-11CF-A442-00A0C90A8F39}'
# ShellWindows=win32com.client.Dispatch(clsid)
# for i in range(ShellWindows.Count):
#     print i
#     # this is the titlebar value
#     print ShellWindows[i].LocationName
#     # this is the current URL
#     print ShellWindows[i].LocationURL
#     print
    # this works after changing [print thing] to [print(thing)], presumably this is python 2 instead of python 3. that means this is on a Aug 02 before 2008. oh the time is on there. it's 03_08_02. what a strange time format.
    # it prints a URL and not a filepath.
# win32com.client has no available documentation.
    # [http://timgolden.me.uk/pywin32-docs/html/com/win32com/HTML/docindex.html]
    # [http://timgolden.me.uk/pywin32-docs/html/com/win32com/readme.htm]
# these don't tell me anything. like they're sparse garbage already they literally don't have a listing for win32com even though there's a lot of other win32xxx's, and then the stuff on win32com has literally no methods or nowhere to look for methods.
# specifically i want to retrieve a filepath if possible instead of a URL and then convert it back.
# some search says [dir] and [help] help. latter seems to be explanations, former a list. using it on [ShellWindows] object i expect to see a list that includes LocationName and LocationURL. neither of these appear. python does some things in reverse from ruby, that might be it.
# it is possible it does not exist. this guy from 2003, along with the other supposed (could not test myself) solutions ive found in Powershell and C#, all call this "9BA05972-F6A8-11CF-A442-00A0C90A8F39" thing. the objective is always "retrieve explorer filepaths" and the solution is always "do it through this thing with internet explorer". spec: bigger people than me could not find it if it does exist.
    # what does exist is a python library that parses URL to string.
# from urllib.parse import unquote
# unquote(url)

# import win32com.client
# from urllib.parse import unquote
# clsid='{9BA05972-F6A8-11CF-A442-00A0C90A8F39}'
# ShellWindows=win32com.client.Dispatch(clsid)
# ls = []
# for i in range(ShellWindows.Count):
#    LURL = ShellWindows[i].LocationURL
#    location = unquote(LURL[8:])
#    ls.append(location)
# print(ls)
    # testing redacted cause can't care to clean out the examples.

# UnicodeEncodeError: 'charmap' codec can't encode characters in position 519-520: character maps to <undefined>
    # presumably this is the japanese characters.
    # and then afterwards have to set encoding in the file. i suppose it makes sense.

# import subprocess
# subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')
    # this opens explorer on given file.
    # how do we get the current selected file?

# import win32com.client
# import pythoncom

# ProgID = "someProgramID"
# com_object = win32com.client.Dispatch(ProgID)

# for key in dir(com_object):
#     method = getattr(com_object,key)
#     if str(type(method)) == "<type 'instance'>":
#         print(key)
#         for sub_method in dir(method):
#             if not sub_method.startswith("_") and not "clsid" in sub_method.lower():
#                 print("\t"+sub_method)
#     else:
#         print("\t",method)
    # [https://stackoverflow.com/questions/27370768/list-all-methods-in-comobject]
    # this is the same as [help()] except with a lot more garbage.
    # how do we get available fucking methods

# [https://stackoverflow.com/questions/43949747/return-a-list-of-all-files-from-the-selected-explorer-window-with-pywin32]
    # hey this guy is like me
# "You are relying on implementation details. Don't. Use the API."
    # AND HOW DO I FUCKIN DO THAT BR0
# "The shell has a dedicated COM API [https://msdn.microsoft.com/en-us/library/windows/desktop/bb773177(v=vs.85).aspx] for things like this, which can be accessed through pywin32."
    # what does this mean? anything in there can be called?
    # what do i import in order to call it?
    # the example script here does something, but not the thing that actually answers the question; seems to have returned every single file in every single folder instead.
    
    # oh there's a setting at the bottom that is set to False. setting it to True actually retrieves it. wao!
    # error doesn't work the way i want it to but the retrieval works....
    # search term for above was "python win32com windows explorer methods".

    # trying to copy and paste these names into microsoft docs and they return garbage.

    # trying to add condition to given to return empty instead of error if nothing selected. can't convert to ls/for in the existing way.
    # appears the error is upstream of this. oh, the entire thing is a for loop.

# ls = ["a","s","d","f","g"]
# for idx, val in enumerate(ls):
#     print(idx, val)
    # for with index
    # hmm... need map...
    # but map returns a map instead of a list, how irritating.

# vec = [2, 4, 6]
# vec = [3*x for x in vec]
# print(vec)
    # i see.

# i was gonna write down something but i seem to have gotten around it. not sure what didn't work? it had to do with something not parsing \\'s. it seems \\'s is the output of the new script too and can be read just fine by subprocess so there is no problem here.

# print('Opening the following files')
# print('in explorer:')
# for file in explorer_list
#     print(file)
# print('in Honeyview:')
# for file in filelist:
#    print(file)
# print('--- --- --- --- --- ---')

# for file in explorer_list
#     try:
#         subprocess.Popen(f'explorer /select, "{file}"')
#         'temp empty'
#     except:
#         print(f'failed to open: {file}')

# for file in filelist:
#     try:
#         os.startfile(file)
#         'temp empty'
#     except:
#         print(f'failed to open: {file}')
# input("Execution complete. Press enter to exit.")
    # i think this is the new format
    # oh but wait, there's windows with selected and unselected items...

# the if statement at the end triggered on first condition.
# apparently [&] and [and] aren't the same. why? actually i don't care.

# a = 5; b = "asdasdasd"
# print(f"{a} + {b}")

# a = ["a","s","g","h"]
# for i in a : print(a)

# print('Opening')
# print('in explorer: --- --- ---')
# for f in wls: print(f)
# print('files in explorer: --- --- ---')
# for f in sls: print(f)
# print('in Honeyview: --- --- ---')
# for f in fls: print(f)
# print('--- --- --- --- --- ---')

# for file in sls:
#    try:
#       subprocess.Popen(f'explorer /select, "{file}"')
#    except:
#       print(f'failed to open explorer on: {file}')

# def stdopen(filelist):
#    for file in filelist:
#       try:
#          os.startfile(file)
#       except:
#          print(f'failed to open: {file}')
# stdopen(wls)
# stdopen(fls)

# input("Execution complete. Press enter to exit.")
    # i forgot to import subprocess.


# the first time it worked, one of the selected files wasn't selected. i couldn't reproduce it again.

# oh it happened again.
# and it's not happening again. hmmmmmmmmm
# can i make everything wait until each popen is done?

# [https://stackoverflow.com/questions/2837214/python-popen-command-wait-until-the-command-is-finished]
# apparently [subprocess.call] in place of [subprocess.Popen] does this.
# apparently [subprocess.run] supersedes [.call]. "Run the command described by args. Wait for command to complete, then return a CompletedProcess instance."
# guy here says "While subprocess is preferred in many answers, it cannot handle space and quota within command very well. The above answer does not directly solve the os.popen question.". i dunno what this means though.
# we'll see if this problem happens again i suppose. [Popen] certainly doesn't say it waits for the command to complete while these other two do.
# there is a "queue" and something about "threading". look into that next if it happens again. im not sure why it would work, [subprocess] is in a for loop that comes first and the rest shouldn't run until it's finished, but that's in the vicinity.

# k didn't stop it... hmm. what if i reverse the order?
# nope... clogs even if it's by itself.
# stops clogging with sufficient sleep. which for 9 folders appears to be 3 seconds. that's uhhhhhhhhhhhhhh retarded.
# well, i guess it is literally retarded, i.e. "slow", "lagging".