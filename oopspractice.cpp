
#include<iostream>
using namespace std;
class Account{
   private:
    int a,b;
    public:
    Account(int x=0,int y=0){a=x;b=y;}
    inline int area();
    void setData(int , int );
    void getData();
    friend void fun(Account);
    Account operator*(Account &c){
        Account temp;
        temp.a=a*c.a;
        temp.b=b*c.b;
        return temp;
    }
    friend ostream & operator<<(ostream &o,Account &c);
};

ostream & operator<<(ostream &o,Account &c){
    o<<c.a<<"+i"<<c.b;
    return o;
    }

void fun(Account c){
    cout<<c.a+c.b<<endl;
    
}
void Account::setData(int a, int b){this->a=a;this->b=b;}
void Account:: getData(){
    cout<<a<<" "<<b<<endl;
}


int Account::area()
{return a*b;}
// float Account::roi=3.5f;
int main(){
    
    
    Account a1(3,4),a2(5,6);
   Account a3=a1*a2;
    a3.getData();
    fun(a1);
    cout<<a3;
    return 0;
}
