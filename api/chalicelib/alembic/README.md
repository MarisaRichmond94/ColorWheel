# Generic single-database configuration.

##Commands to remember:

1. Start the docker shell environment:

        docker-compose exec api /bin/bash

2. Move to the api directory:

        cd /code/api

3. Create a new generated revision file from the db_models:

        alembic -c chalicelib/alembic.ini revision --autogenerate -m "Useful change message"

4. Run the upgrade for your local DB:

        alembic -c chalicelib/alembic.ini upgrade HEAD

5. Connect to your local DB and check your changes

6. If you need to undo your changes, run a downgrade:

        alembic -c chalicelib/alembic.ini downgrade -1
