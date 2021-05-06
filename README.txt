Kobe O'Neil (kobeo2)
LING 406 // Spring 2019

LING 406 Final Project

How to run:

  Make sure to have NLTK first before running.

  >>> python3 baseline.py:
        runs bare-bone baseline system
    (BE WARNED: Percentages given are not multiplied by 100, I give only decimals)
    - Reads from the "bag of words" (positive-words.txt and negative-words.txt),
      cleans movie review data, and calculates the accuracy, precision, and recall the two sets.

  >>> python3 yelpEC.py:
        runs EC yelp baseline system
    (BE WARNED: Percentages given are not multiplied by 100, I give only decimals)
    (ALSO: THIS ONE TENDS TO TAKE LONGER FOR ME)
    - Reads from the "bag of words" (positive-words.txt and negative-words.txt),
      cleans YELP review data, and calculates the accuracy, precision, and recall the two sets.

Also! I cited positive-words.txt and negative-words.txt in my report rather than somewhere in my code.

Also, also! Since I can not find a way of dumping my entire movie reviews, I added individual reviews instead.
  For positive, I used cv005 for readTXTFile and cv750 for testingPath, and for negative, I used
  cv000 for readTXTFile and cv800 for testingPath, just change the path and it should work.
