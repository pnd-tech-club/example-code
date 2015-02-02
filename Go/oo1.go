package main

import "fmt"

type Rectangle struct {
	length int
	width int
}

func (rect Rectangle) RectArea()(area int) {
	area = rect.length * rect.width
	return
}

func main() {
	rect1 := Rectangle{5, 7} // length = 5; width = 7
	fmt.Println("Rectangle parameters: ", rect1)
	fmt.Println("Rectangular area: ", rect1.RectArea())
}

