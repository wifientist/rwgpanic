from flask import Flask, request, render_template
import socket
import json

app = Flask(__name__)

def get_mac_address(ip):
    # This is a placeholder function. MAC address retrieval requires administrative privileges and platform-specific solutions.
    return "00:00:00:00:00:00"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_info', methods=['POST'])
def get_info():
    data = request.get_json()
    #print('received data: ', data)
    result = {
        'IP Address': request.remote_addr,
        'User Agent': request.headers.get('User-Agent'),
        'Locale': request.headers.get('Accept-Language'),
        'Referer': request.headers.get('Referer'),
        'Host': request.headers.get('Host'),
        'Platform': data.get('platform', 'N/A'),
        'Screen Resolution': data.get('screen_resolution', 'N/A'),
        'Timezone': data.get('timezone', 'N/A'),
        'Cookies Enabled': data.get('cookies_enabled', 'N/A'),
        'Online Status': data.get('online_status', 'N/A'),
        'Connection Type': data.get('connection_type', 'N/A'),
        'Downlink': data.get('downlink', 'N/A'),
        'RTT': data.get('rtt', 'N/A')
    }
    print('result:',result)

    #TODO now 1) figure out which RWG this is, and 2) push this data to an RWG endpoint api there

    return result
