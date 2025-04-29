Feature: Linear Equation Solver
  As a user
  I want to solve systems of linear equations
  So I can get accurate solutions

  Scenario Outline: Solving system with unique solution
    Given the system of equations "<equations>"
    When I solve the system
    Then I should get the solution "<solution>"

    Examples:
      | equations                           | solution                    |
      | 2x+3y=5;3x-4z=7;y+z=10              | x:121,y:-79,z:89             |
      | 0.5x+0.25y=1;x-y=0                  | x:1.33,y:1.33                |


  Scenario: Invalid equation format
    Given the system of equations ["2x + ? = 4"]
    When I solve the system
    Then I should get an error containing "Error solving equations"

  Scenario: Equation without equals sign
    Given the system of equations ["2x + 3y"]
    When I solve the system
    Then I should get an error containing "Error solving equations"