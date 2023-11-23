#include<stdio.h>
int main(){
    int arr[]={1,2,3,4,5,6};
    int n=sizeof(arr)/sizeof(int);
    int a[n];
    int j=n-1;
    for (int i=0;i<sizeof(arr)/sizeof(int);i++){
        a[j]=arr[i];
        j--;
    }
    for (int i=0;i<n;i++){
        printf("%d\t",a[i]);
    }

    return 0;
}