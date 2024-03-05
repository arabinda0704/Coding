package main
import "fmt"




type node struct{
    data int
    next *node
} 


type linkedList struct{
    head *node
}

func (l * linkedList) addBeg(n *node){
    second :=l.head
    l.head=n
    l.head.next=second
}

func (l * linkedList) addNext(n *node){
    current :=l.head
    
    for current.next != nil {
        current = current.next
    }
    current.next=n
    

func (l linkedList) printList() {
    // current := l.head//it is not changing the value it works on the copy so no need of current variable
    
    for l.head != nil {
        fmt.Printf("%d -> ", l.head.data)
        l.head = l.head.next
    }
    fmt.Println("nil")
}

type Stack struct{
    items []int
}

func(s *Stack) push(i int){
    s.items=append(s.items,i)
}

func(s *Stack) pop() {
    l:=len(s.items)-1
    i:=s.items[l]
    // s.items=s.items[:l]
    s.items = append(s.items[:l])
    fmt.Println("popping->",i)
}
//Queue
type Queue struct{
    items []int
}
//Enque
func (q * Queue) enque(i int){
    q.items=append(q.items,i)
}
//Deque
func (q *Queue) deque(){
    l:=q.items[0]
    q.items=q.items[1:]
    fmt.Println("dequed->",l)
}
func main() {
    //linkedlist
    mylist:=linkedList{}
    node1:=&node{data:48}
    node2:=&node{data:47}
    node3:=&node{data:46}
    node4:=&node{data:49}
    node5:=&node{data:50}
    
    mylist.addBeg(node1)
    mylist.addBeg(node2)
    mylist.addBeg(node3)
    mylist.addNext(node4)
    mylist.addNext(node5)
    mylist.printList()
    
    //stack
    st:=Stack{}
    fmt.Println(st)
    st.push(5)
    st.push(6)
    st.push(7)
    st.push(8)
    fmt.Println(st)
    st.pop()
    st.pop()
    st.push(9)
    st.push(10)
    fmt.Println(st)
    
    //Queue
    q:=Queue{}
 
    fmt.Println(q)
    q.enque(5)
    q.enque(6)
    q.enque(7)
    q.enque(8)
   
    fmt.Println(q)
    q.deque()
    fmt.Println(q)
    q.deque()
    q.enque(9)
    q.enque(10)
    fmt.Println(q)

}