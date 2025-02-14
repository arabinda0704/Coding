#include <iostream>
using namespace std;

int main()
{   int n=3;
    // cout<<"Hello World";
    for(int i=0;i<n;i++){
        for(char j=65;j<65+n;j++){
            cout<<j<<" ";
        }
        cout<<endl;
    }
    cout<<endl;

    int x=1;
    for(int i=0;i<n;i++){   
        
        for(int j=0;j<n;j++){
            cout<<x<<" ";
            x++;
        }
        cout<<endl;
    }
    cout<<endl;




    for(int i=0;i<n;i++){   
        
        for(int j=0;j<i+1;j++){
            
                cout<<"*";
            
        }
        cout<<endl;
    }
    cout<<endl;
     for(int i=1;i<=n;i++){   
        
        for(int j=1;j<=i;j++){
            cout<<i;
            
        }
        cout<<endl;
    }
    cout<<endl;
     for(int i=1;i<=n;i++){   
        int num=1;
        for(int j=1;j<=i;j++){
            cout<<num;
            num++;
            
        }
        cout<<endl;
    }
    cout<<endl;

    //Floyd's Triangle
    int num=1;
     for(int i=1;i<=n;i++){   
        
        for(int j=1;j<=i;j++){
            cout<<num;
            num++;
            
        }
        cout<<endl;
    }
    return 0;
}