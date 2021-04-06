# input: URL, lower number, upper number
# output: .ps1 file

   def testing
      item = "thing"
      <<~HEREDOC
         #{item}
         line 2
         line 3
      HEREDOC
   end
# this executes.


# responding to gets.chomp with [enter] results in a variable of string [""].
   input = gets.chomp
   input == ""
# this returns true.


   execute = input == ""
# execute is assigned boolean from comparison.
# this looks funny though.
   execute = false
   execute = true if input == ""
# that's better


   # http://xyzcomics.com/wp-content/uploads/2020/05/redux-12.jpg
# URL ends with number then filetype.
# filetype can be removed by the final [.]. name of file is preceded by final [/].
# number detection... every example we've seen has something before the number that isn't a number.
# # of 0's to use as buffer can be read from the filename itself.


# from hangman/lib/hangman.rb,
   def save(state, name="autosave") # defaults assigned at method declaration
      File.open("#{name}.json", "w") do |f|
         f.write(JSON.pretty_generate(state))
      end
   end
# looks like i don't need anything fancy? [f.write(variablename)]?
   test = "wget \"http://xyzcomics.com/wp-content/uploads/2020/05/redux-12.jpg\" -outfile \"redux-12.jpg\""
   name = "testfile"
   File.open("#{name}.ps1", "w") do |f|
      f.write(test)
   end
# this executes as expected. need escape characters.


   until disassembly_a[-1].!.is_a? Integer
# this doesn't work because characters in a string are all String.
   /\d/
# this is regexp for digits. /'s indicates regex, \d is a set of characters.
   def number?(character)
      # ???
   end
# this is what i wanted to do but i wasn't sure how to execute
   /\d/.match(character)
# this outputs nil if not in there, else it outputs the thing itself.
# fount this route:
   class String
      def number?
         match(/\d/) == nil ? false : true
      end
   end
# which modifies the String class so that definition of that method is called. as it so happens, this method is available.


   # read number base, determine how many zeros to put in front
# ...? what are the different cases?
# "if there are 0's before not-0's, then all numbers in set are same length. otherwise no front padding."
# is that it? does that cover everything?
# i don't think ive ever seen a 00,01..99,100. why haven't i? well, i haven't.
# if anything what's not covered is 01, 02a, 02b, 03. but that is not common for the use case here.
# how do "UUIDs" work? would be useful to have something that modifies chrome... oh, that's what an add-on is. oooh....
# well, this really is small-scale then. how are the bigger things built? how much of them are actually built by the final builder?