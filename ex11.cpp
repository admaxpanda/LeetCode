#include <iostream>
#include <cstdio>
using namespace std;
int n,m;
int server[5005][5005];
int relyon[5005];
int relyed[5005];
int vis[5005];
int cannot=0;
void dfs(int now){
    for(int i=0;i<relyon[now];i++){
        if(cannot)
            return;
        if(vis[server[now][i]]){
            can2not=1;
            return;
        }
        vis[server[now][i]]=1;
        relyed[server[now][i]]++;
        dfs(server[now][i]);
        vis[server[now][i]]=0;
    }
}
int main(){
    cin>>n>>m;
    for(int i=0;i<n;i++){
        cin>>relyon[i];
        for(int k=0;k<relyon[i];k++)
            scanf(",%d",&(server[i][k]));
    }
    if(relyon[m]==0){
        cout<<"null";
        return 0;
    }
    dfs(m);
    if(cannot){
        cout<<"-1";
        return 0;
    }
    int first=1;
    for(int i=0;i<n;i++)
    {
        if(relyed[i]){
            if(first){
                first=0;
                cout<<i;
            }
            else {
                cout<<","<<i;
            }
        }
    }
}