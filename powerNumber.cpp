/*Following is the c++ code to calculate N raised to R, where N is number and R is reverse of N*/

#include<cmath>
#include<iostream>
using namespace std;
const long long M = 1e9+7;
long long int p(long long int n,long long int r){
    if(!r)
        return 1;
    long long int t = p(n, r/2);
    if(r%2==1)
        return (n * ((t*t)%M)) %M;
    return (t*t)%M;
}

int main() {

	    long int N=12,sum=0;
	    int l=log10(N);
	    long int x=N;
	    for(int i;x>0;i++){
	        long int temp=0;
	        temp=x%10;
	        x=x/10;
	        sum=sum+temp*pow(10,l--);
	    }
	    cout<<p(N,sum)<<"\n";

	    return 0;
}
