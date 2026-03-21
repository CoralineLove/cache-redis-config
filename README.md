# Cache Redis Config
====================

### Description
===============

A Python package for managing Redis configurations and caching.

### Features
----------

*   Cache operations: set, get, delete, expire
*   Supports multiple Redis configurations
*   Automatic connection pooling
*   Zero dependency on external libraries

### Technologies Used
-------------------

*   Python 3.8+
*   `redis-py` library for Redis interactions
*   `pip` for package management

### Installation
------------

To install the `cache-redis-config` package, run the following command:

```bash
pip install git+https://github.com/your-username/cache-redis-config.git
```

### Usage
-----

```python
from cache_redis_config import Cache

# Initialize the cache with Redis configuration
config = {
    'host': 'localhost',
    'port': 6379,
    'db': 0
}

cache = Cache(config)

# Set a value for a key
cache.set('key', 'value')

# Get a value for a key
value = cache.get('key')

# Delete a key
cache.delete('key')

# Expire a key
cache.expire('key', 3600)  # expires in 1 hour
```

### Usage Configuration
--------------------

You can configure the Redis connection through environment variables or a YAML file.

#### Environment Variables

| Variable Name | Description | Default Value |
| --- | --- | --- |
| REDIS_HOST | Redis host | `localhost` |
| REDIS_PORT | Redis port | `6379` |
| REDIS_DB | Redis database | `0` |

#### YAML Configuration File

Create a `config.yaml` file with the following content:

```yml
redis:
  host: 'your-redis-host'
  port: 6379
  db: 0
```

### Contributing
-------------

Contributions are welcome! Please submit any issues or pull requests to the project repository.

### License
--------

`cache-redis-config` is released under the MIT License.

### Authors
---------

*   Your Name
*   Your Email
*   Your Website
*   Your GitHub Profile