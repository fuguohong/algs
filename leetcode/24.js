/**
 * Created by  on 2018/11/23.
 */


/**
 * https://leetcode-cn.com/explore/interview/card/tencent/224/sort-and-search/929/
 * 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

 说明：
 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 *  解：用二叉树的中序遍历即可，非递归方式实现：
 */
function kthSmallest(root, k){
    const stack = []
    let node = root
    while( node || stack.length !== 0 ){
        while( node ){
            stack.push(node)
            node = node.left
        }
        node = stack.pop()
        if( k-- === 1 ) return node.val
        node = node.right
    }
    return null
}

// ======== 另外两种非递归遍历二叉树方式
function preOrder(root){
    if( !root ) return
    const stack = [ root ]
    let node = null
    while( stack.length !== 0 ){
        node = stack.pop()
        console.log(node.val)
        if( node.right ) stack.push(node.right)
        if( node.left ) stack.push(node.left)
    }
}

function postOrder(root){
    const stack = []
    let node = root
    // 上次访问的结点，对于一个节点来说，上次访问的结点要么是左孩子，要么是右孩子。用来判断又孩子是不是访问过了
    let lastVisit = null
    while( node || stack.length !== 0 ){
        while( node ){
            stack.push(node)
            node = node.left
        }
        // 不能直接出栈，先判断右孩子有没有被访问
        let temp = stack[ stack.length - 1 ]
        if( !temp.right || lastVisit === temp.right ){
            stack.pop()
            lastVisit = temp
            console.log(temp.val)
        }else{
            // 右孩子没有被访问，就不访问该节点，往右下走
            node = temp.right
        }
    }
}


function BFS(root){
    const queue = [ root ]
    while( queue.length > 0 ){
        let node = queue.shift()
        console.log(node.val)
        if( node.left ) queue.push(node.left)
        if( node.right ) queue.push(node.right)
    }
}

const node3 = { val: 4 }
const node2 = { val: 3, left: node3 }
const node1 = { val: 1, }
const root = { val: 2, right: node1, left: node2 }
postOrder(root, root, node1)

