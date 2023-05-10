# python-starter
Pythonのプロジェクトテンプレート

## プロジェクトインストール

```bash
poetry install
```

## credentialファイル作成

```bash
cp python_api_template/.env.sample python_api_template/.env
```

## プログラム実行

```bash
poetry run python python_api_template/main.py
```

or 

```bash
make main
```

## フォーマット

```bash
make format
```

## テスト実行

```bash
make test
```

## 型チェック

```bash
make type-check
```

## 全てまとめてチェック

```bash
make format test type-check
```
