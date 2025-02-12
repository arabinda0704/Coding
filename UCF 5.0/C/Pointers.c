#include<stdio.h>
void swap(int *, int *);
int main(){
    // int x=90;
    // int *j =&x;
    // printf("%d\n",x);
    // printf("%p\n",&x);
    // printf("%d\n",*(&x));
    // printf("%d\n",*j);
    // printf("%p\n",j);

    // int a, b, *p, *q;
    // p = &a;
    // q = &b;
    // printf("Address of a = %p\n", (void*)&a); // Correct: Using %p for pointer
    // printf("Address of b = %p\n", (void*)q);


    // printf("Pointer difference: %td\n", q - p); // Correct format specifier

    //Call by reference , In c call by reference and call by address are the same thing but in c++ both are different
    
    // int a,b;
    // a=10;
    // b=20;
    // swap(&a,&b);
    // printf("a=%d b=%d",a,b);
    // return 0;

    int i,a[5],*p;
    p=&a[0];
    for(i=0;i<5;i++){
        printf("Enter the value at %d ", i);
        // scanf("%d",&a[i]);
        scanf("%d",p+i);
    }
    for(i=0;i<5;i++){
        // printf("value at %d is %d\n", i,a[i]);
        printf("value at %d is %d\n", i,*(p+i));
       
    }
    

}
void swap(int *x,int *y){
    int t;
    t=*x;
    *x=*y;
    *y=t;
}