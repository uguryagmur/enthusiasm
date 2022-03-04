# Simple Image API

### Architecture

> All responses must be lossles and in the same file format

> Original forms of all images will be saved to the system and image id will be send in response. When user send a request, it should contain payload as base64 or image id to retrieve that from db

- **gray_scale**
  - convert an image payload to gray scale
- **deblur**
  - deblurring the image
- **crop**
  - crop for the given coordinates (rectangle crop)
- **flip**
  - flip the image 90 degrees left or right

