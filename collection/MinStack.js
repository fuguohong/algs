/**
 * Created by  on 2018/11/20.
 */
//     MinStack
class MinStack{
    constructor(){
        this.elements = []
        this.mins = []
    }

    isEmpty(){
        return this.size() === 0
    }

    size(){
        return this.elements.length
    }

    push(element){
        if( this.isEmpty() ){
            this.mins.push(element)
        }else if( element <= this.getMin() ){
            this.mins.push(element)
        }
        this.elements.push(element)
    }

    pop(){
        if( this.isEmpty() ) return null
        const value = this.elements.pop()
        if( value === this.getMin() ){
            this.mins.pop()
        }
        return value
    }

    top(){
        if( this.isEmpty() ) return null
        return this.elements[ this.size() - 1 ]
    }

    getMin(){
        return this.mins[ this.mins.length - 1 ]
    }
}


const minStack = new MinStack()
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
console.log(minStack.getMin())
console.log(minStack.pop())
console.log(minStack.top())
console.log(minStack.getMin())

