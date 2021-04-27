/**
 * Created by fgh on 2018/11/16.
 */


/**
 * https://leetcode-cn.com/explore/orignial/card/all-about-lockup-table/238/lookup-table-related-sum-questions/993/
 *
 * 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
 注意：答案中不可以包含重复的三元组。
 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
 满足要求的三元组集合为：
 [
 [-1, 0, 1],
 [-1, -1, 2]
 ]
 */
function threeSum(nums){
    if( nums.length < 3 ){
        return []
    }
    nums.sort((a, b) => {
        return a - b
    })
    const result = []
    let i = -1
    while( i < nums.length ){
        i++
        if( nums[ i ] > 0 ){
            break
        }
        // js允许数组越界所以没有做角标处理，其他语言需要考虑越界问题
        if( nums[ i ] === nums[ i - 1 ] ){ //跳过相同组合
            continue
        }
        let target = -nums[ i ]
        let left = i + 1
        let right = nums.length - 1
        while( left < right ){
            let sum = nums[ left ] + nums[ right ]
            // left-1 和 right+1 相等， 考虑一个即可。由于需要判断 left-1 !== i，所以去判断right+1
            if( sum < target ){
                left++
                continue
            }
            if( sum > target || nums[ right ] === nums[ right + 1 ] ){ //跳过相同组合
                right--
                continue
            }
            result.push([ nums[ i ], nums[ left++ ], nums[ right-- ] ])
        }
    }
    return result
}

console.log(threeSum([ -2, 0, 0, 2, 2 ]))