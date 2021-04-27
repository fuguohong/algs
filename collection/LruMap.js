/**
 * Created by  on 2018/11/20.
 */

class Node{
    constructor(key, value){
        this.pre = null
        this.key = key
        this.value = value
        this.next = null
    }
}

class LRUMap{
    constructor(capacity){
        if( capacity && capacity < 2 ){
            throw new Error('to small capacity')
        }
        this.capacity = capacity
        this.map = new Map()
        this.head = null
        this.end = null
    }

    get(key){
        const node = this.map.get(key)
        if( node ){
            this._moveToHead(node)
            return node.value
        }
        return -1
    }

    put(key, value){
        let node = this.map.get(key)
        if( node ){
            node.value = value
            this._moveToHead(node)
        }else{
            node = new Node(key, value)
            if( this.size() === this.capacity ){
                this._removeLeast()
            }
            if( this.size() === 0 ){
                this.head = node
                this.end = node
            }else{
                this.head.pre = node
                node.next = this.head
                this.head = node
            }
            this.map.set(key, node)
        }
    }

    size(){
        return this.map.size
    }

    _moveToHead(node){
        const pre = node.pre
        if( !pre ){
            return
        }
        if( this.end === node ){
            this.end = pre
        }
        pre.next = node.next
        node.next = this.head
        this.head.pre = node
        node.pre = null
        this.head = node
    }

    _removeLeast(){
        this.map.delete(this.end.key)
        this.end = this.end.pre
        this.end.next = null
    }
}


const cache = new LRUMap(2 /* 缓存容量 */);

cache.put(1, 1);
cache.put(2, 2);
console.log(cache.get(1))     // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
console.log(cache.get(2))       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
console.log(cache.get(1))       // 返回 -1 (未找到)
console.log(cache.get(3))       // 返回  3
console.log(cache.get(4))