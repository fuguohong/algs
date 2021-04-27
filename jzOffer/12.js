/**
 * Created by fgh on 2019/1/16
 */

/**
 * p148 判断一颗二叉树是不是另一个二叉树的子树
 * @param tree
 * @param subtree
 * @returns {*}
 */
function isSubTree(tree, subtree){
    if( !tree || !subtree ){
        return false
    }
    let result
    if( tree.value === subtree.value ){
        result = _isSubTree(tree.left, subtree.left) && _isSubTree(tree.right, subtree.right)
    }
    return result || isSubTree(tree.left, subtree) || isSubTree(tree.right, subtree)
}

function _isSubTree(t1, t2){
    if( !t1 ){
        return !t2
    }
    if( !t2 ){
        return true
    }
    return t1.value === t2.value && _isSubTree(t1.left, t2.left) && _isSubTree(t1.right, t2.right)
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

const sub = {
    value: 8,
    left: {
        value: 9,
        left: null,
        right: null
    },
    right: {
        value: 2,
        left: null,
        right: null
    }
}

const root = nodes[ 0 ]
console.log(isSubTree(root, { value: 2, left: { value: 4 }, right: { value: 0 } }))

