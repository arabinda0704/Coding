//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    int binary_to_decimal(string str) {
        // Code here.int decimal = 0;
       long long binary = stoll(str);
        long long decimal = 0, w = 1;
       while(binary!=0){
           int rem=binary%10;
           decimal=decimal+w*rem;
           binary=binary/10;
           w=w*2;
           
           
       }
       return decimal;
    }
};

//{ Driver Code Starts.
int main() {
    int T;
    cin >> T;
    while (T--) {
        string str;
        cin >> str;
        Solution ob;
        int ans = ob.binary_to_decimal(str);
        cout << ans << "\n";
    }
    return 0;
}
// } Driver Code Ends