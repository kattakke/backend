# backend

## 手順


1. pyenvをインストール

https://github.com/pyenv/pyenv

**環境変数の設定**もお忘れなく(Windows, Mac, Linuxの設定方法が異なることに注意)

2. pythonバージョンの切り替え
```
pyenv install 3.11.0
```

```
pyenv local 3.11.0
```
次のコマンドで、正しく設定されたか確認
```
python --version
```

```
Python 3.11.0
```
上記のように表示されたらオッケー

3. venvで仮想環境を立ち上げる

```
python -m venv env
```

4. 仮想環境に入る

MacまたはLinuxの場合
```
source ./env/bin/activate
```

Windowsの場合
```
.\env\bin\activate.bat
```

5. FastAPIをインストール
```
python -m pip install -r requirements.txt
```

6. コードを実行する

```
uvicorn main:app --reload
```

7. 作動確認

[ここ](http://127.0.0.1:8000)を開き、正しく表示されるか確認すること

以下の内容が表示されたら成功！

```
{"message":"Hello World"}
```

SwaggerからAPIの仕様を確認してみよう

[Swagger](http://127.0.0.1:8000/docs)を開き、正しく表示されるか確認してみよう
