/**
 * Created by fgh on 2019/2/17
 */


exports.selectSort = selectSort
exports.bullingSort = bubblingSort
exports.insertSort = insertSort
exports.shellSort = shellSort
exports.heapSort = heapSort
exports.mergeSort = mergeSort
exports.quickSort = quickSort


function _exchange(arr, i, j){
    let temp = arr[ i ]
    arr[ i ] = arr[ j ]
    arr[ j ] = temp
}


/**
 * 选择排序，每次选择最小的元素和当前元素交换位置，效率和输入无关。空间复杂度O(1),时间复杂度O(n^2).不稳定
 * @param arr
 */
function selectSort(arr){
    if( !arr || arr.length < 2 ){
        return
    }
    for( let i = 0; i < arr.length - 1; i++ ){
        let min = arr[ i ]
        for( let j = i + 1; j < arr.length; j++ ){
            if( arr[ j ] < min ){
                arr[ i ] = arr[ j ]
                arr[ j ] = min
                min = arr[ i ]
            }
        }
    }
}


/**
 * 改进后的冒泡排序，空间复杂度O(1),时间复杂度O(n^2)，最优情况(有序)复杂度(n).稳定
 */
function bubblingSort(arr){
    if( !arr || arr.length < 2 ){
        return
    }
    let lastChange = arr.length - 1
    let hasChange = true
    while( hasChange && lastChange > 0 ){
        hasChange = false
        let max = lastChange
        for( let i = 0; i < max; i++ ){
            if( arr[ i ] > arr[ i + 1 ] ){
                _exchange(arr, i, i + 1)
                lastChange = i
                hasChange = true
            }
        }
    }
}


/**
 * 插入排序，空间复杂度O(1),时间复杂度O(n^2)，最优情况O(n)，是处理接近有序数组最快的算法。稳定
 * @param arr
 */
function insertSort(arr){
    if( !arr || arr.length < 2 ){
        return
    }
    for( let i = 1; i < arr.length; i++ ){
        if( arr[ i ] < arr[ i - 1 ] ){
            let j = i
            while( j > 0 && arr[ j ] < arr[ j - 1 ] ){
                _exchange(arr, j, --j)
            }
        }
    }
}


/**
 * 希尔排序（增量排序），空间复杂度O(1)，时间复杂度不确定，性能接近快排。不稳定
 */
function shellSort(arr){
    if( !arr || arr.length < 2 ){
        return
    }
    // 确定增量
    let gap = arr.length >> 1
    while( gap > 0 ){
        for( let i = gap; i < arr.length; i++ ){
            let j = i
            let nextj = j - gap
            while( j >= gap && arr[ j ] < arr[ nextj ] ){
                let temp = arr[ j ]
                arr[ j ] = arr[ nextj ]
                arr[ nextj ] = temp
                j = nextj
                nextj = j - gap
            }
        }
        gap = gap >> 1
    }
}


/**
 * 堆排序，在最坏的情况下也能保证nlogn的性能。
 * @param arr
 */
function heapSort(arr){
    if( !arr || arr.length < 2 ){
        return
    }
    let max = arr.length
    // 构建一个大顶堆，没有子节点的结点不用下沉
    for( let i = (max >> 1) - 1; i >= 0; i-- ){
        _sink(arr, i, max)
    }
    while( max > 1 ){
        // 依次取出堆顶元素，放到后面
        _exchange(arr, 0, --max)
        _sink(arr, 0, max)
    }
}

function _sink(arr, index, max){
    let child = index * 2 + 1
    while( child < max ){
        if( child + 1 < max && arr[ child ] < arr[ child + 1 ] ){
            child++
        }
        if( arr[ index ] >= arr[ child ] ){
            break
        }
        _exchange(arr, index, child)
        index = child
        child = index * 2 + 1
    }
}


/**
 * 归并排序，空间复杂度O(n) ,时间复杂度O(nlogn)，稳定。
 * @param arr
 * @returns {null}
 */
function mergeSort(arr){
    if( !arr || arr.length < 2 ){
        return
    }
    const aux = new Array(arr.length)
    _mergeSort(arr, aux, 0, arr.length - 1)
}

function _mergeSort(src, aux, start, end){
    if( start >= end ){
        return
    }
    let mid = start + ((end - start) >> 1)
    _mergeSort(src, aux, start, mid)
    _mergeSort(src, aux, mid + 1, end)
    // 复制到辅助数组
    for( let k = start; k <= end; k++ ){
        aux[ k ] = src[ k ]
    }
    // 子数组归并完成，左右分别有序，合并
    let left = start
    let right = mid + 1
    for( let i = start; i <= end; i++ ){
        if( left > mid ){
            src[ i ] = aux[ right++ ]
        }else if( right > end ){
            src[ i ] = aux[ left++ ]
        }else if( aux[ left ] > aux[ right ] ){
            src[ i ] = aux[ right++ ]
        }else{
            src[ i ] = aux[ left++ ]
        }
    }
}


/**
 * 快速排序，时间复杂度nlogn，不稳定
 */
function quickSort(arr){
    if( !arr || arr.length < 2 ){
        return
    }
    _quickSort(arr, 0, arr.length - 1)
}

function _quickSort(arr, left, right){
    if( left >= right ){
        return
    }
    let index = _patition(arr, left, right)
    _quickSort(arr, left, index - 1)
    _quickSort(arr, index + 1, right)
}

function _patition(arr, left, right){
    // 选择一个哨兵位置。这里直接选择中间位置。为了能够尽量把数组平均切分，避免快排退化，可以采取更复杂的策略
    let sentryIndex = (left + right) >> 1
    const sentry = arr[ sentryIndex ]
    _exchange(arr, left, sentryIndex)
    let i = left + 1
    let j = right
    while( true ){
        while( arr[ i ] <= sentry && i < right ){
            i++
        }
        while( arr[ j ] >= sentry && j > left ){
            j--
        }
        if( j <= i ){
            break
        }
        _exchange(arr, i, j)
    }
    _exchange(arr, left, j)
    return j
}

// ========= test==========
const arr = makeRandomArr(600000)
for( let k of Object.keys(exports) ){
    if(k === 'selectSort' || k === 'bullingSort' || k === 'insertSort'){
        continue
    }
    let temp = Array.from(arr)
    let start = Date.now()
    exports[ k ](temp)
    let end = Date.now()
    console.log(k+' : '+ (end-start))
}

function makeRandomArr(len, min, max){
    const arr = new Array(len)
    min = min === undefined ? 0 : min
    max = max === undefined ? len : max
    for( let i = 0; i < len; i++ ){
        arr[ i ] = random(min, max)
    }
    return arr
}

function random(min, max){
    return Math.round(Math.random() * (max - min)) + min
}
