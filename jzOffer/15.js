/**
 * Created by fgh on 2019/1/22
 */
const process = require('process')

/**
 * 从上到下打印一棵树，将同一层的节点放在同一行。
 * 树的广度优先遍历，需要用到一个队列。 将同一层的打印到一行，想办法记录节点是否在同一行
 * @param root
 */
function printBTree(root){
    if( !root ){
        return
    }
    const queue = [ root ]
    // 当前层剩余节点
    let currentLeft = 1
    // 下一层节点数量
    let nextCount = 0
    while( queue.length ){
        const node = queue.shift()
        if( node.left ){
            queue.push(node.left)
            nextCount++
        }
        if( node.right ){
            queue.push(node.right)
            nextCount++
        }
        process.stdout.write(node.value.toString() + '  ')
        currentLeft--
        // 当前层剩余节点为0， 输出换行符。切换到下一层
        if( currentLeft === 0 ){
            process.stdout.write('\r\n')
            currentLeft = nextCount
            nextCount = 0
        }
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

nodes[ 2 ].left = { value: 0 }
const root = nodes[ 0 ]
printBTree(root)