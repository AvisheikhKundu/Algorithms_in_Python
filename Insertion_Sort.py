def insertion_Sort(a):
    for i in range(1,len(a)):
        item=a[i]
        j=i-1
        while(j>=0 and a[j]>item):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=item
    print(a)
a=[11,3,55,45,69,1,125]
insertion_Sort(a)
