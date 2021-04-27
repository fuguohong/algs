/**
 * Created by fgh on 2019/2/15
 */


/*
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
 */
function lengthOfLongestSubstring(str){
    const charIndex = new Map()
    let sublen = 0
    let start = 0
    for( let i = 0; i < str.length; i++ ){
        let ci = charIndex.get(str[ i ])
        if( ci !== undefined ){
            start = Math.max(ci, start)
        }
        if(i-start > sublen){
            sublen = i-start
        }
        // sublen = Math.max(i - start + 1, sublen)
        charIndex.set(str[ i ], i )
    }
    return sublen
}

const s = 'qqfaa'
console.log(lengthOfLongestSubstring(s))