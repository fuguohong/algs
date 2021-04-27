/**
 * Created by  on 2018/11/21.
 */

/**
 * https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/901/
 * 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
 有效字符串需满足：
 左括号必须用相同类型的右括号闭合。
 左括号必须以正确的顺序闭合。
 注意空字符串可被认为是有效字符串。
 */
function validBracket(s){
    if( s.length === 0 ){
        return true
    }
    const match = new Map()
    match.set(')', '(')
    match.set(']', '[')
    match.set('}', '{')
    const stack = []
    for( let i = 0; i < s.length; i++ ){
        if( match.has(s[ i ]) ){
            if( stack[ stack.length - 1 ] !== match.get(s[ i ]) ){
                return false
            }
            stack.pop()
        }else{
            stack.push(s[ i ])
        }
    }
    return stack.length === 0
}
