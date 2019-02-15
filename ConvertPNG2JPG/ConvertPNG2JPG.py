##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## Created by: Xi SHEN
## Ecole des Ponts, Imagine
## Email: xi.shen@enpc.fr
## 
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os 
import argparse
import PIL.Image as Image 


## add your images extension if not in the list 

def ConvertPNG2JPG(inDir, outDir, imgExtension = ['png']) : 
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
				outPath = imgPath.replace('.png', '.jpg')
				w, h = Image.open(imgPath).convert('RGB').size
				## convert
				cmd = 'convert {} -resize {:d}x{:d} -size {:d}x{:d} xc:white +swap -compose over -composite {}'.format(imgPath, w, h, w, h, outPath)
				print (cmd)
				os.system(cmd)
			
				## remove png
				cmd = 'rm {}'.format(imgPath)
				print (cmd)
				os.system(cmd)
			
			
if __name__ == "__main__":
			
	parser = argparse.ArgumentParser()
	parser.add_argument(
		    '--inDir', type=str , help='input image directory')

	parser.add_argument(
		    '--outDir', type=str , help='output image directory, will be created')

	args = parser.parse_args()
	print (args)
	ConvertPNG2JPG(args.inDir, args.outDir)
