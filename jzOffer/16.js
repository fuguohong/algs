/**
 * Created by fgh on 2019/1/28
 */


/**
 * p179
 * 判断一个序列是不是某二叉树后序遍历的结果
 * 后序遍历最后一个值是二叉树根节点，前面的值中，小于它的为其左子树，直到第一个大于它的值及其后面的值都是它的右子树
 * 如果本应是右子树的值中有小于根节点的值，则不可能是二叉树后序遍历结果。
 * 对于左子树和右子树同样如此
 * @param arr
 */
function isBtreePostorder(arr){
    if( !arr ) return false
    return _isBtreePostorder(arr, 0, arr.length - 1)
}

function _isBtreePostorder(arr, start, end){
    if( end - start <= 1 ) return true
    const root = arr[ end ]
    let i = start
    while( i < end && arr[ i ] < root ){
        i++
    }
    const subT = i++
    while( i < end && arr[ i ] > root ){
        i++
    }
    if( i !== end ) return false
    return _isBtreePostorder(arr, start, subT - 1) && _isBtreePostorder(arr, subT, end - 1)
}


// ============= test ==============
const order1 = [ 5, 7, 6, 9, 11, 10, 8 ]
const order2 = [ 7, 4, 6, 5 ]
console.log(isBtreePostorder(order2))