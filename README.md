Twitter-Python-CSV
===============
Gio Cádiz
* Twitter : [@Gio_Cadiz](https://twitter.com/Gio_Cadiz)
## Description
El objetivo de este script en [Python](https://es.wikipedia.org/wiki/Python), es obtener la información generada por los 
usuarios de [Twitter](https://twitter.com/),
mediante un [#Hashtag](https://es.wikipedia.org/wiki/Hashtag) especifico desde la  [API oficial de Twitter](https://apps.twitter.com/) 
y posteriormente almacenar los datos en un archivo [CSV](https://es.wikipedia.org/wiki/Valores_separados_por_comas).


## Requirements
Este script requiere lo siguiente:
* Python version 2.7.13 [Download Python](https://www.python.org/downloads/)
* Api Twitter [Twitter Apps](https://apps.twitter.com/)
* Tweepy [Download Tweepy](https://pypi.python.org/pypi/tweepy/3.5.0) - [Tweepy Documentation](http://pythonhosted.org/tweepy/)

## Installation
La forma más fácil de instalar la última versión de **tweepy** es utilizando **pip** o **easy_install**:
>`pip install tweepy`

>`easy_install tweepy`

Si no tenemos una cuenta de [Twitter](https://twitter.com/) hay que registrarnos, en caso de que la tengamos, 
vamos a logearnos en el [portal de desarrollo](https://apps.twitter.com/) y crearemos una nueva aplicación, 
para tener acceso a los datos de autenticación [OAuth](https://es.wikipedia.org/wiki/OAuth) a la API.
>
Una vez creada la aplicación en el portal debemos guardar los siguientes valores para la autenticación:
>`consumer_key`,
>`consumer_secret`,
>`access_token_key`,
>`access_token_secret`
>
Reemplazar los valores de autenticación en el script:

>`consumer_key = 'consumer_key here'`<br/>
>`consumer_secret = 'consumer_secret here'`<br/>
>`access_token = 'access_token here'`<br/>
>`access_token_secret = 'access_token_secret here'`
>
Reemplazar [#hashtag](https://es.wikipedia.org/wiki/Hashtag) con una "palabra" como parametro de busqueda:
>`twitterStream.filter(track = ["#hashtag here"])` 
