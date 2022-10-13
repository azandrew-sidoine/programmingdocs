# Building and Securing RESTful APIs in ASP. NET Core

## REST API

--- Self-Documentation and HATEOAS (HyperMedia As The Engine Of Application State)

The response from API tell the client what is can do.

--- Head request

HEAD /users/123 - Return the headers information on the route

## Startup.cs file

ASP. NET Core apps use a Startup class, which is named Startup by convention.

Note: Only `IWebHostEnvironment` , `IHostEnvironment` , `IConfiguration` are injectable in the Startup constructor.

``` cs
/// Startup.cs

// ...
// Startup class for configuring application services
// Where configuration options are set by convention.
public void ConfigureServices(IServiceCollection services)
{
    // Add any dependency to the .NET Core Container
    services.AddMVC().SetCompatibilityVersion(
        CompatibilityVersion.Version_2_1
    );

    // Add the database context to the application
    services.AddDbContext<ApplicationDbContext>(options =>
            options.UseSqlServer(
                Configuration.GetConnectionString("DefaultConnection")));
}

// This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    // Each Use extension method adds one or more middleware components to the request pipeline.
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
    }

    app.UseHttpsRedirection();

    app.UseRouting();

    // app.UseAuthorization();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapControllers();
    });
}
// ...
```

* Extending startup with Filters

To configure middleware at the beginning or end of an app's Configure middleware pipeline without an explicit call to Use{Middleware}.

This convention can be used by package builders.

``` cs
// RequestSetOptionsMiddleware.cs
public class RequestSetOptionsMiddleware
{
    private readonly RequestDelegate _next;

    public RequestSetOptionsMiddleware( RequestDelegate next )
    {
        _next = next;
    }

    // Test with https://localhost:5001/Privacy/?option=Hello
    public async Task Invoke(HttpContext httpContext)
    {
        // ... perform tasks

        await _next(httpContext);
    }
}

// RequestSetOptionsStartupFilter.cs
public class RequestSetOptionsStartupFilter : IStartupFilter
{
    public Action<IApplicationBuilder> Configure(Action<IApplicationBuilder> next)
    {
        return builder =>
        {
            builder.UseMiddleware<RequestSetOptionsMiddleware>();
            next(builder);
        };
    }
}

// The IStartupFilter is registered in the service container in ConfigureServices.
// Startup.cs
public void ConfigureServices(IServiceCollection services)
{
    // ...
    services.AddTransient<IStartupFilter,
                      RequestSetOptionsStartupFilter>();
}
```

Note: Libraries may add middleware with one or more IStartupFilter implementations that run before or after other app middleware registered with IStartupFilter. To invoke an IStartupFilter middleware before a middleware added by a library's IStartupFilter:

* Position the service registration before the library is added to the service container.
* To invoke afterward, position the service registration after the library is added.

## Dependency injections

A dependency is an object that another object depends on. ASP. NET Core supports the dependency injection (DI) software design pattern, which is a technique for achieving Inversion of Control (IoC) between classes and their dependencies.

``` cs
// Interface.cs
public interface IMyDependency
{
    void WriteMessage(string message);
}

// ImplementationClass.cs
public class MyDependency : IMyDependency
{
    private readonly ILogger<MyDependency2> _logger;

    public void WriteMessage(string message)
    {
        Console.WriteLine($"MyDependency.WriteMessage Message: {message}");
    }
}

public class MyDependency2 : IMyDependency
{
    public MyDependency2(ILogger<MyDependency2> logger)
    {
        _logger = logger;
    }

    public void WriteMessage(string message)
    {
        _logger.LogInformation( $"MyDependency2.WriteMessage Message: {message}");
    }
}

// Injecting the dependency
public class Index2Model : PageModel
{
    private readonly IMyDependency _myDependency;

    public Index2Model(IMyDependency myDependency)
    {
        _myDependency = myDependency;            
    }

    public void OnGet()
    {
        _myDependency.WriteMessage("Index2Model.OnGet");
    }
}

// Binding using AddScoped
// Startup.cs
public void ConfigureServices(IServiceCollection services)
{
    // ...
    services.AddScoped<IMyDependency, MyDependency2>();
    // ...

}
```

--- Register groups of services with extension methods

The ASP. NET Core framework uses a convention for registering a group of related services. The convention is to use a single `Add{GROUP_NAME}` extension method to register all of the services required by a framework feature. For example, the `AddControllers` extension method registers the services required for MVC controllers.

``` cs
using ConfigSample.Options;
using Microsoft.Extensions.Configuration;

// Microsoft recommend to place extension methods in the Microsoft.Extensions.DependencyInjection namespace to encapsulate groups of service registrations. 
namespace Microsoft.Extensions.DependencyInjection
{
    public static class MyConfigServiceCollectionExtensions
    {
        public static IServiceCollection AddConfig(
             this IServiceCollection services, IConfiguration config)
        {
            services.Configure<PositionOptions>(
                config.GetSection(PositionOptions.Position));
            services.Configure<ColorOptions>(
                config.GetSection(ColorOptions.Color));

            return services;
        }
    }
}

// Startup.cs
public void ConfigureServices(IServiceCollection services)
{
    // ...
    services.AddConfig(Configuration)
            .AddMyDependencyGroup();

    // ...
}

```

Note: To use scoped services in middleware, use one of the following approaches:

* Inject the service into the middleware's Invoke or InvokeAsync method. Using constructor injection throws a runtime exception because it forces the scoped service to behave like a singleton.

* Use Factory-based middleware. Middleware registered using this approach is activated per client request (connection), which allows scoped services to be injected into the middleware's InvokeAsync method

--- Methods for adding services

> AddSingleton<Interface, Implementation>() - Singleton objects are the same for every request.

> AddScoped<Interface, Implementation>() - Scoped objects are the same for each request but different across each reques.

> AddTransient<Interface, Implementation>() - Transient objects are always different. The service locator create a new instance each time the class is resolved.

--- Request Services

The services available within an ASP. NET Core request are exposed through the `HttpContext.RequestServices` collection. When services are requested from inside of a request, the services and their dependencies are resolved from the `RequestServices` collection.

The framework creates a scope per request and `RequestServices` exposes the scoped service provider. All scoped services are valid for as long as the request is active.

--- Disposal of services

The container calls Dispose for the IDisposable types it creates. Services resolved from the container should never be disposed by the developer. If a type or factory is registered as a singleton, the container disposes the singleton automatically.

``` cs
public class Service1 : IDisposable
{
    private bool _disposed;

    public void Write(string message)
    {
        Console.WriteLine($"Service1: {message}");
    }

    public void Dispose()
    {
        if (_disposed)
            return;

        Console.WriteLine("Service1.Dispose");
        _disposed = true;
    }
}

```

## Middlewares

Request delegates are used to build the request pipeline. The request delegates handle each HTTP request.

Request delegates are configured using Run, Map, and Use extension methods.

--- Create a middleware pipeline with IApplicationBuilder

``` cs
using Microsoft.AspNetCore.HttpOverrides;

// ...

public class Startup
{
    public void Configure(IApplicationBuilder app)
    {
        app.UseResponseCompression();
        // Chain multiple request delegates together with Use. The next parameter represents the next delegate in the pipeline. You can short-circuit the pipeline by not calling the next parameter.
        app.Use(async (context, next) =>
        {
            // Do work that doesn't write to the Response.
            await next.Invoke();
            // Do logging or other work that doesn't write to the Response.
        });
        // This case doesn't include an actual request pipeline. Instead, a single anonymous function is called in response to every HTTP request.
        // Run delegates don't receive a next parameter. The first Run delegate is always terminal and terminates the pipeline
        app.Run(async context =>
        {
            await context.Response.WriteAsync("Hello, World!");
        });

        // When running application behind a proxy like nginx
        app.UseForwardedHeaders(new ForwardedHeadersOptions
        {
            ForwardedHeaders = ForwardedHeaders.XForwardedFor | ForwardedHeaders.XForwardedProto
        });
    }
}
```

Note: The order that middleware components are added in the Startup. Configure method defines the order in which the middleware components are invoked on requests and the reverse order for the response.

--- Branch the middleware pipeline

Map extensions are used as a convention for branching the pipeline. Map branches the request pipeline based on matches of the given request path. If the request path starts with the given path, the branch is executed.

``` cs
public class Startup
{
    private static void HandleMapTest1(IApplicationBuilder app)
    {
        app.Run(async context =>
        {
            await context.Response.WriteAsync("Map Test 1");
        });
    }

    private static void HandleBranch(IApplicationBuilder app)
    {
        app.Run(async context =>
        {
            var branchVer = context.Request.Query["branch"];
            await context.Response.WriteAsync($"Branch used = {branchVer}");
        });
    }

    private void HandleBranchAndRejoin(IApplicationBuilder app, ILogger<Startup> logger)
    {
        app.Use(async (context, next) =>
        {
            var branchVer = context.Request.Query["branch"];
            logger.LogInformation("Branch used = {branchVer}", branchVer);

            // Do work that doesn't write to the Response.
            await next();
            // Do other work that doesn't write to the Response.
        });
    }

    public void Configure(IApplicationBuilder app)
    {
        app.Map("/map1", HandleMapTest1);
        // ...

        // MapWhen branches the request pipeline based on the result of the given predicate. Any predicate of type Func<HttpContext, bool> can be used to map requests to a new branch of the pipeline
        app.MapWhen(context => context.Request.Query.ContainsKey("branch"), HandleBranch);

        // UseWhen also branches the request pipeline based on the result of the given predicate. Unlike with MapWhen, this branch is rejoined to the main pipeline if it doesn't short-circuit or contain a terminal middleware
         app.UseWhen(context => context.Request.Query.ContainsKey("branch"),  appBuilder => HandleBranchAndRejoin(appBuilder, logger));

    }
}
```

--- Writing custom middleware class

A middleware class must include:

* A public constructor with a parameter of type RequestDelegate.
* A public method named Invoke or InvokeAsync. This method must:
    - Return a Task.
    - Accept a first parameter of type HttpContext.

``` cs
using Microsoft.AspNetCore.Http;
using System.Globalization;
using System.Threading.Tasks;

namespace Culture
{
    public class RequestCultureMiddleware
    {
        private readonly RequestDelegate _next;

        public RequestCultureMiddleware(RequestDelegate next)
        {
            _next = next;
        }

        public async Task InvokeAsync(HttpContext context)
        {
            var cultureQuery = context.Request.Query["culture"];
            if (!string.IsNullOrWhiteSpace(cultureQuery))
            {
                var culture = new CultureInfo(cultureQuery);

                CultureInfo.CurrentCulture = culture;
                CultureInfo.CurrentUICulture = culture;

            }

            // Call the next delegate/middleware in the pipeline
            await _next(context);
        }
    }
}
```

* Middleware extension method

The following extension method exposes the middleware through.

``` cs
using Microsoft.AspNetCore.Builder;

namespace Culture
{
    public static class RequestCultureMiddlewareExtensions
    {
        public static IApplicationBuilder UseRequestCulture(
            this IApplicationBuilder builder)
        {
            return builder.UseMiddleware<RequestCultureMiddleware>();
        }
    }
}

// ...
// Startup.cs
public class Startup
{
    public void Configure(IApplicationBuilder app)
    {
        app.UseRequestCulture();

        // ...
    }
}
```

## Configurations

Configuration in ASP. NET Core is performed using one or more configuration providers.

Note: `CreateDefaultBuilder` call in Program.cs file provides default config to the app in the following order:

1) `ChainedConfigurationProvider` : Adds an existing IConfiguration as a source. In the default configuration case, adds the host configuration and setting it as the first source for the app configuration.

2) appsettings.json using the JSON configuration provider

3) appsettings. Environment.json using the JSON configuration provider. For example, appsettings. Production.json and appsettings. Development.json.

4) App secrets when the app runs in the Development environment.

5) Environment variables using the Environment Variables configuration provider.

6) Command-line arguments using the Command-line configuration provider.

Note: `Configuration providers that are added later override previous key settings. For example, if MyKey is set in both appsettings.json and the environment, the environment value is used. Using the default configuration providers, the Command-line configuration provider overrides all other providers.`

--- Loading configuration values

``` cs
using Microsoft.Extensions.Configuration;

public class ClassName
{
    // requires using ;
    private readonly IConfiguration Configuration;

    // Inject the Configuration dependency
    public TestModel(IConfiguration configuration)
    {
        Configuration = configuration;
    }

    public ContentResult OnGet()
    {
        var myKeyValue = Configuration["MyKey"];
        var title = Configuration["Position:Title"];
        var name = Configuration["Position:Name"];
        var defaultLogLevel = Configuration["Logging:LogLevel:Default"];
    }
}
```

--- Binding configuration value to a class to enforce typhint

Requirements: 

* All public read-write properties of the type are bound.
* Fields are not bound. In the preceding code, Position is not bound. The Position property is used so the string "Position" doesn't need to be hard coded in the app when binding the class to a configuration provider.

``` cs
// PositionOptions.cs
public class PositionOptions
{
    public const string Position = "Position";

    public string Title { get; set; }
    public string Name { get; set; }
}

// Configuring the options
// Startup.cs

public void ConfigureServices(IServiceCollection services)
{
    // ...
    services.Configure<PositionOptions>(Configuration.GetSection(
                                        PositionOptions.Position));
    // ...
}

// Using configuration option
public class Test2Model : PageModel
{
    private readonly PositionOptions _options;

    public Test2Model(IOptions<PositionOptions> options)
    {
        _options = options.Value;
    }

    public ContentResult OnGet()
    {
        return Content($"Title: {_options.Title} \n" +
                       $"Name: {_options.Name}");
    }
}

```

--- Use IOptionsSnapshot to read updated data

Using IOptionsSnapshot<TOptions>, options are computed once per request when accessed and cached for the lifetime of the request. Changes to the configuration are read after the app starts when using configuration providers that support reading updated configuration values.
The difference between IOptionsMonitor and IOptionsSnapshot is that:

* `IOptionsMonitor` is a singleton service that retrieves current option values at any time, which is especially useful in singleton dependencies.

* `IOptionsSnapshot` is a scoped service and provides a snapshot of the options at the time the IOptionsSnapshot<T> object is constructed. Options snapshots are designed for use with transient and scoped dependencies.

``` cs
public class TestSnapModel : PageModel
{
    private readonly MyOptions _snapshotOptions;

    public TestSnapModel(IOptionsSnapshot<MyOptions> snapshotOptionsAccessor)
    {
        _snapshotOptions = snapshotOptionsAccessor.Value;
    }

    public ContentResult OnGet()
    {
        return Content($"Option1: {_snapshotOptions.Option1} \n" +
                       $"Option2: {_snapshotOptions.Option2}");
    }
}

```

> Key: SubLevelKey:otherSubLevelKey - Loading configuration values from appsettings.json file is done with the preceding syntax

--- Security and user secrets

Configuration data guidelines:

* Never store passwords or other sensitive data in configuration provider code or in plain text configuration files. The Secret Manager tool can be used to store secrets in development.

* Specify secrets outside of the project so that they can't be accidentally committed to a source code repository.

--- Environment variables

Using the default configuration, the EnvironmentVariablesConfigurationProvider loads configuration from environment variable key-value pairs after reading appsettings.json, appsettings. Environment.json, and user secrets.

Note: The : separator doesn't work with environment variable hierarchical keys on all platforms.

Call AddEnvironmentVariables with a string to specify a prefix for environment variables:

``` cs
// Program.cs
// ...
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureAppConfiguration((hostingContext, config) =>
        {
            config.AddEnvironmentVariables(prefix: "MyCustomPrefix_");
        })
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder.UseStartup<Startup>();
        });
```

Note: The default configuration loads environment variables and command line arguments prefixed with DOTNET_ and ASPNETCORE_. The DOTNET_ and ASPNETCORE_ prefixes are used by ASP. NET Core for host and app configuration, but not for user configuration.

--- Naming of environment variables

Environment variable names reflect the structure of an appsettings.json file. Each element in the hierarchy is separated by a double underscore (preferable) or a colon. When the element structure includes an array, the array index should be treated as an additional element name in this path.

``` cs
// This json config
{
    "SmtpServer": "smtp.example.com",
    "Logging": [
        {
            "Name": "ToEmail",
            "Level": "Critical",
            "Args": {
                "FromAddress": "MySystem@example.com",
                "ToAddress": "SRE@example.com"
            }
        },
        {
            "Name": "ToConsole",
            "Level": "Information"
        }
    ]
}

// Can be written as
setx SmtpServer=smtp.example.com
setx Logging__0__Name=ToEmail
setx Logging__0__Level=Critical
setx Logging__0__Args__FromAddress=MySystem@example.com
setx Logging__0__Args__ToAddress=SRE@example.com
setx Logging__1__Name=ToConsole
setx Logging__1__Level=Information
```

--- Kestrel endpoint configuration

Kestrel specific endpoint configuration overrides all cross-server endpoint configurations. Cross-server endpoint configurations include:

* UseUrls
* --urls on the command line

--- Methods

> GetValue<DataType>(string <Key>, DataType default) - extracts a single value from configuration with a specified key and converts it to the specified type

> GetSection(string <Key>) - returns a configuration subsection with the specified subsection key.

> section. GetChildren() - and returns values for a selected section

> section. Exists() - Returns a boolean indicating the presence of the requested configs

* Access configuration in Startup

Simply inject the `IConfiguration` interface in the startup constructor.

## Logging

Logging providers store logs, except for the Console provider which displays logs.

The default ASP. NET Core web app templates:

* Use the Generic Host.
* Call `CreateDefaultBuilder`, which adds the following logging providers:
    - Console
    - Debug
    - EventSource
    - EventLog - Windows only

``` cs
// Program.cs

public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureLogging(logging =>
        {
            // Clear all logging providers
            logging.ClearProviders();
            // Add only the console provider
            logging.AddConsole();
        })
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder.UseStartup<Startup>();
        });
```

--- Creating Log

1) Inject the ILogger<T> object in the constructor of the requiring object

2) call the log method passing a string to log

``` cs

/// Logging method syntax 
/// Log{LogLevel}(<EventID>, <Message>, <...TemplatePlaceHolders>)
/// Log{LogLevel}(<EventID>, <ExceptionInstance>, <Message>, <...TemplatePlaceHolders>)
/// <EventID> : They are simple constant integers that may indicate the events in the application
/// Example: _logger.LogInformation(AppLogEvents.InsertionError, "Failed inserting {Id}", id);
/// The template parameter does not have to match the variable name, only the order is required. Naming placeholder only help Log Provider writters
public class PrivacyModel : PageModel
{
    // Create the logger with category name == PrivacyModel
    private readonly ILogger<PrivacyModel> _logger;

    public PrivacyModel(ILogger<PrivacyModel> logger)
    {
        _logger = logger;
    }

    public void OnGet()
    {
        _logger.LogInformation("GET Pages.PrivacyModel called.");
    }
}
```

* Log Levels

> LogInformation(string message) - Log an informational message

--- Configure Logging

Commonly provide logging configuration in appSettings[<Environment>].json

Note:
Trace = 0, Debug = 1, Information = 2, Warning = 3, Error = 4, Critical = 5, and None = 6.

``` json
// ...
{
  "Logging": {
    // Log levels are grouped by category
    "LogLevel": {
      "Default": "Information", // Default category
      "Microsoft": "Warning", // Microsoft category apply to all key that start with Microsoft
      "Microsoft.Hosting.Lifetime": "Information"
    }
  },
  // Providers specific log level configurations
  // Settings defines here override the global logging configuration
  "Debug": { // Debug provider.
      "LogLevel": {
        "Default": "Information", // Overrides preceding LogLevel:Default setting.
        "Microsoft.Hosting": "Trace" // Debug:Microsoft.Hosting category.
      }
    },
    "EventSource": { // EventSource provider
      "LogLevel": {
        "Default": "Warning" // All categories of EventSource provider.
      }
    }
}
// ...
```

--- Scoped Log

``` cs
// ...
    using (_logger.BeginScope("Using block message"))
    {
        _logger.LogInformation(...);

        // ...
    }
```

--- Creating Logger in No-Host or Console App

``` cs
class Program
{
    static void Main(string[] args)
    {
        using var loggerFactory = LoggerFactory.Create(builder =>
        {
            builder
                .AddFilter("Microsoft", LogLevel.Warning)
                .AddFilter("System", LogLevel.Warning)
                .AddFilter("LoggingConsoleApp.Program", LogLevel.Debug)
                .AddConsole()
                .AddEventLog();
        });
        ILogger logger = loggerFactory.CreateLogger<Program>();
        logger.LogInformation("Example log message");
    }
}
```

## Controllers

All Controllers inherit from the [Microsoft. AspNetCore. Mvc. ControllerBase] class.

Note: Every public method in a controller is callable as an HTTP endpoint.

--- Convention

Dotnet controllers must:

* The class name is suffixed with Controller.
* The class inherits from a class whose name is suffixed with Controller.
* The [Controller] attribute is applied to the class.

Note:

If [NonController] attribute is added to a class it's no more a controller.

--- Controller actions

Public methods on a controller, except those with the [NonAction] attribute, are actions.

Actions can return anything, but frequently return an instance of `IActionResult` (or `Task<IActionResult>` for async methods)

--- ControllerBase helper methods

* HTTP Status code methods [Ok()|BadRequest()|NotFound()]

This type returns an HTTP status code. A couple of helper methods of this type are BadRequest, `NotFound` , and `Ok` . For example, return `BadRequest()` ; produces a 400 status code when executed. When methods such as BadRequest, NotFound, and Ok are overloaded, they no longer qualify as HTTP Status Code responders, since content negotiation is taking place.

* Redirect

This type returns a redirect to an action or destination (using `Redirect` , `LocalRedirect` , `RedirectToAction` , or `RedirectToRoute` ). For example, return RedirectToAction("Complete", new {id = 123}); redirects to Complete, passing an anonymous object.

-- Methods resulting in a non-empty response body with a predefined content type
 

* Formatted Response

This type returns JSON or a similar data exchange format to represent an object in a specific manner. For example, `return Json(customer)` ; serializes the provided object into JSON format.

-- Methods resulting in a non-empty response body formatted in a content type negotiated with the client

This category is better known as Content Negotiation. Content negotiation applies whenever an action returns an ObjectResult type or something other than an IActionResult implementation. An action that returns a non-IActionResult implementation (for example, object) also returns a Formatted Response.
Some helper methods of this type include BadRequest, CreatedAtRoute, and Ok. Examples of these methods include return BadRequest(modelState); , return CreatedAtRoute("routename", values, newobject); , and return Ok(value); , respectively. Note that BadRequest and Ok perform content negotiation only when passed a value

``` cs
using System;
using Microsoft.AspNetCore.Mvc;

namespace Application.Controllers
{
    [ApiController]
    [Route("/")]
    // Tells swagger and ASP.NET Core that the controller returns a JSON object
    [ProduceResponseType(200)]
    class PostsController
    {
        [HttpGet(Name = "[controller]_[action]")]
        public function Index()
        {
            return Ok(new {
                href = Url.Link("post_index", null)
            })
        }
    }
}
```

## Routing

Routing uses a pair of middleware, registered by UseRouting and UseEndpoints:

* UseRouting adds route matching to the middleware pipeline. This middleware looks at the set of endpoints defined in the app, and selects the best match based on the request.

* UseEndpoints adds endpoint execution to the middleware pipeline. It runs the delegate associated with the selected endpoint.

Note: REST APIs should use attribute routing to model the app's functionality as a set of resources where operations are represented by HTTP verbs.

RESTful service configuration is as follow:

``` cs
// Startup.cs
// ...
public void ConfigureServices(IServicesCollection services)
{
    // ...

}

public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    // ...

    // Endpoint aware middleware. 
    // Middleware can use metadata from the matched endpoint.
    // Apply an authorization policy before UseEndpoints dispatches to the endpoint.
    app.UseAuthentication();
    app.UseAuthorization();

    // This call map attribute routed controller in an MVC application
    app.UseEndpoints(e => {
        e.MapControllers();

        // Configure the Health Check endpoint and require an authorized user.
        endpoints.MapHealthChecks("/route-path").RequireAuthorization();
    });
}

// ...

```

* Attribute routing

> Reserved routing names are : `action, area, controller, handler, page`

Attribute routing can be defined: 

> [Route("route-expression", Name="")]

In order to not hard code the route expressions: "[controller]/[action]" return the name of the controller without the suffix Controller and the action to connstruct the path.

> Optional parameters - "[controller]/{param?:datatype}"

* HTTP Verbs template

ASP. NET Core provide the following HTTP verb templates: `HttpGet, HttpPost, HttpPut, HttpDelete, HttpHead, HttpPatch`

``` cs
[Route("api/[controller]")]
[ApiController]
public class Test2Controller : ControllerBase
{
    [HttpGet]   // GET /api/test2
    public IActionResult ListProducts()
    {
        return ControllerContext.MyDisplayRouteInfo();
    }

    [HttpGet("{id}")]   // GET /api/test2/xyz
    public IActionResult GetProduct(string id)
    {
       return ControllerContext.MyDisplayRouteInfo(id);
    }

    [HttpGet("int/{id:int}")] // GET /api/test2/int/3
    public IActionResult GetIntProduct(int id)
    {
        return ControllerContext.MyDisplayRouteInfo(id);
    }

    [HttpGet("int2/{id?}")]  // GET /api/test2/int2/3
    public IActionResult GetInt2Product(int id = null)
    {
        return ControllerContext.MyDisplayRouteInfo(id);
    }
}
```

* Route names

Route names must be unique application-wide.

``` cs
[ApiController]
public class Products2ApiController : ControllerBase
{
    [HttpGet("/products2/{id}", Name = "Products_List")]
    public IActionResult GetProduct(int id)
    {
        return ControllerContext.MyDisplayRouteInfo(id);
    }
}
```

Note: Route templates applied to an action that begin with / or ~/ don't get combined with route templates applied to the controller.

* Use a parameter transformer to customize token replacement

Token replacement can be customized using a parameter transformer. A parameter transformer implements IOutboundParameterTransformer and transforms the value of parameters.

``` cs
// SlugifyParameterTransformer parameter transformer changes the SubscriptionManagement route value to subscription-management
public class SlugifyParameterTransformer : IOutboundParameterTransformer
{
    public string TransformOutbound(object value)
    {
        if (value == null) { return null; }

        return Regex.Replace(value.ToString(),
                             "([a-z])([A-Z])",
                             "$1-$2",
                             RegexOptions.CultureInvariant,
                             TimeSpan.FromMilliseconds(100)).ToLowerInvariant();
    }
}

// ...
// Startup.cs
// The RouteTokenTransformerConvention is registered as an option in ConfigureServices.
public void ConfigureServices(IServiceCollection services)
{
    // ...
    services.AddControllersWithViews(options =>
    {
        options.Conventions.Add(new RouteTokenTransformerConvention(
                                     new SlugifyParameterTransformer()));
    });
    // ...
}
```

Creating a route Link:

``` cs

using Microsoft.AspNetCore.Mvc;

string url = Url.Link('<RouteName>', params = null);
```

* Telling ASP. NET Core to use lowercase urls

``` cs
// Startup.cs
// ...
public void ConfigureServices(IServicesCollection services)
{
    // ...
    services.AddRouting(options => options.LowercaseUrls = true);

}

// ...

```

--- ASP. NET Core endpoint definition

An ASP. NET Core endpoint is:

    - Executable: Has a RequestDelegate.
    - Extensible: Has a Metadata collection.
    - Selectable: Optionally, has routing information.
    - Enumerable: The collection of endpoints can be listed by retrieving the EndpointDataSource from DI.

``` cs
// Startupt.cs
// Configure method

// ...
    // The following code shows how to retrieve and inspect the endpoint matching the current request:
    app.Use(next => context =>
    {
        var endpoint = context.GetEndpoint();
        if (endpoint is null)
        {
            return Task.CompletedTask;
        }
        
        Console.WriteLine($"Endpoint: {endpoint.DisplayName}");

        if (endpoint is RouteEndpoint routeEndpoint)
        {
            Console.WriteLine("Endpoint has route pattern: " +
                routeEndpoint.RoutePattern.RawText);
        }

        foreach (var metadata in endpoint.Metadata)
        {
            Console.WriteLine($"Endpoint has metadata: {metadata}");
        }

        return Task.CompletedTask;
    });

    // Location 2: After routing runs. Middleware can match based on metadata.
    app.Use(next => context =>
    {
        var endpoint = context.GetEndpoint();
        if (endpoint?.Metadata.GetMetadata<AuditPolicyAttribute>()?.NeedsAudit == true)
        {
            Console.WriteLine($"ACCESS TO SENSITIVE DATA AT: {DateTime.UtcNow}");
        }

        return next(context);
    });
    app.UseEndpoints(endpoints =>
    {         
        endpoints.MapGet("/", async context =>
        {
            await context.Response.WriteAsync("Hello world!");
        });

        // Using metadata to configure the audit policy.
        endpoints.MapGet("/sensitive", async context =>
        {
            await context.Response.WriteAsync("sensitive data");
        })
        .WithMetadata(new AuditPolicyAttribute(needsAudit: true));
    });
// ...

// Define the AuditPropertyAttribute somewhere
public class AuditPolicyAttribute : Attribute
{
    public AuditPolicyAttribute(bool needsAudit)
    {
        NeedsAudit = needsAudit;
    }

    public bool NeedsAudit { get; }
}
```

--- URL Generation concepts

``` cs
public class ProductsLinkMiddleware
{
    private readonly LinkGenerator _linkGenerator;

    public ProductsLinkMiddleware(RequestDelegate next, LinkGenerator linkGenerator)
    {
        _linkGenerator = linkGenerator;
    }

    public async Task InvokeAsync(HttpContext httpContext)
    {
        var url = _linkGenerator.GetPathByAction("ListProducts", "Store");

        httpContext.Response.ContentType = "text/plain";

        await httpContext.Response.WriteAsync($"Go to {url} to see our products.");
    }
}
```

--- Route template reference

> "**" - This template match a catch-all route

> "{param?}" - Param is made or declared optional

> "path/{param:<Constraint|Transformer>}" - . NET Core routes definitions

* Route constraints

Check the documentation for more informations

``` cs
/// Multiple, colon delimited constraints can be applied to a single parameter. For example, the following constraint restricts a parameter to an integer value of 1 or greater:
[Route("users/{id:int:min(1)}")]
public User GetUserById(int id) { }
```

--- Custom route constraints

Custom route constraints can be created by implementing the `IRouteConstraint` interface. The `IRouteConstraint` interface contains Match, which returns true if the constraint is satisfied and false otherwise.

``` cs
// ... Defining custom route constraint
public void ConfigureServices(IServiceCollection services)
{
    services.AddControllers();

    services.AddRouting(options =>
    {
        options.ConstraintMap.Add("customName", typeof(MyCustomConstraint));
    });
}
```

--- Parameter transformer reference

* Parameter transformers:
    - Execute when generating a link using LinkGenerator.
    - Implement Microsoft.AspNetCore.Routing.IOutboundParameterTransformer.
    - Are configured using ConstraintMap.
    - Take the parameter's route value and transform it to a new string value.
    - Result in using the transformed value in the generated link.

--- Debugging Routing performance

``` cs
// ...
public void Configure(IApplicationBuilder app, ILogger<Startup> logger)
{
    app.Use(next => async context =>
    {
        var sw = Stopwatch.StartNew();
        await next(context);
        sw.Stop();

        logger.LogInformation("Time 1: {ElapsedMilliseconds}ms", sw.ElapsedMilliseconds);
    });

    app.UseRouting();

    app.Use(next => async context =>
    {
        var sw = Stopwatch.StartNew();
        await next(context);
        sw.Stop();

        logger.LogInformation("Time 2: {ElapsedMilliseconds}ms", sw.ElapsedMilliseconds);
    });

    app.UseAuthorization();

    app.Use(next => async context =>
    {
        var sw = Stopwatch.StartNew();
        await next(context);
        sw.Stop();

        logger.LogInformation("Time 3: {ElapsedMilliseconds}ms", sw.ElapsedMilliseconds);
    });

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapGet("/", async context =>
        {
            await context.Response.WriteAsync("Timing test.");
        });
    });
}
// ...
```

## Exception handlers

``` cs

    // ... Configure method of Startup.cs

    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
    }
    else
    {
        app.UseExceptionHandler(errorApp =>
        {
            errorApp.Run(async context =>
            {
                context.Response.StatusCode = (int) HttpStatusCode.InternalServerError;;
                context.Response.ContentType = "text/html";

                await context.Response.WriteAsync("<html lang=\"en\"><body>\r\n");
                await context.Response.WriteAsync("ERROR!<br><br>\r\n");

                var exceptionHandlerPathFeature =
                    context.Features.Get<IExceptionHandlerPathFeature>();

                if (exceptionHandlerPathFeature?.Error is FileNotFoundException)
                {
                    await context.Response.WriteAsync(
                                              "File error thrown!<br><br>\r\n");
                }

                await context.Response.WriteAsync(
                                              "<a href=\"/\">Home</a><br>\r\n");
                await context.Response.WriteAsync("</body></html>\r\n");
                await context.Response.WriteAsync(new string(' ', 512)); 
            });
        });
        app.UseHsts();
    }
    // ...
        
    // Use status page middleware 
    app.UseStatusCodePages(async context =>
    {
        context.HttpContext.Response.ContentType = "text/plain";

        await context.HttpContext.Response.WriteAsync(
            "Status code page, status code: " +
            context.HttpContext.Response.StatusCode);
    });
```

## WebAPI Specifications

--- Action return Types

* Default Types

When multiple return types are possible, it's common to mix an ActionResult return type with the primitive or complex return type. Either IActionResult or ActionResult<T> are necessary to accommodate this type of action.

* Returning IEnumerable<T> or IAsyncEnumerable<T>

Consider declaring the action signature's return type as IAsyncEnumerable<T> to guarantee the asynchronous iteration. Ultimately, the iteration mode is based on the underlying concrete type being returned. MVC automatically buffers any concrete type that implements IAsyncEnumerable<T>

``` cs
[HttpGet("asyncsale")]
public async IAsyncEnumerable<Product> GetOnSaleProductsAsync()
{
    var products = _repository.GetProductsAsync();

    await foreach (var product in products)
    {
        if (product.IsOnSale)
        {
            yield return product;
        }
    }
}
```

* Asynchronous action

Consider the following asynchronous action in which there are two possible return types:

``` cs
[HttpPost]
[Consumes(MediaTypeNames.Application.Json)]
[ProducesResponseType(StatusCodes.Status201Created)]
[ProducesResponseType(StatusCodes.Status400BadRequest)]
public async Task<IActionResult> CreateAsync(Product product)
{
    if (product.Description.Contains("XYZ Widget"))
    {
        return BadRequest();
    }

    await _repository.AddProductAsync(product);

    return CreatedAtAction(nameof(GetById), new { id = product.Id }, product);
}
```

* ActionResult<T> type

ASP. NET Core 2.1 introduced the ActionResult<T> return type for web API controller actions. It enables you to return a type deriving from ActionResult or return a specific type. ActionResult<T> offers the following benefits over the IActionResult type:

* The [ProducesResponseType] attribute's Type property can be excluded. For example, [ProducesResponseType(200, Type = typeof(Product))] is simplified to [ProducesResponseType(200)]. The action's expected return type is instead inferred from the T in ActionResult<T>.
* Implicit cast operators support the conversion of both T and ActionResult to ActionResult<T>. T converts to ObjectResult, which means return new ObjectResult(T); is simplified to return T; .

``` cs
[HttpGet]
public ActionResult<IEnumerable<Product>> Get() =>
    _repository.GetProducts();
```

--- Handling JSON Patch requests

To enable JSON Patch support in your app, complete the following steps:

* Install the Microsoft. AspNetCore. Mvc. NewtonsoftJson NuGet package.
* Update the project's Startup. ConfigureServices method to call AddNewtonsoftJson. For example:

``` cs
// ...
services
    .AddControllersWithViews()
    .AddNewtonsoftJson();
// ...
```

* JSON Patch, AddNewtonsoftJson, and System. Text. Json

AddNewtonsoftJson replaces the System. Text. Json-based input and output formatters used for formatting all JSON content. To add support for JSON Patch using Newtonsoft. Json, while leaving the other formatters unchanged, update the project's Startup. ConfigureServices method as follows:

``` cs
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Formatters;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Options;
using System.Linq;

// ...
public void ConfigureServices(IServiceCollection services)
{
    services.AddControllersWithViews(options =>
    {
        options.InputFormatters.Insert(0, GetJsonPatchInputFormatter());
    });
}

private static NewtonsoftJsonPatchInputFormatter GetJsonPatchInputFormatter()
{
    var builder = new ServiceCollection()
        .AddLogging()
        .AddMvc()
        .AddNewtonsoftJson()
        .Services.BuildServiceProvider();

    return builder
        .GetRequiredService<IOptions<MvcOptions>>()
        .Value
        .InputFormatters
        .OfType<NewtonsoftJsonPatchInputFormatter>()
        .First();
}
// ...
```

--- Format Response data in ASP. NET Core Web API

* Format-specific Action Results

The built-in helper method Ok returns JSON-formatted data:

``` cs
// GET: api/authors
[HttpGet]
public ActionResult Get()
{
    return Ok(_authors.List());
}
```

To return plain text formatted data, use ContentResult and the Content helper:

``` cs
// GET api/authors/about
[HttpGet("About")]
public ContentResult About()
{
    return Content("An API listing authors of docs.asp.net.");
}
```

--- Configure formatters

XML formatters implemented using XmlSerializer are configured by calling AddXmlSerializerFormatters:

``` cs
// ...
public void ConfigureServices(IServiceCollection services)
{
    //...
    services.AddControllers()
        .AddXmlSerializerFormatters();

    // ..
}
```

The preceding code serializes results using XmlSerializer.
When using the preceding code, controller methods return the appropriate format based on the request's Accept header

## File Upload handlers

Here is a utility class for handling multipart request handlers:

``` cs
using System;
using System.IO;
using Microsoft.Net.Http.Headers;

namespace SampleApp.Utilities
{
    public static class MultipartRequestHelper
    {
        // Content-Type: multipart/form-data; boundary="----WebKitFormBoundarymx2fSWqWSd0OxQqq"
        // The spec at https://tools.ietf.org/html/rfc2046#section-5.1 states that 70 characters is a reasonable limit.
        public static string GetBoundary(MediaTypeHeaderValue contentType, int lengthLimit)
        {
            var boundary = HeaderUtilities.RemoveQuotes(contentType.Boundary).Value;

            if (string.IsNullOrWhiteSpace(boundary))
            {
                throw new InvalidDataException("Missing content-type boundary.");
            }

            if (boundary.Length > lengthLimit)
            {
                throw new InvalidDataException(
                    $"Multipart boundary length limit {lengthLimit} exceeded.");
            }

            return boundary;
        }

        public static bool IsMultipartContentType(string contentType)
        {
            return !string.IsNullOrEmpty(contentType)
                   && contentType.IndexOf("multipart/", StringComparison.OrdinalIgnoreCase) >= 0;
        }

        public static bool HasFormDataContentDisposition(ContentDispositionHeaderValue contentDisposition)
        {
            // Content-Disposition: form-data; name="key";
            return contentDisposition != null
                && contentDisposition.DispositionType.Equals("form-data")
                && string.IsNullOrEmpty(contentDisposition.FileName.Value)
                && string.IsNullOrEmpty(contentDisposition.FileNameStar.Value);
        }

        public static bool HasFileContentDisposition(ContentDispositionHeaderValue contentDisposition)
        {
            // Content-Disposition: form-data; name="myfile1"; filename="Misc 002.jpg"
            return contentDisposition != null
                && contentDisposition.DispositionType.Equals("form-data")
                && (!string.IsNullOrEmpty(contentDisposition.FileName.Value)
                    || !string.IsNullOrEmpty(contentDisposition.FileNameStar.Value));
        }
    }
}
```

--- Increasing Kestrel MaxUpload Size

``` cs
// Program.cs
// ...
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder.ConfigureKestrel((context, options) =>
            {
                // Handle requests up to 50 MB
                options.Limits.MaxRequestBodySize = 52428800;
            })
            .UseStartup<Startup>();
        });
        //...
```

## Request response

```
```
