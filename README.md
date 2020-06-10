# Assignment_redis

## Quickstart

To work in a sandboxed Python environment it is recommended to install the app in a Python [virtualenv](https://pypi.python.org/pypi/virtualenv).

1. Install dependencies

    ```bash
    $ cd /path/to/assignment_redis
    $ pip install -r requirements.txt
    ```

2. Setup a Redis  

  ```Mongodb
rew install redis

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
   To set up nginx to proxy requests and configuring system ctl files follow the steps mentioned here [virtualenv]         (https://pypi.python.org/pypi/virtualenv).

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
2. `GET /get` 

```json
 application/json - {"key":"key"}
```
3. `POST /delete` 

```json
 application/json - {"key":"key"}
```
4. `POST /expire` 

```json
 application/json - {"key":"key", "expiry":"expiry"}
```
5. `POST /keys` 

```json
 application/json - {"key":"key"}
```
6. `POST /pttl` 

```json
 application/json - {"key":"key"}
```
7. `POST /zadd` 

```json
 application/json - {"set_name":"set_name","difficulty_level":"difficulty_level","element":"element"}
```
8. `POST /zrange?withscores=True` 

```json
 application/json - {"set_name":"set_name","start":"start","end":"end"}
```
9. `POST /zrank` 

```json
 application/json - {"set_name":"set_name","element":"element"}
```
10. `POST /smembers` 

```json
 application/json - {"set_name":"set_name"}
``` 
10. `POST /flushdb` 

11. `POST /hmset` 

```json
 application/json - {"key":"key","hash":{"Question":"what is photosynthesis", "answer":"sun", "exam":"upsc", "year":"2019"}}
``` 
12. `POST /hgetall` 

```json
 application/json - {"key":"key"}
``` 
13. `POST /rename` 

```json
 application/json - {"old_key":"old_key","new_key":"new_key"}
``` 
14. `POST /lpush` 

```json
 application/json - {"list_name":"list_name","key":"key"}
``` 
15. `POST /lpop` 

16. `POST /lindex` 

```json
 application/json - {"list_name":"list_name","index":"index"}
 ``` 
 16. `POST /llen` 

```json
 application/json - {"list_name":"list_name"}
 ``` 
  16. `POST /pipeline_example` 

```json
 application/json - {"key":[key1,key2,...]}
 ``` 
