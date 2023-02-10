# Future Capital Coding Interview Submission

## Execution Instructions

Please view this file in its markdown format instead of its raw text format.

1) Fork this repository
2) Clone that forked repository locally
3) Using the command line, navigate to that repository's `backend` folder
4) Using the command line, execute the test cases below

IMPORTANT NOTEs: 
- Every test case must start with `python` to properly execute. 
- Do not add spaces for the input. 
- Do not include `=>` in commands. `=>` refers to the output of each test case.
- The functions support floating numbers so there are small (10^-10) floating point errors

### Part 1

For Part 1, please enter the following commands to test its functionality. Note that each command must start with `python ./app.py -part1`

#### Test Cases

- Wrong ticker name
  - `python ./app.py -part1 fb:12,PLTR:5000` => `KeyError`
  - `python ./app.py -part1 AAPL:34,TSLA:3` => `KeyError`
  - `python ./app.py -part1 FB:34,30:45` => `KeyError`
- Invalid input format
  - `python ./app.py -part1 FB,PLTR:5000` => `SyntaxError`
  - `python ./app.py -part1 12:FB,TSLA:40` => `ValueError`
  - `python ./app.py -part1 FB:300,,` => `SyntaxError`
  - `python ./app.py -part1 FB:12,WISH:` => `ValueError`
- Positive integers for portfolio
  - `python ./app.py -part1 FB:12,PLTR:5000` => `119887.4` <------------------- Given Test Case
  - `python ./app.py -part1 BABA:1,TSLA:5,WISH:1200` => `9891.9` <------------- Given Test Case
- Positive floating numbers for portfolio
  - `python ./app.py -part1 FB:12.5,PLTR:500.33` => `15657.030999999999`
  - `python ./app.py -part1 BABA:1,TSLA:5.62,WISH:1200` => `10376.4548`
- Negative numbers for portfolio
  - `python ./app.py -part1 FB:-12,PLTR:5000` => `ValueError`
- No stock for a given ticker
  - `python ./app.py -part1 TSLA:0,WISH:0` => `0.0`
  - `python ./app.py -part1 TSLA:0,WISH:0,FB:3` => `971.8499999999999`

### Part 2

For Part 2, please enter the following commands to test its functionality. Note that each command must start with `python ./app.py -part2`

#### Test Cases

- Invalid input format
  - `python ./app.py -part2 7,,` => `ValueError`
- Negative stock prices
  - `python ./app.py -part2 7,3,-4` => `ValueError`
- Integer stock prices
  - `python ./app.py -part2 7,1,5,3,6,4` => `5.0` <--------------------- Given Test Case
- Floating stock prices
  - `python ./app.py -part2 1.6,3.5,5.8,1.1,7.9` => `6.800000000000001`
- Decreasing stock prices
  - `python ./app.py -part2 7,6,4,3,1` => `0` <----------------------- Given Test Case
- Increasing stock prices
  - `python ./app.py -part2 2,5,8,10` = > `8.0`
- Mixed stock prices
  - `python ./app.py -part2 4,10.83,3.6,25,35.38,6` => `31.78`
