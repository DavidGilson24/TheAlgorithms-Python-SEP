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

-- NOT DONE YET

## Coverage improvement

-- NOT DONE YET

<!-- ### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>

-->


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
