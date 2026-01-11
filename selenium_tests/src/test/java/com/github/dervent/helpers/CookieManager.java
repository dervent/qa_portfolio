package helpers;

import org.openqa.selenium.Cookie;
import org.openqa.selenium.WebDriver;

/**
 * Class for managing cookies in a WebDriver session.
 */
public class CookieManager {
    private final WebDriver driver;

    /**
     * Constructor for the cookie manager.
     *
     * @param driver WebDriver instance
     */
    public CookieManager(WebDriver driver) {
        this.driver = driver;
    }

    /**
     * Get cookie by its provided name.
     *
     * @param cookieName name of cookie
     * @return Cookie object
     */
    public Cookie getCookie(String cookieName) {
        return this.driver.manage().getCookieNamed(cookieName);
    }

    /**
     * Determine if cookie is set.
     *
     * @param cookieName name of cookie
     * @return true if cookie is present and set, false otherwise
     */
    public boolean isCookiePresent(String cookieName) {
        return getCookie(cookieName) != null;
    }

    /**
     * Get string value of cookie, specified by its name
     *
     * @param cookieName name of cookie whose value needs to be retrieved
     * @return string value of cookie
     */
    public String getCookieValue(String cookieName) {
        Cookie cookie = getCookie(cookieName);
        return cookie != null ? cookie.getValue() : null;
    }
}
