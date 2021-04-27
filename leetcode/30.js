/**
 * Created by fgh on 2019/2/19
 */


/**
 * https://leetcode-cn.com/problems/product-of-array-except-self/
 * 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

 示例:
 输入: [1,2,3,4]
 输出: [24,12,8,6]
 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
 * @param arr
 */
function productExceptSelf(arr){
    if( !arr || !arr.length ){
        throw new Error('invalid input')
    }
    const result = new Array(arr.length)
    result[ 0 ] = 1
    for( let i = 1; i < arr.length; i++ ){
        result[ i ] = result[ i - 1 ] * arr[ i - 1 ]
    }
    let prod = 1
    for( let i = arr.length - 2; i >= 0; i-- ){
        prod *= arr[ i + 1 ]
        result[ i ] *= prod
    }
    return result
}

// ====== test ===========
console.log(productExceptSelf([ 1, 2, 3, 4 ]))