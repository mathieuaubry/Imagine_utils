##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Created by: Xi SHEN
## Ecole des Ponts, Imagine
## Email: xi.shen@enpc.fr
## 
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os 
import argparse 


# add your images extension if not in the list 
def ConvertHR2LR(inDir, outDir, outSize, outQuality, imgExtension=['png', 'jpg', 'jpeg', 'tiff', 'bmp']) :
	## Create output directory
	os.mkdir(outDir)

	## Copy all the files in the input directory to output directory
	cmd = 'cp -r {} {}'.format(inDir, outDir)
	print (cmd)
	os.system(cmd)

	## Conversion
	for root, dirs, files in os.walk(outDir, topdown=False):
		for img in files : 
			if img.split('.')[-1] in imgExtension : 
				imgPath = os.path.join(root, img)
				cmd = 'convert -resize {:d} -quality {:d} {} {}'.format(outSize, outQuality, imgPath, imgPath)
				print (cmd)
				os.system(cmd)
				
if __name__ == "__main__":
			
	parser = argparse.ArgumentParser()
	parser.add_argument(
		    '--inDir', type=str , help='input image directory')

	parser.add_argument(
		    '--outDir', type=str , help='output image directory, will be created')

	parser.add_argument(
		    '--outSize', type=int, default = 256, help='maximum dimension for output images, default value is 256')

	parser.add_argument(
		    '--outQuality', type=int, default = 75, help='output image quality (related to Compression rate), default is 75 (recommended)')

	args = parser.parse_args()
	print (args)
	ConvertHR2LR(args.inDir, args.outDir, args.outSize, args.outQuality)
