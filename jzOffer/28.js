/**
 * Created by fgh on 2019/2/18
 */


/**
 * p273
 * 是否是平衡二叉树
 * 平衡二叉树的左右深度差不超过1. 左右子树都是平衡二叉树的树是一颗平衡二叉树。
 * 自底向上遍历，记录结点深度。判断左右高度差
 * @param root
 * @returns {boolean}
 */
function isBalance(root){
    function _(node){
        let balance = false
        let depth = NaN
        if( !node ){
            balance = true
            depth = 0
        }else{
            const left = _(node.left)
            if( left.balance ){
                const right = _(node.right)
                if( right.balance ){
                    if( left.depth - right.depth <= 1 && left.depth - right.depth >= -1 ){
                        balance = true
                        depth = 1 + (left.depth > right.depth ? left.depth : right.depth)
                    }
                }
            }
        }
        return { balance, depth }
    }

    return _(root).balance
}

// ========= test =============
const values = [ 8, 8, 7, 6, 2, 4, 7 ]
const nodes = values.map(v => {
    return { value: v }
})
nodes[ 0 ].left = nodes[ 1 ]
nodes[ 0 ].right = nodes[ 2 ]
nodes[ 1 ].left = nodes[ 3 ]
nodes[ 1 ].right = nodes[ 4 ]
nodes[ 4 ].left = nodes[ 5 ]
nodes[ 4 ].right = nodes[ 6 ]

nodes[ 2 ].left = { value: 0, left: { value: 9 } }
const root = nodes[ 0 ]
console.log(isBalance(root))