/**
 * Created by fgh on 2019/2/14
 */


/**
 * p210
 * 找到数组中最小的k个数
 * 可以用快排切分的方法解决，时间复杂度O(n)，但是会修改原数组
 * 解法2，不用修改原数组，时间复杂度O(nlogk)
 * 用一个大顶堆（红黑树等logn时间复杂度的容器也行）来保存最小的k个数，依次读取时判断大顶堆最大数是否比当前数大。
 */
function leastNums(arr, k){
    if( !arr || !arr.length || k <= 0 || k > arr.length ){
        throw new Error('invalid param')
    }
    let start = 0
    let end = arr.length - 1
    let index = _partition(arr, start, end)
    while( index !== k  ){
        if( index < k  ){
            start = index + 1
        }else{
            end = index - 1
        }
        index = _partition(arr, start, end)
    }
    return arr.slice(0, index)
}

function _partition(arr, left, right){
    _exchange(arr, left, (left + right) >> 1)
    const sd = arr[ left ]
    let i = left + 1
    let j = right
    while( true ){
        while( arr[ i ] <= sd && i < right ){
            i++
        }
        while( arr[ j ] >= sd && j > left ){
            j--
        }
        if( j <= i ){
            break
        }
        _exchange(arr, i, j)
        i++
        j--
    }
    _exchange(arr, left, j)
    return j
}

function _exchange(arr, i, j){
    const temp = arr[ i ]
    arr[ i ] = arr[ j ]
    arr[ j ] = temp
}

// ============== test =================
const arr = [ 4, 5, 1, 6, 2, 7, 3, 8 ]
console.log(leastNums(arr, 7))