#include<iostream>
using namespace std;
void isPrime(int x){
    if(x==1){
        cout<<"not prime"<<endl;
        return;
    }
    if(x==2){
        cout<<"Prime"<<endl;
        return;
    }
    for(int i=2;i*i<=x;i++){
        if(x%i==0){
            cout<<"Not Prime";
            return;
        }
    
    }
    cout<<"Prime"<<endl;
}
int main(){
    int num;
    cout<<"Enter a number:"<<endl;
    cin>>num;
    isPrime(num);

    return 0;
}