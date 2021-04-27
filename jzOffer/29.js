/**
 * Created by fgh on 2019/2/18
 */


/**
 * p275
 * 一个数组中有两个数字只出现了一次，其他的数都出现了两次。找到这两个数
 * 要求时间复杂度 O(n) 空间复杂度O(1)
 * 将全部数字异或一次，得到的结果是只出现一次的两个数异或的结果。找到异或结果中第一个bit位为1的位置。根据这个位置是1或0将数组分成
 * 两部分。这样只出现一次的两个数就被分到了两个不同的数组中。分别对这两个数组异或即可
 */
function onceNum(arr){
    let firstResult = 0
    for( let i = 0; i < arr.length; i++ ){
        firstResult ^= arr[ i ]
    }
    const bitIndex = firstBitOne(firstResult)
    const arr1 = []
    const arr2 = []
    for( let i = 0; i < arr.length; i++ ){
        if( isBitOne(arr[ i ], bitIndex) ){
            arr1.push(arr[ i ])
        }else{
            arr2.push(arr[ i ])
        }
    }
    let num1 = 0
    for( let i = 0; i < arr1.length; i++ ){
        num1 ^= arr1[ i ]
    }
    let num2 = 0
    for( let i = 0; i < arr2.length; i++ ){
        num2 ^= arr2[ i ]
    }
    return [ num1, num2 ]
}

// 数字中第一个为1的比特位
function firstBitOne(num){
    let index = 0
    while( (num & 1) === 0 ){
        num = num >> 1
        index++
    }
    return index
}

// num的二进制表示中，bitIndex位是否为1
function isBitOne(num, bitIndex){
    num = num >> bitIndex
    return (num & 1) === 1
}

// =========== test ================
const arr = [6,4,9,2,9,3,2,4]
console.log(onceNum(arr))