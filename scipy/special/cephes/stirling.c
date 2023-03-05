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


int stirling2(int n, int k){
    if (k < 0 || k > n){
        return 0;
    }
    const int arraySize = n + 1;
    int prev[arraySize]; // note: requires c99
    int curr[arraySize];
    for (int i=0; i<arraySize; i++){
        prev[i] = 0;
        curr[i] = 0;
    }
    prev[0] = 1;
    if(n > 0){
        //outer for loop iterates over each row of triangle
        for (int i=1; i<arraySize; i++){
            // build up next row in curr
            for (int j=1; j<arraySize; j++){
                curr[j] = prev[j - 1];
                curr[j] += prev[j] * j;
            }
            // copy curr row to prev
            for (int j=0; j<arraySize; j++){
                prev[j] = curr[j];
            }
        }
    }
    return prev[k];
}
