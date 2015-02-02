package main

import "fmt"


type Rectangle struct {
	Sides // Anonymous Field
}

type Sides struct {
	height int
	width int
}

func (s Sides) Perimeter()(totalperim int) {
	totalperim = (2 * s.height) + (2 * s.width)
	return
}

func (s Sides) Area()(totalarea int) {
	totalarea = s.height * s.width
	return
}

func main() {
	r := Rectangle{Sides{4, 4}}
	fmt.Println("Rectangle Perimeter: ", r.Perimeter())
	fmt.Println("Rectangle Area: ", r.Area())
}

