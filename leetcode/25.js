/**
 * Created by  on 2018/11/23.
 */


/**
 * https://leetcode-cn.com/explore/interview/card/tencent/224/sort-and-search/927/
 * 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
 ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
 你可以假设数组中不存在重复的元素。
 你的算法时间复杂度必须是 O(log n) 级别。

 示例 1:
 输入: nums = [4,5,6,7,0,1,2], target = 0
 输出: 4

 示例 2:
 输入: nums = [4,5,6,7,0,1,2], target = 3
 输出: -1
 */
function search(nums, target){
    let left = 0
    let right = nums.length - 1
    while( left <= right ){
        const mid = ((left + right) / 2) << 0
        if( nums[ mid ] === target ) return mid
        // 右边部分有序
        if( nums[ mid ] < nums[ right ] ){
            // target 处于右边部区间中，搜索右边
            if( nums[ mid ] < target && nums[ right ] >= target ){
                left = mid + 1
                // 不在右边区间中，搜索左边
            }else{
                right = mid - 1
            }
            // 左部分有序
        }else{
            if( nums[ mid ] > target && nums[ left ] <= target ){
                right = mid - 1
            }else{
                left = mid + 1
            }
        }
    }
    return -1
}