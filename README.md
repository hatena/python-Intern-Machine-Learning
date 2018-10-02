# python-Intern-Machine-Learning

## 実行方法

コンテナ（Jupyter Notebook）の起動

```
$ docker-compose up --build
```

コンテナ起動後次のようなメッセージが出るので

```
jupyter_1  |     Copy/paste this URL into your browser when you connect for the first time,
jupyter_1  |     to login with a token:
jupyter_1  |         http://localhost:8888/?token=XXXXXXXX
```

認証トークン付きのURLをブラウザで開く

```
$ open 'http://localhost:8888/?token=XXXXXXXX'
```
