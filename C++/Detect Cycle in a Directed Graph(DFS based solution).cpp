//Detect Cycle in a Directed Graph(DFS based solution)
//T.C.=O(v+E)
#include<bits/stdc++.h>
using namespace std;

void add_edge(vector<int> adj[], int u, int v){
    adj[u].push_back(v);
}

bool detect(vector<int> adj[], bool visited[], bool recur[], int i){
    visited[i]=1;
    recur[i]=1;
    for(auto u:adj[i]){
        if(visited[u]==false && detect(adj,visited,recur,u)){
            return true;
        }
        else if(recur[u]){
            return true;
        }
    }
    recur[i]=0;
    return false;
}

bool DFS(vector<int> adj[], int v){
    bool visited[v], recur[v];
    for(int i=0;i<v;i++){
        visited[i]=0;
    }
    for(int i=0;i<v;i++){
        recur[i]=0;
    }
    for(int i=0;i<v;i++){
        if(!visited[i]){
            if(detect(adj,visited,recur,i)){
                return true;
            }
        }
    }
    return false;
}

int main(){
    vector<int> adj[6];
    add_edge(adj,0,1);    
    add_edge(adj,2,1);    
    add_edge(adj,2,3);    
    add_edge(adj,3,4);    
    add_edge(adj,4,5);    
    add_edge(adj,5,3);  
    cout<<DFS(adj,6)<<endl;  
    return 0;
}