Feature: Verify if books are added and deleted using library API

  @library
  Scenario: Verify Add book functionality
    Given The book details need to be added to library
    When we execute post api method
    Then Books are added to library
    And status code should be 201


  @library
  Scenario Outline:Verify Add book functionality
    Given The book details with <isbn> and <aisle> which need to be added to library
    When we execute post api method
    Then Books are added to library
    Examples:
      | isbn | aisle  |
      | QA |  30  |
      | QA  |  32  |



# behave --no-capture -  to run feature files with logs and with smoke tags
# behave features/BookAPI.feature --no-capture --tags=smoke

  # to run feature files and generates allure reports.
# behave features/BookAPI.feature -f allure_behave.formatter:AllureFormatter -o AllureReports

# download allure.zip, set path in env variables and give
# command as allure server pathofallurereports, then browser wil open reports.