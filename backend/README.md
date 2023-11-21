## AFRO-PIX BACKEND



## Description

The **AFRO-PIX-API** is the backbone of an application for an image sharing app.



## Development set up


-   Check that python 3.11.x or above is installed:

    ```
    python --version
    >> Python 3.11.x
    ```

-   Install and set up postgresql:

    Follow the guide in this [documentation](https://docs.google.com/document/d/1G0UQUusBdoAvydu7w_EaaXjvOLC3UidFN3z7dddCG3o/edit?usp=sharing)


    * [How to install PostgreSQL on windows](https://www.geeksforgeeks.org/install-postgresql-on-windows/)
    * [How to install PostgreSQL on Linux](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-22-04-quickstart)
    * [How to install PostgreSQL on Mac](https://www.geeksforgeeks.org/install-postgresql-on-mac/)


-   Install and setup Redis
    * [How to Install and Setup Redis](https://redis.io/docs/install/install-redis/)

-  Database
    * Switch to postgres account (in terminal)
        ```bash
        $ sudo -iu postgres psql
        >>> postgres=#
        ```
    * Create or Change default password
        ```bash
        postgres=# ALTER USER postgres PASSWORD "myPassword";
        >>> ALTER ROLE
        ```
    * Create a database instance.
        ```bash
        postgres=# CREATE DATABASE "afropix";

        ```
    * Finally, exit the psql client by using the `\q` command.


- Clone the Afro-Pix repo and cd into it
    ```
    git clone https://github.com/[username|afro-pix.git]
    ```
- Create a virtual environment with pipenv
    - [How to Install Pipenv](https://pypi.org/project/pipenv/)
    - [Read more about Pipenv](https://realpython.com/pipenv-guide/)

        ```bash
        $ pip install pipenv  # install pipenv

        $ pipenv shell  # create a virtual environment and activate

        $ make  # install dependencies from Pipfile
        ```

- Create Application environment variables and save them in .env file in the root folder
    ```
    DEBUG=True
    SECRET_KEY='super_secret'
    ALLOWED_HOSTS='*'
    RUN_MODE='development'
    LANGUAGE_CODE='en-us'
    TIME_ZONE='Africa/Nairobi'

    REDIS_CACHE_SERVER='127.0.0.1:6379'
    DB_NAME='afropix'
    DB_USER='postgres'
    DB_PASSWORD=*The password that you set while configuring postgres*
    DB_HOST='127.0.0.1'
    DB_PORT='5432'
    ```

- Running migrations

    ```
    make migrations

    make migrate
    ```



- Run application.
    ```
    make serve
    ```



### Merge Request Process

-   A contributor shall identify a task to be done from the board.
-   If there is a bug , feature or chore that has not been included among the tasks, the contributor can add it only after consulting the Scrum Master and the task being accepted.
-   The Contributor shall then create a branch off the `development` branch where they are expected to undertake the task they have chosen.
-   After undertaking the task, a fully detailed pull request shall be submitted to the owners of this repository for review.
-   If there any changes requested ,it is expected that these changes shall be effected and the pull request resubmitted for review.Once all the changes are accepted, the pull request shall be closed and the changes merged into `development` by the owners of this repository.
-   There should be only one commit per Merge Request, to achieve this use `git commit --amend`


### Code Quality Conventions

Please refer to the best practices outlined in BestPractices.md



## Built with
- Python version  3.11
- Django (DRF)
- Djoser
- Postgres
- Redoc
 ```
