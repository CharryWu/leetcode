#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;
int romanToInt(string s) {
    unordered_map<char, int> m;

    m['I'] = 1;
    m['V'] = 5;
    m['X'] = 10;
    m['L'] = 50;
    m['C'] = 100;
    m['D'] = 500;
    m['M'] = 1000;

    int ans = 0;

    for (int i = 0; i < s.length(); i++) {
        if (m[s[i]] < m[s[i + 1]]) {
            ans -= m[s[i]];
        } else {
            ans += m[s[i]];
        }
    }
    return ans;
}

vector<string> split(string str, char delimiter)
{
  // Using str in a string stream
    stringstream ss(str);
    vector<string> res;
    string token;
    while (getline(ss, token, delimiter)) {
        res.push_back(token);
    }
    return res;
}

bool compare(string n1, string n2) {
    int found1 = n1.find_last_of(' ');
    int found2 = n2.find_last_of(' ');

    int num1 = romanToInt(n1.substr(found1+1));
    int num2 = romanToInt(n2.substr(found2+1));
    string name1 = n1.substr(0, found1);
    string name2 = n2.substr(0, found2);

    if (num1 == num2) {
        return name1.compare(name2) < 0;
    }
    return num1 < num2;
}

std::vector<std::string> sortRegalNames(const std::vector<std::string> &names) {
    vector<string> res(names);
    sort(res.begin(), res.end(), compare);
    return res;
}

int main() {
    vector<string> names;

    names.push_back("Nicholas VIII");
    names.push_back("Hy XXIV");
    names.push_back("Gar Yosef II");
    names.push_back("Gar II");
    names.push_back("Gar Yoseg II");
    names.push_back("Nicholas C");
    names.push_back("Mice XXIV");
    auto res = sortRegalNames(names);
    for (const string& name: res) {

        cout << name << endl;
    }
}
