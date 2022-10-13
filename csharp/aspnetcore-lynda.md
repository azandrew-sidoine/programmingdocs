# ASP. NET Lynda Course

[FromQuery] - C# Attribute for loading data from Request query
[FromBody] - . NET Attribute for loading parameters from request body

## API Versioning

URL prefix versioning

> https://example.io/{<VersionNumber>}/rooms

--- Versionning support using

> Microsoft. AspNetCore. Mvc. Versionning Package

``` cs
// .. Startup.cs

public void ConfigureServices(IServiceCollection services)
{
    //...
    services.AddApiVersionning(options => {
        option.DefaultApiVersion = new ApiVersion(1, 0);
        // This tell ASP.NET to User the media type versioning instead of URL versionning passed in Accept header
        // Accept : application/json;v1.0
        option.ApiVersionReader = new MediaTypeApiVersionReader();
        option.AssumeDefaultVersionWhenUnspecified = true;

        option.ReportVersions = true;

        option.ApiVersionSelector = new CurrentImplementationApiVersionSelector(options);
    });
}

// Binding versions to a controller
[ApiVersion("1.0")]
public class RootController : ControllerBase
{

}
```

--- Serializing Exceptions as JSON

1) Create a class that represent Error Response body

``` cs
// Bloc/Models/JsonException.cs
using System.Linq;

public class JsonException
{
    public string Message {get; set; }

    public string Details {get; set; }

    public JsonException(ModelStateDictionary state)
    {
        Message = "Bad Request - Invalid Request parameters";

        Details = state.FirstOrDefault(s => s.Value.Errors.Any()
        .Value.Errors.FirstOrDefault().ErrorMessage;
    }
}
```

2) Create an Exception filter

Exception filters must implement Microsoft. AspNetCore. Mvc. Filters. IExceptionFilter

``` cs
using Microsoft.AspNetCore.Mvc.Filters;
using Bloc.Models.Exceptions;

// Bloc/Filters/JsonExceptionFilter.cs

public class JsonExceptionFilter : IExceptionFilter
{

    private readonly IHostingEnvironment _env;
    public JsonExceptionFilter(IHostingEnvironment env)
    {
        _env = env;
    }

    public void OnException(ExceptionContext context)
    {
        JsonException error;

        if (_env.IsDevelopment()){
            error = new JsonException{Message=context.Exception.Message, Details=context.Exception.StackTrace}
        } else {
            error = new JsonException{Message='Server Error Occured', Details=''}
        }

        context.Result = new ObjectResult(error){
            StatusCode = 500
        };
    }
}
```

3) Tell ASP. NET Core to use the Execption handler class

``` cs

// ... Startup.cs

    public void ConfigureServices(IServiceCollection services)
    {
        services.AddMvc(o => {
            o.Filters.Add<JsonExceptionFilter>();
        })
    }
```

## Security

--- Requiring HTTPS

HTTP Strict Transport Security (HSTS) - Force the browser to reject non HTTPS requests.

Forcing client request to redirect to HTTPS by default:

``` cs
// 

public void Configure()
{
    // ...
    app.UseHttpsRedirection();
    // ...
}
```

* Forcing HTTPs only request using filters

``` cs
// AppNamespace/Http/Filters/RequireHttpsAttribute.cs

using Microsoft.AspNetCore.Mvc;

namespace AppNamespace.Http.Filters
{
    public class RequireHttpsAttribute : RequireHttpsAttribute
    {

        override void HandleNonHttpsRequest(AuthorizationFilterContext context)
        {
            context.Result = new StatusCodeResult(400);
        }

    }
}
```

Next the filter must be add to Mvc

--- HTTP Cors in ASP. NET Core

``` cs
// Startup.cs
// ...

public void ConfigureServices(IServiceCollection services)
{
    services.AddCors(o => {
        // o.AddPolicy("AllowPolicy" , policy => {
        //     policy.WithOrigins("<Domain>");
        // });

        // In dev
        o.AddPolicy("AllowPolicy" , policy => {
            policy.AllowAnyOrigin();
        });
    });
}

public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{

    // ...
    app.UseCors("AllowPolicy");

    // Cors middleware must be define before middleware like MVC
    app.UseMvc();
}

// ...
```

## Represent Resources

--- Json Serialization

``` cs

using Micorosoft.Json;

public abstract class Resource
{
    // Order of -2 put the key on top of  any when generating JSON output
    [JsonProperty(Order = -2, PropertyName = "href", NullValueHandling = NullValueHandling.Ignore)]
    public string Href {get; set; }
}
```

--- Set-up In-memory Database

``` cs

using Microsoft.EntityFrameworkCore;

// 1) Create a DbContext class

namespace AppNamespace.Bloc.DB
{
    public class WebAPIDbContext : DbContext
    {
        public WebAPIDbContext(DbContextOptions options) : base(options)
        {

        }

        public DbSet<ModelEntity> Prop {get; set; }
    }
}

// 2) Create a model that bind to a table
namespace AppNamespace.Bloc.DB
{
    public class ModelEntity
    {
        // ... Define property of the entity
        public Guid Id {get; set; }
        public string Name {get; set }
    }
}

namespace AppNamespace.Bloc.Models
{
    public class ModelResource : Resource
    {
        // ... Define property of the entity
        public string Name {get; set }
    }
}

// 3) Configure ASP.NET to use the DBContext
// Startup.cs
// ...
using Microsoft.EntityFrameworkCore;
// ..
public void ConfigureServices(IServiceCollection services)
{
    services.AddDbContext<WebAPIDbContext>(
        o => o.UseInMemoryDatabase("<DatabaseName>")
    );
}
```

--- Seeding database

``` cs

public static class DatabaseSeeder
{
    public static async Task InitializeAsync(IServiceProvider services)
    {
        await AddTestData(services.GetRequiredService<WebAPIDbContext>());
    }
    public static async Task AddTestData(WebAPIDbContext context)
    {
        if (context.Prop.Any()) {
            // Database already contains data
            return;
        }

        context.Prop.Add(new ModelEntity{
            Id = Guid.Parse("u940-3490-9837-jkn22"),
            Name = "Oxford Suite"
        });

        await context.SaveChangesASync();
    }
}

// Program.cs

// ...
public void Main(string[] args)
{
    var host = CreateWebHostBuilder().Build();
    InitializeDatabase(host)
    host.Run();
}

// ...

public static void InitializeDatabase(IWebHost host)
{
    using (var scope = host.Services.CreateScope())
    {
        var services = scope.ServiceProvider();

        try {
            DatabaseSeeder.InitializeAsync(services);
        } catch (Exception e) {
            var logger = services.GetRequiredService<ILogger<Program>>();

            logger.LogError(e, "Error Writting to database");
        }
    }
}
```

--- Return ressource from controller

``` cs

// Service class for handling data access context
// AppNamespace/BLoc/Contracts/Service/IRoomService.cs
namespace AppNamespace.Bloc.Contracts.Services
{
    public class IModelEntityService
    {
        Task<IEnumerable<ModelResource>> GetRoomsAsync();

        Task<ModelResource> GetRoomAsync(Guid id);
    }

}

// AppNameSpace/Bloc/Services/ModelEntityService.cs
namespace AppNamespace.Bloc.Services
{
    public class ModelEntityService : IModelEntityService
    {
        private readonly DbContext _context;
        private readonly IConfigurationProvider _mappingConfiguration;

        public ModelEntityService(DbContext context, IConfigurationProvider mappingConfiguration)
        {
            _context = context;
            _mappingConfiguration = mappingConfiguration;
        }

        public Task<ModelResource> GetRoomAsync(Guid id)
        {
            var entity = await _context.SingleOrDefaultAsync(e => e.Id == id);
            if (entity == null) {
                return null;
            }
            // Model properties mapping using AutoMapper

            var mapper = _mappingConfiguration.CreateMapper();
            return mapper.Map<ModelRessource>(entity);
        }

        public async Task<IEnumerable<ModelResource>> GetRoomsAsync()
        {
            var query = _context.Prop
                .ProjectTo<ModelResource>(_mappingConfiguration);

            return await query.ToArrayAsync();
        }
    }

}

namespace AppNamespace.Http.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class ModelEntityController : ControllerBase
    {
        private IModelEntityService _service;

        public ModelEntityController(IModelEntityService service)
        {
            _service = service;
        }

        [HttpGet]
        public IActionResult Index()
        {

        }

        [HttpGet("{id}")]
        [ProduceResponseType(404)]
        public Task<IActionResult<ModelResource>> Show(Guid id)
        {
            // Get the entity using the service provider
            var resource = _service.GetRoomAsync(id);
            if (resource == null) {
                return NotFound();
            }

            return resource;
        }
    }
}

// Next Add the service as a scope service in the Startup.cs
```

--- Mapping models automatically

Require adding Automapper packages:

> AutoMapper
> AutoMapper. Extensions. Microsoft. DependencyInjection

* Usage

``` cs
// 1) Create an automapper profile
using AutoMapper;

namespace AppNamesapce.Bloc.Helpers
{
    public class MappingProfile : Profile
    {

        public MappingProfile()
        {
            CreateMap<ModelEntity, ModelResource>()
                .FromMember(dest => dest.<PropertyToConvertExplicitly>, o => o.MapFrom(src => src.<SourcePropertyToConvertExplicitly>));
        }
    }
}

// 2) Add Automapper to the ASP.NET Core workflow
// Use AutoMapper.Extensions.Microsoft.DependencyInjection

// Startup.cs

// ...
services.AddAutoMapper(
    op => op. AddProfile<MappingProfile>());
```

--- Represent Links

* Link class for constructing ASP. NET Core Links

``` cs
namespace AppNamespace.Core.Links
{
    public class Link
    {
        public const string GetMethod = "GET";

        public static Link To(string routeName, object routeValues = null)
            => new Link
            {
                RouteName = routeName,
                RouteValues = routeValues,
                Method = GetMethod,
                Relations = null
            };

        public static Link ToCollection(string routeName, object routeValues = null)
            => new Link
            {
                RouteName = routeName,
                RouteValues = routeValues,
                Method = GetMethod,
                Relations = new[] { "collection" }
            };

        [JsonProperty(Order = -4)]
        public string Href { get; set; }

        [JsonProperty(Order = -3,
            PropertyName = "rel",
            NullValueHandling = NullValueHandling.Ignore)]
        public string[] Relations { get; set; }

        [JsonProperty(Order = -2,
            DefaultValueHandling = DefaultValueHandling.Ignore,
            NullValueHandling = NullValueHandling.Ignore)]
        [DefaultValue(GetMethod)]
        public string Method { get; set; }

        // Stores the route name before being rewritten by the LinkRewritingFilter
        [JsonIgnore]
        public string RouteName { get; set; }

        // Stores the route parameters before being rewritten by the LinkRewritingFilter
        [JsonIgnore]
        public object RouteValues { get; set; }
    }
}
```

``` cs
// Link rewriter class
namespace AppNamespace.Core.Link
{
    public class LinkRewriter
    {
        private readonly IUrlHelper _urlHelper;

        public LinkRewriter(IUrlHelper urlHelper)
        {
            _urlHelper = urlHelper;
        }

        public Link Rewrite(Link original)
        {
            if (original == null) return null;

            return new Link
            {
                Href = _urlHelper.Link(original.RouteName, original.RouteValues),
                Method = original.Method,
                Relations = original.Relations
            };
        }
    }
}
```

* ResponseResultFilter Helper

``` cs
namespace AppNamespace.Filters
{
    public class LinkRewritingFilter : IAsyncResultFilter
    {
        private readonly IUrlHelperFactory _urlHelperFactory;

        public LinkRewritingFilter(IUrlHelperFactory urlHelperFactory)
        {
            _urlHelperFactory = urlHelperFactory;
        }

        public Task OnResultExecutionAsync(
            ResultExecutingContext context, ResultExecutionDelegate next)
        {
            var asObjectResult = context.Result as ObjectResult;
            bool shouldSkip = asObjectResult?.StatusCode >= 400
                || asObjectResult?.Value == null
                || asObjectResult?.Value as Resource == null;

            if (shouldSkip)
            {
                return next();
            }

            var rewriter = new LinkRewriter(_urlHelperFactory.GetUrlHelper(context));
            RewriteAllLinks(asObjectResult.Value, rewriter);

            return next();
        }

        private static void RewriteAllLinks(object model, LinkRewriter rewriter)
        {
            if (model == null) return;

            var allProperties = model
                .GetType().GetTypeInfo()
                .GetAllProperties()
                .Where(p => p.CanRead)
                .ToArray();

            var linkProperties = allProperties
                .Where(p => p.CanWrite && p.PropertyType == typeof(Link));

            foreach (var linkProperty in linkProperties)
            {
                var rewritten = rewriter.Rewrite(linkProperty.GetValue(model) as Link);
                if (rewritten == null) continue;

                linkProperty.SetValue(model, rewritten);

                // Special handling of the hidden Self property:
                // unwrap into the root object
                if (linkProperty.Name == nameof(Resource.Self))
                {
                    allProperties
                        .SingleOrDefault(p => p.Name == nameof(Resource.Href))
                        ?.SetValue(model, rewritten.Href);

                    allProperties
                        .SingleOrDefault(p => p.Name == nameof(Resource.Method))
                        ?.SetValue(model, rewritten.Method);

                    allProperties
                        .SingleOrDefault(p => p.Name == nameof(Resource.Relations))
                        ?.SetValue(model, rewritten.Relations);
                }
            }

            var arrayProperties = allProperties.Where(p => p.PropertyType.IsArray);
            RewriteLinksInArrays(arrayProperties, model, rewriter);

            var objectProperties = allProperties
                .Except(linkProperties)
                .Except(arrayProperties);
            RewriteLinksInNestedObjects(objectProperties, model, rewriter);
        }

        private static void RewriteLinksInNestedObjects(
            IEnumerable<PropertyInfo> objectProperties,
            object model,
            LinkRewriter rewriter)
        {
            foreach (var objectProperty in objectProperties)
            {
                if (objectProperty.PropertyType == typeof(string))
                {
                    continue;
                }

                var typeInfo = objectProperty.PropertyType.GetTypeInfo();
                if (typeInfo.IsClass)
                {
                    RewriteAllLinks(objectProperty.GetValue(model), rewriter);
                }
            }
        }

        private static void RewriteLinksInArrays(
            IEnumerable<PropertyInfo> arrayProperties,
            object model,
            LinkRewriter rewriter)
        {

            foreach (var arrayProperty in arrayProperties)
            {
                var array = arrayProperty.GetValue(model) as Array ?? new Array[0];

                foreach (var element in array)
                {
                    RewriteAllLinks(element, rewriter);
                }
            }
        }

    }
}
```

--- Represent Collections

* Pagination

``` cs
// Adding a pagination collection class
// Core/Models
namespace AppNamespace.Core.Models.Pagination
{
    public class PagedCollection<T> : Collection<T>
    {
        public static PagedCollection<T> Create(
            Link self, T[] items, int size, PagingOptions pagingOptions)
            => new PagedCollection<T>
            {
                Self = self,
                Value = items,
                Size = size,
                Offset = pagingOptions.Offset,
                Limit = pagingOptions.Limit,
                First = self,
                Next = GetNextLink(self, size, pagingOptions),
                Previous = GetPreviousLink(self, size, pagingOptions),
                Last = GetLastLink(self, size, pagingOptions)
            };
        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? Offset { get; set; }

        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public int? Limit { get; set; }

        public int Size { get; set; }

        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public Link First { get; set; }

        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public Link Previous { get; set; }

        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public Link Next { get; set; }

        [JsonProperty(NullValueHandling = NullValueHandling.Ignore)]
        public Link Last { get; set; }

        
        private static Link GetNextLink(
            Link self, int size, PagingOptions pagingOptions)
        {
            if (pagingOptions?.Limit == null) return null;
            if (pagingOptions?.Offset == null) return null;

            var limit = pagingOptions.Limit.Value;
            var offset = pagingOptions.Offset.Value;

            var nextPage = offset + limit;
            if (nextPage >= size)
            {
                return null;
            }

            var parameters = new RouteValueDictionary(self.RouteValues)
            {
                ["limit"] = limit,
                ["offset"] = nextPage
            };

            var newLink = Link.ToCollection(self.RouteName, parameters);
            return newLink;
        }

        private static Link GetLastLink(Link self, int size, PagingOptions pagingOptions)
        {
            if (pagingOptions?.Limit == null) return null;

            var limit = pagingOptions.Limit.Value;

            if (size <= limit) return null;

            var offset = Math.Ceiling((size - (double)limit) / limit) * limit;

            var parameters = new RouteValueDictionary(self.RouteValues)
            {
                ["limit"] = limit,
                ["offset"] = offset
            };
            var newLink = Link.ToCollection(self.RouteName, parameters);

            return newLink;
        }

        private static Link GetPreviousLink(Link self, int size, PagingOptions pagingOptions)
        {
            if (pagingOptions?.Limit == null) return null;
            if (pagingOptions?.Offset == null) return null;

            var limit = pagingOptions.Limit.Value;
            var offset = pagingOptions.Offset.Value;

            if (offset == 0)
            {
                return null;
            }

            if (offset > size)
            {
                return GetLastLink(self, size, pagingOptions);
            }

            var previousPage = Math.Max(offset - limit, 0);

            if (previousPage <= 0)
            {
                return self;
            }

            var parameters = new RouteValueDictionary(self.RouteValues)
            {
                ["limit"] = limit,
                ["offset"] = previousPage
            };
            var newLink = Link.ToCollection(self.RouteName, parameters);

            return newLink;
        }
    }
}

// Optional
// 2) Create a Paging option class for Mapping model in controller action

namespace AppNamespace.Core.Models.Pagination
{
    public class PagingOptions
    {
        [Range(1, 99999, ErrorMessage = "Offset must be greater than 0.")]
        public int? Offset { get; set; }

        [Range(1, 100, ErrorMessage = "Limit must be greater than 0 and less than 100.")]
        public int? Limit { get; set; }
    }
}

// 3) Create a structure of the pagination result

namespace AppNamespace.Core.Models.Pagination
{
    public class PagedResults<T>
    {
        public IEnumerable<T> Items { get; set; }

        public int TotalSize { get; set; }
    }
}

// Skip and Take some values based on the pagination data

var result = list
    .Skip(pagingOptions.Offset.Value)
    .Take(pagingOptions.Limit.Value);

return new PagedResults<ModelName>
{
    Items = result,
    TotalSize = result.Count
};

```

--- Forcing ASP. NET to Throw Exception during validation

``` cs

// Startup.cs

public void ConfigureServices(IServiceCollection services)
{
    // ...
    services.Configure<ApiBehaviorOptions>(op => {
        return new BadRequestObjectResult(new JsonException(context.ModelState));
    });
    // ...
}
```

## Sorting Collection

``` cs
// 1) Create a sortable Attribute

using System;

namespace AppNamespace.Core.Sorting
{

    [AttributeUsage(AttributeTragets.Property, AllowMultiple = false)]
    public class SortableAttribute :  Attribute
    {
        public bool Default {get; set; }
    }

    public class SortTerm
    {
        public string Name {get; set; }

        public bool Descending {get; set; }

        public bool Default {get; set; }
    }
}

// 2) Add the sortable attribute to the model 
/// Example
/// class ModelResource : Ressource
/// {
///     [Sortable]
///     public string Name {get; set; } 
/// }

// 3) Create a sorting option class that can be loaded using the .NET Configuration class

using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using AppNamespace.Core.Helpers;

namespace AppNameSpace.Core.Sorting.Models
{
    public class SortOptions<T, TEntity> : IValidatableObject
    {
        public string[] OrderBy {get; set; };

        // ASP.NET Core call this method 
        public IEnumerable<ValidationResult> Validate(ValidationContext validationContext)
        {
            var delegate = new SortOptionsDelegate<T, TEntity>(OrderBy);

            var validTerms = delegate.GetValidTerms().Select(t => t.Name);

            var invalidTerms = delegate.GetAllTerms().Select(t => t.Name).Except(validTerms, StringComparison.OrdinalIgnoreCase);

            foreach (var term in invalidTerms)
            {
                yield return new ValidationResult(
                    $"Invalid sort term '{term}'.",
                    new [] { nameof(OrderBy) }
                );
            }
        }

        // Called by the services codes to apply sort options to the database query 
        public IQueryable<TEntity> Apply(IQueryable<TEntity> query)
        {
            var delegate = new SortOptionsDelegate<T, TEntity>(OrderBy);
            return delagate.Apply(query);
        }
    }

    public class SortOptionsDelegate<T, TEntity>
    {
        private readonly string[] _orderBy;

        public SortOptionsDelegate(string[] orderBy)
        {
            _orderBy = orderBy;
        }

        public IEnumerable<SortTerm> GetAllTerms()
        {
            if (_orderBy == null) yield break;

            foreach (var term in _orderBy)
            {
                if (string.IsNullOrEmpty(term)) continue;

                var tokens = term.Split(' ');

                if (tokens.Length == 0){
                    yield return new SortTerm { Name = term }
                    continue;
                }

                var descending = token.Length  > 1 && tokens[1].Equals("desc", StringComparison.OrdinalIgnoreCase);

                yield return new SortTerm
                {
                    Name = token[0],
                    Descending = descending
                };
            }
        }

        public static IEnumerable<SortTem> GetValidTerms()
        {
            var queryTerms = GetAllTerms().ToArray();

            if (!queryTerms.Any()) yield break;

            // Get set of proof term from model
            var declaredTerms = GetTermsFromModel();

            foreach (var term in queryTerms) {
                var declaredTerm = declaredTerms.SingleOrDefault(t => t.Name.Equals(term.Name, StringComparison.OrdinalIgnoreCase));

                if (declaredTerm == null) yield continue;

                yield return new SortTerm
                {
                    Name = declaredTerm.Name,
                    Descending = term.Descending,
                    Default = declaredTerm.Default
                };
            }
        }

        private static IEnumerable<SortTem> GetTermsFromModel() => typeof(T).GetTypeInfo().DeclaredProperties
        .Where(p => p.GetCustomAttributes<SortableAttribute>.Any())
        .Select(p => new SortTerm
        {
            Name = p.Name,
            Default = p.GetCustomAttribute<SortableAttribute>().Default
        });

        public IQueryable<TEntity> Apply(IQueryable<TEntity> query)
        {
            // Get all valid terms from the query
            var terms  = GetValidTerms().ToArray();

            terms  = !terms.Any() ? GetTermsFromModel().Where(t => t.Default).ToArray() : terms;

            if (!term.Any()) return query;

            var _query = query;
            var useThenBy = false;

            foreach (var t in terms)
            {
                // Get the property information on the entity model attache to the sortTerm Name
                var propertyInfo = ExpressionHelper.GetPropertyInfo<TEntity>(t.Name);

                // Get the Generic reference to the TEntity object
                var obj = ExpresionHelper.Parameter<TEntity>();

                // Build the link expression backward
                var k = ExpressionHelper.GetPropertyExpression(obj, propertyInfo);

                var kSelector = ExpressionHelper.GetLambda(typeof(TEntity), propertyInfo.PropertyType, obj, k);

                // query OrderBy/ThenBy[Desc](x => )

                _query = ExpressionHelper.CallOrderByOrThenBy(_query, useThenBy, term.Descending, propertyInfo.PropertyType, kSelector);

                usThenBy = true;
            }
            return _query;
        }
    }
}

// 4) Inject the sort option as query to the contoller action that can passed the loaded sort option data to the model service

// 5) In model service, call the sortOption apply method
// ...
IQueryable<RoomEntity> query = sortOptions.Apply(_context.Prop);


namespace AppNamespace.Core.Helpers
{
    public static class ExpressionHelper
    {
        private static readonly MethodInfo LambdaMethod = typeof(Expression)
            .GetMethods()
            .First(x => x.Name == "Lambda" && x.ContainsGenericParameters && x.GetParameters().Length == 2);

        private static MethodInfo[] QueryableMethods = typeof(Queryable)
            .GetMethods()
            .ToArray();

        private static MethodInfo GetLambdaFuncBuilder(Type source, Type dest)
        {
            var predicateType = typeof(Func<,>).MakeGenericType(source, dest);
            return LambdaMethod.MakeGenericMethod(predicateType);
        }

        public static PropertyInfo GetPropertyInfo<T>(string name)
            => typeof(T).GetProperties()
            .Single(p => p.Name == name);

        public static ParameterExpression Parameter<T>()
            => Expression.Parameter(typeof(T));

        public static MemberExpression GetPropertyExpression(ParameterExpression obj, PropertyInfo property)
            => Expression.Property(obj, property);

        public static LambdaExpression GetLambda<TSource, TDest>(ParameterExpression obj, Expression arg)
            => GetLambda(typeof(TSource), typeof(TDest), obj, arg);

        public static LambdaExpression GetLambda(Type source, Type dest, ParameterExpression obj, Expression arg)
        {
            var lambdaBuilder = GetLambdaFuncBuilder(source, dest);
            return (LambdaExpression)lambdaBuilder.Invoke(null, new object[] { arg, new[] { obj } });
        }

        public static IQueryable<T> CallWhere<T>(IQueryable<T> query, LambdaExpression predicate)
        {
            var whereMethodBuilder = QueryableMethods
                .First(x => x.Name == "Where" && x.GetParameters().Length == 2)
                .MakeGenericMethod(new[] { typeof(T) });

            return (IQueryable<T>)whereMethodBuilder
                .Invoke(null, new object[] { query, predicate });
        }

        public static IQueryable<TEntity> CallOrderByOrThenBy<TEntity>(
            IQueryable<TEntity> modifiedQuery,
            bool useThenBy,
            bool descending,
            Type propertyType,
            LambdaExpression keySelector)
        {
            var methodName = "OrderBy";
            if (useThenBy) methodName = "ThenBy";
            if (descending) methodName += "Descending";

            var method = QueryableMethods
                .First(x => x.Name == methodName && x.GetParameters().Length == 2)
                .MakeGenericMethod(new[] { typeof(TEntity), propertyType });

            return (IQueryable<TEntity>)method.Invoke(null, new object[] { modifiedQuery, keySelector });
        }
    }
}
```


## Compress HTTP response

--- Response Compression

HTTP response compression can be done only if client support compression. 

If client can accept compression 'Accept-Encoding' by the client.


It ASP.NET, we can send compression by making use of Microsoft.AspNetCore.ResponseCompression middleware.

Only use it when not running API behind revers proxy

--- Http Caching

Cache-Control : max-age=100 (fresh caches last for 100seconds)

Cache-Control: no-cache, no-store (Never cache)

Etag : "<FingerPrint>" perform better that the Last-Modified Header.


--- Adding Caching in ASP.NET Core


```cs

// ControllerFile.cs
// Cache duration is almost 1 day cause the data return by the action does not change often
[ResponseCache(Duration = 86400)]
public ActionResult<Type> GetInfo()
{

}
```


--- Server side caching

> service.AddResponseCaching() -  in ConfigureServices method

> app.UseResponseCaching() - Before `app.UseMvc()` in Configure method

> [ResponseCache(Duration = 30, VaryByKeys = new [] {"offset", "limit", "orderBy", "search"})] - To controller action that perform havy weight request and need to be cached


--- How to Add Authentication and Authorization