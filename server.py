# Copy over your server code from https://github.com/CP-Evenings-and-Weekends/http-server-2
# Then add a third endpoint that returns JSON, and remember to send CORS headers
# (Access-Control-Allow-Origin) so the browser will let your frontend talk to it.


import socket
import datetime
import json
import random

class Request:
    def __init__(self, request_text):
        self.parse_request(request_text.recv(4096).decode('utf-8').split('\r\n'))

    def parse_request(self, decoded_request_text):
        request_text = decoded_request_text[0].split()
        self.parsed_request = {
            "method": request_text[0],
            "uri": request_text[1]
        }

def build_html_response(text_body):
    html_body = f'<html><head><title>An Example Page</title></head><body>{text_body}</body></html>'
    return f"HTTP/1.1 200 OK\r\nContent-Type:text/html\r\nAccess-Control-Allow-Origin: *\r\nContent-Length:{len(html_body)}\r\n\r\n{html_body}"

def build_json_response(data_dict):
    json_body = json.dumps(data_dict)
    return f"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nAccess-Control-Allow-Origin: *\r\nContent-Length: {len(json_body)}\r\n\r\n{json_body}"

horror_characters = [
    {"character": "Michael Myers",
     "movie": "Halloween",
    },

    {"character": "Ghostface",
     "movie": "Scream",
    },

    {"character": "Freddy Krueger",
     "movie": "A Nightmare on Elm Street",
    },

    {"character": "Jason Voorhees",
     "movie": "Friday the 13th",
    },

    {"character": "Pennywise",
     "movie": "It",
    },

    {"character": "Art the Clown",
     "movie": "Terrifier",
    },

    {"character": "Leatherface",
     "movie": "The Texas Chainsaw Massacre",
    },

    {"character": "Chucky",
     "movie": "Child's Play",
    },

    {"character": "Pinhead",
     "movie": "Hellraiser",
    },

    {"character": "Hannibal Lecter",
     "movie": "The Silence of the Lambs",
    },

    {"character": "Candyman",
     "movie": "Candyman",
    },
]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 9292))

while True:
    server.listen()
    print("Waiting for a request on localhost:9292")

    client_connection, _client_address = server.accept()
    client_request = Request(client_connection)
    path = client_request.parsed_request['uri']

    if path == '/':
        client_connection.send(build_html_response('Hello World').encode())

    elif path == '/time':
        now = datetime.datetime.now()
        time_dict = {"current_time": str(now)}
        client_connection.send(build_json_response(time_dict).encode())

    elif path == "/horror-character":
        random_character = random.choice(horror_characters)
        client_connection.send(build_json_response(random_character).encode())

    client_connection.close()
