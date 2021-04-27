/**
 * Created by fgh on 2019/2/18
 */


/**
 * p271
 * 对于一棵树，其深度为左右节点深度的较大值+1。空树深度为0. 因此递归
 */
function depth(root){
    if( !root ){
        return 0
    }
    let ld = depth(root.left)
    let rd = depth(root.right)
    return ld > rd ? ld + 1 : rd + 1
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

nodes[ 2 ].left = { value: 0 }
const root = nodes[ 0 ]
console.log(depth(root))