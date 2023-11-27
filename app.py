from flask import Flask, request, jsonify
import docker
import os

app = Flask(__name__)

client = docker.from_env()

api_key = os.environ['API_KEY']

@app.route('/healthcheck')
def hello_world():
    return 'Hello World'

@app.route('/create', methods=['POST'])
def create_service():
    json = request.get_json()
    if json["api-key"] == api_key:
        try:
            service_name = json.get('service_name')
            service = client.services.create(image=json.get('image'), 
                                             name=service_name, 
                                             env=json.get('env'), 
                                             constraints=json.get('constraints'))
            return jsonify({"message": f"Service {service_name} created successfully."})
        except:
            return jsonify({"message": "Error Occured"})
    else : 
        return jsonify({"message": "Wrong API Key"})

@app.route('/logs', methods=['POST'])
def log_service():
    json = request.get_json()
    if json["api-key"] == api_key:
        try:
            service_name = json.get('service_name')
            service = client.services.get(service_name)
            return service.logs(timestamps=True, tail=100, details=True, stdout=True, stderr=True)
        except:
            return jsonify({"message": "Error Occured"})
    else : 
        return jsonify({"message": "Wrong API Key"})

@app.route('/delete', methods=['POST'])
def delete_service():
    json = request.get_json()
    if json["api-key"] == api_key:
        try:
            service_name = json.get('service_name')
            service = client.services.get(service_name)
            service.remove()
            return jsonify({"message": f"Service {service_name} deleted successfully."})
        except:
            return jsonify({"message": "Error Occured"})
    else : 
        return jsonify({"message": "Wrong API Key"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)