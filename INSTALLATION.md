## Setting up Vue.js

1. Navigate to the Vue.js project directory:
    ```sh
    cd my-vue-project
    ```

2. Install the necessary dependencies:
    ```sh
    npm install
    ```

3. Start the development server:
    ```sh
    npm run serve
    ```

## Setting up Django

1. Navigate to the Django project directory:
    ```sh
    cd demo_app/
    ```

2. Install the necessary Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Start the Django development server:
    ```sh
    python manage.py runserver
    ```

## Log in Page Credentials

- **Username:** `test_user`
- **Password:** `securepassword`

## Database Information

- **Postgres Database Name:** `postgres`
- **Table Name for Storing Passwords:** `users`

## Restoring the PostgreSQL Database

1. Ensure PostgreSQL is running on your machine.

2. Navigate to the directory containing the database dump file:
    ```sh
    cd path/to/your/repo
    ```

3. Restore the database using the `pg_restore` command:
    ```sh
    pg_restore -h localhost -p 5432 -U postgres -d postgres -v db_backup.dump
    ```

    - `-h localhost`: Specifies the host. Replace `localhost` with your database host if it's different.
    - `-p 5432`: Specifies the port. Replace `5432` with your database port if it's different.
    - `-U postgres`: Specifies the username. Replace [`postgres`]
    - `-d postgres`: Specifies the database name. Replace [`postgres`]
    - `-v`: Enables verbose mode.
    - [`db_backup.dump`]

This will restore the PostgreSQL database from the dump file.