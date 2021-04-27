/**
 * Created by fgh on 2019/1/14
 */


/**
 * p142
 * 反转链表，返回新的头结点
 * @param head
 * @returns {*}
 */
function reverseList(head){
    if( !head || !head.next ){
        return head
    }
    let pre = head
    let current = head.next
    let temp = null
    while( current ){
        temp = current.next
        current.next = pre
        pre = current
        current = temp
    }
    // !!!!
    head.next = null
    return pre
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


const arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
let list = makeLinkedList(arr)
list = reverseList(list)
console.log(linkedList2Arr(list))