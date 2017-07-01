# app-service
This is a webservice built with Flask, which simply implements crawlers and requests third-party interfaces.
-----
just a example: 
We request url as follows: `http://<host>:<port>/news`

the response is:
```
{
    "status": 0,
    "data": [
        {
            "content": "http://www.toutiao.com/group/6412743762997739778/",
            "source": "toutiao",
            "pic": "http://p3.pstatp.com/large/9301/1246877109",
            "id": "toutiao-b5678d645466361",
            "title": "Reporters visited the workshop to explore the high-iron lunch production process"
        },
        {
            "content": "http://www.toutiao.com/group/6412696976362504449/",
            "source": "toutiao",
            "pic": "http://p3.pstatp.com/large/5136/4760770724",
            "id": "toutiao-70ff299ff60a664",
            "title": "Traces the tragedy of the rules of the Chinese fake paper"
        }
        .......
    ]
}
```

There are many features are being improved...

# usage:
1. Install all dependencies
```
pip install -r requirements.txt
```

2. Run it now
```
python wsgi.py 
```
it will be run in `http://127.0.0.1:5000/` (if you in localhost)


if you run this on server , you need a nginx server and uwsgi.
