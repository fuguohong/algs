/**
 * Created by fgh on 2018/11/15.
 */

/**
 https://leetcode-cn.com/explore/orignial/card/all-about-array/233/sliding-window/971/
 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
 示例:
 输入: s = 7, nums = [2,3,1,2,4,3]
 输出: 2
 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
 */

function minSubArrayLen(nums, s){
    let left = 0
    let right = 1
    let sum = nums[ 0 ]
    let len = Number.POSITIVE_INFINITY
    while( right < nums.length || sum >= s ){
        if( sum < s ){
            sum += nums[ right++ ]
        }else{
            len = Math.min(right - left, len)
            sum -= nums[ left++ ]
        }
    }
    return len === Number.POSITIVE_INFINITY ? 0 : len
}

console.log(minSubArrayLen(
  [ 2, 3, 1, 2, 4, 3 ], 7))