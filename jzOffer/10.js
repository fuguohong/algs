/**
 * Created by fgh on 2019/1/14
 */


/**
 *  p134
 * 链表的倒数第k个元素
 * 定义两个指针，一个先移动k-1步，第二个再从头结点开始移动。当第一个指针移动到尾的时候，第二个指针指向倒数第k个元素
 * 该方案只需遍历链表一次
 * 注意容错处理
 * @param head
 * @param k
 * @returns
 */
function kToTail(head, k){
    if( !head || !k ){
        return null
    }
    let gap = k
    let p1 = head
    let p2 = head
    while( gap > 1 && p1.next ){
        gap--
        p1 = p1.next
    }
    if( gap > 1 ){
        throw Error('k out of range')
    }
    while( p1.next ){
        p1 = p1.next
        p2 = p2.next
    }
    return p2.value
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


const arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
let list = makeLinkedList(arr)
console.log(kToTail(list, 10))