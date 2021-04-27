/**
 * Created by fgh on 2018/11/19
 */

/**
 * p100
 * 输入一个整数，输出其二进制（此处其实应该是补码）表示中含有多少个1
 */
function countOf1(number){
    let count = 0
    let flage = 1
    while( flage ){
        if( flage & number ){
            count++
        }
        flage = flage << 1
    }
    return count
}

function countOf12(number){
    let count = 0
    while( number ){
        count++
        number = number & (number - 1)
    }
    return count
}


/**
 * 一条语句判断一个整数是不是2的整数次方
 */
const n = 67
console.log((n & (n - 1)) === 0)