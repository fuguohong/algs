/**
 * Created by fgh on 2019/2/13
 */


/**
 * p182
 * 找到二叉树中所有和为n的路径
 * 采用一个栈来保存路径，前序遍历二叉树
 */
class BTreePath{
    constructor(root, sum){
        if( !root ) throw new Error('root is required')
        this.pathes = []
        this.targetSum = sum
        this.currentSum = 0
        this.path = []
        this._find(root)
    }

    _find(node){
        this.path.push(node)
        this.currentSum += node.value
        if( this.currentSum === this.targetSum ){
            this.pathes.push(Array.from(this.path))
        }
        if( node.left ){
            this._find(node.left)
        }
        if( node.right ){
            this._find(node.right)
        }
        this.currentSum -= node.value
        this.path.pop()
    }

    getPathes(){
        return this.pathes
    }
}


// =============== test ====================
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
const p = new BTreePath(root, 22)
console.log(p.getPathes())