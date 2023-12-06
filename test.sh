curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/monkey.webp" \
  -F "username=CryptoCanvasArt" \
  -F "description=A very common image that was famous on NFT"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/monkey-2.jpeg" \
  -F "username=NFTNomad" \
  -F "description=An image similar to the already posted image with minor visual modifications"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_62.png" \
  -F "username=NFTJediMaster" \
  -F "description=Hazard celebrating a sizzling solo goal"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_60.jpg" \
  -F "username=SelenaGomez" \
  -F "description=How does this dress look?"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_59.png" \
  -F "username=ArtVortex" \
  -F "description=Bee-ware: fashion hazard"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_45.png" \
  -F "username=PixelProphet" \
  -F "description=A low resolution bee-man"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_49.png" \
  -F "username=CryptoCanvasArt" \
  -F "description=A portrait that I made(Theft)"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_27.png" \
  -F "username=EtherVisions" \
  -F "description=Lego Man"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_28.png" \
  -F "username=EtherMystique" \
  -F "description=Lego Woman"

sleep 2

# Images 75 and 76 are from DAALE

# curl -X POST http://localhost:8000/api/upload/ \
#   -H "Content-Type: multipart/form-data" \
#   -F "image=@test-images/image_75.png" \
#   -F "username=ArtVortex" \
#   -F "description=your_description"

# curl -X POST http://localhost:8000/api/upload/ \
#   -H "Content-Type: multipart/form-data" \
#   -F "image=@test-images/image_76.png" \
#   -F "username=DigitalDynamo" \
#   -F "description=your_description"

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_2.png" \
  -F "username=QuantumCanvas" \
  -F "description=Signed poster of 'Scarf game so strong, it's got me bone-afide'"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_3.png" \
  -F "username=PixelProphet" \
  -F "description=A tampered poster"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_61.png" \
  -F "username=SelenaFanPage" \
  -F "description=My favourite celebrity"