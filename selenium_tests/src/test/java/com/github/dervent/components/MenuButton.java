package components;

import org.openqa.selenium.By;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

/**
 * Class representing hamburger menu button.
 */
public class MenuButton {
    private final WebDriver driver;
    private final WebDriverWait wait;
    private static final String SELECTOR = "react-burger-menu-btn";

    /**
     * Constructor for hamburger menu button.
     *
     * @param driver WebDriver instance
     */
    public MenuButton(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(5));
    }

    /**
     * Determine if menu button is visible.
     *
     * @return true if menu button is visible, false otherwise
     */
    public boolean isVisible() {
        try {
            WebElement element = this.wait.until(ExpectedConditions.visibilityOfElementLocated(By.id(SELECTOR)));
            return element.isDisplayed();
        } catch (TimeoutException e) {
            return false;
        }
    }
}
