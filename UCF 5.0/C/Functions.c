#include<stdio.h>
// void add(void);
int main(){
    void add(void);//funtion prototype or function declaration here it is local declaration
    add();//Function Call
}
void add()//Function Definition
{   int a , b;
    printf("Enter 2 numbers: ");
    scanf("%d %d",&a,&b);
    printf("Addition is :%d",a+b);
}