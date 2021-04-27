/**
 * Created by  on 2018/11/22.
 */


/**
 *https://leetcode-cn.com/explore/interview/card/tencent/222/linked-list/916/
 给定一个链表，判断链表中是否有环。

 进阶：
 你能否不使用额外空间解决此题？

 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

function hasCycle(head){
    if( !head ) return false
    let slow = head
    let fast = head.next
    while( slow !== fast ){
        if( !fast || !fast.next ){
            return false
        }
        slow = slow.next
        fast = fast.next.next
    }
    return true
}

/**
 * https://leetcode-cn.com/problems/linked-list-cycle-ii/
 * 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
 说明：不允许修改给定的链表。

 进阶：
 你是否可以不用额外空间解决此题？
 */
/**
 * 此题代码不直观，附上解题思路
 解题思路：
 如果存在环，fast和slow相遇的时候，fast正好比slow多走了n圈。设起点到环的距离为a， 环起点到slow的距离为b。
 fast速度是slow两倍，slow走了a+b， fast就多走了a+b ,即a+b就是n圈的长度。如果slow再走a+b，将再次回到相遇点。
 少走一个b(环起点到slow的距离)，就刚好在起点。a+b-b=a,即slow再走a个长度，就到达了环起点。 a为起点到环起点距离
 则slow从相遇点走a， 另一个指针p从起点走a，他们就会在环起点相遇。
 */
function detectCycle(head){
    if( !head ) return null
    let fast = head
    let slow = head
    let p = head
    do{
        if( !fast || !fast.next ){
            return null
        }
        fast = fast.next.next
        slow = slow.next
    }while( fast !== slow )
    while( p !== slow ){
        p = p.next
        slow = slow.next
    }
    return p
}