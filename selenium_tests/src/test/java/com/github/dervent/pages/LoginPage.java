package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

/**
 * Class representing the login page.
 */
public class LoginPage {
    private final WebDriver driver;
    private final WebDriverWait wait;

    @FindBy(id = "user-name")
    private WebElement usernameTextBox;

    @FindBy(id = "password")
    private WebElement passwordTextBox;

    @FindBy(id = "login-button")
    private WebElement loginButton;

    /**
     * Constructor for the login page.
     *
     * @param driver WebDriver instance
     */
    public LoginPage(WebDriver driver) {
        this.driver = driver;
        int waitTimeout = Integer.parseInt(System.getProperty("wait.timeout", "5"));
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(waitTimeout));
        PageFactory.initElements(driver, this);
    }

    /**
     * Enter username into the username field.
     *
     * @param username user's username
     */
    public void enterUsername(String username) {
        this.wait.until(ExpectedConditions.visibilityOf(usernameTextBox));
        this.usernameTextBox.clear();
        this.usernameTextBox.sendKeys(username);
    }

    /**
     * Enter password into the password field.
     *
     * @param password user's password
     */
    public void enterPassword(String password) {
        this.wait.until(ExpectedConditions.visibilityOf(passwordTextBox));
        this.passwordTextBox.clear();
        this.passwordTextBox.sendKeys(password);
    }

    /**
     * Click the login button.
     */
    public void clickLoginButton() {
        this.wait.until(ExpectedConditions.elementToBeClickable(loginButton));
        this.loginButton.click();
    }

    /**
     * Log in with the provided username and password
     *
     * @param username user's username
     * @param password user's password
     */
    public void login(String username, String password) {
        this.enterUsername(username);
        this.enterPassword(password);
        this.clickLoginButton();
    }
}
