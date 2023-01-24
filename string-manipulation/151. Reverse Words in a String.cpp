class Solution {
public:
    string reverseWords(string s) {
        reverse(s.begin(), s.end());
        int n = s.size();
        int writep = 0;
        int ws = 0;
        while (ws < n) {
            if (s[ws] != ' ') {
                // 为上个单词末尾添加空格
                if (writep > 0) s[writep++] = ' ';
                int we = ws;
                // 写入当前单词，然后再反转回正序
                while (we < n && s[we] != ' ') s[writep++] = s[we++];
                reverse(s.begin()+writep-(we-ws), s.begin()+writep);
                ws = we;
            }
            ws++;
        }
        return s;
    }
};
