package helpers;

import org.testng.IRetryAnalyzer;
import org.testng.ITestResult;


/**
 * Class for retrying failed tests up to a set number of times.
 */
public class RetryAnalyzer implements IRetryAnalyzer {

    private int retryCount = 0;
    private static final int MAX_RETRY_COUNT = Integer.parseInt(System.getProperty("retry.count","2"));

    /**
     * Retry a failed test up to the provided max number of times.
     *
     * @param testResult test result
     * @return true if test should be retried, false otherwise.
     */
    @Override
    public boolean retry(ITestResult testResult) {
        if (retryCount < MAX_RETRY_COUNT) {
            retryCount++;
            return true;
        }
        return false;
    }
}
