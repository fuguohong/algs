/**
 * Created by fgh on 2019/2/14
 */


/**
 * https://leetcode-cn.com/problems/subsets/
 * 求一个集合的所有子集
 * @param arr
 * @returns {*}
 */
function subsets(arr){
    if( !arr || !arr.length ) return arr
    const result = [ [] ]
    for( let i = 0; i < arr.length; i++ ){
        const reslen = result.length
        for( let j = 0; j < reslen; j++ ){
            const newset = Array.from(result[ j ])
            newset.push(arr[ i ])
            result.push(newset)
        }
    }
    return result
}

// =========== test =============
const arr = [ 1, 2, 3 ]
console.log(subsets(arr))