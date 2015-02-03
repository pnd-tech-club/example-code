/* Conceived by Sean Hinchee */
package main

import (
"fmt"
)

func main() {
	var a, b int
	usrname := ""

	fmt.Print("What's your name?: ")
	fmt.Scan(&usrname)
	fmt.Println("Hello, ", usrname, "!")

	a, b = 2, 2
	c := a + b
	fmt.Println("Two plus two is: ", c)
}
