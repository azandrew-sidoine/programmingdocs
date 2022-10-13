# ASP.NET Core : Middleware

Notes: HttpContext

> context.Request.Headers -> Return a Dictionary of the HTTP headers

> context.Request -> Return the Request object on the HTTP 

> context.Response -> Return the HTTP response object

## ASP.NET Core Modular approach to HTTP Application Pipeline

ASP.NET Core allow for modular creation of an HTTP Application Pipeline that processes requests

HTTP Pipeline is Configured by default in `Startup.Configure` method.

- Keyword:

    * Run Execute a (this) delegate and terminate processing
    * Use - Execute (this) delegate and proceed to next delegate in the pipeline
    * Map - Conditionnaly execute method and does not return to the pipeline

Note: These keyword delegates must be used on `IApplicationBuilder` instance.

## ASP.NET Core

{Request} -> [{Middleware_21}] -> [{Middleware_2}] -> {Response}

### UseStaticFiles

```cs

// Startup.cs

public void Configure(IApplicationBuilder app)
{
    // Provide capability to ASP.NET for static files usage
    app.UseStaticFiles();
}
```

## Use Delegate

```cs
app.Use(async (context, Func<Task> next) => {
    var timer = System.Diagnostics.Stopwatch.StartNew();

    logger.LogInformation($"Processing Next Pipeline in {env.EnvironmentName} environment");
    await next();
    logger.LogInformation($"Request completed in {timer.ElapsedMilliseconds} ms");

});
```

## Using class as middleware

```cs

// Startup.cs
// ...
    app.UseMiddleware<EnviromentMiddleware>();
// ...

// App.Http.Middleware

using Microsoft.AspNetCore.Http;
usinf Microsoft.AspNetCore.
using System.Threading.Tasks;

internal class EnviromentMiddleware
{
    private RequestDelegate _next;
    private string _env;

    public EnviromentMiddleware(RequestDelegate next, IHostingEnvironment env)
    {
        _next = next;
        _env = env.EnvironmentName;
    }

    /// This method is called to handle and process middleware
    // Execution. It must return a System.Threading.Tasks.Task class
    public async Task Invoke(HttpContext ctx)
    {
        var timer = System.Diagnostics.Stopwatch.StartNew();

        ctx.Response.Headers.Add("X-HostingEnvironment", new[] {_env});
        await _next(ctx);
        // Perform action after the execution of the pipeline get completed
        if ((ctx.Response.ContentType != null) && ctx.Response.ContentType.Contains("html")) {
            ctx.Response.WriteAsync($"<span>From {_env} in {timer.ElapsedMilliseconds} ms </span>");
        }
    }
}
```

Note: `UseStaticFiles()` does not allow to modify static files cause static files are flushed to the browser

## Map keyword

Conditionnaly execute method and does not return to the pipeline:

> app.Map(string <Path>, Func<HttpContext, Task> handler);

> app.MapWhen(Func<HttpContext, bool> handler) - 