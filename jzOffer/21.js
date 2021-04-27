/**
 * Created by fgh on 2019/2/14
 */


/**
 * p208
 * 数组中某个数出现的次数超过了数组的一半，找出它。
 * 可以用快排的切分来实现
 * 有一种不需要修改数组的方法，比快排切分更快。
 * 保存一个次数，出现相同的数字就加一，不同就减一。如果为0，则保存该数并把次数置为1，最后把次数置为1的数就是要找的数
 * @param arr
 */
function moreThanHalf(arr){
    let times = 0
    let result = null
    const half = arr.length >> 1
    for( let i = 0; i < arr.length; i++ ){
        if( times === 0 ){
            result = arr[ i ]
            times = 1
        }else if( arr[ i ] === result ){
            times++
            if( times > half ){
                break
            }
        }else{
            times--
        }
    }
    return result
}

// =========== test ================
const arr = [ 1, 2, 5, 2, 5, 5, 3,2, 4, 2, 2, 5, 2, 2, 2 ]
console.log(moreThanHalf(arr))