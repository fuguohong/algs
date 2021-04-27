/**
 * Created by fgh on 2019/1/13
 */

/**
 * p119
 * 给定一个单向链表的头结点和待删除节点，在O(1)时间内删除节点。
 * 将待删除节点的下一个节点值复制到待删除节点上，链表跳过下一个节点
 * 如果待删除节点是尾节点，仍需O(n)时间找到前节点，然后删除
 * @param head
 * @param toBeDel
 */
function delNode(head, toBeDel){
    if( !head || !toBeDel ) return
    let list = head
    if( toBeDel.next ){
        toBeDel.value = toBeDel.next.value
        toBeDel.next = toBeDel.next.next
        // else ,待删除节点是尾节点
    }else if( head === toBeDel ){
        // 待删除节点是头结点
        list = null
    }else{
        let node = head
        while( node.next !== toBeDel && node.next ){
            node = node.next
        }
        if( node.next !== toBeDel ){
            throw new Error('toBeDel not in list')
        }
        node.next = toBeDel.next
    }
    return list
}

function Node(value, next = null){
    this.value = value
    this.next = next
    return this
}

// ====================== test ==============

function makeLinkedList(arr){
    if( !arr || !arr.length ){
        throw new Error('arr must be an array with some value')
    }
    const head = new Node(arr[ 0 ])
    let node = head
    for( let i = 1; i < arr.length; i++ ){
        node.next = new Node(arr[ i ])
        node = node.next
    }
    return head
}

function linkedList2Arr(llist){
    const arr = []
    while( llist ){
        arr.push(llist.value)
        llist = llist.next
    }
    return arr
}

function findNode(head, value){
    let node = head
    while( node && node.value !== value ){
        node = node.next
    }
    if( !node ){
        throw new Error('toBeDel not in list')
    }
    return node
}

const arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
let list = makeLinkedList(arr)
const toBeDel = findNode(list, 1)
list = delNode(list, new Node(10))
console.log(linkedList2Arr(list))