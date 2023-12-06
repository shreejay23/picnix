curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/monkey.webp" \
  -F "username=your_username" \
  -F "description=your_description"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/monkey-2.jpeg" \
  -F "username=your_username" \
  -F "description=your_description"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_62.png" \
  -F "username=your_username" \
  -F "description=your_description"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_60.jpg" \
  -F "username=your_username" \
  -F "description=your_description"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_59.png" \
  -F "username=your_username" \
  -F "description=your_description"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_45.png" \
  -F "username=your_username" \
  -F "description=your_description"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_49.png" \
  -F "username=your_username" \
  -F "description=your_description"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_27.png" \
  -F "username=your_username" \
  -F "description=your_description"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_28.png" \
  -F "username=your_username" \
  -F "description=your_description"

sleep 2

# Images 75 and 76 are from DAALE

# curl -X POST http://localhost:8000/api/upload/ \
#   -H "Content-Type: multipart/form-data" \
#   -F "image=@test-images/image_75.png" \
#   -F "username=your_username" \
#   -F "description=your_description"

# curl -X POST http://localhost:8000/api/upload/ \
#   -H "Content-Type: multipart/form-data" \
#   -F "image=@test-images/image_76.png" \
#   -F "username=your_username" \
#   -F "description=your_description"

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_2.png" \
  -F "username=your_username" \
  -F "description=your_description"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_3.png" \
  -F "username=your_username" \
  -F "description=your_description"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_61.png" \
  -F "username=your_username" \
  -F "description=your_description"