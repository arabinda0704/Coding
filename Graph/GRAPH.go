package main

import "fmt"

// Graph represents adjacency list Graph
type Graph struct {
	vertices []*Vertex
}

// Vertex represents graph vertex
type Vertex struct {
	key      int
	adjacent []*Vertex
}

// Add vertex-->adds a vertex to the graph
func (g *Graph) AddVertex(k int) {
	g.vertices = append(g.vertices, &Vertex{key: k})

}

//Add edge

//get Vertex
// Contains
// Print
// func (g *Graph) Print(){
// 	for _,v:=g.vertices{
// 		fmt.Println(v)
// 	}

// }
func main() {

	test := &Graph{}
	for i := 0; i < 6; i++ {
		test.AddVertex(i)
	}
	fmt.Println(test)
}
