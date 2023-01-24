/**
    我们不要每次都去一个字符一个字符地比较子串和模式串，而是维护一个滑动窗口，运用滑动哈希算法一边滑动一边计算窗口中字符串的哈希值，拿这个哈希值去和模式串的哈希值比较，这样就可以避免截取子串，从而把匹配算法降低为 O(N)，这就是 Rabin-Karp 指纹字符串查找算法的核心逻辑。

    那你可能会问，刚才我们处理的题目给你输入的只有 AGCT 四种字符，所以可以转化成数字，但面对五花八门的字符串，如何把他们转化成数字计算哈希值呢？其实很简单，字符本质上就是编码，而编码其实就是数字。

    比方说以 ASCII 码为例，ASCII 码其实就是 0~255 这 256 个数字，分别对应所有英文字符和英文符号。那么一个长度为 L 的 ASCII 字符串，我们就可以等价理解成一个 L 位的 256 进制的数字，这个数字就可以唯一标识这个字符串，也就可以作为哈希值。

    有了这个想法，我们就可以直接复制粘贴上一道题的大部分代码，写出 Rabin-Karp 算法的主要逻辑
*/

// 文本串
String txt;
// 模式串
String pat;


// 需要寻找的子串长度为模式串 pat 的长度
int L = pat.length();
// 仅处理 ASCII 码字符串，可以理解为 256 进制的数字
int R = 256;
// 存储 R^(L - 1) 的结果
int RL = (int) Math.pow(R, L - 1);
// 维护滑动窗口中字符串的哈希值
int windowHash = 0;
// 计算模式串的哈希值
long patHash = 0;
for (int i = 0; i < pat.length(); i++) {
    patHash = R * patHash + pat.charAt(i);
}

// 滑动窗口代码框架
int left = 0, right = 0;
while (right < txt.length()) {
    // 扩大窗口，移入字符（在最低位添加数字）
    windowHash = R * windowHash + txt[right];
    right++;

    // 当子串的长度达到要求
    if (right - left == L) {
        // 根据哈希值判断窗口中的子串是否匹配模式串 pat
        if (patHash == windowHash) {
            // 找到模式串
            print("找到模式串，起始索引为", left);
            return left;
        }
        
        // 缩小窗口，移出字符（删除最高位数字）
        windowHash = windowHash - txt[left] * RL;
        left++;
    }
}
// 没有找到模式串
return -1;
