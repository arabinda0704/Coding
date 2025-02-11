#include<stdio.h>
#include<stdlib.h>

int main(){
    // int x,y,z;
    // printf("Enter a number: ");
    

    // scanf("%d",&x);

    // x>0?printf("%d is positive", x):printf("%d is not positive", x);//Conditional operator or Ternary operato
    // printf("\nEnter two number: ");
    // scanf("%d %d",&y,&z);
    // // max=y>z?y:z;
    // printf("greater number is %d",y>z?y:z);


    int choice,a,b,s;
    

    while(1){
    
    printf("\n1.Addition");
    printf("\n2.Even or odd");
    printf("\n3.Print first n natural number");
    printf("\n4.Exit");
    printf("\nEnter your choice:\n");
    scanf("%d",&choice);
    
    switch(choice)
    {
        case 1:
            printf("\nEnter two numbers:");
            scanf("%d %d",&a,&b);
            printf("\nsum is %d",a+b);
            break;
        case 2:
            printf("\nEnter a number:");
            scanf("%d",&a);
            a%2==0?printf("\neven"):printf("\nodd");
            break;
        case 3:
            printf("\nEnter the  number: ");
            scanf("%d",&s);
            
            for(int b=1;b<=s;b++){
                printf("%d\t",b);
            }
            break;
        case 4:
            exit(0);
        default:
            printf("\nInvalid Choice");
    }
    }

}