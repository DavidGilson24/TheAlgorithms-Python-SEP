# Report for Assignment 1

## Project chosen

### Name: TheAlgorithms Python

### URL: (https://github.com/subbarayudu-j/TheAlgorithms-Python)

#### Programming language: Python

## Number of lines  + Tool  

11810 python lines counted using lizard

How to: 

``` ruby
    > pip install lizard

    > lizard -l python # -l chooses the lines of the language lizard should count
```

<img width="524" alt="Screenshot_2" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/9cff3900-e610-4245-9487-3d328d67c2cb">
<img width="637" alt="Screenshot_1" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/8ca65a2c-411c-47a2-a97b-4bcc25993bf1">

## Coverage measurement with existing tool

#### Tool Used: coverage

How to: 

``` ruby
    > pip install coverage


    > coverage run -m pytest # in tests folder


    > coverage report  # or "coverage html" for a nice representation
```

### Results:

<img width="852" alt="Screenshot_3" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/3a9dabb9-b6f1-4883-ab9a-a107d2990ce9">
<img width="505" alt="Screenshot_4" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/732de1f2-ce1e-4537-bdfe-c6127156bfe3">

#### For 'coverage html'

<img width="431" alt="Screenshot_5" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/885cf24f-7990-421b-bfc1-abdcc670865e">

## Coverage measurement with our own "tool"

## David Gilson

### depth_of_tree:

[Link to commit for coverage instrumentation](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/1dddc7a05b52fffcfd7d42214c472636acc4ae78#diff-70d4ca69a6fefc96d43feaec9b654b4fba441d9371afa02e6ee485e87354ccb6)
<img width="212" alt="Screenshot 2024-06-12 161958" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/727555bb-f4b8-4ec2-a297-efb0a3a27ac5">

### is_full_binary_tree:

[Link to commit for coverage instrumentation](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/1dddc7a05b52fffcfd7d42214c472636acc4ae78#diff-70d4ca69a6fefc96d43feaec9b654b4fba441d9371afa02e6ee485e87354ccb6)
<img width="212" alt="Screenshot 2024-06-12 161958" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/727555bb-f4b8-4ec2-a297-efb0a3a27ac5">)

## Melisa Damian

### binary_search.py

[Link to the commit with coverage measurement](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/932fe9bad41abeb4a31228306a9f7a6c746640ca)
[Edited the print_coverage later on](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/85fb6e61eaeb5a554d2d6e6940bb43db2a8794af)
[Screenshot of the coverage measurement]![Screenshot 2024-06-12 211542](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/122413865/91f6fb9a-0715-4a1b-bb63-20d624ce4c17)

### bucket_sort.py

[Link to the commit with coverage measurement](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/dfdfd2e6187a52363a0248c038e43712f87a9cab)
[Screenshot of the coverage measurement]![Screenshot 2024-06-12 212839](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/122413865/9da69e31-2c0f-44f8-aead-9160ab7e1f94)

For bucket sort, the coverage should be the same for all lists except for the empty one, because all the possible inputs trigger all the branches except for the one checking for an empty list. Due to an error whenever I am attempting to input an empty list which could be fixed only by editing the code of the authors of this repo, I am unable to present that one in the screenshot.

## Ashwin Iyer

### gnome_sort.py

[[Link to the commit for gnome_sort.py]](https://github.com/subbarayudu-j/TheAlgorithms-Python/commit/8ed09f1fcd70fa8b963f7cb404f5d9895a9c4752)
[[Added more coverage]](https://github.com/subbarayudu-j/TheAlgorithms-Python/commit/89e412c5ec74b226e7860d20f62660edb1300378)

<img width="896" alt="Screenshot 2024-06-13 at 10 46 54 AM" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/122367043/e45730d4-3209-43c9-8252-74652cc5c672">

### jump_search.py

[[Link to the commit for jump_search.py]](https://github.com/subbarayudu-j/TheAlgorithms-Python/commit/cfe65cc219e8d35dfedb4d461b7e8dcf45c6a205)

<img width="883" alt="Screenshot 2024-06-13 at 10 50 32 AM" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/122367043/1368b437-3713-4c8c-8611-0772bb89d9c6">

## Patrick Darie

### bubble_sort.py

[Link to the commit with coverage measurement](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/6c45f9b2ecca196f925d3fcb92c86e76da962174)
<img width="673" alt="SCR-20240613-pkhb" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/63929969/06b0c829-6301-4cc9-b8fc-434486bd4a1c">

### merge_sort.py

[Link to the commit with coverage measurement](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/25ec6ff795751ce0758ac8b4e893a93b36b5c091)
<img width="662" alt="SCR-20240613-ppho" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/63929969/13030114-6b4d-416c-aff9-ea411f0ebf50">

# Coverage improvement

## David Gilson

### test_tree_depth.py:

[Link to a commit the new test tree depth tests](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/1dddc7a05b52fffcfd7d42214c472636acc4ae78#diff-719efa461e1601f23bd2d6082e80548bef79e2b6e54f709f36f704c4ab3ca06a)

#### Before adding new tests

<img width="641" alt="Screenshot 2024-06-12 163654" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/76930bf9-0b6b-489f-b5b7-9fa51ad466be">

#### After adding new tests

<img width="588" alt="Screenshot 2024-06-12 16384" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/56ceb796-6619-44fc-a663-0494d09cf512">

The coverage goes straight to 96% as it had no previous tests covering it. So by creating tests covering each branch of the depth_of_tree function, we could already cover 96% of it without needing to enchance anything, just making new tests.

### test_full_binary:

[Link to a commit the new test tree depth tests](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/1dddc7a05b52fffcfd7d42214c472636acc4ae78#diff-61905f78e6f4c80d20903383f6e052ce4cc481462c99b605d278a1334276a8b1)

#### Before adding new tests

<img width="588" alt="Screenshot 2024-06-12 16384" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/56ceb796-6619-44fc-a663-0494d09cf512">

#### After adding new tests

<img width="840" alt="Screenshot 2024-06-12 165137" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/b8344f1a-ecde-4d76-941c-ca0c3bc497bc">

The coverage goes straight to 97% as it had no previous tests covering it. So by creating tests covering each branch of the is_full_binary function, we could already cover 97% of it without needing to enchance anything, just making new tests.

## Melisa Damian

### test_binary_search.py

[Link to the commit](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/932fe9bad41abeb4a31228306a9f7a6c746640ca)

#### Before adding new tests

![image](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/122413865/ec7fbbcb-db4b-4090-ad0c-e056290dc480)

#### After adding new tests

![image](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/122413865/148a8ab5-8131-4b45-87af-043553eeda97)

The overall coverage for the project went lower because there are functions inside of the binary_search.py file which are not being covered by any other tests than mine. The coverage for the whole binary_search.py file is 41% due to the fact that there are multiple functions within it, and I have improved the coverage only for one of them. Furthermore, the code doesn't have any tests to cover for those missing it. Below I will provide a screenshot of the coverage html with my binary_search function.

![image](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/122413865/cfff06f7-b4b5-47a6-a145-7d368a6d98b3)

### test_bucket_sort.py

[Link to the commit](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/70b6cabcb4743dcbd0853b7376fab4e0b49cc475)

#### Before adding new tests

![image](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/122413865/148a8ab5-8131-4b45-87af-043553eeda97)

#### After adding new tests

![Screenshot 2024-06-12 222703](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/122413865/a37f0963-9bfb-4e40-a11d-fe012502abd9)

![image](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/122413865/1276aa48-2faa-4095-ab30-1d349ad4382a)

Here, the overall coverage for the project increases due to the fact that within bucket_sort.py, the only function in it is bucket_sort, which is 95% covered by the tests I've added. It's 95% because it lacks the case for an empty list, which doesn't work (mentioned above why).

## Ashwin Iyer

### jump_search.py

[Link to the commit](https://github.com/subbarayudu-j/TheAlgorithms-Python/commit/a0ddef9ae294524891426c4e8994c32ad9ac9c8d)

#### Before adding new tests
<img width="811" alt="Screenshot 2024-06-13 at 1 19 04 PM" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/122367043/bf717089-bd53-4fb0-a23e-28352de6c0b9">


#### After adding new tests
<img width="758" alt="Screenshot 2024-06-13 at 1 19 23 PM" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/122367043/d7bdbe61-8e6c-486e-b633-d81ae52324e1">

There were no previous tests for jump_search, and therefore the coverage is at 94% for test_jump_search.py. As we can see, the overall coverage has increased from 92% to 93%.
This has been achieved by creating tests for each branch of the jump_sort function.

### gnome_sort.py

[Link to the commit](https://github.com/subbarayudu-j/TheAlgorithms-Python/commit/c8aac39aacfcca1fe3a682b5a7cc400346ef0886)

#### Before adding new tests
<img width="758" alt="Screenshot 2024-06-13 at 1 19 23 PM" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/122367043/a0bb3591-7a14-4b64-9b74-29426e77ff58">

#### After adding new tests
<img width="556" alt="Screenshot 2024-06-13 at 3 02 20 PM" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/122367043/c30ef11d-c878-4122-ac73-c7864707e964">

There were no previous tests for gnome_sort and hence, the coverage for test_gnome_sort.py is 97%. As we can observe, the overall coverage has jumped from 93% to 94%. This has been achieved by creating tests for each branch of the gnome_sort function.

## Patrick Darie

### bubble_sort.py

[Link to the commit](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/c84343b232ddcc904a9c65478773ecd8be16340b)

#### Before adding new tests
<img width="1171" alt="before adding bubble" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/63929969/c2f6a24c-973e-4233-bea9-5f7a73446100">

#### After adding new tests
<img width="1170" alt="after adding bubble" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/63929969/e7ab2f0c-af13-4329-8a1b-104760ebc752">

The overall coverage goes down a bit from 92% to 86% because bubble_sort is also included in the report and it's percentage is 56% because not all the functions are tested in the file bubble_sort.py, just the main function bubble_sort(), as we can see in the html report down below the coverage for the function bubble_sort is at 100%. But we can see the coverage of the function with the test file test_bubble_sort() being at 95% this contributing to the higher overall coverage.

### merge_sort.py

[Link to the commit](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/dd0a3c186f0ceac6bf4e8fccf453ec9bc23de1b4)

#### Before adding new tests
<img width="1170" alt="after adding bubble" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/63929969/e7ab2f0c-af13-4329-8a1b-104760ebc752">

#### After adding new tests
<img width="1168" alt="after adding merge" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/63929969/9d67c123-d409-4ccc-aaf5-1dde1e714968">

We can see here the same things happening as with bubble_sort. The overall coverage goes down from 86% to 84% because the coverage report is also considering the merge_sort.py file and all of it's functions, but from the html report we can see that the coverage for merge_sort is at 100%. Adding the test to the coverage improves it, but becuase it considers also the merge_sort.py file the overall coverage is reduced

<img width="978" alt="coverage html" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/63929969/99a2a3cc-c0c6-4f1f-a2ff-bf3abb3e3b27">

# Overall

### Old Results

<img width="505" alt="Screenshot_4" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/732de1f2-ce1e-4537-bdfe-c6127156bfe3">

### New results


## Statement of individual contributions


Install Instructions
--------------------

Pygame-menu can be installed via pip. Simply run:


    $> pip install pygame-menu -U

To build the documentation from a Git repository:


    $> clone https://github.com/ppizarror/pygame-menu
    $> cd pygame-menu
    $> pip install -e ."[docs]"
    $> cd docs
    $> make html
