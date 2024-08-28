import "strconv"

func isDigit(c byte) bool {
    return c >= 48 && c <= 57
}

func validWordAbbreviation(word string, abbr string) bool {
    i, j := 0, 0
    m, n := len(word), len(abbr)
    for i < m && j < n {
        if word[i] == abbr[j] {
            i++
            j++
        } else if abbr[j] == '0' {
            return false
        } else if isDigit(abbr[j]) {
            k := j
            for k < n && isDigit(abbr[k]) {
                k++
            }
            numlen, _ := strconv.Atoi(abbr[j:k])
            i += numlen
            j = k
        } else {
            return false
        }
    }
    return i == m && j == n
}
