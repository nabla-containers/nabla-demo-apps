package helper

import "fmt"
import "C"
import "os"
import "github.com/golang/example/stringutil"

func Process_args() {
    args := os.Args[1:]
    fmt.Println(stringutil.Reverse(":sgra enildnammoc toG"))
    fmt.Println(args)
}
