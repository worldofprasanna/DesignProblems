
**TDD**

Recently was playing with Python Koans. It was very good to practice python and could get the flavour of TDD. Implemented one of the solution using TDD and it can be seen in the commit history.


*problem*:

 Greed is a dice game where you roll up to five dice to accumulate
 points.  The following "score" function will be used calculate the
 score of a single roll of the dice.

 A greed roll is scored as follows:

 * A set of three ones is 1000 points

 * A set of three numbers (other than ones) is worth 100 times the
   number. (e.g. three fives is 500 points).

 * A one (that is not part of a set of three) is worth 100 points.

 * A five (that is not part of a set of three) is worth 50 points.

 * Everything else is worth 0 points.


 Examples:

```
 score([1,1,1,5,1]) => 1150 points
 score([2,3,4,6,2]) => 0 points
 score([3,4,5,3,3]) => 350 points
 score([1,5,1,2,4]) => 250 points
```
