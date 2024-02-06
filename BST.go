/******************************************************************************
Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
package main
import "fmt"
// Node--> represents the components of a tree
type Node struct{
    Key int
    Left * Node
    Right * Node
}
// Insert--> it will add node to the tree
func(n * Node) Insert(d int){
   
    
    if d>n.Key{
        //move Right
        if n.Right==nil{
            n.Right=&Node{Key:d}
        }else{
            n.Right.Insert(d)
        }
    }else if d< n.Key{
        //move left
         if n.Left==nil{
            n.Left=&Node{Key:d}
        }else{
            n.Left.Insert(d)
        }
    }
    
}
// Search-->it will search for a key
func (n *Node) Search (d int) bool{
    
    if n==nil{
        return false
    }
    if d>n.Key{
        return n.Right.Search(d)
    }else if d< n.Key{
        return n.Left.Search(d)
    }
    return true
    
}

func main() {
    tree:=&Node{Key:100}
    fmt.Println(tree)
    tree.Insert(50)
    tree.Insert(150)
    fmt.Println(tree)
    fmt.Println(tree.Search(100))
    
    
}