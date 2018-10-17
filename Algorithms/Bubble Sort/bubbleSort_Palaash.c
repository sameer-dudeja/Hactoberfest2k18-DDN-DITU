#include<stdio.h>
//Descending Bubble Sort using C
int main()
{
	int a[20],i,j,size,temp,swap;
	printf("\n Enter Array Size : ");
	scanf("%d",&size);
	printf("\n Enter Array Elements : ");
	for(i=0;i<size;i++)
        scanf("%d",&a[i]);

	//BUBBLE SORT : Descending
	for(i=0;i<size-1;i++){
        swap=0;
        //COMPARE ELEMENTS AND SWAP:
        for(j=0;j<(size-1)-1;j++){
            if(a[j]<a[j+1]){
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
                swap=1;
            }
        }
        if(swap==0){
            break;
        }
	}

	printf("\nArray after sort: ");
	for(i=0;i<size;i++)
        printf("%d",a[i]);

    return 0;
}
