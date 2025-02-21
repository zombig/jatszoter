# Jatszoter Service Agent

Agent for manage Docker Containers on hosts and provide
web SSH to containers.

## Build

Use Poetry to build a package, as a tarball and a wheel by default.

```shell
poetry build
```

## Development

You can install a packege to a current local environment by using
Poetry.

```shell
poetry install
```

## Run

You can run agent as a simple command line after install package, e.g.:

```shell
jatszoter-agent
```

Or you can use Poetry for the same without installation:

```shell
poetry run jatszoter-agent
```

Otherwise, you still could use package as a python module, e.g.:

```shell
python -m jatszoter.agent
```
