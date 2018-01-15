# webapp-eval-django

This example application is part of an evaluation of web environments. The objective is to implement the same requirements and compare the results in terms of effort, performance and maintainability.

This particular repository tests the [Python](https://www.python.org/)/[Django](https://www.djangoproject.com/) environment.

## Common requirements

- Public homepage *done*
- Authentication system with password and email confirmation *done*
- Authentication system with Github *done*
- Authenticated page to display user info *done*
- Authenticated form to alter password *done*
- Unique request ID *done*
- Structured logging *done*
- I18n, adapt to browser headers *done*
- Authentication system with OpenID connect
- Permissions system
- OAuth 2 provider
- API with OAuth auth
- API method to obtain token via user and pw
- API to retrieve user info in JSON
- API to update user info in JSON
- Fast dev cycle
- Web tests
- Bonus: JavaScript pipeline integration
- Bonus: real-time (websockets) user change notification
- Bonus: small deployment size (containerized)
- Bonus: efficiently deal with multiple cores
- Bonus: serve static content with correct headers
- Bonus: call external API
- Bonus: exception reporting

## Important additional modules used

TODO

## How to run project

1. Create database __webapp_django__ manually
1. Configure database connection parameters in __webapp/settings.py__
1. __./manage.py createsuperuser__
1. __./manage.py runserver__

## i18n

First extract messages to file:

    django-admin makemessages -l pt

Then compile messages:

    django-admin compilemessages


## Links to tests of other environments

- Go (TODO)
- Elixir/Phoenix (TODO)
- Scala/Play (TODO)
- Haskell/Yesod (TODO)