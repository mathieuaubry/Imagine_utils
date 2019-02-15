
import argparse
import os
import re
parser = argparse.ArgumentParser()

parser.add_argument(
	'--out-html', type=str, help='output html file')

parser.add_argument(
	'--img-dir', type=str, help='image directory')

args = parser.parse_args()



### Writing the table format###
f = open(args.out_html, 'w')
f.write('<html>\n')
f.write('<head>\n')
f.write('\t<title></title>\n')
f.write('\t<meta name=\"keywords\" content= \"Visual Result\" />  <meta charset=\"utf-8\" />\n')
f.write('\t<meta name=\"robots\" content=\"index, follow\" />\n')
f.write('\t<meta http-equiv=\"Content-Script-Type\" content=\"text/javascript\" />\n')
f.write('\t<meta http-equiv=\"expires\" content=\"0\" />\n')
f.write('\t<meta name=\"description\" content= \"Project page of style.css\" />\n')
f.write('\t<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\" media=\"screen\" />\n')
f.write('\t<link rel=\"shortcut icon\" href=\"favicon.ico\" />\n')
f.write('</head>\n')
f.write('<body>\n')
f.write('<div id="website">\n')
f.write('<center>\n')
f.write('\t<div class=\"blank\"></div>\n')
f.write('\t<h1>\n')
f.write('\t\tVisual Results\n')
f.write('\t</h1>\n')
f.write('</center>\n')
f.write('<div class=\"blank\"></div>\n')
f.write('<center>\n')
f.write('<div>\n')

f.write('</div>\n')

### --- ###


cluster_dir = os.listdir(args.img_dir)

for i in range(len(cluster_dir)) : 
	cluster_path = os.path.join(args.img_dir, cluster_dir[i])
	
	
	f.write('<table>\n')
	caption = '\t\t<caption>Cluster {:d}</caption>\n'.format(i)
	f.write(caption)
	f.write('\t<tr>\n')
	imgs = os.listdir(cluster_path)
	imgs = sorted(imgs, key=lambda x: int(x.split('_')[0]))
	for j in range(len(imgs)) : 
		
		tmp_path = os.path.join(cluster_path, imgs[j])
		msg = '\t\t<td> <a download=\" {} \" href=\"{}\" title="ImageName"> <img  src=\"{}\" /></a>\n'.format(tmp_path, tmp_path, tmp_path)
		f.write(msg)
		if j % 10 == 9 :
			f.write('\t</tr>\n')
			f.write('\t<tr>\n')
	f.write('\t</tr>\n')
	
	f.write('</table>\n')
	
f.write('</center>\n</div>\n </body>\n</html>\n')
f.close()

