#!/usr/bin/env ruby

regex = /School/
input_str = ARGV[0]

if input_str =~ regex
  puts "The input string '#{input_str}' matches the regex '#{regex}'."
else
  puts "The input string '#{input_str}' does not match the regex '#{regex}'."
end
