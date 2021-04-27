/**
 * Created by fgh on 2018/11/16.
 */

/**
 https://leetcode-cn.com/explore/orignial/card/all-about-lockup-table/237/learn-to-use-dict/983/
 给定两个数组，编写一个函数来计算它们的交集。

 示例 1:
 输入: nums1 = [1,2,2,1], nums2 = [2,2]
 输出: [2,2]
 示例 2:
 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
 输出: [4,9]

 说明：
 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
 我们可以不考虑输出结果的顺序。
 */
function intersect(nums1, nums2){
    if( nums1.length === 0 || nums2.length === 0 ){
        return []
    }
    const m1 = new Map()
    for( let i = 0; i < nums1.length; i++ ){
        increase(m1, nums1[ i ])
    }
    const result = []
    for( let j = 0; j < nums2.length; j++ ){
        if( m1.has(nums2[ j ]) ){
            result.push(nums2[ j ])
            decrease(m1, nums2[ j ])
        }
    }
    return result
}

function increase(map, num){
    let count = map.get(num)
    if( count ){
        map.set(num, count + 1)
    }else{
        map.set(num, 1)
    }
}

function decrease(map, num){
    let count = map.get(num)
    if( count === 1 ){
        map.delete(num)
    }else{
        map.set(num, count - 1)
    }
}