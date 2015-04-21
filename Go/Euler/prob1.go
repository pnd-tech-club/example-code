package main

import "fmt"

func main() {
   a:=0
   for i:=0;i<1000;i+=1 {
       if ((i%3) == 0) || ((i%5) == 0) {
           a=(a+i)
       }
   }
   fmt.Print(a, "\n")
}

