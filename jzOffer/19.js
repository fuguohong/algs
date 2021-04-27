/**
 * Created by fgh on 2019/2/14
 */


/**
 * p199
 * 求集合的组合
 */
class Combinations{
    constructor(arr, n){
        this.arr = arr
        this.n = n
        this.comb = []
        this.result = []
        if( !arr || !arr.length || !n || n > arr.length ){
            return this
        }
        for( let i = 0; i <= arr.length - n; i++ ){
            this._find(i)
            this.comb.pop()
        }
    }

    _find(current){
        this.comb.push(this.arr[ current ])
        if( this.comb.length === this.n ){
            this.result.push(Array.from(this.comb))
            return
        }
        for( let i = current + 1; i < this.arr.length; i++ ){
            this._find(i)
            this.comb.pop()
        }

    }

    getCombinations(){
        return this.result
    }
}

// =========== test =============
const arr = [ 1, 2, 3, 4, 5 ]
console.log(new Combinations(arr, 2).getCombinations())

