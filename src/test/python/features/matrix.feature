Feature: Matrices operations in the calculator


  Scenario: Adding two matrices of the same size with IntegerNumbers
    Given the following IntegerNumber matrix:
      | 1 | 2 |
      | 3 | 4 |
    And the following IntegerNumber matrix:
      | 5 | 6 |
      | 7 | 8 |
    When I add the matrices
    Then the result should be:
      | 6 | 8 |
      | 10 | 12 |

  Scenario: Multiplying two matrices with RealNumbers
    Given I have the following RealNumber matrix:
      | 1.5 | 2.5 |
      | 3.5 | 4.5 |
    And I have the following RealNumber matrix:
      | 5.5 | 6.5 |
      | 7.5 | 8.5 |
    When I multiply the matrices
    Then the result should be:
      | 19.0 | 22.0 |
      | 43.0 | 50.0 |

  Scenario: Transposing a matrix with RationalNumbers
    Given I have the following RationalNumber matrix:
      | 1/2 | 2/3 |
      | 3/4 | 5/6 |
    When I transpose the matrix
    Then the result should be:
      | 1/2 | 3/4 |
      | 2/3 | 5/6 |

  Scenario: Inverting a matrix with IntegerNumbers
    Given I have the following IntegerNumber matrix:
      | 4 | 7 |
      | 2 | 6 |
    When I invert the matrix
    Then the result should be:
      | 0.6 | -0.7 |
      | -0.2 | 0.4 |

  Scenario: Adding matrices with incompatible dimensions
    Given I have the following IntegerNumber matrix:
      | 1 | 2 |
    And I have the following IntegerNumber matrix:
      | 5 | 6 | 7 |
    When I add the matrices
    Then I should see an error message "Incompatible matrix dimensions for addition"

  Scenario: Trying to invert a non-invertible matrix with RationalNumbers
    Given I have the following RationalNumber matrix:
      | 1/2 | 2/3 |
      | 2/3 | 4/6 |
    When I invert the matrix
    Then I should see an error message "Matrix is not invertible"
