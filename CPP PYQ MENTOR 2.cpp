/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include<string>
using namespace std;

    

void f(int &x){
    
    x=x+10;
    cout<<x<<endl;
}

class A { 
private: 
    int f1(){return 1;} 
  
protected: 
    int f2(){return 2;}
  
public: 
    int f3(){return 3;} 
  
   
}; 
  
class B : A {
private:
    int f4() { return 4; }

protected:
    int f5() { return 5; }

public:
    
   virtual void f6() { cout<<"6 from B"; }
};

class C : public B {
    
public:
// void f6() { cout<<"6 from c"; }

 void f7(){
    cout<< f5();
 }


};
class A1{
    public:
     virtual void f1(){
         cout<<"f1 of A";
     }
};
class B1 : public A1{
    public:
     void f1(int x){
         cout<<"f1 of B";
     }
};
int main()
{
    A1 *p=new B1;
    p->f1();
    
    
    // B o2; 

    //   cout<<o2.f6() ;
    // C o3;
    //   o3.f6();
    
    // B *o2= new C;
    // o2->f6();
    // string s;
    // getline(cin,s);//for string class
    // cin.getline(s,50);//not for string only for character array of string
    // char s[50];
    // char s[20],s1[20];
    // cout<<"enter a string  ";
    // cin>>s;
    // cin.getline(s,50);
    // getline(cin,s);//not for character array of string
    // cin.get(s,50);
    // cout<<s;
    // int a=10;
    // cout<<a<<endl;
    // f(a);
    // cout<<a;
    
    // int n=10;
    // void *p=&n;
    // cout<<*(int*)p;
    
//   void *ptr;   // void pointer declaration  
//   int a=9;   // integer variable initialization  
//   ptr=&a;   // storing the address of 'a' variable in a void pointer variable.  
//   cout << &a << endl;  
//   cout <<*(int*) ptr <<endl; 
    //  char a[] = "123456";
    // //  int x=(int)a;
    // int val=atoi(a);
    // //  x=x+3;
    //  val+=3;
    //  cout<<val;
    return 0;
}
