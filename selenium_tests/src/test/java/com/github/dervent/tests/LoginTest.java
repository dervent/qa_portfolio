package tests;

import components.LoginErrorMessageBox;
import components.MenuButton;
import helpers.CookieManager;
import org.testng.annotations.*;
import pages.LoginPage;

import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertTrue;

/**
 * Class for testing the login feature of Swag Labs.
 */
public class LoginTest extends BaseTest {
    // User credentials
    private static final String STANDARD_USER = "standard_user";
    private static final String PASSWORD = "secret_sauce";

    // Cookie name that is set after a login session begins
    private static final String SESSION_COOKIE_NAME = "session-username";

    /**
     * Test successful login to Swag Labs.
     */
    @Test
    public void testLoginSuccess() {
        LoginPage loginPage = new LoginPage(driver.get());
        MenuButton menuButton = new MenuButton(driver.get());
        CookieManager cookieManager = new CookieManager(driver.get());

        loginPage.login(STANDARD_USER, PASSWORD);

        // Verify user is successfully redirected to application and session cookie is set
        assertTrue(menuButton.isVisible(),
                "Menu button not visible. User may not have logged in successfully.");
        assertTrue(cookieManager.isCookiePresent(SESSION_COOKIE_NAME));
        assertEquals(cookieManager.getCookieValue(SESSION_COOKIE_NAME), STANDARD_USER);
    }

    /**
     * Get invalid credentials and corresponding error messages displayed on login page.
     *
     * @return invalid credentials and corresponding error messages
     */
    @DataProvider(parallel = true)
    public Object[][] invalidCredentialsAndMessages() {
        return new Object[][]{
                // Username but no password
                {STANDARD_USER, "", "Password is required"},

                // Password but no username
                {"", PASSWORD, "Username is required"},

                // No username or password
                {"", "", "Username is required"},

                // Username and password not matching any existing user
                {"invalid_username", PASSWORD, "Username and password do not match any user in this service"},

                // Username and password matching a locked out user
                {"locked_out_user", PASSWORD, "Sorry, this user has been locked out."}
        };
    }

    /**
     * Test failed login to Swag Labs using various invalid combinations of credentials.
     *
     * @param username     username
     * @param password     password
     * @param errorMessage corresponding error message
     */
    @Test(dataProvider = "invalidCredentialsAndMessages")
    public void testLoginFailure(String username, String password, String errorMessage) {
        LoginPage loginPage = new LoginPage(driver.get());
        LoginErrorMessageBox loginErrorMessageBox = new LoginErrorMessageBox(driver.get());

        loginPage.login(username, password);

        // Verify presence of error message and its text content
        assertTrue(loginErrorMessageBox.isVisible(), "User should see error message on " +
                "login screen, upon failed authentication.");
        assertEquals(loginErrorMessageBox.getMessage(),
                String.format("Epic sadface: %s", errorMessage));
    }
}
