curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/monkey.webp" \
  -F "username=CryptoCanvasArt" \
  -F "description=A very common image that was famous on NFT" \
  -F "timestamp=1701179721"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/monkey-2.jpeg" \
  -F "username=NFTNomad" \
  -F "description=An image similar to the already posted image with minor visual modifications" \
  -F "timestamp=1701285243"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_62.png" \
  -F "username=NFTJediMaster" \
  -F "description=Hazard celebrating a sizzling solo goal" \
  -F "timestamp=1701357892"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_60.jpg" \
  -F "username=SelenaGomez" \
  -F "description=How does this dress look?" \
  -F "timestamp=1701406327"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_59.png" \
  -F "username=ArtVortex" \
  -F "description=Bee-ware: fashion hazard" \
  -F "timestamp=1701502785"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_45.png" \
  -F "username=PixelProphet" \
  -F "description=A low resolution bee-man" \
  -F "timestamp=1701600034"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_49.png" \
  -F "username=CryptoCanvasArt" \
  -F "description=A portrait that I made(Theft)" \
  -F "timestamp=1701656978"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_27.png" \
  -F "username=EtherVisions" \
  -F "description=Lego Man" \
  -F "timestamp=1701728846"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_28.png" \
  -F "username=EtherMystique" \
  -F "description=Lego Woman" \
  -F "timestamp=1701785567"

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
  -F "description=Signed poster of 'Scarf game so strong, it's got me bone-afide'" \
  -F "timestamp=1701834210"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_3.png" \
  -F "username=PixelProphet" \
  -F "description=A tampered poster" \
  -F "timestamp=1701884402"

sleep 2

curl -X POST http://localhost:8000/api/upload/ \
  -H "Content-Type: multipart/form-data" \
  -F "image=@test-images/image_61.png" \
  -F "username=SelenaFanPage" \
  -F "description=My favourite celebrity" \
  -F "timestamp=1701892756"