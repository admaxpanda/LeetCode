#include <iostream>
using namespace std;
int m,n;
int mx,my;
int zx,zy;
int n_mount;
int x_mount,y_mount;
int main(){
    cin>>m>>n;
    cin>>mx>>my;
    cin>>zx>>zy;
    cin>>n_mount;
    cin>>x_mount>>y_mount;
    m=m-mx-(m-1-zx);
    n=n-my-(n-1-zy);
    x_mount=x_mount-mx;
    y_mount=y_mount-my;
    int **dp = new int*[m];
    for(int i=0;i<n;i++)
    {
        dp[i]=new int[n];
    }
    for(int i=0;i<m;i++)
    {
        dp[i][0]=1;
    }
    for(int i=0;i<n;i++)
    {
        dp[i][0]=1;
    }

    for(int i=1;i<m;i++)
    {
        for(int j=1;j<n;j++)
        {
            if( i==x_mount&& j==y_mount )
                dp[i][j]=0;
        }
    }
    for(int i=1;i<m;i++)
    {
        for(int j=1;j<n;j++)
        {
            if( i!=x_mount&& j!=y_mount )
                dp[i][j]=dp[i][j-1]+dp[i-1][j];
        }
    }
    cout << dp[m-1][n-1]<<" "<<m+n-2;
}

//mx=0;
//my=0;


