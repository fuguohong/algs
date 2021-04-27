/**
 * Created by fgh on 2019/2/16
 */


/**
 * p249
 * 逆序对
 * 实际上就是归并排序，找到数组中顺序不对的数量
 */
function inverserCount(arr){
    if( !arr || !arr.length ){
        return 0
    }
    // 辅助数组
    const aux = new Array(arr.length)
    return _(arr, aux, 0, arr.length - 1)
}

function _(src, aux, start, end){
    if( start === end ){
        aux[ start ] = src[ start ]
        return 0
    }
    // 将数组分成两半，对应的长度。
    const len = (end - start) >> 1
    const leftCount = _(src, aux, start, start + len)
    const rightCount = _(src, aux, start + len + 1, end)
    // 子数组递归完成，此时左右两边都是有序的
    for( let k = start; k <= end; k++ ){
        aux[ k ] = src[ k ]
    }
    //  第一个数组的末尾
    let i = start + len
    // 第二个数组的末尾
    let j = end
    // 当前复制位置,从后往前
    let copyI = end
    // 找到的逆序对数量
    let count = 0
    while( i >= start && j >= start + len + 1 ){
        // 前面的比后面的大，发现逆序对
        if( aux[ i ] > aux[ j ] ){
            src[ copyI-- ] = aux[ i-- ]
            // 子数组有序，j和j前面的都比i小。
            count += j - start - len
        }else{
            // j往前移动，查找是否有比当前i小的
            src[ copyI-- ] = aux[ j-- ]
        }
    }
    // j 或者 i找完，两个while最多只会执行一个，将剩余的部分复制到辅助数组中
    while( i >= start ){
        src[ copyI-- ] = aux[ i-- ]
    }
    while( j >= start + len + 1 ){
        src[ copyI-- ] = aux[ j-- ]
    }
    return leftCount + rightCount + count
}

// ============ test =============
const arr = [ 3,2,1 ]
console.log(inverserCount(arr))