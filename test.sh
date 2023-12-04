# echo "\nCase 2"

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@../../AP/PicNix/images/test/image_10.png" \
  -F "username=your_username" \
  -F "description=your_description"

# echo "\nTest Process Img 10"
# curl -X POST -F "image=@../../AP/PicNix/images/test/image_27.png" http://localhost:8000/api/picnix/

# echo "\nTest Process Img 10"
# curl -X POST -F "image=@../../AP/PicNix/images/test/image_2.png" http://localhost:8000/api/picnix/

# echo "\nCase 2"
# curl -X POST -F "image=@../AP/PicNix/images/test/image_2.png" http://localhost:8000/upload/

# echo "\nCase 3"
# curl -X POST -F "image=@../AP/PicNix/images/test/image_3.png" http://localhost:8000/upload/

# echo "\nCase 4"
# curl -X POST -F "image=@../AP/PicNix/images/test/image_9.png" http://localhost:8000/upload/

# echo "\nCase 5"
# curl -X POST -F "image=@../AP/PicNix/images/test/image_10.png" http://localhost:8000/upload/

# echo "\nCase 6"
# curl -X POST -F "image=@../AP/PicNix/images/test/image_14.png" http://localhost:8000/upload/

# echo "\nCase 7"
# curl -X POST -F "image=@../AP/PicNix/images/test/image_27.png" http://localhost:8000/upload/

# echo "\nCase 8"
# curl -X POST -F "image=@../AP/PicNix/images/test/image_45.png" http://localhost:8000/upload/

# echo "\nCase 9"
# curl -X POST -F "image=@../AP/PicNix/images/test/image_49.png" http://localhost:8000/upload/
