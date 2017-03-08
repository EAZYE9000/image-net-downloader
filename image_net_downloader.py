import urllib2
import os
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

def store_raw_images():
	
	url = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07745940'
	response = urllib2.urlopen(url)
	image_urls = response.read().decode()
	print(image_urls)

	if not os.path.exists('imagedownload'):
		os.makedirs('imagedownload')

	#pic_num = 1
	pic_num = len(os.listdir('imagedownload/')) + 1

	for i in image_urls.split('\n'):
		try:
			f = urllib2.urlopen(i).read()
			with open("imagedownload/"+str(pic_num)+".jpg", "wb") as code:
				code.write(f)
			pic_num += 1
		except Exception as e:
			pic_num = len(os.listdir('imagedownload/')) + 1

store_raw_images()