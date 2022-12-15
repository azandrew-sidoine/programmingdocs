# Flask Framework

## Quickstart

- The Framework object

Flask framework object provides a Web Server Gateway interface (WSGI) written in Python.

Flask application entry point create a new instance of the flask object with the module name of the project or library.

```python
from flask import Flask

# Create a new flask web application instance
app = Flask(__name__);


# Provide a route controllere
@app.route('/')
def index():
    return "<p>Hello World</p>"
```

**Note** The `__name__` as parameter to the flash web app object.
Flask object takes a entry point of the application as parameter to allow itself to resolve static resource easily. By convention `__name__` which return the path to the project module is used as argument to the flask object constructor.

**Note** Dev server
Flask comes by default with development server that allows developpers to easily debug when application written in flask.

> python -m flask --app <main_script_name> run -> Start a flask dev server

**Note**
By default flask dev server is only accessible on the host machine, and not available on the network on which the host runs.
In order to make the dev server availbale in the host network environement use the `--host 0.0.0.0` option when running flask.

- Routing

As modern web applications uses meaningful URL to help users to navigate through the application, flask provides an out-of-box routing mechanism with mordern application routing in mind.

To register a listener for request on a given route, flask provide a `route()` decorator for action function or object:

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    # Define the login to serve application user
    pass
```

**Note**
With the code above any request to the base route of the application will be handled by the `index()` route.

**Note**
By default response from flask action handlers have the `application/html` content type.

Flask support path static path routing and path variable routing as most modern framework.

```py
@app.route('/api/users')
def index():
    # Define the login to serve application user
    pass
```

The code above handle any request /GET /api/users send to the web application endpoints.

```py
@app.route('/api/users/<name>')
def index(name: str):
    # Define the login to serve application user
    pass
```

The code above defines a path variable route that will handle /GET /api/users/test for instance. The `<name>` at the end will hold a value that is passed to the request handler.

-- Route parameters converters
In order to convert route variables to a given type, flask provides a list of converters for `strings`, `integers`, `floating` point value, `path` which is similar to string but also accepts slashes and universal identifier type.

> `string` -> (default) accepts any text without a slash
> `int` -> accepts positive integers
> `float` -> accepts positive floating point values
> `path` -> like string but also accepts slashes
> `uuid` -> accepts UUID strings

-- URL redirection behaviour

**Note**
/api/users/ will always be redirected to /api/users similar to how UNIX folder system works
/api/posts will always match /api/posts and any attempt from the client to access /api/posts/ will return a 404 http response.

-- URL Building

To build a URL to a specific function, use the `url_for()` function from `flask` namespace. It accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule.

The benefit of using generated url is to prevent typo error that happen when developper has to manually type in url for a given route.

```py
from flask import url_for

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('profile', username='John Doe'))
```

-- HTTP Method in route decorator

By defailt flask supports http `GET` method for all route defines by the application. In order to override the HTTP method used for a given action, developpers must pass `methods=[]` keywargs to `route()` decorator:

```py
from flask import request

# The route below support GET and POST http methods
@app.route('/api/users', methods=['GETE', 'POST'])
def users():
    if (request.method) == 'POST':
        # Perform POST action
    else:
        # Perform GET action
```

**Note** request
`request` is `flask` singleton that holds a reference to the current application request.

**Note** `@app.post()`, `@app.put()`, `@app.get()`, `@app.delete()`
For various HTTP method, flask provides a decorator function to easily with routing.

**Note**
If `GET` is present, Flask automatically adds support for the `HEAD` method and handles `HEAD` requests according to the HTTP RFC. Likewise, OPTIONS is automatically implemented for you.

- Static Files
  Flask can support serving static assets during development phase of web application. But in production, rely on the webserver serving the application instead.

**Note**
ust create a folder called `static` in your package or next to your module and it will be available at `/static` on the application.

Generating url for a css file on the web server:

```py
url = url_for('static', filename='style.css')
```

- Template rendering

Flask support template rendering through the `Jinja` python module. To render a template you can use the render_template() method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments.

```py
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

**Note**
Flask will look for templates in the templates folder. So if your application is a module, this folder is next to that module, if it’s a package it’s actually inside your package

**Note**
Inside templates you also have access to the `config`, `request`, `session` and g 1 objects as well as the `url_for()` and `get_flashed_messages()` functions.

- Interacting with Flask Request

Flask `request` is a global with implementation based on the `Context Local` API standard.

-- Context Locals

`Context Locals` are global instances that are proxies to objects that are local to a specific context.

**Scenario**
Imagine the context being the handling thread. A request comes in and the web server decides to spawn a new thread. When Flask starts its internal request handling it figures out that the current thread is the active context and binds the current application and the WSGI environments to that context (thread).

**Note**
In some environment like testing, flask might not provide a context a gloabl request object with the context. To solve that issue, developper might create a request object and bind it to the context.

Flask provides `test_request_context()` function to create a test context request object:

```py
from flask import request

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
```

> app.request_context(environment) -> Returns a request object for the current context to be used by the flask application.

```py
with app.request_context(environ):
    assert request.method == 'POST'
```

-- Basic Request methods

> request.path -> Returns the request path string
> request.method -> Returns the HTTP verb of the request
> request.form -> Returns an array of the attributes sends through the `POST` or `PUT` verbs

```py
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

```

> request.args -> Request Query or URL Search parameters

```py
searchword = request.args.get('key', '')
```

> request.files -> Returns a list of uploaded files

**Note**
List of returned files are python `file` API object, therefore `save(dst)` on the object is avaible for writing file to disk.

```py
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
```

If you want to use the filename of the client to store the file on the server, pass it through the secure_filename() function that Werkzeug provides for you:

```py
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(file.filename)
```

> request.cookies -> Dictionary of with all clients transmitted cookies.

```py
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
```

- Flask response object

Flask offer developper with function for creating response:

```py
from flask import make_response

@app.route('/')
def index():
    res = make_response(render_template(...))
    # Transform the flask response
    return res

```

-- Basic response method

> make_response(content, code) -> To create flask response object
> response.set_cookie(name, value) -> used to add cookie to the client response
> response.headers -> List of response headers

```py
def index():
    response = make_response(render_template('index.html', foo=42), 200)
    # Add a response header
    response.headers['X-Parachutes'] = 'parachutes are cool'
    return response
```

> app.redirect(location, code) -> Redirect client to an application location or an external location

```py
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))
```

> app.abort(code) -> Throw an HTTP error code that end the request exection

```py
from flask import abort

@app.route('/login')
def login():
    abort(401)
    # Any code after the abort call never get executed
```

- Flask error handlers

By default a black and white error page is shown for each error code. If you want to customize the error page, you can use the errorhandler() decorator:

```py
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```

- APIs with JSON

A common response format when writing an API is JSON. It’s easy to get started writing such an API with Flask. By default, If you return a dict or list from a view, it will be converted to a JSON response.

```py
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

@app.route("/users")
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]
```

**Note**
This is a shortcut to passing the data to the jsonify() function, which will serialize any supported JSON data type. That means that all the data in the dict or list must be JSON `serializable`.

- Flask Sessions

n addition to the request object there is also a second object called `session` which allows you to store information specific to a user from one request to the `next`.

This is implemented on top of cookies for you and signs the cookies cryptographically.

```py
from flask import session

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

```

> session.put(name, value) -> Add a value to the session
> session.pop(name, None) -> retrieve an element from the session

**Note**
A secret key should be as random as possible. Your operating system has ways to generate pretty random data based on a cryptographic random generator. Use the following command to quickly generate a value for `Flask.secret_key` (or `SECRET_KEY`):

> python -c 'import secrets; print(secrets.token_hex())' '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'

## Flask request context

The request context keeps track of the request-level data during a request. Rather than passing the request object to each function that runs during a request, the `request` and `session` proxies are accessed instead.

- Purpose
  When the Flask application handles a request, it creates a Request object based on the environment it received from the WSGI server. Because a worker (thread, process, or coroutine depending on the server) handles only one request at a time, the request data can be considered global to that worker during that request.

- Lifetime

When flask starts handling a request, it pushes the request context, which also push the `app context`. When it serve response to client, it pop the `request context` and then the `app context`

**Note**
The context is unique to each thread (or other worker type). request cannot be passed to another thread, the other thread has a different context space and will not know about the request the parent thread was pointing to.

Context locals are implemented using Python’s contextvars and Werkzeug’s LocalProxy. Python manages the lifetime of context vars automatically, and local proxy wraps that low-level interface to make the data easier to work with.

- Manually pushing the request context

If you try to access request, or anything that uses it, outside a request context, like in test environment, you’ll get an error message. using `app.test_request_context()` pushes a request context that can be used in test environemnt:

```py
def generate_report(year):
    format = request.args.get('format')
    ...

with app.test_request_context(
        '/make_report/2017', data={'format': 'short'}):
    generate_report()
```

**Note** How context works
When the request starts, a RequestContext is created and pushed, which creates and pushes an AppContext first if a context for that application is not already the top context. While these contexts are pushed, the current_app, g, request, and session proxies are available to the original thread handling the request.

**Note**
Immediately before application context and request context are popped, `the teardown_request()` and `teardown_appcontext()` functions are executed. These execute even if an unhandled exception occurred during dispatch.

- Callbacks and Errors

Flask dispatches a request in multiple stages which can affect the request, response, and how errors are handled. The contexts are active during all of these stages.

-- Blueprints
A Blueprint can add handlers for these events that are specific to the blueprint. The handlers for a blueprint will run if the blueprint owns the route that matches the request:

1. `before_request()` is called before each request. If the before_request return a value, it's treated as the response and other handlers are not called

2. If `before_request()` the view function for the matching request is called

3. View response (a.k.a string/html for HTML, or json for APIs) is passed to `after_request()` function which might returned a modified version of the response.

4. `after_request()` returns which calls the `teardown_request()` and `teardown_appcontext()` functions.

**Note** When exceptions are raised
If an exception is raised before the teardown functions, Flask tries to match it with an errorhandler() function to handle the exception and return a response. If no error handler is found, or the handler itself raises an exception, Flask returns a generic 500 Internal Server Error response.

## Modular application with blueprints

It's a technique provided by flask to componentize (separation of concern) large application development.
Blueprints, works like flask application but are actually not flask application. They are instead blueprint of how application is to be constructed.

### Use cases

- Factor an application into a set of blueprints. (For large applications)
- Register a blueprint on an application at a URL prefix and/or subdomain.
- Register a blueprint multiple times on an application with different URL rules.
- Provide template filters, static files, templates, and other utilities through blueprints.
- Register a blueprint on an application for any of these cases when initializing a Flask extension.

**Note**
A blueprint in Flask is not a pluggable app because it is not actually an application – it’s a set of operations which can be registered on an application, even multiple times.

**Note**
Blueprints instead provide separation at the `Flask level`, `share application config`, and can `change an application object` as necessary with being registered. The downside is that you cannot unregister a blueprint once an application was created without having to destroy the whole application object.

- Creating a Blueprint

To create a blueprint, flask provides a `Blueprint` class for the purpose:

> blueprint = Blueprint(name, module, [template_folder='', static_folder=''])

```py
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template(f'pages/{page}.html')
    except TemplateNotFound:
        abort(404)

```

**Note**
Using `@blueprint_name.route()` decorator on a method, the blueprint will record the intention of registering action on the application when registered.

**Note**
`name` parameter used when creating a blueprint will be used as prefix to route actions defined in the blueprint

- Registering blueprints

To register a blueprint on a given application call `register_blueprint()` on the application context.

> app.register_blueprint(blueprint_module, [url_prefix='prefix']) -> url_prefix add a prefix to blueprint routes

```py
from flask import Flask
from module.blueprint_name import blueprint_name

app = Flask(__name__)
app.register_blueprint(simple_page)
```

- Nesting blueprints

Flask makes it possible to nest a blueprint on another blueprint. For the code below, the child blueprint will gain the parent’s name as a prefix to its name, and child URLs will be prefixed with the parent’s URL prefix.

```py
# parent module file
parent = Blueprint('parent', __name__, url_prefix='/parent')
child = Blueprint('child', __name__, url_prefix='/child')
parent.register_blueprint(child)

# main.py
app.register_blueprint(parent)

# To build the url to create action of the child blueprint
url_for('parent.child.create') # /parent/child/create
```

- Blueprint Resources

-- Blueprint Resource Folder
The folder is inferred from the second argument to `Blueprint` which is usually `__name__`. This argument specifies what logical Python module or package corresponds to the blueprint.

**Note**
If it points to an actual Python package that package (which is a folder on the filesystem) is the resource folder. If it’s a module, the package the module is contained in will be the resource folder.

> Blueprint.root_path -> Returns the resource folder of the blueprint
> Blueprint.open_resource('path/to/file') -> Open a resource from the blueprint folder

- Static Files

A blueprint can expose a folder with static files by providing the path to the folder on the filesystem with the `static_folder` argument.

```py
admin = Blueprint('admin', __name__, static_folder='assets')

url_for('admin.assets', filename='style.css') # Returns the url to the static assets in the blueprint
```

- Templates

If you want the blueprint to expose templates you can do that by providing the `template_folder` parameter to the Blueprint constructor:

```py
admin = Blueprint('admin', __name__, template_folder='templates')
```

**Note**
So if you have a blueprint in the folder `yourapplication/admin` and you want to render the template `'admin/index.html'` and you have provided `templates` as a `template_folder` you will have to create a file like this: `yourapplication/admin/templates/admin/index.html`. The reason for the extra admin folder is to avoid getting our template overridden by a template named index.html in the actual application template folder.

- Blueprint Error Handlers

Blueprints support the errorhandler decorator just like the Flask application object, so it is easy to make Blueprint-specific custom error pages.

```py
blueprint_name = Blueprint(...)

@blueprint_name.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html')
```

**Note**
404 and 405 exceptions will not be handled by blueprints. Therefore if there is need to provide a custom handlers for them, it must be done at the application level:

```py
@app.errorhandler(404)
@app.errorhandler(405)
def _handle_api_error(ex):
    if request.path.startswith('/api/'):
        return jsonify(error=str(ex)), ex.code
    else:
        return ex
```

## Signals (Flask 0.6+)

Flask signals is provided through the `blinker` library, but will gracefully fallback if it os not available.

Flask signal provides a mecahnism for implementing pub-sub pattern in the core framework or other extension.
By default, flask comes with couple of signals. Signals should not modify data, data is pass to subscriber and subscribers perform action based on the data passed.

> connect(subscriber_func, sender) -> Contract exposed by the signal API to subscribe to the signal produced data.
> disconnect() -> Unsubscribe from the signal instance

**Note**
For all core signals, the sender is the application that issue the signal. Unless one want to listen from all signal from all applications, one should provide a sender reference when connecting to a signal.

```py
from flask import template_rendered
from contextlib import contextmanager

@contextmanager
def captured_templates(app):
    recorded = []
    # Make sure to subscribe with an extra **extra argument so that your calls don’t fail if Flask introduces new arguments to the signals API.
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

with captured_templates(app) as templates:
    rv = app.test_client().get('/')
    assert rv.status_code == 200
    assert len(templates) == 1
    template, context = templates[0]
    assert template.name == 'index.html'
    assert len(context['items']) == 10
```

**Note**
Make sure to subscribe with an extra \*\*extra argument so that your calls don’t fail if Flask introduces new arguments to the signals API.

Additionally there is a convenient helper method (connected_to()) that allows you to temporarily subscribe a function to a signal with a context manager on its own. Because the return value of the context manager cannot be specified that way, you have to pass the list in as an argument:

```py
from flask import template_rendered

def captured_templates(app, recorded, **extra):
    def record(sender, template, context):
        recorded.append((template, context))
    return template_rendered.connected_to(record, app)

with captured_templates(app, templates, **extra) as templates:
    rv = app.test_client().get('/')
    assert rv.status_code == 200
    assert len(templates) == 1
    template, context = templates[0]
    assert template.name == 'index.html'
    assert len(context['items']) == 10
```

- Creating signals

If you want to use signals in your own application, you can use the blinker library directly.
The most common use case are named signals in a custom Namespace.. This is what is recommended most of the time:

```py
my_signals = flask.signals.Namespace()

# Create a signal that will be fired when the model is saved
model_saved = my_signals.signal('model-saved')

# model_saved.name -> Returns the name of the signal
```

- Sending signals

If you want to emit a signal, you can do so by calling the send() method. It accepts a sender as first argument and optionally some keyword arguments that are forwarded to the signal subscribers:

```py
class Model(object):
    # ...

    def save(self):
        model_saved.send(self)
```

**Warning**
Never pass current_app as sender to a signal. Use `current_app._get_current_object()` instead. The reason for this is that current_app is a proxy and not the real application object.
That means you should never pass a proxy to the signal as sender.

- Decorator Based Signal Subscriptions

With Blinker 1.1 you can also easily subscribe to signals by using the new `connect_via()` decorator:

```py
from flask import template_rendered

@template_rendered.connect_via(app)
def when_template_rendered(sender, template, context, **extra):
    print(f'Template {template.name} is rendered with {context}')
```

## Error and Exception management

- Error Logging

Sentry provides an interface or API for dealing with application errors.
Sentry aggregates duplicate errors, captures the full stack trace and local variables for debugging, and sends you mails based on new errors or frequency thresholds.

To install flask sentry sdk:

> pip install sentry-sdk[flask]

And to integrate sendtry into flask application:

```py
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init('YOUR_DSN_HERE', integrations=[FlaskIntegration()])
```

- Error Handlers

When an error occurs in Flask, an appropriate `HTTP status code` will be returned.

> 400 - 499 -> Errors related to client request or request data.
> 500 - 599 -> Indicates a server error or application error

**Note**
An error handler is a function that return a response when a type or error is raised.
Error handlers are passed the error to handle wich most of time are the `HTTPException` error class.

- Registering error handlers
  To register an error handlers, we decorate the function with `@errorhandler()` or use `register_error_handler()` function of the flask insance.

```py
@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

# or, without decorator
app.register_error_handler(400, handle_bad_request)
```

**Note**
`werkzeug.exceptions.BadRequest` is a base class of `werkzeug.exceptions.HTTPException` base with `400` as exception code.

- Registring non-standard error codes

Non-standard HTTP codes cannot be registered by code because they are not known by Werkzeug.

To register non-standard HTTP code, developpers must create a class that inherit from the `werkzeug.exceptions.HTTPException` with the appropriate error code:

```py
class InsufficientStorage(werkzeug.exceptions.HTTPException):
    code = 507
    description = 'Not enough storage space.'

app.register_error_handler(InsufficientStorage, handle_507)

def main():
    # Executes code
    raise InsufficientStorage() # Raise a Non-Standard HTTP error

if __name__ === '__main__':
    main()
```

- Error handling

**Note**
By default, flask handle `InternalServerError` for 500 application exception, `NotFound` for 404 exception, and `MethodNotAllowed` for 405 exceptions.
They are all subclasses of `HTTPException` class.

**How Flask Hanldles Error**
When Flask catches an exception while handling a request, it is first looked up by code. If no handler is registered for the code, Flask looks up the error by its class hierarchy; the most specific handler is chosen. If no handler is registered, HTTPException subclasses show a generic message about their code, while other exceptions are converted to a generic “500 Internal Server Error”.

**Example**
For example, if an instance of `ConnectionRefusedError` is raised, and a handler is registered for `ConnectionError` and `ConnectionRefusedError`, the more specific `ConnectionRefusedError` handler is called with the exception instance to generate the response.

**Note**
Handlers registered on the blueprint take precedence over those registered globally on the application.

- Unhandled Exceptions

`InternalServerError` is thrown by default if exception occured at the application level.

If there is an error handler registered for `InternalServerError`, this will be invoked. As of Flask 1.1.0, this error handler will always be passed an instance of `InternalServerError`, not the original unhandled error.

**Note**
The original error is available as `e.original_exception`.

- `abort`

`abort()` function that aborts a request with a HTTP error from werkzeug as desired. It will also provide a plain black and white error page for you with a basic description, but nothing fancy.

- Blueprint Error Handlers

In Modular Applications with Blueprints, most error handlers will work as expected. However, there is a caveat concerning handlers for `404` and `405` exceptions. These error handlers are only invoked from an appropriate raise statement or a call to abort in another of the blueprint’s view functions; they are not invoked by, e.g., an invalid URL access.

## Configurations Handling

The way Flask is designed usually requires the configuration to be available when the application starts up.

`config` object of the flask instance is the place where flask puts framework related configuration values, and can be used by application developpers or extensions developpers.

- Basic configurations

`config` is a dictionary on which values (configuration values) can be added:

```py
from flask import Flask

app = Flask(__name__)

app.config['TESTING'] = True
```

The code above test how testing configuration value can be defined in flask application.

To add multiple values at one, use the dict update method:

```py
app.config.update(
    TESTING=Tue,
    SECRET='SuperSecretKey'
)
```

- Builtin configuration values

> ENV -> (Default: `production`) The environment in which the application is running on

> DEBUG -> Whether the application is running in debug mode. `FLASH_DEBUG` in OS environment.

> TESTING -> Enable testing mode. Exceptions are propagated rather than handled by the the app’s error handlers.

> PROPAGATE_EXCEPTIONS -> Exceptions are re-raised rather than being handled by the app’s error handlers. If not set, this is implicitly true if TESTING or DEBUG is enabled.

> TRAP_HTTP_EXCEPTIONS -> If there is no handler for an `HTTPException-type` exception, re-raise it to be handled by the interactive debugger instead of returning it as a simple error response.

> TRAP_BAD_REQUEST_ERRORS -> Trying to access a key that doesn’t exist from request dicts like args and form will return a `400 Bad Request` error page. Enable this to treat the error as an unhandled exception instead so that you get the interactive debugger. This is a more specific version of TRAP_HTTP_EXCEPTIONS. If unset, it is enabled in debug mode.

> SECRET_KEY -> A secret key that will be used for securely signing the session cookie and can be used for any other security related needs by extensions or your application. It should be a long random bytes or str. For example, copy the output of this to your config:

> SESSION_COOKIE_NAME -> (Default: `session`) The name of the session cookie. Can be changed in case you already have a cookie with the same name.

> SESSION_COOKIE_DOMAIN -> (Default: `None`) The domain match rule that the session cookie will be valid for. If not set, the cookie will be valid for all subdomains of SERVER_NAME. If False, the cookie’s domain will not be set.

> SESSION_COOKIE_PATH -> (Default: `None`) The path that the session cookie will be valid for. If not set, the cookie will be valid underneath APPLICATION_ROOT or / if that is not set.

> SESSION_COOKIE_HTTPONLY -> (Default: `True`) Browsers will not allow JavaScript access to cookies marked as “HTTP only” for security.

> SESSION_COOKIE_SECURE -> (Default: `False`) Browsers will only send cookies with requests over HTTPS if the cookie is marked “secure”. The application must be served over HTTPS for this to make sense.

> SESSION_COOKIE_SAMESITE -> (Default: `None`) Restrict how cookies are sent with requests from external sites. Can be set to 'Lax' (recommended) or 'Strict'. See Set-Cookie options.

> PERMANENT_SESSION_LIFETIME -> (Default: `timedelta(days=31) (2678400 seconds)`) If session.permanent is true, the cookie’s expiration will be set this number of seconds in the future. Can either be a datetime.timedelta or an int. Flask’s default cookie implementation validates that the cryptographic signature is not older than this value.

> SESSION_REFRESH_EACH_REQUEST -> (Default: `True`) Control whether the cookie is sent with every response when session.permanent is true. Sending the cookie every time (the default) can more reliably keep the session from expiring, but uses more bandwidth. Non-permanent sessions are not affected.

> USE_X_SENDFILE -> (Default: `False`) When serving files, set the X-Sendfile header instead of serving the data with Flask. Some web servers, such as Apache, recognize this and serve the data more efficiently. This only makes sense when using such a server.

> SEND_FILE_MAX_AGE_DEFAULT -> (Default: `None`) When serving files, set the cache control max age to this number of seconds. Can be a datetime.timedelta or an int. Override this value on a per-file basis using `get_send_file_max_age()` on the application or blueprint.
> If None, send_file tells the browser to use conditional requests will be used instead of a timed cache, which is usually preferable.

> SERVER_NAME -> (Default: `None`) Inform the application what host and port it is bound to. Required for subdomain route matching support. If set, will be used for the session cookie domain if `SESSION_COOKIE_DOMAIN` is not set. Modern web browsers will not allow setting cookies for domains without a dot. To use a domain locally, add any names that should route to the app to your hosts file.
> If set, `url_for` can generate external URLs with only an application context instead of a request context.

> APPLICATION_ROOT -> (Default: `'/'`) Inform the application what path it is mounted under by the application / web server. This is used for generating URLs outside the context of a request (inside a request, the dispatcher is responsible for setting SCRIPT_NAME instead; see Application Dispatching for examples of dispatch configuration). Will be used for the session cookie path if SESSION_COOKIE_PATH is not set.

> PREFERRED_URL_SCHEME -> (Default: `'http'`) Use this scheme for generating external URLs when not in a request context.

> MAX_CONTENT_LENGTH -> (Default: `None`) Don’t read more than this many bytes from the incoming request data. If not set and the request does not specify a CONTENT_LENGTH, no data will be read for security.

> JSON_AS_ASCII (Deprecated) -> (Default: `True`) Serialize objects to ASCII-encoded JSON. If this is disabled, the JSON returned from jsonify will contain Unicode characters. This has security implications when rendering the JSON into JavaScript in templates, and should typically remain enabled.

> JSON_SORT_KEYS (Deprecated v2.2: use app.json.sort_keys) -> (Default: `True`) Sort the keys of JSON objects alphabetically. This is useful for caching because it ensures the data is serialized the same way no matter what Python’s hash seed is. While not recommended, you can disable this for a possible performance improvement at the cost of caching.

> JSONIFY_PRETTYPRINT_REGULAR (Deprecated v2.2: use app.json.compact) -> (Default: False) jsonify() responses will be output with newlines, spaces, and indentation for easier reading by humans. Always enabled in debug mode.

> JSONIFY_MIMETYPE (Deprecated: use app.json.mimetype) -> (Default: `'application/json'`) The mimetype of jsonify responses.

> TEMPLATES_AUTO_RELOAD -> (Default: `None`) Reload templates when they are changed. If not set, it will be enabled in debug mode.

> EXPLAIN_TEMPLATE_LOADING -> (Default: `False`) Log debugging information tracing how a template file was loaded. This can be useful to figure out why a template was not loaded or the wrong file appears to be loaded.

> MAX_COOKIE_SIZE -> Warn if cookie headers are larger than this many bytes. Defaults to 4093. Larger cookies may be silently ignored by browsers. Set to 0 to disable the warning.

- Configuration from Python files

```py
app = Flask(__name__)
app.config.from_object('yourapplication.default_settings')
app.config.from_envvar('YOURAPPLICATION_SETTINGS')

```

In the code above, the first loads the configuration from the `yourapplication.default_settings` module and then overrides the values with the contents of the file the `YOURAPPLICATION_SETTINGS` environment variable points to. This environment variable can be set in the shell before starting the server.

**Note**
The configuration files themselves are actual Python files. Only values in uppercase are actually stored in the config object later on. So make sure to use uppercase letters for your config keys.

An example configuration file:

```cfg
SECRET_KEY = '...'
DB_HOST = '127.0.0.1'
```

- Configuration from data files
It is also possible to load configuration from a file in a format of your choice using from_file().

To load configuration from toml file:

```py
import toml
app.config.from_file('path/to/file', load=tom.load)
```

To load configuration from json file:

```py
app.config.from_file('path/to/file', load=json.load)
```

- Configuring from Environment Variables

In addition to pointing to configuration files using environment variables, you may find it useful (or necessary) to control your configuration values directly from the environment.

```py
app.config.from_prefixed_env() #load configuration files from OS environment
```

**Note**
Configuration that might be loaded from the environment variable must have `FLASK_` as prefix to be able to be a candidate to the load.
