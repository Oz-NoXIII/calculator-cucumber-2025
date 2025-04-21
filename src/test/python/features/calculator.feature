Feature:  Arithmetic Expressions
  This feature provides a range of scenarios corresponding to the
  intended external behaviour of arithmetic expressions on integers.

  # This is just a comment.
  # You can start with a Background: that will be run before executing each scenario.

  Background:
    Given I initialise a calculator

  # Each scenario can be seen as a test that can be executed with JUnit,
  # provided that each of the steps (Given, When, And and Then) are
  # implemented in a Java mapping file (CalculatorSteps.Java)

  Scenario: Adding two integer numbers
    Given an integer operation '+'
    When I provide a first number 4
    And I provide a second number 5
    Then the operation evaluates to 9

  Scenario: Subtracting two integer numbers
    Given an integer operation '-'
    When I provide a first number 7
    And I provide a second number 5
    Then the operation evaluates to 2

  Scenario: Multiplying two integer numbers
    Given an integer operation '*'
    When I provide a first number 7
    And I provide a second number 5
    Then the operation evaluates to 35

  Scenario: Dividing two integer numbers
    Given an integer operation '/'
    When I provide a first number 7
    And I provide a second number 5
    Then the operation evaluates to 1

  Scenario: Dividing by zero
    Given an integer operation '/'
    When I provide a first number 5
    And I provide a second number 0
    Then the operation evaluates to NaN

  Scenario: Printing the sum of two integer numbers
    Given the sum of two numbers 8 and 6
    Then its INFIX notation is ( 8 + 6 )
    And its PREFIX notation is + (8, 6)
    And its POSTFIX notation is (8, 6) +

  # This is an example of a scenario in which we provide a list of numbers as input.
  # (In fact, this is not entirely true, since what is given as input is a table of
  # strings. In this case, the table is of dimension 1 * 3 (1 line and three columns).
  Scenario: Evaluation arithmetic operations over a list of integer numbers
    Given the following list of integer numbers
      | 8 | 2 | 2 |
    Then the sum is 12
    And the product is 32
    And the difference is 4
    And the quotient is 2

  # A scenario outline (or template) is a scenario that is parameterised
  # with different values. The outline comes with a set of examples.
  # The scenario will be executed with each of the provided inputs.
  Scenario Outline: Adding two integer numbers
    Given an integer operation '+'
    When I provide a first number <n1>
    And I provide a second number <n2>
    Then the operation evaluates to <result>

    Examples:
      |n1|n2|result|
      |4|5|9|
      |5|3|8|

  Scenario Outline: Dividing two integer numbers
    Given an integer operation '/'
    When I provide a first number <n1>
    And I provide a second number <n2>
    Then the operation evaluates to <result>

    Examples:
      |n1|n2|result|
      |35|5|7|
      |7|5|1|
      |5|7|0|

  Scenario Outline: Evaluating arithmetic operations with two integer parameters
    Given an integer operation '<op>'
    When I provide a first number <n1>
    And I provide a second number <n2>
    Then the operation evaluates to <result>

    Examples:
      | op  |n1|n2|result|
      | + | 4| 5|     9|
      | - | 8| 5|     3|
      | * | 7| 2|    14|
      | / | 6| 2|     3|

  Scenario Outline: Evaluating composite expressions with a hierarchy depth higher than one
    Given an integer operation '<op>'
    When I provide an expression containing an integer operation <op2> with the following list of integer numbers
      | 3 | 4 | 5 |
    And I provide an expression containing an integer operation <op3> with the following list of integer numbers
      | 5 | 3 |
    And I provide a last number 5
    Then the operation evaluates to <result>
    Examples:
      | op | op2 | op3 | result |
      | +  |  "+"  |  "+" | 25 |
      | -  |  "-"  |  "-" | -13 |
      | *  |  "*"  |  "*" | 4500 |
      | /  |  "/"  |  "/" | 0 |
      | /  |  "+"  |  "-" | 1 |

  Scenario Outline: Testing the output notation of composite expressions with a hierarchy depth higher than one
    Given an integer operation '<op>'
    When I provide an expression containing an integer operation "<op2>" with the following list of integer numbers
      | 3 | 4 | 5 |
    And I provide an expression containing an integer operation "<op3>" with the following list of integer numbers
      | 5 | 3 |
    And I provide a last number 5
    Then its INFIX notation is ( ( 3 <op2> 4 <op2> 5 ) <op> ( 5 <op3> 3 ) <op> 5 )
    And its PREFIX notation is <op> (<op2> (3, 4, 5), <op3> (5, 3), 5)
    And its POSTFIX notation is ((3, 4, 5) <op2>, (5, 3) <op3>, 5) <op>
    Examples:
      | op | op2 | op3 |
      | /  |  +  |  - |

  Scenario: Adding two real numbers
    Given a real number 3.5
    And another real number 1.2
    When I add them
    Then the result should be 4.7

  Scenario: Negative divided by 0.0
    Given a real number -1.0
    And another real number 0.0
    When I divide them
    Then the result should be -Infinity

  Scenario: Square root of negative
    Given a real number -4.0
    When I take the square root
    Then the result should be NaN


  Scenario: Subtracting two real numbers
    Given a real number 5.0
    And another real number 2.5
    When I subtract them
    Then the result should be 2.5

  Scenario: Multiplying two real numbers
    Given a real number 3.0
    And another real number 2.0
    When I multiply them
    Then the result should be 6.0

  Scenario: Adding a negative real number
    Given a real number -1.5
    And another real number 2.0
    When I add them
    Then the result should be 0.5

  Scenario: Formatting with precision
  Given a real number 3.14159265
  When I set the precision to 4
  Then its string representation is "3.1416"

  Scenario: Scientific notation
    Given a real number 6.022574E23
    When I set the precision to 3
    Then the scientific notation is "6.023E+23"

  Scenario: Scientific notation
    Given a real number 6.022574E-23
    When I set the precision to 3
    Then the scientific notation is "6.023E-23"

  Scenario: Degrees to radians
    Given a real number 180.0
    When I convert to radians
    Then the result is approximately 3.14159265

  Scenario: Radians to degrees
    Given a real number 3.14159265
    When I convert to degrees
    Then the result is approximately 180.0


  Scenario: Multiplying by zero
    Given a real number 0.0
    And another real number 99.99
    When I multiply them
    Then the result should be 0.0


  Scenario: Adding two rational numbers
    Given a rational number 1/2
    And another rational number 1/4
    When I add them
    Then the rational result should be 3/4

  Scenario: Dividing by zero
    Given a rational number 1/2
    And another rational number 0/1
    When I divide them
    Then the result should be NaN

  Scenario: Subtracting two rational numbers
    Given a rational number 3/4
    And another rational number 1/4
    When I subtract them
    Then the rational result should be 1/2

  Scenario: Multiplying two rational numbers
    Given a rational number 2/3
    And another rational number 3/5
    When I multiply them
    Then the rational result should be 2/5

  Scenario: Dividing two rational numbers
    Given a rational number 1/2
    And another rational number 1/4
    When I divide them
    Then the rational result should be 2/1

  Scenario: Adding rational and integer
    Given a rational number 3/4
    And an integer number 1
    When I add them
    Then the rational result should be 7/4

  Scenario: Simplification of rational result
    Given a rational number 3/6
    And another rational number 3/6
    When I add them
    Then the rational result should be 1/1

  Scenario: Adding a list of rational numbers
    Given the following list of rational numbers
      | 1/2 | 1/3 | 1/6 |
    When I compute their sum
    Then the rational result should be 1/1

  Scenario: Multiplying a list of rational numbers
    Given the following list of rational numbers
      | 2/3 | 3/5 | 5/4 |
    When I compute their product
    Then the rational result should be 1/2

  Scenario: Show simplified rational in fraction form
    Given a rational number 18/12
    Then its fraction form is "3/2"

  Scenario: Show simplified rational in mixed form
    Given a rational number 18/12
    Then its mixed form is "1 1/2"

  Scenario: Negative rational in mixed form
    Given a rational number -7/3
    Then its mixed form is "-2 1/3"

  Scenario: Rational with whole result
    Given a rational number 3/1
    Then its mixed form is "3"

  Scenario: NaN rational
    Given a rational number 1/0
    Then its mixed form is "NaN"
    And its fraction form is "NaN"


  Scenario: Advanced composition
    Given a rational expression first using + with the list
      | 1/2 | 1/2 |
    And a rational expression second using - with the list
      | 1/1 | 1/2 |
    When I combine expressions first,second with *
    Then the rational result should be 1/2

  Scenario: Mixing integers and rationals in a list
    Given the following mixed list of rational and integer numbers
      | 1/2 | 1/2 | 1 |
    When I compute their sum
    Then the rational result should be 2/1

  Scenario: Adding complex numbers
    Given a complex number 2+3i
    And another complex number 1-1i
    When I add them
    Then the complex result should be 3+2i

  Scenario: Subtracting complex numbers
    Given a complex number 5+2i
    And another complex number 1+4i
    When I subtract them
    Then the complex result should be 4-2i

  Scenario: Multiplying complex numbers
    Given a complex number 1+2i
    And another complex number 3+4i
    When I multiply them
    Then the complex result should be -5+10i

  Scenario: Dividing complex numbers
    Given a complex number 1+2i
    And another complex number 3+4i
    When I divide them
    Then the complex result should be 0.44+0.08i

  Scenario: Division of complex by zero
    Given a complex number 1+2i
    And another complex number 0+0i
    When I divide them
    Then the result should be NaN

  Scenario: Getting the modulus of a complex number
    Given a complex number 3+4i
    When I get its modulus
    Then the result is approximately 5.0

  Scenario: Getting the conjugate of a complex number
    Given a complex number 2-3i
    When I get its conjugate
    Then the complex result should be 2+3i

  Scenario: Square root of a complex number
    Given a complex number -1+0i
    When I take the square root
    Then the complex result should be 0+1i


  Scenario: Logarithm of positive real number
    Given a real number 2.718281828
    When I take the logarithm
    Then the result is approximately 1.0

  Scenario: Logarithm of zero
    Given a real number 0.0
    When I take the logarithm
    Then the result should be NaN

  Scenario: Logarithm of negative real
    Given a real number -5.0
    When I take the logarithm
    Then the result should be NaN

