/*find the smallest positive number missing from the array*/

#include<iostream>
using namespace std;
typedef long int li;
typedef long long int ll;
int main()
 {

	    li n;
            cin>>n;
	    ll a[n],max=0;
	    for(li i=0;i<n;i++){
	        cin>>a[i];
	        if(a[i]>max){
	            max=a[i];
	        }
	    }
	    ll b[max+1]={0};
	    for(ll i=0;i<n;i++){
	        if(a[i]>0){
	            b[a[i]]++;
	        }
	    }
	    int c=0;
	    for(ll i=1;i<max;i++){
	        if(b[i]<1){
	            cout<<i<<"\n";
	            c++;
	            break;
	        }
	    }
	    if(c==0){
	        cout<<max+1<<"\n";
	    }

	return 0;
}
