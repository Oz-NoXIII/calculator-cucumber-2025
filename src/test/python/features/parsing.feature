Feature: Parsing Arithmetic Expressions
  This feature provides a range of scenarios corresponding to the
  intended external behaviour of the Expression parser.

  Scenario Outline: Parsing a simple arithmetic integer expression
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
      | +(1,2) | 1 + 2 |
      | -(1,2) | 1 - 2 |
      | *(1,2) | 1 * 2 |
      | /(1,2) | 1 / 2 |
      | ^(1,2) | 1 ^ 2 |

      | ( 1 2 ) + | 1 + 2 |
      | ( 1 2 ) - | 1 - 2 |
      | ( 1 2 ) * | 1 * 2 |
      | ( 1 2 ) / | 1 / 2 |
      | ( 1 2 ) ^ | 1 ^ 2 |
      | (1,2)+ | 1 + 2 |
      | (1,2)- | 1 - 2 |
      | (1,2)* | 1 * 2 |
      | (1,2)/ | 1 / 2 |
      | (1,2)^ | 1 ^ 2 |


  Scenario Outline: Parsing a negative arithmetic integer expression
    Given the following expression <expression>
    When I parse the expression
    Then the result should be <result>

    Examples:
      | expression | result|
      | (-1) | ( 1 * -1 ) |
      | (-1) + 2 | ( ( 1 * -1 ) + 2 ) |
      | (-1) * 2 | ( ( 1 * -1 ) * 2 ) |
      | (-1) / 2 | ( ( 1 * -1 ) / 2 ) |

      | (- (1 + 2)) | ( ( 1 + 2 ) * -1 ) |
      | (- (1 * 2)) | ( ( 1 * 2 ) * -1 ) |
      | (- (1 / 2)) | ( ( 1 / 2 ) * -1 ) |


  Scenario Outline: Parsing a complex arithmetic integer expression
  Given the following expression <expression>
  When I parse the expression
  Then the result is between ( ( ( ( 4 + 5 ) + 6 ) * ( 7 + ( ( 5 / 2 ) / 7 ) ) ) * 9 ) or ( ( 4 + 5 + 6 ) * ( 7 + ( 5 / 2 / 7 ) ) * 9 )


    Examples:
      | expression |
      | ((4 + 5 + 6) * (7 + (5 / 2 / 7)) * 9) |
      | (4 + 5 + 6) * (7 + (5 / 2 / 7)) * 9 |
      | *(+(4 5 6) +(7 /(5 2 7)) 9) |
      | ((4 5 6)+ (7 (5 2 7)/)+ 9)* |
      | *(+(4,5,6),+(7,/(5,2,7)),9) |
      | ((4,5,6)+,(7,(5,2,7)/)+,9)* |
      | ( ( ( ( 4 + 5 ) + 6 ) * ( 7 + ( ( 5 / 2 ) / 7 ) ) ) * 9 ) |
      | ( ( 4 + 5 ) + 6 ) * ( 7 + ( ( 5 / 2 ) / 7 ) ) * 9 |


  Scenario Outline: Parsing simple real number expressions
    Given the following expression <expression>
    When I parse the expression
    Then the result should be ( <result> )

    Examples:
      # Infix notation
      | expression | result       |
      | 1.5 + 2.25 | 1.5 + 2.25   |
      | 3.14 - 0.5 | 3.14 - 0.5   |
      | 2.5 * 1.5  | 2.5 * 1.5    |
      | 5.0 / 2.0  | 5 / 2    |

      # Prefix notation
      | + ( 1.5 2.25 )  | 1.5 + 2.25   |
      | - ( 3.14 0.5 )  | 3.14 - 0.5   |
      | * ( 2.5 1.5 )   | 2.5 * 1.5    |
      | / ( 5.0 2.0 )   | 5 / 2    |

      # Postfix notation
      | ( 1.5 2.25 ) +  | 1.5 + 2.25   |
      | ( 3.14 0.5 ) -  | 3.14 - 0.5   |
      | ( 2.5 1.5 ) *   | 2.5 * 1.5    |
      | ( 5.0 2.0 ) /   | 5 / 2    |

  Scenario Outline: Parsing complex number expressions
    Given the following expression <expression>
    When I parse the expression
    Then the result should be ( <result> )

    Examples:
      # Infix notation
      | expression        | result            |
      | (3+4j) + (1+2j)  | ( 3 + 4j ) + ( 1 + 2j ) |
      | (5-2j) - (3+1j)  | ( 5 - 2j ) - ( 3 + 1j ) |
      | (2+3j) * (1-4j)  | ( 2 + 3j ) * ( 1 - 4j ) |
      | (6+3j) / (2-1j)  | ( 6 + 3j ) / ( 2 - 1j ) |

      # Prefix notation
      | + ( +(3 4j) +(1 2j) )      | ( 3 + 4j ) + ( 1 + 2j ) |
      | - ( -(5 2j) +(3 1j) )      | ( 5 - 2j ) - ( 3 + 1j ) |
      | * ( +(2 3j) -(1 4j) )      | ( 2 + 3j ) * ( 1 - 4j ) |
      | / ( +(6 3j) -(2 1j) )      | ( 6 + 3j ) / ( 2 - 1j ) |

      # Postfix notation
      | ( (3 4j)+ (1 2j)+ ) +      | ( 3 + 4j ) + ( 1 + 2j ) |
      | ( (5 2j)- (3 1j)+ ) -      | ( 5 - 2j ) - ( 3 + 1j ) |
      | ( (2 3j)+ (1 4j)- ) *      | ( 2 + 3j ) * ( 1 - 4j ) |
      | ( (6 3j)+ (2 1j)- ) /      | ( 6 + 3j ) / ( 2 - 1j ) |

  Scenario Outline: Parsing mixed real and complex expressions
    Given the following expression <expression>
    When I parse the expression
    Then the result should be ( <result> )

    Examples:
      # Infix notation
      | expression           | result |
      | 2.5 * (3+1j)         | 2.5 * ( 3 + 1j ) |
      | (4 - 2j) / 2.0         | ( 4 - 2j ) / 2 |
      | 1.5 + (2+3j) - 0.5   | ( 1.5 + ( 2 + 3j ) ) - 0.5 |

      # Prefix notation
      | * ( 2.5 +(3 1j) )           | 2.5 * ( 3 + 1j ) |
      | / ( -(4 2j) 2.0 )           | ( 4 - 2j ) / 2 |
      | - ( + ( 1.5 +(2 3j) ) 0.5 ) | ( 1.5 + ( 2 + 3j ) ) - 0.5 |

      # Postfix notation
      | ( 2.5 (3 1j)+ ) *           | 2.5 * ( 3 + 1j ) |
      | ( (4 2j)- 2.0 ) /           | ( 4 - 2j ) / 2 |
      | ( ( 1.5 (2 3j)+ ) + 0.5 ) - | ( 1.5 + ( 2 + 3j ) ) - 0.5 |

  Scenario Outline: Parsing complex expressions with parentheses
    Given the following expression <expression>
    When I parse the expression
    Then the result should be ( <result> )

    Examples:
      | expression                                    | result                           |
      | ((2+3j) * (1-4j)) + ((5+2j) / 2.0)            | ( ( 2 + 3j ) * ( 1 - 4j ) ) + ( ( 5 + 2j ) / 2 ) |
      | + ( * ( +(2 3j) -(1 4j) ) / ( +(5 2j) 2.0 ) ) | ( ( 2 + 3j ) * ( 1 - 4j ) ) + ( ( 5 + 2j ) / 2 ) |
      | ( ( (2 3j)+ (1 4j)- ) * ( (5 2j)+ 2.0 ) / ) + | ( ( 2 + 3j ) * ( 1 - 4j ) ) + ( ( 5 + 2j ) / 2 ) |



