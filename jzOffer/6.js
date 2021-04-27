/**
 * Created by fgh on 2018/11/18
 */

/**
 * p89
 * 判断矩阵中是否包含给定的路径， 路径可以从任意一点开始，每次可以在矩阵中向上下左右移动一格，不能走过重复的点
 */
function hasPath(matrix, way){
    if( !matrix || matrix.length < 1 || matrix[ 0 ].length < 1 ){
        return null
    }
    const path = new Set()
    for( let x = 0; x < matrix.length; x++ ){
        for( let y = 0; y < matrix[ 0 ].length; y++ ){
            if( visit(matrix, way, path, x, y) ){
                return true
            }
        }
    }
    return false
}

function visit(matrix, way, path, x, y){
    if( x < 0 || x >= matrix.length || y < 0 || y >= matrix[ 0 ].length ){
        return false
    }
    let key = x + ',' + y
    if( matrix[ x ][ y ] !== way[ path.size ] || path.has(key) ){
        return false
    }
    path.add(key)
    if( path.size === way.length ){
        return true
    }
    const result = visit(matrix, way, path, x + 1, y) || visit(matrix, way, path, x - 1, y)
      || visit(matrix, way, path, x, y + 1) || visit(matrix, way, path, x, y - 1)
    if( !result ){
        path.delete(key)
    }
    return result
}


//=============test===============
const m = [
    [ 'a', 'b', 't', 'g' ],
    [ 'c', 'f', 'c', 's' ],
    [ 'j', 'd', 'e', 'h' ]
]

const w = 'cedjcfa'

console.log(hasPath(m, w))