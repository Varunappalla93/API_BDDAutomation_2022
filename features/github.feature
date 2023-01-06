Feature: Verify Github API validation
  Scenario: Session Management Verification
    Given I have github creds
    When I hit gitrepo api
    Then status code should be 200