echo "Case 1"
curl -X POST -F "image=@2.jpg" http://localhost:8000/upload/
echo "\nCase 2"
curl -X POST -F "image=@3.jpg" http://localhost:8000/upload/
echo "\nCase 3"
curl -X POST -F "image=@copy.png" http://localhost:8000/upload/
echo "\nCase 4"
curl -X POST -F "image=@copy2.png" http://localhost:8000/upload/