# Assignment_redis

## Quickstart

To work in a sandboxed Python environment it is recommended to install the app in a Python [virtualenv](https://pypi.python.org/pypi/virtualenv).

1. Install dependencies

    ```bash
    $ cd /path/to/assignment_redis
    $ pip install -r requirements.txt
    ```

2. Setup a Redis  

  ```bash
brew install redis

start Redis server using configuration file

redis-server

```
3. Run server in development environment

   ```bash
   $ python app/runserver.py
   ```

   View at http://127.0.0.1:5000
   
4. Prod level server using Nginx, Gunicorn, Uwsgi

   ```bash
   $ pip install gunicorn
   $ gunicorn --bind 0.0.0.0:5000 wsgi:app
   ```
   To set up nginx to proxy requests and configuring system ctl files follow the steps mentioned here [nginx-gunicorn](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04).

## Project Structure

### Backend 
```shell
assignment_redis
├── app                           # contains application files
│    └── app.py                   # contains resource files for API
├── runserver.py                  # contains runserver to run development code
├── wsgi.py                       # wsgi file
├── nginx.conf                    # nginx configuration file 
├── assignment_redis.conf         # standard way of actually running application                                            └── app.ini                       # create the unix socket which to used to communicate between nginx and uwsgi                                                
```
## API Documentation 

### `set` 

1. `POST /set` 

```json
 application/json - {"key":"key", "value":"value"}
```
### `get` 
2. `GET /get` 

```json
 application/json - {"key":"key"}
```
### `delete` 
3. `POST /delete` 

```json
 application/json - {"key":"key"}
```
### `expire` 
4. `POST /expire` 

```json
 application/json - {"key":"key", "expiry":"expiry"}
```
### `keys` 
5. `POST /keys` 

```json
 application/json - {"key":"key"}
```
### `pttl` 
6. `POST /pttl` 

```json
 application/json - {"key":"key"}
```
### `zadd` 
7. `POST /zadd` 

```json
 application/json - {"set_name":"set_name","difficulty_level":"difficulty_level","element":"element"}
```
### `zrange` 
8. `POST /zrange?withscores=True` 

```json
 application/json - {"set_name":"set_name","start":"start","end":"end"}
```
### `zrank` 
9. `POST /zrank` 

```json
 application/json - {"set_name":"set_name","element":"element"}
```
### `smembers` 
10. `POST /smembers` 

```json
 application/json - {"set_name":"set_name"}
``` 
### `flushdb` 
11. `POST /flushdb`

### `hmset` 
12. `POST /hmset` 

```json
 application/json - {"key":"key","hash":{"Question":"what is photosynthesis", "answer":"sun", "exam":"upsc", "year":"2019"}}
``` 
### `hgetall` 
13. `POST /hgetall` 

```json
 application/json - {"key":"key"}
``` 
### `rename` 
14. `POST /rename` 

```json
 application/json - {"old_key":"old_key","new_key":"new_key"}
``` 
### `lpush` 
15. `POST /lpush` 

```json
 application/json - {"list_name":"list_name","key":"key"}
``` 
### `lpop` 
16. `POST /lpop` 

### `lindex` 
17. `POST /lindex` 

```json
 application/json - {"list_name":"list_name","index":"index"}
 ``` 
 ### `llen` 
 18. `POST /llen` 

```json
 application/json - {"list_name":"list_name"}
 ``` 
 ### `pipeline_example` 
  19. `POST /pipeline_example` 

```json
 application/json - {"keys":[key1,key2,...]}
 ``` 
