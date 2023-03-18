## Library

```
pip freeze > requirements.txt
```

라이브러리 설치
Install the library

```
pip install -r requirements.txt
```

## Execute

```
main.py
```

###########  DR    ################

## For uvicorn launch to test/deploy
# Issue : **error Error loading ASGI app. Could not import module "main".**
# When lanching deploy command of uvicorn "out of the bound" (aka web server side)
# => What Fails : 
#  uvicorn main:app --port 8100 --host '::' --proxy-headers --forwarded-allow-ips "::1"
# THUS before we MUST do this (after completed pip modules installaions) :
<code>
$ cd <source directory of clone>

$ uvicorn main:app --reload
</code>

