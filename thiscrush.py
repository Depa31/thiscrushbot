import requests
import threading
import random

def comment(vitt,nom,mess,proxy):
    #return requests.post('http://www.thiscrush.com/postcrush.php',proxies=proxy,headers={'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1'}, data={'id':vitt,'name':nom,'comment':descr,'captcha_result':'0'}).status_code
    return requests.post('http://www.thiscrush.com/postcrush.php',proxies=proxy,headers={'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1'}, data={'id':vitt,'name':nom,'anon':'Y','comment':mess}).status_code
def like(vitt,proxy):
    return requests.post('http://www.thiscrush.com/quicklike.php',proxies=proxy,headers={'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A402 Safari/604.1'}, data={'id':vitt}).status_code
def job(mode):
    global proxy
    global vitt
    global nom
    global mess
    pxy = random.choice(proxy)
    pxyd = {"http":"http://"+pxy, "https":"https://"+pxy, "ftp":"ftp://"+pxy}
    if mode=='c':
        f=comment(vitt,nom,mess,pxyd)
        if f==200:
            print('Comment\n')
    elif mode=='l':
        f=like(vitt,pxyd)
        if f==200:
            print('Liked\n')

def main(mode):
    while True:
        try:
            job(mode)
        except:
            pass    

vitt=input('Persona di thiscrush: ')
mode=input('Commenti o like?(c/l): ')
if mode=='c':
    nom=input('Nome(anche a caso tanto non si vede): ')
    mess=input('Messaggio: ')
threads=2000
proxy = open('proxies.txt', 'r').read().split('\n')
for x in range(0,threads):
    t = threading.Thread(target=main, args=(mode),)
    t.start()
