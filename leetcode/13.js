/**
 * Created by fgh on 2018/11/15.
 */

/**
 https://leetcode-cn.com/problems/container-with-most-water/
 盛最多水的容器
 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

 说明：你不能倾斜容器，且 n 的值至少为 2。
 */

function maxArea(lines){
    let left = 0
    let right = lines.length - 1
    let max = 0
    while( left < right ){
        let volume = 0
        if( lines[ left ] < lines[ right ] ){
            volume = lines[ left ] * (right - left)
            left++
        }else{
            volume = lines[ right ] * (right - left)
            right--
        }
        if( volume > max ){
            max = volume
        }
    }
    return max
}


console.log(maxArea([ 1, 8, 6, 2, 5, 4, 8, 3, 7 ]))