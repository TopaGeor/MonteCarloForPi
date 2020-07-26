# MonteCarloForPi
Calculate pi using a Monte Carlo algorithm.
A Monte Carlo algorithm is an algorithm that can produce an approximation of the result in a short time.
Here we can calculate the number pi by:
* Generate a series of random points (line 20, 21), 
* `count` how many of these `points` have euclidean norm smaller than 1 (line 22, 23),
* multiply `count` by 4 and divided by the total `points` (line 25)
* and repeat that process for `times` 

Explanation of variables:
* The variable `decimals` at line 7, sets how many decimals you want to calculate pi
* The variable `points` is how many points you will use, (100 is enough, someone can try more or less)
* The variable `times` how many times should the process be repeated
