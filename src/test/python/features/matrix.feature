Feature: Matrix operations

  Scenario: Matrix addition
    Given I have matrix A = [[1, 2], [3, 4]]
    And I have matrix B = [[5, 6], [7, 8]]
    When I add the matrices
    Then the result matrix should be [[6, 8], [10, 12]]

  Scenario: Matrix multiplication
    Given I have matrix A = [[1, 2], [3, 4]]
    And I have matrix B = [[5, 6], [7, 8]]
    When I multiply the matrices
    Then the result matrix should be [[19, 22], [43, 50]]

  Scenario: Matrix transposition
    Given I have matrix A = [[1, 2], [3, 4]]
    When I transpose the matrix
    Then the result matrix should be [[1, 3], [2, 4]]

  Scenario: Matrix inversion
    Given I have matrix A = [[4, 7], [2, 6]]
    When I invert the matrix
    Then the result matrix should be [[0.6, -0.7], [-0.2, 0.4]]

  Scenario: Adding matrices with incompatible dimensions
    Given I have matrix A = [[1, 2]]
    And I have matrix B = [[5, 6], [7, 8]]
    When I add the matrices
    Then I should see an error message "Dies must have the same dimensions for addition"

  Scenario: Trying to invert a non-invertible matrix
    Given I have matrix A = [[1, 2], [2, 4]]
    When I invert the matrix
    Then I should see an error message "The matrix is not invertible."