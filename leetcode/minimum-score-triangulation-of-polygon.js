/**
 * @param {number[]} A
 * @return {number}
 */
var minScoreTriangulation = function (A) {
    //    console.log(A)
    var n = A.length;
    var cache = {};

    function f(i, j, k) {
        // console.log(i, j, k);
        var key = i + '.' + j + '.' + k;
        if (key in cache) {
            return cache[key];
        }
        var value = 1 << 30;
        for (var idx = j + 1; idx <= k; idx++) {
            var res = A[i] * A[j] * A[idx];
            if (res >= value) {
                continue;
            }
            if (idx < k) {
                res += f(i, idx, k);
            }
            if ((j + 1) < idx) {
                res += f(j, j + 1, idx);
            }
            if (res < value) {
                value = res;
            }
        }
        cache[key] = value;
        return value;
    }
    res = f(0, 1, n - 1);
    return res;

};

var run_test_cases = function (fn, cases) {
    var failed = false;

    for (var i = 0; i < cases.length; i++) {
        var c = cases[i];
        var args = c.slice(0, c.length - 1);
        var exp = c[c.length - 1];
        //    console.log(args, exp)
        var res = fn.apply(null, args);
        if (res != exp) {
            failed = true;
            console.log("case#%d: %s failed. output = %s", i, JSON.stringify(c), JSON.stringify(res));
        }
    }
    if (!failed) {
        console.log("all cases passed!!!");
    }
}


var cases = [
    [[1, 2, 3], 3],
    [[3, 7, 4, 5], 144],
    [[1, 3, 1, 4, 1, 5], 13],
];
run_test_cases(minScoreTriangulation, cases);
