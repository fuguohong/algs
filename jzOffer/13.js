/**
 * Created by fgh on 2019/1/17
 */


/**
 * p157
 * 二叉树的镜像
 * @param tree
 * @returns {*}
 */
function mirrorTree(tree){
    if( !tree ) return null
    const root = new Node(tree.value)
    root.left = mirrorTree(tree.right)
    root.right = mirrorTree(tree.left)
    return root
}

function Node(value){
    return {
        value: value,
        left: null,
        right: null
    }
}

// =============== test ====================
const values = [ 8, 8, 7, 9, 2, 4, 7 ]
const nodes = values.map(v => {
    return { value: v }
})
nodes[ 0 ].left = nodes[ 1 ]
nodes[ 0 ].right = nodes[ 2 ]
nodes[ 1 ].left = nodes[ 3 ]
nodes[ 1 ].right = nodes[ 4 ]
nodes[ 4 ].left = nodes[ 5 ]
nodes[ 4 ].right = nodes[ 6 ]
const root = nodes[ 0 ]
let res = mirrorTree(root)
console.log(res)