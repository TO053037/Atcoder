#include <iostream>
#include <string>
using namespace std;

int main(){
    string s, t;
    cin >> s;
    cin >> t;
    int ans = 0;
    for (int i = 0; i < 3; i ++){
        if (s[i] == t[i]){
            ans += 1;

        }
    }
    cout << ans << endl;
    
    
}
