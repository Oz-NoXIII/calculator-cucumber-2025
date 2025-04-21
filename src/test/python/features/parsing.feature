Feature: Parsing Arithmetic Expressions
  This feature provides a range of scenarios corresponding to the
  intended external behaviour of the Expression parser.

  Scenario Outline: Parsing a simple arithmetic expression
    Given the following expression 1 <op> 2
    When I parse the expression
    Then the result should be ( <result> )

    Examples:
      | op | result|
      | + | 1 + 2 |
      | - | 1 - 2 |
      | * | 1 * 2 |
      | / | 1 / 2 |