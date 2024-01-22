#include<iostream>
#include<fstream>
using namespace std;
int main(){


    ofstream fout;
    fout.open("hello_abcd.txt");
    fout<<"hello from helloabcd.txt";
    fout.close();
    return 0; 
}