#include<stdio.h>
struct date{
    int d, m, y;
}d2,d3;
struct date d1;
int main()
{
    struct date today={12,2,2025};
    struct date tomorrow;
    tomorrow.d=13;
    tomorrow.m=2;
    tomorrow.y=2025;
    printf("%d",today.d);
}