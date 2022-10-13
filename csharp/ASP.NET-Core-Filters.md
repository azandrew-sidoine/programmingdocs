# ASP.NET Core Filters

--- How filters work

Filters run within the ASP.NET Core action invocation pipeline, sometimes referred to as the filter pipeline. The filter pipeline runs after ASP.NET Core selects the action to execute.

Request -> [{Middleware}] -> [{Middleware}] -> {CallMVCAction} -> {Filter} -> {Response}

--- Filter Types

Each filter type is executed at a different stage in the filter pipeline:

- `Authorization filters`: run first and are used to determine whether the user is authorized for the request. Authorization filters short-circuit the pipeline if the request is not authorized.

- `Resource filters:`: Runs after authorization.

[OnResourceExecuting] runs code before the rest of the filter pipeline. For example, [OnResourceExecuting] runs code before model binding.
[OnResourceExecuted] runs code after the rest of the pipeline has completed.

- `Action filters`: Run code immediately before and after an action method is called. It's not supported by Razor Pages. It can be used to:
    * Can change the arguments passed into an action.
    * Can change the result returned from the action.

- `Exception filters` apply global policies to unhandled exceptions that occur before the response body has been written to.

- `Result filters` run code immediately before and after the execution of action results. They run only when the action method has executed successfully. They are useful for logic that must surround view or formatter execution.

### Action filters

They must implements [IActionFilter] interface

--- Synchronous filters

```cs

public class MySampleActionFilter : IActionFilter 
{
    public void OnActionExecuting(ActionExecutingContext context)
    {
        var httpContext = context.HttpContext;
        // Runs logic before action executes...
    }

    public void OnActionExecuted(ActionExecutedContext context)
    {
        var httpContext = context.HttpContext;
        // Runs logic after action execute
    }
}

```

--- Async action filters

```cs
public class SampleAsyncActionFilter : IAsyncActionFilter
{
    public async Task OnActionExecutionAsync(
        ActionExecutingContext context,
        ActionExecutionDelegate next)
    {
        // Do something before the action executes
        var resultContext = await next();
        // resultContext.Result is set.
        // Do something after the action executes
    }
}
```

## Multiple filters stage

Interfaces for multiple filter stages can be implemented in a single class. For example, the [ActionFilterAttribute] class implements:

* Synchronous: IActionFilter and IResultFilter
* Asynchronous: IAsyncActionFilter and IAsyncResultFilter
* IOrderedFilter

Note: Implement either the synchronous or the async version of a filter interface, not both.

### Built-in filter attributes

ASP.NET Core includes built-in attribute-based filters that can be subclassed and customized. For example, the following result filter adds a header to the response:

```cs
/// Attributes allow filters to accept arguments.
public class AddHeaderAttribute : ResultFilterAttribute
{
    private readonly string _name;
    private readonly string _value;

    public AddHeaderAttribute(string name, string value)
    {
        _name = name;
        _value = value;
    }

    public override void OnResultExecuting(ResultExecutingContext context)
    {
        context.HttpContext.Response.Headers.Add( _name, new string[] { _value });
        base.OnResultExecuting(context);
    }
}

/// Apply the AddHeaderAttribute to a controller or action method and specify the name and value of the HTTP header:

[AddHeader("Author", "Rick Anderson")]
public class SampleController : Controller
{
    // Provide Actions implementations
}
```

```cs
// Injecting to FilterAttributes
public class MyActionFilterAttribute : ActionFilterAttribute
{
    private readonly PositionOptions _settings;

    public MyActionFilterAttribute(IOptions<PositionOptions> options)
    {
        _settings = options.Value;
        Order = 1;
    }

    public override void OnResultExecuting(ResultExecutingContext context)
    {
        context.HttpContext.Response.Headers.Add(_settings.Title, 
                                                 new string[] { _settings.Name });
        base.OnResultExecuting(context);
    }
}

// Startup.cs
// ...
    services.Configure<PositionOptions>(
             Configuration.GetSection("Position"));
    services.AddScoped<MyActionFilterAttribute>();
// ...

[AddHeader("Author", "Rick Anderson")]
public class SampleController : Controller
{
    // ...

    [ServiceFilter(typeof(MyActionFilterAttribute))]
    public IActionResult Index()
    {
        return Content("Header values by configuration.");
    }
}
```

Note: Several of the filter interfaces have corresponding attributes that can be used as base classes for custom implementations.
[ActionFilterAttribute], [ExceptionFilterAttribute], [ResultFilterAttribute], [FormatFilterAttribute], [ServiceFilterAttribute], [TypeFilterAttribute]


## Filter scopes and order of execution

- Using an attribute on a controller action. Filter attributes cannot be applied to Razor Pages handler methods.

- Using an attribute on a controller or Razor Page.

- Globally for all controllers, actions, and Razor Pages as shown in the following code:

```cs
// Startup.cs
public void ConfigureServices(IServiceCollection services)
{
    // ...
    services.AddControllersWithViews(options =>
   {
        options.Filters.Add(typeof(MySampleActionFilter));
    });
}
// ...
```

{OnActionExecuting[GLobal]} -> {OnActionExecuting[Controller|RazorPage]} -> {OnActionExecuting[Method]} -> {OnActionExecuted[Method]} -> {OnActionExecuted[Controller|RazorPage]} -> {OnActionExecuted[Global]}

--- Controller level filters

Every controller that inherits from the Controller base class includes Controller.OnActionExecuting, Controller.OnActionExecutionAsync, and Controller.OnActionExecuted OnActionExecuted methods. These methods:

### Cancellation and short-circuiting

The filter pipeline can be short-circuited by setting the Result property on the ResourceExecutingContext parameter provided to the filter method. For instance, the following Resource filter prevents the rest of the pipeline from executing:

```cs
public class ShortCircuitingResourceFilterAttribute : Attribute, IResourceFilter
{
    public void OnResourceExecuting(ResourceExecutingContext context)
    {
        context.Result = new ContentResult()
        {
            Content = "Resource unavailable - header not set."
        };
    }

    public void OnResourceExecuted(ResourceExecutedContext context)
    {
    }
}
```

## Dependency injection

Filters can be added by type or by instance. If an instance is added, that instance is used for every request. If a type is added, it's type-activated. A type-activated filter means:

* An instance is created for each request.
* Any constructor dependencies are populated by dependency injection (DI).

Filters that are implemented as attributes and added directly to controller classes or action methods cannot have constructor dependencies provided by dependency injection (DI). Constructor dependencies cannot be provided by DI because:

* Attributes must have their constructor parameters supplied where they're applied.
* This is a limitation of how attributes work.

But:

The following filters support constructor dependencies provided from DI:
- ServiceFilterAttribute
- TypeFilterAttribute
- IFilterFactory implemented on the attribute.

--- ServiceFilterAttribute

Service filter implementation types are registered in ConfigureServices. A ServiceFilterAttribute retrieves an instance of the filter from DI.

ServiceFilterAttribute implements IFilterFactory. IFilterFactory exposes the CreateInstance method for creating an IFilterMetadata instance. CreateInstance loads the specified type from DI.

```cs
public class AddHeaderResultServiceFilter : IResultFilter
{
    private ILogger _logger;
    public AddHeaderResultServiceFilter(ILoggerFactory loggerFactory)
    {
        _logger = loggerFactory.CreateLogger<AddHeaderResultServiceFilter>();
    }

    public void OnResultExecuting(ResultExecutingContext context)
    {
        // Perform logic before action execution
    }

    public void OnResultExecuted(ResultExecutedContext context)
    {
        // Perform logic after action execution
    }
}

// Startup.cs
public void ConfigureServices(IServiceCollection services)
{
    // Add service filters.
    services.AddScoped<AddHeaderResultServiceFilter>();
    // ...
}

// Controller
[ServiceFilter(typeof(AddHeaderResultServiceFilter))]
public IActionResult Index()
{
    return View();
}
```

Cons:

Should not be used with a filter that depends on services with a lifetime other than singleton.

--- TypeFilterAttribute

TypeFilterAttribute is similar to ServiceFilterAttribute, but its type isn't resolved directly from the DI container. It instantiates the type by using [Microsoft.Extensions.DependencyInjection.ObjectFactory].

Because TypeFilterAttribute types aren't resolved directly from the DI container:

* Types that are referenced using the [TypeFilterAttribute] don't need to be registered with the DI container. They do have their dependencies fulfilled by the DI container.

* [TypeFilterAttribute] can optionally accept constructor arguments for the type.

Note : Should not be used with a filter that depends on services with a lifetime other than singleton.

## Authorization filters

Authorization filters:

* Are the first filters run in the filter pipeline.
* Control access to action methods.
* Have a before method, but no after method.

Custom authorization filters require a custom authorization framework. Prefer configuring the authorization policies or writing a custom authorization policy over writing a custom filter. The built-in authorization filter:

* Calls the authorization system.
* Does not authorize requests.

Do not throw exceptions within authorization filters:

* The exception will not be handled.
* Exception filters will not handle the exception.

Consider issuing a challenge when an exception occurs in an authorization filter.

## Resource filters

Resource filters:

* Implement either the [IResourceFilter] or [IAsyncResourceFilter] interface.
* Execution wraps most of the filter pipeline.
* Only Authorization filters run before resource filters.

Resource filters are useful to short-circuit most of the pipeline. For example, a caching filter can avoid the rest of the pipeline on a cache hit.

## Action filters

Action filters do not apply to Razor Pages. Razor Pages supports IPageFilter and IAsyncPageFilter . For more information, see Filter methods for Razor Pages.

Action filters:

* Implement either the [IActionFilter] or [IAsyncActionFilter] interface.
* Their execution surrounds the execution of action methods.

```cs
public class MySampleActionFilter : IActionFilter 
{
    public void OnActionExecuting(ActionExecutingContext context)
    {
        // Do something before the action executes.
    }

    public void OnActionExecuted(ActionExecutedContext context)
    {
        // Do something after the action executes.
    }
}
```

The [ActionExecutingContext] provides the following properties:

* ActionArguments - enables reading the inputs to an action method.
* Controller - enables manipulating the controller instance.
* Result - setting Result short-circuits execution of the action method and subsequent action filters.

Throwing an exception in an action method:

* Prevents running of subsequent filters.
* Unlike setting Result, is treated as a failure instead of a successful result.

The [ActionExecutedContext] provides Controller and Result plus the following properties:

* Canceled - True if the action execution was short-circuited by another filter.
* Exception - Non-null if the action or a previously run action filter threw an exception. Setting this property to null:
    * Effectively handles the exception.
    * Result is executed as if it was returned from the action method.

For an [IAsyncActionFilter], a call to the ActionExecutionDelegate:

* Executes any subsequent action filters and the action method.
* Returns [ActionExecutedContext].

To short-circuit, assign [Microsoft.AspNetCore.Mvc.Filters.ActionExecutingContext.Result] to a result instance and don't call next (the [ActionExecutionDelegate]).

The framework provides an abstract [ActionFilterAttribute] that can be subclassed.
The [OnActionExecuting] action filter can be used to:

The [OnActionExecuted] method runs after the action method:

* And can see and manipulate the results of the action through the Result property.
* Canceled is set to true if the action execution was short-circuited by another filter.
* Exception is set to a non-null value if the action or a subsequent action filter threw an exception. Setting [Exception] to null:
    * Effectively handles an exception.
    * [ActionExecutedContext.Result] is executed as if it were returned normally from the action method.

```cs
public class ValidateModelAttribute : ActionFilterAttribute
{
    public override void OnActionExecuting(ActionExecutingContext 
                                           context)
    {
        if (!context.ModelState.IsValid)
        {
            context.Result = new BadRequestObjectResult(
                                                context.ModelState);
        }
    }


    public override void OnActionExecuted(ActionExecutedContext 
                                          context)
    {
        var result = context.Result;
        // Do something with Result.
        if (context.Canceled == true)
        {
            // Action execution was short-circuited by another filter.
        }

        if(context.Exception != null)
        {
            // Exception thrown by action or action filter.
            // Set to null to handle the exception.
            context.Exception = null;
        }
        base.OnActionExecuted(context);
    }
}
```

## Exception filters

Exception filters:

* Implement [IExceptionFilter] or [IAsyncExceptionFilter].
* Can be used to implement common error handling policies.

```cs
public class CustomExceptionFilter : IExceptionFilter
{
    private readonly IWebHostEnvironment _hostingEnvironment;
    private readonly IModelMetadataProvider _modelMetadataProvider;

    public CustomExceptionFilter(
        IWebHostEnvironment hostingEnvironment,
        IModelMetadataProvider modelMetadataProvider)
    {
        _hostingEnvironment = hostingEnvironment;
        _modelMetadataProvider = modelMetadataProvider;
    }

    public void OnException(ExceptionContext context)
    {
        if (!_hostingEnvironment.IsDevelopment())
        {
            return;
        }
        var result = new ViewResult {ViewName = "CustomError"};
        result.ViewData = new ViewDataDictionary(_modelMetadataProvider,
                                                    context.ModelState);
        result.ViewData.Add("Exception", context.Exception);
        // TODO: Pass additional detailed data via ViewData
        context.Result = result;
    }
}

```

Exception filters:

* Don't have before and after events.
* Implement OnException or OnExceptionAsync.
* Handle unhandled exceptions that occur in Razor Page or controller creation, model binding, action filters, or action methods.
* Do not catch exceptions that occur in resource filters, result filters, or MVC result execution.

Exception filters:
* Are good for trapping exceptions that occur within actions.
* Are not as flexible as error handling middleware.

## Result filters

Result filters:

* Implement an interface: [IResultFilter] or [IAsyncResultFilter] [IAlwaysRunResultFilter] or [IAsyncAlwaysRunResultFilter]

* Their execution surrounds the execution of action results.

### IResultFilter and IAsyncResultFilter

The following code shows a result filter that adds an HTTP header:

```cs
public class AddHeaderResultServiceFilter : IResultFilter
{
    private ILogger _logger;
    public AddHeaderResultServiceFilter(ILoggerFactory loggerFactory)
    {
        _logger = loggerFactory.CreateLogger<AddHeaderResultServiceFilter>();
    }

    public void OnResultExecuting(ResultExecutingContext context)
    {
        var headerName = "OnResultExecuting";
        context.HttpContext.Response.Headers.Add(
            headerName, new string[] { "ResultExecutingSuccessfully" });
        _logger.LogInformation("Header added: {HeaderName}", headerName);
    }

    public void OnResultExecuted(ResultExecutedContext context)
    {
        // Can't add to headers here because response has started.
        _logger.LogInformation("AddHeaderResultServiceFilter.OnResultExecuted");
    }
}
```

### IAlwaysRunResultFilter and IAsyncAlwaysRunResultFilter

The [IAlwaysRunResultFilter] and [IAsyncAlwaysRunResultFilter] interfaces declare an IResultFilter implementation that runs for all action results. This includes action results produced by:
Authorization filters and resource filters that short-circuit.
Exception filters.

```cs
// For example, the following filter always runs and sets an action result (ObjectResult) with a 422 Unprocessable Entity status code when content negotiation fails:
public class UnprocessableResultFilter : Attribute, IAlwaysRunResultFilter
{
    public void OnResultExecuting(ResultExecutingContext context)
    {
        if (context.Result is StatusCodeResult statusCodeResult &&
            statusCodeResult.StatusCode == (int) HttpStatusCode.UnsupportedMediaType)
        {
            context.Result = new ObjectResult("Can't process this!")
            {
                StatusCode = (int) HttpStatusCode.UnsupportedMediaType,
            };
        }
    }

    public void OnResultExecuted(ResultExecutedContext context)
    {
    }
}
```

## IFilterFactory

[IFilterFactory] implements IFilterMetadata. Therefore, an [IFilterFactory] instance can be used as an IFilterMetadata instance anywhere in the filter pipeline. When the runtime prepares to invoke the filter, it attempts to cast it to an [IFilterFactory]. If that cast succeeds, the CreateInstance method is called to create the IFilterMetadata instance that is invoked. This provides a flexible design, since the precise filter pipeline doesn't need to be set explicitly when the app starts.

IFilterFactory can be implemented using custom attribute implementations as another approach to creating filters:

```cs
public class AddHeaderWithFactoryAttribute : Attribute, IFilterFactory
{
    // Implement IFilterFactory
    public IFilterMetadata CreateInstance(IServiceProvider serviceProvider)
    {
        return new InternalAddHeaderFilter();
    }

    private class InternalAddHeaderFilter : IResultFilter
    {
        public void OnResultExecuting(ResultExecutingContext context)
        {
            context.HttpContext.Response.Headers.Add(
                "Internal", new string[] { "My header" });
        }

        public void OnResultExecuted(ResultExecutedContext context)
        {
        }
    }

    public bool IsReusable
    {
        get
        {
            return false;
        }
    }
}
```

Note:

Filters that implement [IFilterFactory] are useful for filters that:
* Don't require passing parameters.
* Have constructor dependencies that need to be filled by DI.

[TypeFilterAttribute] implements [IFilterFactory]. [IFilterFactory] exposes the CreateInstance method for creating an [IFilterMetadata] instance. CreateInstance loads the specified type from the services container (DI).

```cs
public class SampleActionFilterAttribute : TypeFilterAttribute
{
    public SampleActionFilterAttribute()
                         :base(typeof(SampleActionFilterImpl))
    { 
    }

    private class SampleActionFilterImpl : IActionFilter
    {
        private readonly ILogger _logger;
        public SampleActionFilterImpl(ILoggerFactory loggerFactory)
        {
            _logger = loggerFactory.CreateLogger<SampleActionFilterAttribute>();
        }

        public void OnActionExecuting(ActionExecutingContext context)
        {
           _logger.LogInformation("SampleActionFilterAttribute.OnActionExecuting");
        }

        public void OnActionExecuted(ActionExecutedContext context)
        {
            _logger.LogInformation("SampleActionFilterAttribute.OnActionExecuted");
        }
    }
}

/// The following code shows three approaches to applying the [SampleActionFilter]:

[SampleActionFilter]
public IActionResult FilterTest()
{
    return Content("From FilterTest");
}

[TypeFilter(typeof(SampleActionFilterAttribute))]
public IActionResult TypeFilterTest()
{
    return Content("From TypeFilterTest");
}

// ServiceFilter must be registered in ConfigureServices or
// System.InvalidOperationException: No service for type '<filter>'
// has been registered. Is thrown.
[ServiceFilter(typeof(SampleActionFilterAttribute))]
public IActionResult ServiceFilterTest()
{
    return Content("From ServiceFilterTest");
}
```