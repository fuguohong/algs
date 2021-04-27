/**
 * Created by fgh on 2019/2/18
 */


/**
 * p282
 * 和为s的连续正数序列。
 * 例：输入15； 由于 1+2+3+4+5=4+5+6=7+8=15； 所以输出三个序列1-5,4-6,7-8
 */
function sequence(num){
    let half = num / 2 + 1
    const reslut = []
    const current = []
    let sum = 0
    for( let i = 1; i < half; i++ ){
        sum += i
        current.push(i)
        while( sum > num ){
            sum -= current.shift()
        }
        if( sum === num ){
            reslut.push(Array.from(current))
        }
    }
    return reslut
}

// ========= test =======
console.log(sequence(7))