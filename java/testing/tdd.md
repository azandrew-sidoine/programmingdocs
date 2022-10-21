# Test Driven Development in Java

JUnit 5 [https://junit.org] is the 5th version of the programmer-friendly testing framework for java

## Core Concept

- `@Test`
`@Test` is a method decorator that tells JUnit 5, that makes a method a test candidate method.

- `@ParameterizedTest`
It denotes that a method is a parameterized test method. Such methods are ihnerited unless overriden

- `@RepeatedTest`
Denotes a method is a test template for a repeated test. Such methods are ihnerited unless overriden

- `@TestFactory`
Denotes a method is a test factory for dynamic tests. Such methods are ihnerited unless overriden

- `@TestTemplate`
Denote that a method is a template for test cases, designed to be invoked multiple times depending on the number of invocation contexts returned by the registered providers.

Remaining: `@AfterEach`, `@BeforeEach`, `@AfterAll`, `@Disable` (used to disable a test class or method), `@TimeOut`

```java
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class TestClassTests {

    @Test
    void addition() {
        // Assert for equality
        assertEquals(<expected>, <actual>);
    }
}
```

**Note**
groupId: `com.h2.database` - artifactId: `h2` - scope `test`
H2 database is an in-memory database for java project to use when testing.

## AssertJ

AssertJ is a better version of JUnit 5 assertion framework.

## Mokito `org.mokito`

Moking is a JUnit 5 mocking framework.
