package helpers;

import org.apache.commons.lang3.EnumUtils;

/**
 * Available browser types for tests.
 */
public enum BrowserType {
    CHROME,

    FIREFOX,

    SAFARI;

    /**
     * Return the browser matching the given string.
     *
     * @param value string representing desired browser type
     * @return matching browser type
     */
    public static BrowserType from(String value) {
        return EnumUtils.getEnumIgnoreCase(BrowserType.class, value);
    }
}
