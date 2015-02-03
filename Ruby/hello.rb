# Conceived by Sean Hinchee

def main()
	print "What is your name?: "
	$usrname = $stdin.gets.chomp
	print "Hello, #{$usrname}!\n"

	$a = 2
	$b = 2
	$c = $a + $b
	print "2 plus 2 equals: #{$c}!\n"
end

main()
