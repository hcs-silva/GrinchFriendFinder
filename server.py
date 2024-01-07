from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer, HTTPServer
import json, os, random
from urllib.parse import urlparse, parse_qs

from GrinchGame import GrinchGame

grinch = GrinchGame()

HOST = "localhost"
# HOST="2.82.173.210"
PORT = 8080
HOSTNAME= "http://"+HOST+":"+str(PORT)

class MyServer(BaseHTTPRequestHandler):

    # def do_GET(self):
    #     self.send_response(200)
    #     self.send_header("Content-type", "application/json")
    #     self.send_header("Access-Control-Allow-Origin", "*")  # Allowing any origin, update as needed
    #     self.end_headers()

    #     # Create a dictionary to represent your JSON data
    #     response_data = {
    #         "method": "GET",
    #         "message": grinch.getNames(),
    #         "path": self.path
    #     }

    #     # Convert the dictionary to a JSON-formatted string
    #     json_response = json.dumps(response_data)

    #     # Send the JSON response as bytes
    #     self.wfile.write(bytes(json_response, "utf-8"))

    def get_filenames(self, name):
        try:
            # Get the list of filenames in the directory
            filenames = os.listdir("./images")

            # Print the filenames
            print('Filenames in the directory:')
            filenames_allowed=[]
            for filename in filenames:
                if name.lower() in filename:
                    filenames_allowed.append(filename)
            print(filenames_allowed)
            return filenames_allowed

        except FileNotFoundError:
            print(f"Directory not found.")
        except PermissionError:
            print(f"Permission error while accessing directory.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def do_GET(self):
        if self.path.startswith("/getImagefor/"):
            print(self.path.replace("/getImagefor/", ""))
            keyword=self.path.replace("/getImagefor/", "").replace("ç", "c")
            print("Keyword: "+keyword)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")  # Allowing any origin, update as needed
            self.end_headers()

            file_list=self.get_filenames(keyword)
            if len(file_list)==0:
                file_list=['get_fuck_out.jpeg']

            # Create a dictionary to represent your JSON data
            image_choice = file_list[random.randint(0, len(file_list) - 1)]

            response_data = {
                "image": HOSTNAME + "/images/"+image_choice
            }

            # Convert the dictionary to a JSON-formatted string
            json_response = json.dumps(response_data)

            # Send the JSON response as bytes
            self.wfile.write(bytes(json_response, "utf-8"))
        elif self.path.startswith("/images/"):
            # If the requested path starts with "/images/", serve images
            file_list=self.get_filenames("bacalhuco")
            image_file_path="./images/"+self.path.replace("/images/", "").replace("ç", "c")

            print("Image file path: "+image_file_path)
            if os.path.isfile(image_file_path):
                # If the file exists, send the image
                self.send_response(200)
                self.send_header("Content-type", "image/jpeg")  # Adjust content type based on your image type
                self.end_headers()

                with open(image_file_path, "rb") as image_file:
                    self.wfile.write(image_file.read())
            else:
                # If the file does not exist, return a 404 response
                self.send_response(404)
                self.end_headers()
                self.wfile.write(bytes("File not found", "utf-8"))
        else:
            # For other paths, respond with a basic message
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Image Server</title></head>", "utf-8"))
            self.wfile.write(bytes("<body><p>This is an image server. Try accessing images in the '/images/' path.</p></body></html>", "utf-8"))


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = json.loads(post_data)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")  # Allowing any origin, update as needed
        self.end_headers()

        # Create a dictionary to represent your JSON data
        # print(json.loads(post_data)['name'])
        print(parsed_data)
        response_data = {
            "method": "POST",
            "grinch_response": grinch.iAm(parsed_data['name'], parsed_data['code_word']),
            "message": "This is an example JSON response",
            "data_received": parsed_data,
            "path": self.path
        }

        # Convert the dictionary to a JSON-formatted string
        json_response = json.dumps(response_data)

        # Send the JSON response as bytes
        self.wfile.write(bytes(json_response, "utf-8"))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")  # Allow requests from any origin, update as needed
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

if __name__ == "__main__":        
    host_name = HOST
    server_port = PORT

    # web_server = HTTPServer((host_name, server_port), MyServer)
    web_server = ThreadingHTTPServer((host_name, server_port), MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")
