**Description:**

ruby generates a powershell file of [wget]s.

**History:**

downloading a bunch of things manually is a pain. downloading anything manually when the site doesn't allow you to right click is a bigger pain. now that i think about it, can i just disable that? but what i thought of was to CTRL+SHIFT+I and it turned out the site i was looking at at the time had named almost all its files in numerical series and not some fancy UUIDs. UUIDs are nice but i have no idea how to deal with them. a bunch of numbers though i can use.

first i changed the numbers in the browser navigation bar directly.

then it occurred to me powershell might have curl or an equivalent to curl and i could just CTRL+ALT in N++.

then it occurred to me changing a bunch of numbers is something plausibly within my reach with my grasp of ruby.

then i thought about scraping stuff just given the folder/album/directory URL but that became a lot more difficult so it was settled here.

**Format/Usage/Notes:**

Find an internet directory where all the files you want start with the same name but end with different numbers. Inspector/Devtools/CTRL+SHIFT+I helps sometimes. Wordpress? types sites make this easy, or that is my impression.

Run [main.rb].

It will ask you for a URL, a start number, and an end number.

URL is preferably the first file. I have found that numbering conventions I can think of follow this logic:

> "if there are 0's in front, then all numbers in set are same length. otherwise no front padding."

I have seen 0, 1..99, 100. I have not ever seen 00, 01..99, 100; if there's padding it always fits the same length. There's also never a 0, 01..099, 0100, for example. In other words, format of lowest number predicts higher numbers. As this ruby script is a guesser-generator and not a scraper, giving it the lowest number is a good idea.

No need to pad the other inputs. If it starts at 001 and goes to 099, you can type "1" and "99."