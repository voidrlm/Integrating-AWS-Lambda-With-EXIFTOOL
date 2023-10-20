export EXIFTOOL_VERSION=12.68 #Specific the version here
rm -rf layer
curl https://exiftool.org/Image-ExifTool-${EXIFTOOL_VERSION}.tar.gz  --output Image-ExifTool-${EXIFTOOL_VERSION}.tar.gz
tar -xf Image-ExifTool-${EXIFTOOL_VERSION}.tar.gz
rm -rf Image-ExifTool-${EXIFTOOL_VERSION}.tar.gz
mkdir -p layer/bin
cp Image-ExifTool-${EXIFTOOL_VERSION}/exiftool layer/bin/.
sed -i "1 s/^.*$/#\!\/opt\/bin\/perl -w/" ./layer/bin/exiftool
cp -r Image-ExifTool-${EXIFTOOL_VERSION}/lib layer/bin/.
rm -rf Image-ExifTool-${EXIFTOOL_VERSION}
cd layer
zip -r exiftool.zip ./*
cd ..
mv layer/exiftool.zip .
rm -rf layer