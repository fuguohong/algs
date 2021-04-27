/**
 * Created by fgh on 2018/11/19.
 */

/**
 * https://leetcode-cn.com/explore/orignial/card/all-about-lockup-table/239/learn-to-use-keys/1003/
 * 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
 *
 * 输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
 输出: 4
 */
function maxPoints(points){
    if( points.length === 0 ){
        return 0
    }
    if( points.length < 3 ){
        return points.length
    }
    let max = 0
    for( let i = 0; i < points.length; i++ ){
        max = Math.max(max, linePoints(points, i))
    }
    return max
}

function linePoints(points, index){
    const slopes = new Map()
    const p = points[ index ]
    let same = 0
    for( let i = 0; i < points.length; i++ ){
        if( p[ 0 ] === points[ i ][ 0 ] && p[ 1 ] === points[ i ][ 1 ] ){
            same++
            continue
        }
        // js 其实没有除零异常
        // 计算斜率存在精度丢失问题
        // const slope = (points[ i ][ 1 ] - p[ 1 ]) / (points[ i ][ 0 ] - p[ 0 ]) || Number.MIN_VALUE
        const slope = calculateSlope(points[ i ], p)
        const count = slopes.get(slope)
        slopes.set(slope, count === undefined ? 1 : count + 1)
    }
    return Math.max(0, ...slopes.values()) + same
}

function calculateSlope(p1, p2){
    const divd = p1[ 1 ] - p2[ 1 ]
    const div = p1[ 0 ] - p2[ 0 ]
    if( div === 0 ){
        return Number.MAX_VALUE
    }
    if( Math.abs(divd) > 10000 && -100 < Math.abs(divd) - Math.abs(div) < 100 ){
        // 这里左移可能会丢失高位，但是依然会造成比值非常接近1的斜率计算结果不同
        // js核心api没有提供decimal采用这种没有经过严格测试的临时方案，其他语言用decimal来解决精度问题
        return ((divd << 6) / div) / 64
    }
    return divd / div
}

console.log(maxPoints([ [ 0, 0 ], [ 94911151, 94911150 ], [ 94911152, 94911151 ] ]))