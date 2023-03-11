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
#include <limits.h>
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
        return -2L;
    }
    /* Computes from the bottom up using the recurrence relation
     * stirling2(n, k) = k * stirling2(n, k - 1) + stirling2(n - 1, k - 1)
     * with boundary conditions: stirling2(n, 1) = 1, stirling2(n, n) = 1.
     * The below implementation only computes the Stirling numbers necessary
     * for the final result. Arranging the Stirling numbers in a triangle
     * with stirling2(1, 1) at the top, n increasing from top to bottom and
     * k increasing from left to right, to compute stirling2(n, k) one
     * only needs to compute the values in the parallelogram with vertices at
     * (1, 1), (k, k), (k, 1), (n, k). This is illustrated in the ASCII diagram
     * below for stirling2(5, 3).
     *
     * x
     * x x
     * x x x
     * o x x o
     * o o x o o
     * o o o o o o
     *
     * To minimize the memory needed, if k <= n - k + 1, an array of length k
     * is allocated and the cells of the parallelogram are filled in order from
     * left to right and then top to bottom. If k > n - k + 1, an array of
     * length n - k + 1 is allocated and the cells are filled in order from top
     * to bottom and then left to right. See
     * https://github.com/scipy/scipy/pull/18103#discussion_r1130036365
     */
    for (int i = 0; i < arraySize; i++){
        curr[i] = 1L;
    }
    long tmp;
    if (k <= n - k + 1) {
        for (int i = 1; i < n - k + 1; i++){
            for (int j = 1; j < k; j++){
	      if (curr[j] > LONG_MAX / (j + 1)) {
		free(curr);
		sf_error("stirling2", SF_ERROR_NO_RESULT,
		         "integer overflow has occured");
		return -1L;
	      }
	      tmp = curr[j] * (j + 1);
	      if (tmp > LONG_MAX - curr[j - 1]) {
		free(curr);
		sf_error("stirling2", SF_ERROR_NO_RESULT,
		         "integer overflow has occured");
		return -1L;
	      }
	      curr[j] = tmp + curr[j - 1];
            }
        }
    } else {
        for (int i = 1; i < k; i++){
            for (int j = 1; j < n - k + 1; j++){
	      if (curr[j - 1] > LONG_MAX / (i + 1)){
		free(curr);
		sf_error("stirling2", SF_ERROR_NO_RESULT,
		         "integer overflow has occured");
		return -1L;
	      }
	      tmp = curr[j - 1] * (i + 1);
	      if (tmp > LONG_MAX - curr[j]) {
		free(curr);
		sf_error("stirling2", SF_ERROR_NO_RESULT, 
		         "integer overflow has occured");
		return -1L;
	      }
	      curr[j] = tmp + curr[j];
          }
      }
  }
    long output = curr[arraySize - 1];
    free(curr);
    return output;
}
