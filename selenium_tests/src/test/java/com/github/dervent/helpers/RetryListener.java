package helpers;

import org.testng.IAnnotationTransformer;
import org.testng.annotations.ITestAnnotation;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;

/**
 * Class for retrying each test method.
 */
public class RetryListener implements IAnnotationTransformer {

    /**
     * Set retry analyzer for each test method.
     *
     * @param annotation      test annotation
     * @param testClass       test class
     * @param testConstructor test constructor
     * @param testMethod      test method
     */
    @Override
    public void transform(ITestAnnotation annotation,
                          Class testClass,
                          Constructor testConstructor,
                          Method testMethod) {
        annotation.setRetryAnalyzer(RetryAnalyzer.class);
    }
}
