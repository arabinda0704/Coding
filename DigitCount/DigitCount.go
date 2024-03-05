package main

import "fmt"

func digitSum(n int) int{
    sum :=0
    for n>0 {
        p:=n%10
        sum+=p
        n/=10
    }
    return sum
}


func digitSumOneDigit(n int) int{
    x:=digitSum(n);
    if x>=10 {
       return digitSumOneDigit(x)
    }

				return x;
}
func main(){  
    fmt.Println(digitSumOneDigit(9999));

}
