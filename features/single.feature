Feature: Google\'s Search Functionality
    Scenario: can find search results
        Given I go to "https://www.google.com/ncr"
            When field with name "q" is given "BrowserStack"
            Then title becomes "BrowserStack - Google Search"
