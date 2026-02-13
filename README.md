# Sample Web Server

A simple Python HTTP web server with multiple endpoints for learning and development purposes.

## Features

- Simple HTTP server using Python's built-in `http.server` module
- RESTful API endpoints
- JSON response format
- Query parameter support
- HTML home page with documentation

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

Clone the repository:

```bash
git clone https://github.com/moongomoongo/sample-web-server.git
cd sample-web-server
```

## Usage

Run the server:

```bash
python app.py
```

The server will start on `http://localhost:8000`

## Available Endpoints

### GET /
Returns the home page with HTML documentation and links to API endpoints.

### GET /api/hello
Returns a JSON greeting message.

**Query Parameters:**
- `name` (optional): The name to greet. Defaults to "Guest"

**Examples:**
```
http://localhost:8000/api/hello
http://localhost:8000/api/hello?name=World
```

**Response:**
```json
{
  "message": "Hello, Guest!"
}
```

### GET /api/info
Returns server information in JSON format.

**Example:**
```
http://localhost:8000/api/info
```

**Response:**
```json
{
  "server": "Sample Python HTTP Server",
  "version": "1.0",
  "port": 8000,
  "status": "running"
}
```

## Testing

You can test the endpoints using curl:

```bash
# Test home page
curl http://localhost:8000/

# Test hello endpoint
curl http://localhost:8000/api/hello
curl http://localhost:8000/api/hello?name=Python

# Test info endpoint
curl http://localhost:8000/api/info
```

Or simply open them in your web browser.

## Project Structure

```
sample-web-server/
├── app.py           # Main server application
├── README.md        # This file
└── requirements.txt # Python dependencies (if any)
```

## License

MIT License

## Contributing

Feel free to fork this repository and submit pull requests with improvements.
