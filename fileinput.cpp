#include<iostream>
#include<fstream>
using namespace std;
int main(){


    ifstream fin;
    char ch;
    fin.open("hello_abc.txt");
    
    // fin>>ch;
    ch=fin.get();
    while(!fin.eof()){

     cout<<ch;
    //  fin>>ch;//space not included
    ch=fin.get();//space included

    }
    fin.close();
    return 0; 
}