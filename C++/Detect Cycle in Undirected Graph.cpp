//Detect Cycle in Undirected Graph
//T.C.=O(v+E)
#include<bits/stdc++.h>
using namespace std;

void add_edge(vector<int> adj[], int u, int v){
    adj[u].push_back(v);
    adj[v].push_back(u);

}

bool DFSrec(vector<int>adj[], int s, bool visited[], int parent){ 
    visited[s]=1;
    for(auto u:adj[s]){
        if(!visited[u]){
            if(DFSrec(adj,u,visited,s)){
                return true;
            }
        }
        else if(u!=parent){
            return true;
        }
    }
    return false;
}

bool DFS(vector<int>adj[], int v){ 
    bool visited[v];
    for(int i=0;i<v;i++){
        visited[i]=0;
    }
    for(int i=0;i<v;i++){
        if(!visited[i]){
            if(DFSrec(adj,i,visited,i)){
                return true;
            }
        }
    }
    return false;
}

int main(){
    vector<int> adj[5];
    add_edge(adj,0,1);
    add_edge(adj,0,2);
    add_edge(adj,1,3);
    add_edge(adj,2,3);
    add_edge(adj,1,4);
    add_edge(adj,3,4);
    cout<<DFS(adj,5)<<endl;
    return 0;
}