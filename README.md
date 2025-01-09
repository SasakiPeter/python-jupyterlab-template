# python-jupyterlab-template

## 環境構築

### Docker

docker で仮想環境を構築しています。次のコマンドで、環境が作成されます。

```shell
$ docker compose up -d
```

Jupyter Lab を開く際は、ホストマシンから次のコマンドを実行するのが便利です。

```shell
$ make open-jupyter
```

動作しない場合は Jupyter Lab のサーバー URL を以下のコマンドで取得してください。

ホストマシンから確認するとき

```shell
$ docker compose logs
```

コンテナ内から確認するとき

```shell
$ jupyter lab list
```

#### VSCode (Remote Container)

[Visual Studio Code Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)の入れてください。

`.devcontainer/devcontainer.json`に設定ファイルを置いているので、こちらの拡張機能を使うことで直接コンテナ環境にアクセスできます。
