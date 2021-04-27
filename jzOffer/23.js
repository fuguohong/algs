/**
 * Created by fgh on 2019/2/15
 */


/**
 * p218
 * 找出一个数组中，连续数和的最大值
 * 如 {1,-2,3,5,-1,4} 的最大和为3+5+-1+4 = 11
 * sum(i) = max( 0,arr[i], sum(i-1)+arr[i] ),时间复杂度O(n)
 */
function greatestSum(arr){
    if( !arr || !arr.length ) return 0
    let maxSum = 0
    let currentSum = 0
    for( let i = 0; i < arr.length; i++ ){
        if( currentSum < 0 ){
            currentSum = arr[ i ]
        }else{
            currentSum += arr[ i ]
        }
        maxSum = maxSum > currentSum ? maxSum : currentSum
    }
    return maxSum
}

// =========== test ===============
const arr = [ 1, -2, 3, 5, -1, 4 ]
const arr2 = [ 1, -2, 3, 10, -4, 7, 2, -5 ]
const arr3 = [ -5, -8, 1, -3, -9 ]

console.log(greatestSum(arr))
console.log(greatestSum(arr2))
console.log(greatestSum(arr3))