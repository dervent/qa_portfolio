# Selenium Tests
This Selenium test suite contains cases for the [Swag Labs](https://www.saucedemo.com/) application.

## Running Tests
At bare minimum, this projects requires a Java 17 and Apache Maven 3.9.9.
To run tests, you may execute the following command:
```shell
mvn clean test -Dsurefire.suiteXmlFiles=testng.xml
```
Some properties are configurable during runtime. Please see the pom.xml for such properties.
