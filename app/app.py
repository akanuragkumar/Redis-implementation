import redis
from flask import Flask, request, jsonify
from healthcheck import HealthCheck

r = redis.Redis()
pipe = r.pipeline()

app = Flask(__name__)
app.config["DEBUG"] = True
error = {"code": 400, "message": "error in format data"}

health = HealthCheck(app, "/healthcheck")


@app.route("/set", methods=["POST"])
def set():
	data = request.json
	if request.json and ({"key", "value"} <= data.keys()):
		pass
	else: 
		return jsonify(error)
	key = data['key']	
	value = data['value']
	resp = r.set(key, value)
	return jsonify(resp)


@app.route("/get", methods=["GET"])
def get():
	data = request.json	
	if request.json and ({"key"} <= data.keys()):
		pass
	else: 
		return jsonify(error)	
	key = data['key']
	resp = r.get(key)
	if resp == None:
		return 'key not present'
	return jsonify(resp)


@app.route("/delete", methods=["POST"])
def delete():
	data = request.json
	if request.json and ({"key"} <= data.keys()):
		pass
	else: 
		return jsonify(error)		
	key = data['key']
	resp = r.delete(key)
	if resp == None:
		return 'key not present'
	return jsonify(resp)     


@app.route("/expire", methods=["POST"])
def expire():
	data = request.json
	if request.json and ({"key", "expiry"} <= data.keys()):
		pass
	else: 
		return jsonify(error)   	 
	key = data['key']
	expiry = data['expiry']
	resp = r.expire(key, expiry)
	if resp == None:
		return 'key not present'
	return jsonify(resp)   


@app.route("/keys", methods=["POST"])
def keys():
	data = request.json
	if request.json and ({"key"} <= data.keys()):
		pass
	else: 
		return jsonify(error)	
	key = data['key']
	resp = r.keys(key)
	if resp == None:
		return 'key not present'
	return jsonify(resp)  


@app.route("/pttl", methods=["POST"])
def pttl():
	data = request.json
	if request.json and ({"key"} <= data.keys()):
		pass
	else: 
		return jsonify(error)		
	key = data['key']
	resp = r.pttl(key)
	if resp == None:
		return 'key not present'
	return jsonify(resp)  


@app.route("/zadd", methods=["POST"])
def zadd():
	data = request.json
	if request.json and ({"set_name", "difficulty_level", "element"} <= data.keys()):
		pass
	else: 
		return jsonify(error)		
	set_name = data['set_name']
	difficulty_level = data['difficulty_level']
	element = data['element']
	dict = {element : difficulty_level}
	resp = r.zadd(set_name, dict)
	return jsonify(resp)   


@app.route("/zrange", methods=["POST"])
def zrange():
	data = request.json
	if request.json and ({"set_name", "difficulty_level", "element"} <= data.keys()):
		pass
	else: 
		return jsonify(error)	
	set_name = data['set_name']
	start = data['start']
	end = data['end']
	if request.args['withscores'] is not None:
		withscores = request.args['withscores']
		resp = r.zrange(set_name, start, end, withscores=True)
	else:
		resp = r.zrange(set_name, start, end)
	if resp == None:
		return 'set_name not present'		
	return jsonify(resp) 


@app.route("/zrank", methods=["POST"])
def zrank():
	data = request.json
	if request.json and ({"set_name", "value"} <= data.keys()):
		pass
	else: 
		return jsonify(error)	
	set_name= data['set_name']
	element = data['value']
	resp = r.zrank(set_name, element)
	if resp == None:
		return 'set_name not present'
	return jsonify(resp)  


@app.route("/smembers", methods=["POST"])
def smembers():
	data = request.json
	if request.json and ({"set_name"} <= data.keys()):
		pass
	else: 
		return jsonify(error)	
	set_name= data['set_name']
	resp = r.members(set_name)
	if resp == None:
		return 'set_name not present'
	return jsonify(resp) 


@app.route("/flushdb", methods=["GET"])
def flushdb():
	resp = r.flushdb()
	return jsonify(resp) 


@app.route("/hmset", methods=["POST"])
def hmset():
	data = request.json
	if request.json and ({"key", "hash"} <= data.keys()):
		pass
	else: 
		return jsonify(error)			
	key= data['key']
	hash_data = data['hash']
	resp = r.hmset(key, hash_data)
	return jsonify(resp)


@app.route("/hgetall", methods=["POST"])
def hgetall():
	data = request.json
	if request.json and ({"key"} <= data.keys()):
		pass
	else: 
		return jsonify(error)
	key= data['key']
	resp = r.hgetall(key)
	if resp == None:
		return 'key not present'
	return jsonify(resp)


@app.route("/rename", methods=["POST"])
def rename():
	data = request.json
	if request.json and ({"old_key", "new_key"} <= data.keys()):
		pass
	else: 
		return jsonify(error)
	old_key= data['old_key']
	new_key= data['new_key']
	resp = r.rename(old_key, new_key)
	if resp == None:
		return 'key not present'
	return jsonify(resp) 


@app.route("/lpush", methods=["POST"])
def lpush():
	data = request.json
	if request.json and ({"list_name", "key"} <= data.keys()):
		pass
	else: 
		return jsonify(error)
	list_name = data['list_name']
	key = data['key']
	resp = r.lpush(list_name, key)
	return jsonify(resp) 


@app.route("/lpop", methods=["POST"])
def lpop():
	resp = r.lpop()
	return jsonify(resp) 


@app.route("/lindex", methods=["POST"])
def lindex():
	data = request.json
	if request.json and ({"list_name", "index"} <= data.keys()):
		pass
	else: 
		return jsonify(error)
	list_name = data['list_name']
	index = data['index']
	resp = r.lindex(list_name, index)
	return jsonify(resp) 	


@app.route("/llen", methods=["POST"])
def llen():
	data = request.json
	if request.json and ({"list_name"} <= data.keys()):
		pass
	else: 
		return jsonify(error)
	list_name = data['list_name']
	resp = r.llen(list_name)
	return jsonify(resp) 


@app.route("/pipeline_example", methods=["POST"])
def pipeline_example():
	data = request.json
	if request.json and ({"key"} <= data.keys()):
		pass
	else: 
		return jsonify(error)
	keys = data['keys']
	for key in keys:
		pipe.get(key)
	resp = pipe.execute()
	return jsonify(resp) 


if __name__ == '__main__':
	app.run()
