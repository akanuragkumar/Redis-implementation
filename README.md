# Assignment_redis

## [Link for assignment questions](https://github.com/akanuragkumar/assignment_redis/blob/master/assignment_questions.pdf)

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
5. TCP-KeepAlive for better performance

   ```bash
    vim /etc/redis/redis.conf
   # Update the value to 0
    tcp-keepalive 0
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
Set the value at key name to value\
Time complexity: O(1)

```json
 application/json - {"key":"key", "value":"value"}
```
### `get` 
2. `GET /get` 
Return the value at key name, or error if the key doesn't exist\
Time complexity: O(1)
```json
 application/json - {"key":"key"}
```
### `delete` 
3. `POST /delete` 
Delete one or more keys specified by names\
Time complexity: O(1)
```json
 application/json - {"key":"key"}
```
### `expire` 
4. `POST /expire` 
Set an expire flag on key name for time seconds. time can be represented by an integer or a Python timedelta object\
Time complexity: O(1)
```json
 application/json - {"key":"key", "expiry":"expiry"}
```
### `keys` 
5. `POST /keys` 
Returns a list of keys matching pattern\
Time complexity: O(N) where N is the numbers of keys in database
```json
 application/json - {"key":"key"}
```
### `pttl` 
6. `POST /pttl` 
Returns the number of milliseconds until the key name will expire\
Time complexity: O(1)
```json
 application/json - {"key":"key"}
```
### `zadd` 
7. `POST /zadd` 
Set any number of element-name, score pairs to the key name\
Time complexity: O(log(N)) where N is the number of elements in the set
```json
 application/json - {"set_name":"set_name","difficulty_level":"difficulty_level","element":"element"}
```
### `zrange` 
8. `POST /zrange?withscores=True` 
Return a range of values from sorted set name between start and end sorted in ascending order
start and end can be negative, indicating the end of the range
desc a boolean indicating whether to sort the results descendingly
withscores indicates to return the scores along with the values. The return type is a list of (value, score) pairs\
Time complexity: O(log(N)+M) where N is number of elemets in set and M is number of elements returned
```json
 application/json - {"set_name":"set_name","start":"start","end":"end"}
```
### `zrank` 
9. `POST /zrank` 
Returns a 0-based value indicating the rank of value in sorted set name\
Time complexity: O(log(N)) where N is the number of elements in the set
```json
 application/json - {"set_name":"set_name","element":"element"}
```
### `smembers` 
10. `POST /smembers` 
Return all members of the set name\
Time complexity: O(log(N)) where N is the set cardinality

```json
 application/json - {"set_name":"set_name"}
``` 
### `flushdb` 
11. `POST /flushdb`
Delete all keys in the current database\
Time complexity: O(log(N) where N is the number of keys in database

### `hmset` 
12. `POST /hmset` 
Sets each key in the mapping dict to its corresponding value in the hash name\
Time complexity: O(N) where N is the number of fields being set
```json
 application/json - {"key":"key","hash":{"Question":"what is photosynthesis", "answer":"sun", "exam":"upsc", "year":"2019"}}
``` 
### `hgetall` 
13. `POST /hgetall` 
Return a Python dict of the hash's name/value pairs\
Time complexity: O(N) where N is the size of the hash
```json
 application/json - {"key":"key"}
``` 
### `rename` 
14. `POST /rename` 
Rename key src to dst\
Time complexity: O(1)
```json
 application/json - {"old_key":"old_key","new_key":"new_key"}
``` 
### `lpush` 
15. `POST /lpush` 
Push values onto the head of the list name\
Time complexity: O(1)
```json
 application/json - {"list_name":"list_name","key":"key"}
``` 
### `lpop` 
16. `POST /lpop` 
Remove and return the first item of the list name\
Time complexity: O(1)

### `lindex` 
17. `POST /lindex` 
Return the item from list name at position index
Negative indexes are supported and will return an item at the end of the list\
Time complexity: O(N) where N is the number of elements to traverse to get to the element at index
```json
 application/json - {"list_name":"list_name","index":"index"}
 ``` 
 ### `llen` 
 18. `POST /llen` 
Return the length of the list name\
Time complexity: O(S+N) where S is the distance of start offset from HEAD for small lists, from nearest end (HEAD or TAIL) for large lists; and N is the number of elements in the specified range
```json
 application/json - {"list_name":"list_name"}
 ``` 
 ### `pipeline_example` 
  19. `POST /pipeline_example` 
Return a new pipeline object that can queue multiple commands for later execution. transaction indicates whether all commands should be executed atomically. Apart from making a group of operations atomic, pipelines are useful for reducing the back-and-forth overhead between the client and server
```json
 application/json - {"keys":[key1,key2,...]}
 ``` 
