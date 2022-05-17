#!/usr/bin/python3


from email import message
from email.policy import default
import subprocess
from Wappalyzer import Wappalyzer, WebPage
from pprint import pprint
import requests, argparse, sys, time
import warnings  

#inputs al fichero
def inlineopts():
        """ Parsing command args """
        parser = argparse.ArgumentParser()

        parser.add_argument(    "--url",
                help='Target URL (ex: http://localhost/index.php)',
                type=str,
                default='-1',
                required=False)

        parser.add_argument(    "--file",
                help='File with urls (ex: abc.txt)',
                type=str,
                default='-1',
                required=False)

        return parser.parse_args()


opt = inlineopts()

#print("hol "+opt.url+" "+opt.file)

#no se ha introducido ni url ni fichero,no debe funcionar y se muestra mensaje de ayuda. 
if (opt.url=='-1' and opt.file=='-1'):
  print("Exiting.........")
  print("Need to introduce url or file")
  print("use -h or --help for help")

#se ha introducido  url y fichero,no debe funcionar y muestra mensaje de ayuda. 
elif (opt.url!='-1' and opt.file!='-1'):
  print("Exiting.........")
  print("Cannot introduce url and file")
  print("use -h or --help for help")

#si introduce URL, Analisis contenido url
elif (opt.url!='-1' and opt.file=='-1'):
  print("analizando url")
  print("")
  print("")
  #comprobar url es valida
  a=opt.url
  if(('http://' not in  a )and ( 'https://' not in  a)):
    print ("La string introducida no es una web")
    exit()

  warnings.filterwarnings("ignore", category=UserWarning, module="Wappalyzer")
  wappalyzer = Wappalyzer.latest()
  webpage = WebPage.new_from_url(opt.url)
  tecnologias = wappalyzer.analyze_with_versions_and_categories(webpage)
  cms_list='WordPress','Joomla','Drupal','Shopify','Wix','Magento','Prestashop','Blogger'
  nueva_lista={}
  subdict={}
  comando=''
  site=-1
  #print(tecnologias)
  for clave,valor in tecnologias.items():
        if clave in cms_list:
                for clave2,valor2 in valor.items():
                        subdict[clave2]=valor2
                        nueva_lista[clave]=subdict
  #print(nueva_lista)
  #subprocess.run(["searchsploit "])
  for i in nueva_lista:
    for j in nueva_lista[i]:
      for count in nueva_lista[i][j]:
        if(j=='versions'):
          comando=count
    comando= i+' '+comando
    site=comando
    if(site == -1):
      print("No CMS detectad")
    else:
      print("El CMS detectado y su version es: ",f'{site}')
      subprocess.run(['searchsploit',f'{site}'])


#si introduce un fichero, Analisis contenido fichero
elif (opt.url=='-1' and opt.file!='-1'):
  print("analizando fichero")
  print("")
  print("")
  #comprobar fichero es valido
  a=opt.file
  a=a[-3:]

  if(a != 'txt'):
    print ("El fichero no es un archivo de texto")
    exit()
  else:
    #leer archivo txt python
    f = open ('juan.txt','r')
    mensaje = f.read()
    abc=mensaje.split()
    f.close()
    for i in abc:
      #comprobar que la url es valida
      if(('http://' not in  i )and ( 'https://' not in i)):
        print ("La string introducida no es una web")
        exit()

      warnings.filterwarnings("ignore", category=UserWarning, module="Wappalyzer")
      wappalyzer = Wappalyzer.latest()
      webpage = WebPage.new_from_url(i)
      tecnologias = wappalyzer.analyze_with_versions_and_categories(webpage)
      cms_list='WordPress','Joomla','Drupal','Shopify','Wix','Magento','Prestashop','Blogger'
      nueva_lista={}
      subdict={}
      comando=''
      site=-1
      for clave,valor in tecnologias.items():
        if clave in cms_list:
                for clave2,valor2 in valor.items():
                        subdict[clave2]=valor2
                        nueva_lista[clave]=subdict
      for k in nueva_lista: 
        for j in nueva_lista[k]:
          for count in nueva_lista[k][j]:
            if(j=='versions'):
              comando=count
        comando= k+' '+comando
        site=comando
        if(site == -1):
          print("No CMS detectad")
        else:
          print("El CMS detectado y su version es: ",f'{site}')
          subprocess.run(['searchsploit',f'{site}'])
