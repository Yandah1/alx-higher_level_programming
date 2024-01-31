PROJECT: 0x14. JavaScript - Web scraping


# File Operations Script

This script provides functionality for reading and printing the content of a file, writing a string to a file, and displaying the status code of a GET request. It utilizes the `utf-8` encoding and the `request` module.

## Read and Print File Content

The script reads and prints the content of a file specified by the file path argument.

### Usage

```shell
node read-file.js [file path]
```

### Arguments

- `file path`: The path to the file to be read.

## Write to File

The script writes a string to a file specified by the file path argument.

### Usage

```shell
node write-file.js [file path] [string to write]
```

### Arguments

- `file path`: The path to the file to be written.
- `string to write`: The string that will be written to the file.

## Display GET Request Status Code

The script performs a GET request to a specified URL and displays the status code.

### Usage

```shell
node get-request.js [URL]
```

### Arguments

- `URL`: The URL to request using the GET method.

## Error Handling

If an error occurs during the file reading or writing process, the script will print the error object.

## Dependencies

- `request` module: This script relies on the `request` module to perform GET requests.

## Installation

1. Make sure you have [Node.js](https://nodejs.org) installed on your system.
2. Install the dependencies by running the following command:

```shell
npm install request
```

## License

This script is licensed under the [MIT License](LICENSE).
# Star Wars Movie Title Script

This script retrieves and prints the title of a Star Wars movie based on the given movie ID. It utilizes the Star Wars API and the `request` module.

## Print Star Wars Movie Title

The script retrieves the title of a Star Wars movie by matching the episode number with the given movie ID.

### Usage

```shell
node star-wars-movie.js [movie ID]
```

### Arguments

- `movie ID`: The ID of the Star Wars movie.

## Dependencies

- `request` module: This script relies on the `request` module to make API requests.

## Installation

1. Make sure you have [Node.js](https://nodejs.org) installed on your system.
2. Install the dependencies by running the following command:

```shell
npm install request
```

## License

This script is licensed under the [MIT License](LICENSE).

# Star Wars Wedge Antilles Script

This script prints the number of movies where the character "Wedge Antilles" is present. It utilizes the Star Wars API and the `request` module.

## Print Number of Movies with Wedge Antilles

The script retrieves the number of movies where the character "Wedge Antilles" appears.

### Usage

```shell
node star-wars-wedge-antilles.js [API URL]
```

### Arguments

- `API URL`: The URL of the Star Wars API films endpoint.

## Dependencies

- `request` module: This script relies on the `request` module to make API requests.

## Installation

1. Make sure you have [Node.js](https://nodejs.org) installed on your system.
2. Install the dependencies by running the following command:

```shell
npm install request
```

## License

This script is licensed under the [MIT License](LICENSE).

# Loripsum Script

This script retrieves the contents of a webpage and stores it in a file. It utilizes the `request` module.

## Get Webpage Content and Store in File

The script performs a GET request to the specified URL and stores the body response in the specified file path.

### Usage

```shell
node loripsum.js [URL] [file path]
```

### Arguments

- `URL`: The URL to request.
- `file path`: The file path to store the body response.

## Dependencies

- `request` module: This script relies on the `request` module to make HTTP requests.

## Installation

1. Make sure you have [Node.js](https://nodejs.org) installed on your system.
2. Install the dependencies by running the following command:

```shell
npm install request
```

## License

This script is licensed under the [MIT License](LICENSE).

# Number of Completed Tasks Script

This script computes the number of tasks completed by user ID. It utilizes the `request` module.

## Compute Number of Completed Tasks

The script retrieves the tasks from the specified API URL and computes the number of completed tasks for each user.

### Usage

```shell
node completed-tasks.js [API URL]
```

### Arguments

- `API URL`: The URL of the API.

## Dependencies

- `request` module: This script relies on the `request` module to make API requests.

## Installation

1. Make sure you have [Node.js](https://nodejs.org) installed on your system.
2. Install the dependencies by running the following command:

```shell
npm install request
```

## License

This script is licensed under the [MIT License](LICENSE).
