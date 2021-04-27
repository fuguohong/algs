/**
 * Created by fgh on 2018/11/16.
 */

/**
 https://leetcode-cn.com/explore/orignial/card/all-about-lockup-table/236/learn-to-use-set/980/
 编写一个算法来判断一个数是不是“快乐数”。
 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

 示例:
 输入: 19
 输出: true
 解释:
 12 + 92 = 82
 82 + 22 = 68
 62 + 82 = 100
 12 + 02 + 02 = 1
 */
function isHappy(n){
    const nums = new Set()
    while( true ){
        let sum = 0
        while( n !== 0 ){
            let x = n % 10
            sum += x * x
            n = parseInt(n / 10)
        }
        if( nums.has(sum) ){
            return false
        }
        if( sum === 1 ){
            return true
        }
        nums.add(sum)
        n = sum
    }
};

function getUnit(n){
    const units = []
    let div = 10
    while( true ){
        let remainder = n % div
        units.push(parseInt((remainder * 10) / div))
        if( remainder === n ){
            break
        }
        div *= 10
    }
    return units
}

console.log(isHappy(19))