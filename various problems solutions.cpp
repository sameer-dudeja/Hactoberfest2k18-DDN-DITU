#include<iostream>
using namespace std;
int main() {
	int n,no,r;

	cin>>n;
	for(int i=1;i<=n;i++){
    cin>>no;
     int s=0;
     int p=1;

    while(no>0)
        {

        r = no%10;
		s = s+r*p;
		p = p*2;
		no = no/10;
     }

cout<<s<<endl;
}


	return 0;
}
/*
for pattern
    1
    2 3
    4 5 6
    int i,j,n ;
    int val=1;
    cout<<"number";
    cin>>n;
    for (i=1;i<=n;i++){
        for(j=1;j<=i;j++){
            cout<<val;
            val=val+1;
            }
            cout<<endl;
        }
        for 123=1+2+3
        int n;
    cout<<"number";
    cin>>n;
    int r,s=0;
    while(n!=0){
        r=n%10;
        s=s+r;
        n=n/10;
    }
    cout<<"sum is"<<s;

    for pattern
        1
        11
        111
        1001

        int i,j,n ;

    cout<<"number";
    cin>>n;
    for (i=1;i<=n;i++){
                        if(i%2!=0)
                        {
                              for(j=1;j<=i;j++)
                                {
                              cout<<1;
                                }

                        }
                        else
                        {
                        cout<<1;
                        for(j=1;j<=i-2;j++)
                         {
                        cout<<0;
                         }
                        cout<<1;

                        }
                         cout<<endl;

                    }

decimal to binary
int n ,r;
    int p=1;
    int s=0;
    cout<<"number";
    cin>>n;
    while(n!=0)
    {
        r=n%10;
        s=s+p*r;
        p=p*2;
        n=n/10;
    }
    cout<<s;
for pattern
  1
 232
34543

 int i ,j ,k, l;
    int n;


    cout<<"number"<<endl;
    cin>>n;
    for(i=1;i<=n;i++){
        for(j=1;j<=n-i;j++){
            cout<<" ";
        }
        int val=i;
        for(k=1;k<=i;k++){
                cout<<val;
               val++;

        }
        val=val-2;
        for(l=1;l<=i-1;l++){
            cout<<val;
            val--;
        }
        cout<<endl;
    }

*/
