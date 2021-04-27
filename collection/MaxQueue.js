/**
 * Created by fgh on 2019/2/19
 */


/**
 * O(1)时间获取最大值的队列
 */
class MaxQueue{
    constructor(){
        this._data = []
        this._max = []
    }

    push(elm){
        while( this._max.length && this._max[ this._max.length - 1 ] <= elm ){
            this._max.pop()
        }
        this._max.push(elm)
        this._data.push(elm)
    }

    shift(){
        if( !this._data.length ){
            throw new Error('can not shift element from empty queue')
        }
        const elm = this._data.shift()
        if( this._max[ 0 ] === elm ){
            this._max.shift()
        }
        return elm
    }

    max(){
        if( !this._data.length ){
            throw new Error('can not get max from empty queue')
        }
        return this._max[ 0 ]
    }
}

//========== test ==========
const q = new MaxQueue()
q.push(5)
console.log(q.max())
q.push(4)
console.log(q.max())
q.push(7)
console.log(q.max())
q.shift()
q.shift()
console.log(q.max())
q.push(1)
q.shift()
console.log(q.max())
