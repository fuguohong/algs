/**
 * Created by  on 2018/11/20.
 */


/**
 * https://leetcode-cn.com/problems/longest-palindromic-substring/
 * 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

 示例 1：
 输入: "babad"
 输出: "bab"
 注意: "aba" 也是一个有效答案。

 示例 2：
 输入: "cbbd"
 输出: "bb"
 */
function longestPalindrome(s){
    if( s.length < 2 ){
        return s
    }
    let lp = ''
    let i = 0
    while( i < s.length - (lp.length / 2) ){
        let j = i
        let k = i + 1
        while( s[ j ] === s[ k ] && k < s.length ) k++
        i = k--
        while( j >= 0 && k < s.length ){
            if( s[ j ] !== s[ k ] ){
                break
            }
            j--
            k++
        }
        lp = lp.length < (k - j - 1) ? s.substring(j + 1, k) : lp
    }
    return lp
}

console.log(longestPalindrome("asasaqwqwqwqw"))