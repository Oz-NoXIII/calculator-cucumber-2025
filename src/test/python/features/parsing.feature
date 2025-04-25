Feature: Parsing Arithmetic Expressions
  This feature provides a range of scenarios corresponding to the
  intended external behaviour of the Expression parser.

  Scenario Outline: Parsing a simple arithmetic expression
    Given the following expression <expression>
    When I parse the expression
    Then the result should be ( <result> )

    Examples:
      | expression | result|
      | 1 + 2 | 1 + 2 |
      | 1 - 2 | 1 - 2 |
      | 1 * 2 | 1 * 2 |
      | 1 / 2 | 1 / 2 |
      | 1 ^ 2 | 1 ^ 2 |

      | + ( 1 2 ) | 1 + 2 |
      | - ( 1 2 ) | 1 - 2 |
      | * ( 1 2 ) | 1 * 2 |
      | / ( 1 2 ) | 1 / 2 |
      | ^ ( 1 2 ) | 1 ^ 2 |

      | ( 1 2 ) + | 1 + 2 |
      | ( 1 2 ) - | 1 - 2 |
      | ( 1 2 ) * | 1 * 2 |
      | ( 1 2 ) / | 1 / 2 |
      | ( 1 2 ) ^ | 1 ^ 2 |


  Scenario Outline: Parsing a negative arithmetic expression
    Given the following expression <expression>
    When I parse the expression
    Then the result should be <result>

    Examples:
      | expression | result|
      | -1 | -1 |
      | -1 + 2 | ( -1 + 2 ) |
      | -1 * 2 | ( -1 * 2 ) |
      | -1 / 2 | ( -1 / 2 ) |

      | -1 | -1 |
      | -1 + 2 | ( -1 + 2 ) |
      | -1 * 2 | ( -1 * 2 ) |
      | -1 / 2 | ( -1 / 2 ) |


  Scenario Outline: Parsing a complex arithmetic expression
  Given the following expression <expression>
  When I parse the expression
  Then the result is between ( ( ( ( 4 + 5 ) + 6 ) * ( 7 + ( ( 5 / 2 ) / 7 ) ) ) * 9 ) or ( ( 4 + 5 + 6 ) * ( 7 + ( 5 / 2 / 7 ) ) * 9 )


    Examples:
      | expression |
      | ((4 + 5 + 6) * (7 + (5 / 2 / 7)) * 9) |
      | (4 + 5 + 6) * (7 + (5 / 2 / 7)) * 9 |
      | *(+(4 5 6) +(7 /(5 2 7)) 9) |
      | ((4 5 6)+ (7 (5 2 7)/)+ 9)* |

