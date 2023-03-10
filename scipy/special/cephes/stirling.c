/* c implementation of Stirling numbers of the second kind */

/*
 *
 *     Stirling numbers of the second kind
 *
 *
 *
 * SYNOPSIS: Stirling numbers of the second kind count the
 *  number of ways to make a partition of n distinct elements
 *  into k non-empty subsets.
 *
 * DESCRIPTION: n is the number of distinct elements of the set
 *  to be partitioned and k is the number of non-empty subsets.
 *  The values for n < 0 or k < 0 are interpreted as 0. If you
 *
 * ACCURACY: The method returns an unsigned integer type and
 *  the size of the type 32 bits.
 *
 *
 * NOTE: this file is *NOT* part of the ceph distribution and was
 *  added by Lucas Roberts in 2023 after opening this issue
 *  https://github.com/scipy/scipy/issues/17890
 */
#include "mconf.h"
#include <stdlib.h>

long stirling2(int n, int k){
    if (n == 0 && k == 0){
        return 1L;
    }
    if (k <= 0 || k > n || n <= 0){
        return 0L;
    }
    int arraySize = k <= n - k + 1 ? k : n - k + 1;
    long *curr = malloc(arraySize * sizeof(long));
    if (!curr) {
        sf_error("stirling2", SF_ERROR_NO_RESULT, "failed to allocate memory");
        return -1L;
    }
    // initialize array to 1-here we're either doing the LHS and working to the
    // right until we get to column k or we're working with a slanted down to
    // the left array and we're scrolling that angled array from top to the
    // bottom of the parallelogram as a subset of (n,k) pairs of the Stirling
    // triangle.
    for (int i = 0; i < arraySize; i++){
        curr[i] = 1L;
    }
    if (k <= n - k + 1) {
        for (int i = 1; i < n - k + 1; i++){
            for (int j = 1; j < k; j++){
                curr[j] = (j + 1) * curr[j] + curr[j - 1];
                if (curr[j] <= 0){
                    free(curr);
                    return -2; // numeric overflow
                }
            }
        }
    } else {
        for (int i = 1; i < k; i++){
            for (int j = 1; j < n - k + 1; j++){
                curr[j] = (i + 1) * curr[j - 1] + curr[j];
                if (curr[j] <= 0){
                    free(curr);
                    return -2; // numeric overflow
                }
            }
        }
    }
    long output = curr[arraySize - 1];
    free(curr);
    return output;
}
