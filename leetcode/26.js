/**
 * Created by  on 2018/11/23.
 */
'use strict'

/**
 * https://leetcode-cn.com/explore/interview/card/tencent/224/sort-and-search/934/
 * 给定一个二叉树(非搜索树), 找到该树中两个指定节点的最近公共祖先。
 * 解：由于不是二叉搜索树，没有规矩。 采用后序遍历，找到某个结点时，栈中剩余的结点（包括它自己）即为结点从上到下的祖先。
 * 两个结点的祖先都找到后，找到他们从下往上第一个相同的祖先
 */
function lowestCommonAncestor(root, p, q){
    const stack = [] // 遍历栈
    let rootp = null // p的祖先
    let rootq = null // q的祖先
    // 后序遍历，找到祖先
    let node = root
    let lastVisit = null
    while( node || stack.length > 0 ){
        while( node ){
            stack.push(node)
            node = node.left
        }
        let temp = stack[ stack.length - 1 ]
        if( !temp.right || lastVisit === temp.right ){
            stack.pop()
            lastVisit = temp
            if( temp === p ){
                rootp = Array.from(stack)
                // p q有可能为直系关系，所以把自己也包含进去
                rootp.push(temp)
            }
            if( temp === q ){
                rootq = Array.from(stack)
                rootq.push(temp)
            }
            if( rootp && rootq ) break
        }else{
            node = temp.right
        }
    }
    if( !rootp || !rootq ) return null
    let i = Math.min(rootp.length - 1, rootq.length - 1)
    // 找到最后的一个相同祖先
    while( i >= 0 ){
        if( rootp[ i ] === rootq[ i ] ) return rootp[ i ]
        i--
    }
}

const node1 = { val: 1 }
const root = { val: 2, right: node1 }
console.log(lowestCommonAncestor(root, root, node1))

/**
 * 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
 解： 直接搜索，找到第一个值处于p ，q之间的结点，即为他们的最近公共祖先
 */
function lowestCommonAncestor2(root, p, q){
    if( !p || !q ) return null
    let sm = Math.min(p.val, q.val)
    let lg = Math.max(p.val, q.val)
    let node = root
    while( node ){
        if( node.val < sm ){
            node = node.right
        }else if( node.val > lg ){
            node = node.left
        }else{
            return node
        }
    }
    return null
}