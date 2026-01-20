package tests;

import helpers.DriverFactory;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;

/**
 * Class containing common functionality to be inherited
 * across implementing test subclasses.
 */
public class BaseTest {
    // Make WebDriver thread-local so each test method gets its own instance
    protected ThreadLocal<WebDriver> driver = new ThreadLocal<>();

    protected static final String BASE_URL = System.getProperty("app.url");

    /**
     * Set up WebDriver instance and navigate to application page.
     */
    @BeforeMethod(alwaysRun = true)
    public void setUp() {
        driver.set(DriverFactory.getDriver());
        driver.get().manage().window().setSize(new Dimension(1920, 1080));
        driver.get().get(BASE_URL);
    }

    /**
     * Tear down WebDriver instance.
     */
    @AfterMethod(alwaysRun = true)
    public void tearDown() {
        if (driver.get() != null) {
            driver.get().quit();
            //  Remove the current thread's value for the thread-local variable
            driver.remove();
        }
    }
}
