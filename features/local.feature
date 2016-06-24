Feature: BrowserStack Local Testing
    Scenario: can check tunnel working
        Given I go to "http://bs-local.com:45691/check"
            Then page contains "Up and running"
