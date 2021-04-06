# execution
# puts "Please enter base  URL format."
# input = gets.chomp
# puts "Start number?"
# puts "Final number?"
# puts ""

class String
   def number?
      match(/\d/) == nil ? false : true
   end
end

class WgetGenerator
   # input loop reset
   def initialize
      setup
   end

   # a multiline put
   def confirmation(url, start, final)
      <<~HEREDOC
         These were given:
         URL: #{url}
         Start: #{start}
         Final: #{final}
         If these are correct, press enter to execute.
      HEREDOC
   end

   # input loop
   # user input, execute output. no exit built in, use CTRL+C.
   def setup
      url = ""
      start = ""
      final = ""
      execute = false

      puts "Please enter base URL format."
      url = gets.chomp
      puts "Start number?"
      start = gets.chomp
      puts "Final number?"
      final = gets.chomp
      puts confirmation(url, start, final)
      execute = true if gets.chomp == ""
      if execute == false
         setup
      elsif execute == true
         # run
      end
   end

   # parses URL to relevant components
   # no input. outputs URL base, filename base, number base.
   def parse(url)
      # parse URL
         # URL ends with number then filetype.
         # filetype can be removed by the final [.]. name of file is preceded by final [/].
         # number detection... every example we've seen has something before the number that isn't a number.
         # # of 0's to use as buffer can be read from the filename itself.
      # parts:
         # URL base (everything up to number)
         # filename base (after /, before number)
         # number base
   end

   # main logic executor.
   # no input. no output.
   def execution
      # read number base, determine how many zeros to put in front
      # read start, find relevant equivalent
      # loop: assembles each line command from start to end number. add escape characters.
      # concat each iteration to... string? string. then write string at end.
      # call file writer at end
   end

   # writes commands to a .ps1.
   # called as part of [generator].
   def file_writer
      test = "wget \"http://xyzcomics.com/wp-content/uploads/2020/05/redux-12.jpg\" -outfile \"redux-12.jpg\""
      name = "testfile"
      File.open("#{name}.ps1", "w") do |f|
         f.write(test)
      end
      # this executes as expected.
      # will need to add filename? no, can be parsed from URL.
      # don't need directory.
   end

end

# wget = WgetGenerator.new