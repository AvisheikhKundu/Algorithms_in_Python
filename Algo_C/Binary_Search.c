#include<stdio.h>
int main(){
    int arr[]={1,2,3,4,5,6,7,8};
    int number;
    scanf("%d",&number);
    int start=0;
    
    int end=sizeof(arr)/sizeof(int);
    int mid=start+(end-start)/2;
    while (start<=end){
        if (arr[mid]==number){
            printf("Found at nidex  %d\n",mid);
            return 0;
        }
        else if (arr[mid]>number){
            end=mid-1;
        }
        else {
            start=mid+1;
        }
        
        
    }
    printf("Not found\n");
    return 1;
}