/**
 * Created by fgh on 2019/2/19
 */


/**
 * p310
 * 不使用+ - * / 运算符的加法
 */
function add(num1, num2){
    let carry = 1
    let sum = 0
    while( carry ){
        sum = num1 ^ num2
        carry = (num1 & num2) << 1
        num1 = sum
        num2 = carry
    }
    return sum
}


// ======  test ==========
console.log(add(10 ,21))