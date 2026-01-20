package components;

import org.openqa.selenium.By;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

/**
 * Class representing container that holds error messages on the login page.
 */
public class LoginErrorMessageBox {
    private final WebDriver driver;
    private final WebDriverWait wait;
    private static final String SELECTOR = "div.error-message-container";

    /**
     * Constructor the login error message box.
     *
     * @param driver WebDriver instance.
     */
    public LoginErrorMessageBox(WebDriver driver) {
        this.driver = driver;
        int waitTimeout = Integer.parseInt(System.getProperty("wait.timeout", "5"));
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(waitTimeout));
    }

    /**
     * Determine if error message box is visible.
     *
     * @return true if error message box is visible, false otherwise
     */
    public boolean isVisible() {
        try {
            return wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(SELECTOR))).isDisplayed();
        } catch (TimeoutException e) {
            return false;
        }
    }

    /**
     * Get string contained within error message box.
     *
     * @return error message string
     */
    public String getMessage() {
        try {
            return wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(SELECTOR))).getText().trim();
        } catch (TimeoutException e) {
            return null;
        }
    }
}
