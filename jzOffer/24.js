/**
 * Created by fgh on 2019/2/15
 */


/**
 * p233
 * 礼物最大值，在m*n的棋盘中每一格都放有礼物，从左上角出发，每次向左或下移动一格，直到右下角。计算最多拿到多少价值的礼物？
 * f(i,j) = max(f(i-1,j), f(i,j-1)) + value[i][j]
 */
function maxValue(matrix){
    if( !matrix || !matrix.length || !matrix[ 0 ].length ){
        throw new Error('invalid input')
    }
    // 初始化矩阵
    const max = new Array(matrix.length)
    const rowlen = matrix[ 0 ].length
    for( let i = 0; i < max.length; i++ ){
        max[ i ] = new Array(rowlen)
    }
    // 初始化起点
    max[ 0 ][ 0 ] = matrix[ 0 ][ 0 ]
    // 初始化第一行
    for( let i = 1; i < max[ 0 ].length; i++ ){
        max[ 0 ][ i ] = max[ 0 ][ i - 1 ] + matrix[ 0 ][ i ]
    }
    // 初始化第一列
    for( let i = 1; i < max.length; i++ ){
        max[ i ][ 0 ] = max[ i - 1 ][ 0 ] + matrix[ i ][ 0 ]
    }
    for( let i = 1; i < max.length; i++ ){
        for( let j = 1; j < max[ 0 ].length; j++ ){
            max[ i ][ j ] = Math.max(max[ i - 1 ][ j ], max[ i ][ j - 1 ]) + matrix[ i ][ j ]
        }
    }
    return max[ max.length - 1 ][ rowlen - 1 ]
}

// ============ test =============
const m = [
    [ 1, 10, 3, 8 ],
    [ 12, 2, 9, 6 ],
    [ 5, 7, 4, 11 ],
    [ 3, 7, 16, 5 ]
]

console.log(maxValue(m))