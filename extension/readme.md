
File Extensions and Media Types
# Description

Most files on Windows and macOS have file extensions, which are suffixes that begin with a period (.), such as .gif, .jpg, or .pdf. Operating systems use these extensions to decide which program should open a file.

Web browsers, however, do not rely on file extensions. Instead, they use media types (also known as MIME types) sent by a web server in an HTTP header. Media types tell the browser how to handle and display a file.
For example:

.gif → image/gif

.jpg / .jpeg → image/jpeg

Web servers usually determine a file’s media type by looking at its file extension and mapping it to the appropriate media type.

#  Objective

Create a Python program called extensions.py that:

Prompts the user for the name of a file.

Outputs the correct media type based on the file’s extension.

Treats file extensions case-insensitively.

#  Supported File Extensions

The program should recognize the following extensions:

File Extension	Media Type
.gif	image/gif
.jpg, .jpeg	image/jpeg
.png	image/png
.pdf	application/pdf
.txt	text/plain
.zip	application/zip

#  Default Behavior

If the file has an unknown extension

OR if the file has no extension at all

The program should output:

application/octet-stream

This is a common default media type for binary data.

# we can't use "in" in this program because file name can be myjpg.pdf

# we can use endswith() function if we have multiple values we use tuple (value1, value2 ) in endswith 