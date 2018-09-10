package main

import (
	"C"
	"fmt"
	"net/http"
	"./helper"
)

func reqHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Response 200 from go-http\n")
}

func main() {
	fmt.Println("Hi")
	helper.Process_args()
	httpd()
}

func httpd() {
	fmt.Println("You can now call `wget <ip>:3000' now")
	http.HandleFunc("/", reqHandler)
	http.ListenAndServe(":3000", nil)
}
