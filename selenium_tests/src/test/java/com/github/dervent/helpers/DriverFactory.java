package helpers;

import org.openqa.selenium.PageLoadStrategy;
import org.openqa.selenium.UnexpectedAlertBehaviour;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.openqa.selenium.remote.AbstractDriverOptions;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.safari.SafariDriver;
import org.openqa.selenium.safari.SafariOptions;

import java.net.MalformedURLException;
import java.net.URL;

/**
 * Factory class for handling WebDriver creation.
 */
public final class DriverFactory {

    /**
     * Private constructor.
     */
    private DriverFactory() {
    }

    /**
     * Get WebDriver appropriate for local/remote running of tests.
     *
     * @return WebDriver for running of tests
     */
    public static WebDriver getDriver() {
        BrowserType browserType = getBrowser();

        if (getGridUrl() != null && !getGridUrl().isBlank()) {
            return getRemoteDriver(browserType);
        }
        return getLocalDriver(browserType);
    }

    /**
     * Get browser type to create corresponding WebDriver instance.
     *
     * @return browser type
     */
    private static BrowserType getBrowser() {
        String browserName = System.getProperty("browser");
        BrowserType browserType = BrowserType.from(browserName);

        if (browserType == null) {
            throw new IllegalArgumentException("Browser is not supported: " + browserName);
        }
        return browserType;
    }

    /**
     * Get remote grid URL for running tests remotely.
     *
     * @return remote grid URL
     */
    private static String getGridUrl() {
        return System.getProperty("gridUrl");
    }

    /**
     * Get WebDriver instance for LOCAL running of tests.
     *
     * @param browserType browser type to determine type of WebDriver
     * @return WebDriver instance to run locally
     */
    private static WebDriver getLocalDriver(BrowserType browserType) {
        return switch (browserType) {
            case CHROME -> new ChromeDriver(getChromeOptions());
            case FIREFOX -> new FirefoxDriver(getFirefoxOptions());
            // Skip adding SafariOptions as it is very limited and often ignored
            case SAFARI -> new SafariDriver();
        };
    }

    /**
     * Get WebDriver instance for REMOTE running of tests on a grid or other server.
     *
     * @param browserType browser type to determine type of WebDriver
     * @return WebDriver instance to run remotely
     */
    private static WebDriver getRemoteDriver(BrowserType browserType) {
        try {
            URL gridUrl = new URL(getGridUrl());
            return switch (browserType) {
                case CHROME -> new RemoteWebDriver(gridUrl, getChromeOptions());
                case FIREFOX -> new RemoteWebDriver(gridUrl, getFirefoxOptions());
                case SAFARI -> new RemoteWebDriver(gridUrl, getSafarioptions());
            };
        } catch (MalformedURLException e) {
            throw new RuntimeException("Grid url is invalid: " + getGridUrl());
        }
    }

    /**
     * Apply common capabilities to use across browser-specific options.
     *
     * @param options browser-specific options
     * @return browser-specific options merged with common capabilities
     */
    private static <T extends AbstractDriverOptions<?>>
    T applyCommonCapabilities(T options) {
        options.setPageLoadStrategy(PageLoadStrategy.EAGER);
        options.setUnhandledPromptBehaviour(UnexpectedAlertBehaviour.DISMISS);
        options.setAcceptInsecureCerts(true);
        return options;
    }

    /**
     * Get options specific to ChromeDriver.
     *
     * @return ChromeDriver options
     */
    private static ChromeOptions getChromeOptions() {
        ChromeOptions options = new ChromeOptions();
        // Do not show any prompts or notifications, do not load any extensions
        options.addArguments(
                "--disable-notifications",
                "--disable-extensions"
        );
        return applyCommonCapabilities(options);
    }

    /**
     * Get options specific to FirefoxDriver.
     *
     * @return FirefoxDriver options
     */
    private static FirefoxOptions getFirefoxOptions() {
        FirefoxOptions options = new FirefoxOptions();
        // Do not show any prompts or notifications, do not load any extensions
        options.addPreference("dom.webnotifications.enabled", false);
        options.addPreference("extensions.enabledScopes", 0);
        options.addPreference("extensions.autoDisableScopes", 0);
        return applyCommonCapabilities(options);
    }

    /**
     * Get options specific to SafariDriver.
     *
     * @return SafariDriver options
     */
    private static SafariOptions getSafarioptions() {
        return applyCommonCapabilities(new SafariOptions());
    }
}
