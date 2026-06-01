from http.server import HTTPServer, SimpleHTTPRequestHandler
from functools import partial
import threading

WEB_DIR = "./www"

servers = []

for i in range(3):
    port = 400 + i
    directory = f"{WEB_DIR}{i}"

    handler = partial(SimpleHTTPRequestHandler, directory=directory)

    server = HTTPServer(("localhost", port), handler)

    servers.append(server)

    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    print(f"Serving {directory} on http://localhost:{port}")

# Keep main thread alive
input("Press Enter to stop servers...\n")

for server in servers:
    server.shutdown()