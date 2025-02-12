#include<stdio.h>
int main(){
    // int A[3][3],B[3][3],C[3][3],i,j;

    // printf("Enter 9 numbers for first matrix");
    // for(i=0;i<3;i++){
    //     for(j=0;j<3;j++){
    //         scanf("%d",&A[i][j]);
    //     }
    // }

    // printf("Enter 9 numbers for Second matrix");
    // for(i=0;i<3;i++){
    //     for(j=0;j<3;j++){
    //         scanf("%d",&B[i][j]);
    //     }
    // }

    // printf("Addition matrix is\n");
    // for(i=0;i<3;i++){
    //     for(j=0;j<3;j++){
    //        C[i][j]=A[i][j]+B[i][j];
    //        printf("%d ", C[i][j]);
    //     }
    //     printf("\n");
    // }

    //Strings
    // char s[]={'A','Y','R','A','\0'};
    // char s[]="Arabinda Das";

    // for(int i=0;s[i]!='\0';i++){
    //     printf("%c",s[i]);
    // }

    // printf("%s",s);
    char s[30];
    printf("Enter your name: ");
    // scanf("%s",s);   //s=&s[0] it does not take space enter or tab or any other delimeter thats why we use gets() now it is fgets()
    fgets(s, sizeof(s), stdin);
    puts(&s[0]);//same as puts(s)
    




}