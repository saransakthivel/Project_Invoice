@echo off

rem Create app directory if it doesn't exist
if not exist app (
    mkdir app
    echo Created app directory.
) else (
    echo app directory already exists, skipping creation.
)

rem Create app\routers directory if it doesn't exist
if not exist app\routers (
    mkdir app\routers
    echo Created app\routers directory.
) else (
    echo app\routers directory already exists, skipping creation.
)

rem Create app\templates directory if it doesn't exist
if not exist app\templates (
    mkdir app\templates
    echo Created app\templates directory.
) else (
    echo app\templates directory already exists, skipping creation.
)

rem Create static directory if it doesn't exist
if not exist static (
    mkdir static
    echo Created static directory.
) else (
    echo static directory already exists, skipping creation.
)

rem Create files if they don't exist
if not exist app\main.py (
    type nul > app\main.py
    echo Created app\main.py
) else (
    echo app\main.py already exists, skipping creation.
)

if not exist app\database.py (
    type nul > app\database.py
    echo Created app\database.py
) else (
    echo app\database.py already exists, skipping creation.
)

if not exist app\models.py (
    type nul > app\models.py
    echo Created app\models.py
) else (
    echo app\models.py already exists, skipping creation.
)

if not exist app\schemas.py (
    type nul > app\schemas.py
    echo Created app\schemas.py
) else (
    echo app\schemas.py already exists, skipping creation.
)

if not exist app\crud.py (
    type nul > app\crud.py
    echo Created app\crud.py
) else (
    echo app\crud.py already exists, skipping creation.
)

if not exist app\utils.py (
    type nul > app\utils.py
    echo Created app\utils.py
) else (
    echo app\utils.py already exists, skipping creation.
)

echo Directories and files creation completed.
