word :: String 
word = "world"

a,b,c :: Int
a = 2
b = 2
c = a + b

main = do 
	putStrLn "What's your name? "
	usrname <- getLine
	print "Hello"	
	putStrLn ("Hello " ++ usrname)
	putStrLn "2 plus 2 is: "
	print c

