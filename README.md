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

[Link to commit for coverage instrumentation](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/240092b8891d198672c52f480112a9585ed9d539)
<img width="212" alt="Screenshot 2024-06-12 161958" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/727555bb-f4b8-4ec2-a297-efb0a3a27ac5">

### is_full_binary_tree:

[Link to commit for coverage instrumentation](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/240092b8891d198672c52f480112a9585ed9d539)
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

## Coverage improvement

## David Gilson

### test_tree_depth.py:

[Link to a commit the new test tree depth tests](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/5b66c6d74806727dd03a2c02ecab1f7ce34542ed#diff-719efa461e1601f23bd2d6082e80548bef79e2b6e54f709f36f704c4ab3ca06a)

#### Before adding new tests

<img width="641" alt="Screenshot 2024-06-12 163654" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/76930bf9-0b6b-489f-b5b7-9fa51ad466be">

#### After adding new tests

<img width="588" alt="Screenshot 2024-06-12 16384" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/56ceb796-6619-44fc-a663-0494d09cf512">

The coverage goes straight to 96% as it had no previous tests covering it. So by creating tests covering each branch of the depth_of_tree function, we could already cover 96% of it without needing to enchance anything, just making new tests.

### test_full_binary:

[Link to a commit the new test tree depth tests](https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/commit/5b66c6d74806727dd03a2c02ecab1f7ce34542ed#diff-61905f78e6f4c80d20903383f6e052ce4cc481462c99b605d278a1334276a8b1)

#### Before adding new tests

<img width="588" alt="Screenshot 2024-06-12 16384" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/56ceb796-6619-44fc-a663-0494d09cf512">

#### After adding new tests

<img width="840" alt="Screenshot 2024-06-12 165137" src="https://github.com/DavidGilson24/TheAlgorithms-Python-SEP/assets/100478140/b8344f1a-ecde-4d76-941c-ca0c3bc497bc">

The coverage goes straight to 97% as it had no previous tests covering it. So by creating tests covering each branch of the is_full_binary function, we could already cover 97% of it without needing to enchance anything, just making new tests.

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>
-->

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
