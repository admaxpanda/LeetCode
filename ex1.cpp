#include <iostream>
#include <queue>
using namespace std;
struct Pos{
    int x;
    int y;
    int depth=0;
};
queue<Pos> q;
int n,m;
int map[5000][5000];
Pos startpos,endpos;
int poolnum;
int mindis=1e9;
int cnt=0;
int main(){

    cin>>n>>m;
    cin>>startpos.x>>startpos.y>>endpos.x>>endpos.y;
    cin>>poolnum;
    for(int i=0;i<poolnum;i++){
        int x,y;
        cin>>x>>y;
        map[x][y]=1;
    }
    q.push(startpos);
    while(!q.empty()){
        Pos pos=q.front();
        q.pop();
        //cout<<mindis<<endl;
        // for(int i=0;i<pos.depth;i++)
        //     cout<<' ';
        // cout<<pos.x<<" "<<pos.y<<endl;
        //cout<<pos.x<<" "<<pos.y<<endl;
        if(pos.depth>mindis)
            continue;
        if(pos.x==endpos.x&&pos.y==endpos.y){
            mindis=pos.depth;
            cnt++;
            // for(int i=0;i<pos.depth;i++)
            //     cout<<' ';
            // cout<<"BACK"<<endl;
            continue;
        }
        if(pos.x>0){
            if(map[pos.x-1][pos.y]==0){
                Pos p;
                p.x=pos.x-1;
                p.y=pos.y;
                p.depth=pos.depth+1;
                q.push(p);
            }
        }
        if(pos.x<n-1){
            if(map[pos.x+1][pos.y]==0){
                Pos p;
                p.x=pos.x+1;
                p.y=pos.y;
                p.depth=pos.depth+1;
                q.push(p);
            }
        }
        if(pos.y>0){
            if(map[pos.x][pos.y-1]==0){
                Pos p;
                p.x=pos.x;
                p.y=pos.y-1;
                p.depth=pos.depth+1;
                q.push(p);
            }
        }
        if(pos.y<m-1){
            if(map[pos.x][pos.y+1]==0){
                Pos p;
                p.x=pos.x;
                p.y=pos.y+1;
                p.depth=pos.depth+1;
                q.push(p);
            }
        }
    }
    cout<<cnt<<" "<<mindis;
    return 0;
}