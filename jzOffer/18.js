/**
 * Created by fgh on 2019/2/14
 */


/**
 * p197
 * 求集合的所有排列。
 * 递归的将当前元素和后续所有元素交换位置
 * @param arr
 */
function arranges(arr){
    if( !arr || !arr.length ) return
    const result = []
    _arranges(arr, 0, result)
    return result
}

function _arranges(order, current, result){
    if( current === order.length ){
        result.push(Array.from(order))
        return
    }
    for( let i = current; i < order.length; i++ ){
        _switch(order, current, i)
        _arranges(order, current + 1, result)
        _switch(order, current, i)
    }
}

function _switch(arr, i, j){
    const temp = arr[ i ]
    arr[ i ] = arr[ j ]
    arr[ j ] = temp
}

// =============== test ==================
const arr = [ 1, 2, 3 ]
console.log(arranges(arr))