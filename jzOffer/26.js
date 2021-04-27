/**
 * Created by fgh on 2019/2/17
 */


/**
 * p266
 * 长度为n-1的数组中所有数字唯一并且都在0~n-1中，求0~n-1中缺失的那个数
 * 利用二分法找到第一个数字和脚标不同的数即可。 时间复杂度O(logn)
 * @param arr
 * @returns {number}
 */
function missNum(arr){
    if( !arr || !arr.length ){
        return -1
    }
    let left = 0
    let right = arr.length - 1
    while( left <= right ){
        let mid = (right + left) >> 1
        if( arr[ mid ] === mid ){
            left = mid + 1
        }else{
            if( mid === 0 || arr[ mid - 1 ] === mid - 1 ){
                return mid
            }else{
                right = mid - 1
            }
        }
    }
    return -1
}

// =============== test ================
const arr = [ 0, 1, 3, 4, 5, 6 ]
console.log(missNum(arr))