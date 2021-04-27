/**
 * Created by fgh on 2018/11/16.
 */

/**
 * https://leetcode-cn.com/explore/orignial/card/all-about-lockup-table/237/learn-to-use-dict/989/
 * 给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
 *
     示例 1:
     输入:
     "tree"
     输出:
     "eert"

     解释:
     'e'出现两次，'r'和't'都只出现一次。
     因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
 */
function frequencySort(s){
    const counter = new Map()
    for( let i = 0; i < s.length; i++ ){
        let c = counter.get(s[ i ])
        if( c === undefined ){
            counter.set(s[ i ], 1)
        }else{
            counter.set(s[ i ], c + 1)
        }
    }
    const values = new Array(s.length + 1).fill('')
    for( let [ k, v ] of counter.entries() ){
        values[ s.length - v ] += new Array(v).fill(k).join('')
    }
    return values.join('')
};

console.log(frequencySort('apppppppppkk'))