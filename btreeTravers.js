/**
 * Created by fgh on 2019/2/15
 */


//非递归后序遍历
function postOrder(root){
    if( !root ){
        return null
    }
    const order = []
    const stack = [ root ]
    let node = null
    let lastVisit = {}
    while( stack.length ){
        node = stack[ stack.length - 1 ]
        // 如果节点的左右孩子都已经访问过，就访问它。 1.上次访问的是它的右孩子 2. 它没有孩子 3.上次访问的是它的左孩子并且它没有右孩子
        if( (lastVisit === node.right) || (!node.left && !node.right) || (node.left === lastVisit && !node.right) ){
            order.push(node.value)
            lastVisit = node
            stack.pop()
        }else{
            // 它的孩子节点还没有访问
            if( node.right ){
                stack.push(node.right)
            }
            if( node.left ){
                stack.push(node.left)
            }
        }
    }
    return order
}


// 递归后序遍历
function rPostOrder(root){
    if( !root ) return null
    const order = []

    function _(node){
        if( node.left ){
            _(node.left)
        }
        if( node.right ){
            _(node.right)
        }
        order.push(node.value)
    }

    _(root)
    return order
}


// 非递归前序遍历
function preOrder(root){
    const order = []
    const stack = [ root ]
    let node = null
    while( stack.length ){
        node = stack.pop()
        order.push(node.value)
        if( node.right ){
            stack.push(node.right)
        }
        if( node.left ){
            stack.push(node.left)
        }
    }
    return order
}

// 递归前序遍历
function rPreOrder(root){
    const order = []

    function _(node){
        if( !node ) return
        order.push(node.value)
        _(node.left)
        _(node.right)
    }

    _(root)
    return order
}


// 非递归中序遍历
function midOrder(root){
    const order = []
    let node = root
    const stack = []
    while( node || stack.length ){
        while( node ){
            stack.push(node)
            node = node.left
        }
        node = stack.pop()
        order.push(node.value)
        node = node.right
    }
    return order
}

// 递归中序遍历
function rMidOrder(root){
    const order = []

    function _(node){
        if( !node ) return
        _(node.left)
        order.push(node.value)
        _(node.right)
    }

    _(root)
    return order
}

// ============ test ==================
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
