#include<stdio.h>

int main(){
    // printf("\033[13;40H");  // Moves the cursor to column 40, row 13
    // printf("Hello World from Arabinda");
    // int x;
    // printf("Enter a number:");
    //Unary Operator
    int x,y,p,q;
    int a=5;
    int b=5;
    int c=5;
    int d=5;
    x=++a;
    y=b++;
    p=--c;
    q=d--;
    printf("\n%d\n%d\n%d\n%d\n",x,y,p,q);

    int z= sizeof(int);
    printf("%d",z);
    


}