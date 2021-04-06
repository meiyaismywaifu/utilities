# add regex detector for digits
class String
   def number?
      match(/\d/) == nil ? false : true
   end
end

# main
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
         execution(url, start, final)
      end
   end

   # main logic executor.
   # no input. no output.
   def execution(url, start, final)
      parts = parse(url) # [url_base, filename_base, number_base, filetype]. all strings.
      url_base = parts[0]
      filename_base = parts[1]
      number_base = parts[2]
      filetype = parts[3]

      # read number base, determine how many zeros to put in front
      # "if there are 0's in front, then all numbers in set are same length. otherwise no front padding."
      if number_base.length != 1 && number_base[0] == "0"
         min_length = number_base.length
      else
         min_length = false
      end

      # convert inputted start value to correct equivalent
      # outputs string
      if min_length != false
         start.prepend("0") until start.length == min_length
      else
         # nothing
      end
      start_i = start.to_i
      final_i = final.to_i

      # loop assembles each line command from start to end number (integer counter)
      current_i = start_i
      current_number = start
      output = ""
      until current_i > final_i
         current_filename = "#{filename_base}#{current_number}.#{filetype}"
         current_line = "wget \"#{url_base}#{current_filename}\" -outfile \"#{current_filename}\"\n"
         output << current_line

         current_i += 1
         current_number = current_i.to_s
         current_number.prepend("0") until current_number.length == min_length if min_length != false
      end

      file_writer(filename_base, output)

   end

   # writes commands to a .ps1. name is parsed from URL.
   # called as part of [generator].
   def file_writer(name, text)
      File.open("#{name}.ps1", "w") do |f|
         f.write(text)
      end
   end

   # parses URL to relevant components
   # no input. outputs array [URL base, filename base, number base, filetype].
   def parse(url)
      disassembly_a = url
      disassembly_b = ""
   
      until disassembly_a[-1] == "/"
         disassembly_b.prepend(disassembly_a.slice!(-1))
      end
      url_base = disassembly_a
   
      disassembly_a = disassembly_b
      disassembly_b = ""
   
      until disassembly_a[-1] == "."
         disassembly_b.prepend(disassembly_a.slice!(-1))
      end
      disassembly_a.slice!(-1)
      filetype = disassembly_b
      
      disassembly_b = ""
   
      until disassembly_a[-1].number? == false
         disassembly_b.prepend(disassembly_a.slice!(-1))
      end
      filename_base = disassembly_a
      number_base = disassembly_b
   
      return [url_base, filename_base, number_base, filetype]
   end
end

wget = WgetGenerator.new
