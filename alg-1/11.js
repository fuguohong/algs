/**
 * Created by fgh on 2019/2/18
 */


/**
 * https://www.cnblogs.com/lfeng1205/p/5981198.html
 * 01背包问题
 * c[i][m]=max{c[i-1][m-w[i]]+pi , c[i-1][m]}
 * c[i][m] 表示容量为m时，放入前i个物品能得到的最大价值
 * @param values {array} 物品的价值
 * @param volumes {array} 物品的体积
 * @param capacity {number} 背包的容量
 */
function maxPack(values, volumes, capacity){
    if( values.length !== volumes.length ){
        throw new Error('invalid input')
    }
    // 物品数量+1行，多一个0物品
    const table = new Array(values.length + 1)
    for( let i = 0; i < table.length; i++ ){
        table[ i ] = new Array(capacity + 1)
    }
    // 0列全部为0
    for( let i = 0; i < table.length; i++ ){
        table[ i ][ 0 ] = 0
    }
    // 0行全部为0
    for( let i = 0; i < capacity + 1; i++ ){
        table[ 0 ][ i ] = 0
    }
    for( let row = 1; row < table.length; row++ ){
        for( let col = 1; col <= capacity; col++ ){
            // 如果背包的容量可以放下第row个物品
            if( volumes[ row - 1 ] <= col ){
                // 放入当前物品比不放获得的价值更大
                let afterPick = table[ row - 1 ][ col - volumes[ row - 1 ] ] + values[ row - 1 ]
                if( table[ row - 1 ][ col ] < afterPick ){
                    table[ row ][ col ] = afterPick
                }else{
                    // 装后比不装价值下，放弃
                    table[ row ][ col ] = table[ row - 1 ][ col ]
                }
            }else{
                // 装不下，直接等于不装
                table[ row ][ col ] = table[ row - 1 ][ col ]
            }
        }
    }
    return table[ table.length - 1 ][ capacity ]
}

/**
 * 完全背包问题，物品可以被重复选择
 c[i][m]=max{c[i][m-w[i]]+pi , c[i-1][m]}
 c[i][m] 表示容量为m时，放入前i个物品能得到的最大价值
 相较于01背包，由于可以继续放入物品i，状态转移方程 由c[i][m]=max{c[i-1][m-w[i]]+pi , c[i-1][m]}，变为 c[i][m]=max{c[i][m-w[i]]+pi , c[i-1][m]}
 不需要再去考虑c[i][m-w[i]]+pi是不是一个最优状态， 因为 c[i][m-w[i]] >= c[i-1][m-w[i]],所以只考虑 c[i][m-w[i]] 即可
 */
function entirePack(values, volums, capacity){
    if( values.length !== volums.length ){
        throw new Error('invalid input')
    }
    const table = new Array(values.length + 1)
    table[ 0 ] = new Array(capacity + 1).fill(0)
    for( let i = 1; i < table.length; i++ ){
        table[ i ] = new Array(capacity + 1)
    }
    for( let i = 1; i < table.length; i++ ){
        table[ i ][ 0 ] = 0
    }
    for( let row = 1; row < table.length; row++ ){
        for( let col = 1; col <= capacity; col++ ){
            if( volums[ row - 1 ] <= col ){
                let afterPick = table[ row ][ col - volums[ row - 1 ] ] + values[ row - 1 ]
                if( table[ row - 1 ][ col ] < afterPick ){
                    table[ row ][ col ] = afterPick
                }else{
                    table[ row ][ col ] = table[ row - 1 ][ col ]
                }
            }else{
                table[ row ][ col ] = table[ row - 1 ][ col ]
            }
        }
    }
    return table[ table.length - 1 ][ capacity ]
}


/**
 * 多重背包问题
 * 物品有个数限制，可能不止一个，但也不是可以无限选择
 * 解：转换为01背包问题即可。物品a有n个，转换为n个体积和价值相同的物品
 */

// ========== test ===============
const v = [ 999, 20, 10, 21, 16, 6 ]
const vol = [ 11, 8, 3, 7, 4, 3 ]
console.log(maxPack(v, vol, 10))
console.log(entirePack(v, vol, 10))