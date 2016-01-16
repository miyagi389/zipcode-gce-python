zipcode-gce-python
====

Japan ZIP Code search API.

# Requirements
* [Python 2.7](http://www.python.org/) 
* [Google App Engine 1.9.31](https://cloud.google.com/appengine/) 


# Import Initial ZIP Code
```bash
## Download ZIP Code
curl http://www.post.japanpost.jp/zipcode/dl/oogaki/zip/ken_all.zip | tar xz

## Convert Shift_JIS (CRLF) -> UTF-8 (LF)
nkf -w -Lu -d --overwrite KEN_ALL.CSV

## Import (Local)
appcfg.py upload_data --config_file=bulkloader.yaml --url=http://localhost:8080/_ah/remote_api --filename=KEN_ALL.CSV  --batch_size=50000 --kind=ZipCode .

## Import (Google App Engine)
appcfg.py upload_data --config_file=bulkloader.yaml --filename=KEN_ALL.CSV  --batch_size=50000 --kind=ZipCode .
```


# APIs Explorer
http://localhost:8080/_ah/api/explorerø


# TIPS

## Download source code
```bash
rm ./out ; mkdir ./out && appcfg.py download_app --application zipcode-gce-python ./out
```
