/**
 * Created by  on 2018/11/21.
 */

/**
 * https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/912/
 *给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

 示例 1:
 输入:
 [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
 ]
 输出: [1,2,3,6,9,8,7,4,5]
 */
function spiralOrder(matrix){
    if( matrix.length === 0 || matrix[ 0 ].length === 0 ){
        return []
    }
    let x = 0
    let y = 0
    let minx = 0
    let maxx = matrix[ 0 ].length - 1
    let miny = 0
    let maxy = matrix.length - 1
    const result = []
    let falge = true
    while( minx <= maxx && miny <= maxy ){
        // js 直接用 x < y < z 判断是错误的。
        falge = miny <= y && y <= maxy
        while( x < maxx && falge ){
            result.push(matrix[ y ][ x++ ])
        }
        miny++
        falge = minx <= x && x <= maxx
        while( y < maxy && falge ){
            result.push(matrix[ y++ ][ x ])
        }
        maxx--
        falge = miny <= y && y <= maxy
        while( x > minx && falge ){
            result.push(matrix[ y ][ x-- ])
        }
        maxy--
        falge = minx <= x && x <= maxx
        while( y > miny && falge ){
            result.push(matrix[ y-- ][ x ])
        }
        minx++
    }
    result.push(matrix[ y ][ x ])
    return result
}

/**
 * https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/913/
 * 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
 示例:
 输入: 3
 输出:
 [
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
 ]
 */
function generateMatrix(n){
    if( n < 1 ){
        return []
    }
    const matrix = new Array(n)
    for( let i = 0; i < matrix.length; i++ ){
        matrix[ i ] = new Array(n)
    }
    let x = 0
    let y = 0
    let minx = 0
    let maxx = n - 1
    let miny = 0
    let maxy = n - 1
    let falge = true
    let num = 1
    while( minx <= maxx && miny <= maxy ){
        // js 直接用 x < y < z 判断是错误的。
        falge = miny <= y && y <= maxy
        while( x < maxx && falge ){
            matrix[ y ][ x++ ] = num++
        }
        miny++
        falge = minx <= x && x <= maxx
        while( y < maxy && falge ){
            matrix[ y++ ][ x ] = num++
        }
        maxx--
        falge = miny <= y && y <= maxy
        while( x > minx && falge ){
            matrix[ y ][ x-- ] = num++
        }
        maxy--
        falge = minx <= x && x <= maxx
        while( y > miny && falge ){
            matrix[ y-- ][ x ] = num++
        }
        minx++
    }
    matrix[ y ][ x ] = num
    return matrix
}

const res = generateMatrix(2)

for( let i = 0; i < res.length; i++ ){
    console.log(res[ i ])
}