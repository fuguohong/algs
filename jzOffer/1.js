/**
 * Created by fgh on 2019/2/26
 */


/**
 p39
 长度为n的数组中所有数字都在0到n-1的范围内，确定数组中是否存在重复的数字
 要求时间复杂度 O(n) 空间复杂度 O(1)

 此算法虽然有双重循环，但是执行时间复杂度为O(n)。每个数字最多经过两次交换就找到了自己的位置。在对应位置的数字不会进入while循环。
 此算法会改变原数组
 */
function repetNum(arr){
    if( !arr || arr.length < 2 ){
        return false
    }
    for( let i = 0; i < arr.length; i++ ){
        while( arr[ i ] !== i ){
            if( arr[ i ] === arr[ arr[ i ] ] ){
                return true
            }
            let temp = arr[ i ]
            arr[ i ] = arr[ temp ]
            arr[ temp ] = temp
        }
    }
    return false
}