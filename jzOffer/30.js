/**
 * Created by fgh on 2019/2/18
 */


/*
 p278
 数组中除某一个数只出现一次，其他数字都出现了三次，找出只出现一次的数.(int类型)
 解：把数组中每一个数字的二进制表示按位相加。得到的结果中，只出现一次数字二进制为1的位一定是3的倍数+1.为0的地方一定是3的倍数或0
 时间复杂度 O(n) 空间复杂 O(1)
 */
function onceNum(arr){
    if( !arr || arr.length <= 3 ){
        throw new Error('invalid input')
    }
    const aux = new Array(32).fill(0)
    for( let i = 0; i <= arr.length; i++ ){
        for( let j = 0; j < 32; j++ ){
            if( ((arr[ i ] >> j) & 1) === 1 ){
                aux[ j ]++
            }
        }
    }
    let result = 0
    for( let i = 31; i >= 0; i-- ){
        result = result << 1
        if( aux[ i ] % 3 !== 0 ){
            result++
        }
    }
    return result
}

// ======== test ============
const arr = [ -9, -9, -9, 0, -6, -6, -6, -2, -2, -2 ]
console.log(onceNum(arr))