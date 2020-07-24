import os
import PyPluMA

class LEfSePlugin:
   def input(self, filename):
      infile = open(filename, 'r')
      self.parameters = dict()
      for line in infile:
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1].strip()
      self.parameters['inputfile'] = PyPluMA.prefix()+"/"+self.parameters['inputfile']
      print(self.parameters['inputfile'])
      self.parameters['outputdir'] = PyPluMA.prefix()+"/"+self.parameters['outputdir']
      if (os.path.exists(self.parameters['outputdir'])):
         os.system("rm -r "+self.parameters['outputdir'])

   def run(self):
      os.system('./plugins/LEfSe/lefse-format_input.py '+self.parameters['inputfile']+' tmp.in -c '+self.parameters['class']+' -s '+self.parameters['subclass']+' -u '+self.parameters['subject']+' -f c -o 1000000')
      #subprocess.call('plugins/LEfSe/run_lefse.py', 'tmp.in', 'output.lefse.res')

   def output(self, filename):
      os.system('./plugins/LEfSe/run_lefse.py tmp.in '+filename+'.res')
      os.system('./plugins/LEfSe/lefse-plot_res.py '+filename+'.res'+' '+filename+".bargraph.png")
      os.system('./plugins/LEfSe/lefse-plot_cladogram.py '+filename+'.res'+' '+filename+".cladogram.png --format png")
      if (not os.path.exists(self.parameters['outputdir'])):
         os.system('mkdir '+self.parameters['outputdir']) 
      os.system('./plugins/LEfSe/lefse-plot_features.py tmp.in '+filename+".res"+' '+self.parameters['outputdir']+"/")
      os.system('rm tmp.in')
      #subprocess.call('plugins/LEfSe/lefse-plot_features.py', 'tmp.in', 'output.lefse.res', self.parameters['outputdir'])
