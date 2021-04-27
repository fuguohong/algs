/**
 * Created by fgh on 2019/1/19
 */

/**
 * p168
 * pushOder是入栈顺序，判断popOrder是不是一个可能的出栈顺序
 * @param pushOrder
 * @param popOrder
 */
function isPopOrder(pushOrder, popOrder){
    if( !pushOrder.length || pushOrder.length !== popOrder.length ) return false
    let p1 = 0
    let p2 = 0
    const auxStack = []
    while( p1 < pushOrder.length ){
        while( p1 < pushOrder.length ){
            if( pushOrder[ p1 ] === popOrder[ p2 ] ){
                p1++
                p2++
                break
            }else{
                auxStack.push(pushOrder[ p1++ ])
            }
        }
        while( auxStack.length && p2 < popOrder.length && auxStack[ auxStack.length - 1 ] === popOrder[ p2 ] ){
            auxStack.pop()
            p2++
        }
    }
    return p1 === p2
}

console.log(isPopOrder([ 1, 2, 3, 4, 5 ], [5,1,3,2,4]))