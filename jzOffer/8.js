/**
 * Created by fgh on 2018/11/25
 */

/**
 * p112
 * 此题虽然简单，但是需要注意的细节很多
 */
function power(num, exponent){
    if( num === 0 ) return 0
    const result = __power(num, Math.abs(exponent))
    if( exponent < 0 ) return 1 / result
    return result
}

function __power(num, e){
    if( e === 0 ) return 1
    if( e === 1 ) return num
    // n次方等于两个n/2次方相乘
    let result = __power(num, e >> 1)
    result *= result
    // 如果e是单数，右移之后少了1次，需要多乘一次本身
    if( (e & 1) === 1 ){
        return result * num
    }
    return result
}