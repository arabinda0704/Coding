#include<iostream>
#include<vector>
#include<list>
#include<queue>
#include<map>
#include<set>

using namespace std;
int main() {

    //Vector

    vector<int>vec={1,2,3,4,5};
    vector<int>vec1(3,10);// 3 size vector all of them containing 10--important for dynamic programming tabulation
    vector<int>vec2(vec);
    vec.push_back(2);// inserts data in the last
    vec.push_back(3);//      ,,
    vec.push_back(4);//      ,,
    vec.emplace_back(4);//   ,,

    vec.pop_back();// Deletes data from the back or last

    // vec.push_back(4);

    // cout<<vec.size()<<endl;
    // cout<<vec.capacity()<<endl;

    for (int val: vec){
        cout<<val<<" ";
    }
    cout<<endl;

    for (int val: vec1){
        cout<<val<<" ";
    }

    cout<<endl;for (int val: vec2){
        cout<<val<<" ";
    }
    cout<<endl;

    cout<<"value at idx 2:"<<vec[2]<<endl<<"or value at index 2 is "<<vec.at(2)<<endl;
    cout<<vec.front()<<endl<<vec.back()<<endl;
     
    vec2.erase(vec2.begin()+2);
    cout<<endl;for (int val: vec2){
        cout<<val<<" ";
    }
    cout<<endl;

    vec2.erase(vec2.begin()+1,vec2.begin()+3);
    cout<<endl;for (int val: vec2){
        cout<<val<<" ";
    }
    cout<<endl;
    vec2.insert(vec2.begin()+1,3);
    cout<<endl;for (int val: vec2){
        cout<<val<<" ";
    }
    cout<<endl;
    vec2.clear();
    cout<<endl;for (int val: vec2){
        cout<<val<<" ";
    }
    cout<<endl;
    cout<<"vec2.size:"<<vec2.size()<<endl;
    cout<<"vec2.capacity"<<vec2.capacity()<<endl;
    cout<<"isempty vec:"<<vec.empty()<<" isempty vec1:"<<vec1.empty()<<"isempty vec2:"<<vec2.empty()<<endl;
    
    cout<<"Vec2.begin="<<*(vec2.begin())<<endl;
    cout<<"Vec2.end="<<*(vec2.end())<<endl;

    vector<int>::iterator it;
    for(it=vec.begin();it!=vec.end();it++){
        cout<<*(it)<<" ";
    }
    cout<<endl;
    vector<int>::reverse_iterator it1;
    for(it1=vec.rbegin();it1!=vec.rend();it1++){
        cout<<*(it1)<<" ";
    }
    cout<<endl;

    // vector<int>::iterator it;
    for(auto it=vec.begin();it!=vec.end();it++){
        cout<<*(it)<<" ";
    }
    cout<<endl;
    // vector<int>::reverse_iterator it1;
    for(auto it1=vec.rbegin();it1!=vec.rend();it1++){
        cout<<*(it1)<<" ";
    }
    cout<<endl;


   //List
    list<int> l;
    l.push_back(1);
    l.emplace_back(2);
    l.push_front(3);
    l.emplace_front(4);
    for(int val:l){
        cout<<val<<" ";
    }
    cout<<endl;
    l.pop_back();
    l.pop_front();
    for(int val:l){
        cout<<val<<" ";
    }
    cout<<endl;


    //Pair
    pair<int, int> p={1,5};
    cout<<p.first<<endl;
    cout<<p.second<<endl;
    
    pair<int, string> p1={1,"Arabinda"};
    pair<int, string> p2={2,"Ayra"};

    cout<<p1.first<<" "<<p1.second<< endl;
    cout<<p2.first<<" "<<p2.second<<endl;

    pair<int,pair<char,int>> p3={1,{'A',3}};
    cout<<p3.first<<" "<<p3.second.first<< " "<<p3.second.second<< endl;

    vector<pair<int,int>> vec4={{1,2},{3,4},{4,5},{5,6}};
    vec4.push_back({6,7});//insert
    vec4.emplace_back(7,8);//in-place object create

    // for( pair<int,int> p:vec4){
    //     cout<<p.first<< " "<< p.second<<endl;
    // }
    for( auto p:vec4){
        cout<<p.first<< " "<< p.second<<endl;
    }
    //Piority Queue

    // priority_queue<int> q;//maxheap
    priority_queue<int,vector<int>,greater<int>> q;//Here greater<int> is functor it will make it into minheap

    q.push(2);
    q.emplace(3);
    q.push(4);
    q.push(1);
    while(!q.empty()){
        cout<<q.top()<<endl;
        q.pop();
    }
    //Map
    map<int,string> m;
    m[4]="Arabinda";
    m[2]="Ayra";
    m[2]="Ayra Das";

    m[3]="Ayra";
    m.insert({1,"Rabindranath"});
    m.emplace(5,"Tagore");

    for(auto p:m){//Map prints in ascending order of keys and key is unuique
        cout<<p.first<<" "<<p.second<<endl;
    }
    cout<<endl;

    cout<<m.count(2)<<endl;
    
    m.erase(3);
    for(auto p:m){//Map prints in ascending order of keys and key is unuique
        cout<<p.first<<" "<<p.second<<endl;
    }
    cout<<endl;

    //Set
    set<int> s;
    s.insert(2);
    s.insert(3);
    s.insert(1);
    s.insert(5);

    for(auto i:s){
        cout<<i<<" ";
    }
    cout<<endl;
    cout<<*(s.lower_bound(4))<<endl;//return 4 if available otherwise returns just bigger than 4
    cout<<*(s.upper_bound(3))<<endl;//does not return 3 return just bigger than 3



    return 0;
}