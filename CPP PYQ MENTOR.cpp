/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>

using namespace std;
class Test{
    public:
    int a;int *p;
    Test(int x){
        a=x;
        p=new int[a];
    }
    
    Test(Test &t){
        a=t.a;
        p=t.p;//shallow copy->copy all the member of that object as it is
        // p=new int[a];//Deep copy
       for (int i = 0; i < a; i++) {
            p[i] = t.p[i];}
    }
    
};
class Your;//forward declaration
class My{
    private: int a=10;
    friend Your;//friend class
};
class Your{
    public:
    My m;
    void fun(){
        cout<<m.a;
    }
};


int main()
{
    // Test t(5);
    // for (int i = 0; i < 5; i++) {
    //     t.p[i] = i ;
    // }
    // Test t2=t;
    // cout<<t2.p[1];
    Your y;
    y.fun();

    return 0;
}