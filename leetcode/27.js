/**
 * Created by  on 2018/11/23.
 */
'use strict'

/**
 * https://leetcode-cn.com/explore/interview/card/tencent/227/hui-su-suan-fa/935/
 * 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
 例如，给出 n = 3，生成结果为：
 [
 "((()))",
 "(()())",
 "(())()",
 "()(())",
 "()()()"
 ]
 */
function generateParenthesis(n){
    if( n < 1 ) return ''
    const result = []
    gener('', n, 0, 0, result)
    return result
}

function gener(s, n, left, right, result){
    if( s.length === n * 2 ){
        return result.push(s)
    }
    if( left < n ){
        gener(s + '(', n, left + 1, right, result)
    }
    if( right < left ){
        gener(s + ')', n, left, right + 1, result)
    }
}

console.log([1,2,3].splice(0,0))