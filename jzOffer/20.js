/**
 * Created by fgh on 2019/2/14
 */

/**
 * https://www.jianshu.com/p/65c8c60b83b8
 * 八皇后问题
 */
class NQueen {
  constructor (n) {
    this.chessboard = []
    this.result = 0
    this.n = n
    for (let i = 0; i < n; i++) {
      this.chessboard[ i ] = new Array(n).fill(0)
    }
    this._find(0)
  }

  _find (row) {
    if (row > 7) {
      // this.result.push(this._snapshoot())
      this.result++
      return
    }
    for (let col = 0; col < this.n; col++) {
      if (this._check(row, col)) {
        this.chessboard[ row ][ col ] = 1
        this._find(row + 1)
        // 回溯
        this.chessboard[ row ][ col ] = 0
      }
    }
  }

  _check (row, col) {
    // 检查同列
    for (let i = 0; i < this.n; i++) {
      if (this.chessboard[ i ][ col ] === 1) {
        return false
      }
    }
    // 检查西北斜线
    for (let i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
      if (this.chessboard[ i ][ j ] === 1) {
        return false
      }
    }
    // 检查东北斜线
    for (let i = row - 1, j = col + 1; i >= 0 && j < this.n; i--, j++) {
      if (this.chessboard[ i ][ j ] === 1) {
        return false
      }
    }
    // 东南西南不用检查，因为下面的行还没有放置棋子
    return true
  }

  // _snapshoot(){
  //     const sh = []
  //     for( let i = 0; i < this.chessboard.length; i++ ){
  //         sh[ i ] = Array.from(this.chessboard[ i ])
  //     }
  //     return sh
  // }

  // resultCount(){
  //     return this.result.length
  // }

  getResult () {
    return this.result
  }
}

// ================ test =====================
const t = Date.now()
const q = new NQueen(16)
console.log(q.getResult())
console.log('消耗时间：', Date.now() - t)
