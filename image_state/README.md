# Image State

**Description:**

retrieves all open files in Honeyview, creates script that opens said files on execution.

**History:**

i usually have a bunch of images open. i want to close them about as much as i want to close browser tabs. sometimes i have to/end up closing them. more often, windows explorer decides it's time to die and i lose my stuff. in any case i wanted a way to go back to where i was. ideally, it would be a bookmark system, except on the desktop. something that opened images and folders.

was poking around in powershell last time with [[wget generator](https://github.com/meiyaismywaifu/utilities/tree/main/wget_generator)]. my understanding was everything that controlled windows had to pass through CMD or powershell. complained to friends about microsoft's Introduction to Powershell making my eyes glaze over, was pointed at python. something something python something libraries and APIs something something something. i don't understand what's going on. but apparently you can make windows do things outside CMD and powershell. between the known hellhole and the unknown hellhole at least python was easier to read. i've never touched python before.

psutil's docs were alright. took some fiddling to find the filename and path from Honeyview. i thought it'd be under [open_files()] but that returned empty. apparently there's a definition of "open file" that isn't the obvious one. in any case it was found. windows folders / explorer.exe's were not found. psutil's apparently strongest retrieval is [as_dict()] and it returned nothing. apparently something to do with COM. which is supposedly covered by pywin32 / win32api. but that made my eyes glaze over. i think i looked at some other things too but they were worse and i already forgot them.

more broadly though it doesn't seem standard, either how psutil retrieves, or how processes run, opening files. in trying these two diagnostics on other things i'd want to restore, foobar2000 was the only other one that gave a usable return. does there exist another diagnostic that retrieves names/paths of open files? what is it? how would i have found it? it wasn't on the first several pages of google or stackexchange.

in other words, that i use Honeyview as my image viewer was a large part of why this effort connected.

considered making a folder of shortcuts versus a script. i thought it would be nice to have a GUI (Good User Interface). but it was nicer that i had already tested that [startfile()] worked, and generating scripts was a Known, versus who knows what it'd take to make shortcuts. decided to decide on difficulty of implementing error messages, since shortcuts autogenerate errors and the script stopped opening images if it failed. it turned out making these error messages was trivial.

well, i still think it would be nice. maybe some other time.

**Format/Usage/Notes:**

Running generator script while at least one Honeyview instance is open will generate a script in its own directory. Running generator script while no Honeyview instances are open will generate nothing.

Output script can be moved and renamed.

It's possible that other image viewers or other programs/filetypes can use this. Find one of their PIDs in Task Manager, then run

```python
p = psutil.Process(12345)
print(p.open_files())
print(p.as_dict())
```

If a name/path turns up, you're in luck. Find the exact name of the process [p.name()] and replace it in line 51. If the name/path is in [open_files()] or elsewhere with a bunch of junk, it'll have to be filtered. If there is no junk and the filename-path is in position 1 of [.cmdline()[]], then hopefully, that's all you need to do.

**Author System Environment:**

generator and output scripts run in Python 3.9.4 on Windows 10. this script uses [[os.startfile()](https://docs.python.org/3/library/os.html#os.startfile)].
Honeyview 5.18.
requires [[psutil](https://pypi.org/project/psutil/)].

