# ガントチャートをウェブサイトで共有する手順

作成したガントチャートをウェブ上で公開・共有するための手順を説明します。ここでは、GitHubの無料機能である **GitHub Pages** を使用する方法を推奨します。

## 準備

本プロジェクトでは、スクリプトを実行することでガントチャートが `docs/index.html` として生成されるように設定されています。

この `docs/` フォルダをウェブサイトの公開フォルダとして使用します。

## 手順 1: ガントチャートの生成

まず、最新のデータでガントチャートを生成します。
以下のいずれかの方法（R または Python）で実行してください。

### 方法 A: Rを使用する場合 (推奨)
1. `dx_plan_2025.xlsx` を必要に応じて更新します。
2. 以下のコマンドを実行します。

   ```bash
   Rscript visualize_dx_plan.R
   ```

### 方法 B: Pythonを使用する場合 (代替手段)
R環境のセットアップが難しい場合は、Pythonでも同様のチャートを生成できます。
1. 必要なライブラリをインストールします（初回のみ）。
   ```bash
   pip install pandas plotly openpyxl
   ```
2. 以下のコマンドを実行します。
   ```bash
   python visualize_dx_plan.py
   ```

3. どちらの方法でも、`docs/index.html` が更新されたことを確認してください。

## 手順 2: GitHubへのアップロード

変更内容をGitHubにアップロード（プッシュ）します。

```bash
git add docs/index.html
git commit -m "ガントチャートを更新"
git push
```

## 手順 3: GitHub Pagesの設定

ウェブサイトとして公開するための設定を行います（初回のみ）。

1. GitHubのリポジトリページを開きます。
2. 上部メニューの **Settings**（設定）をクリックします。
3. 左サイドバーの **Pages** をクリックします。
4. **Build and deployment** セクションの **Source** で `Deploy from a branch` を選択します。
5. **Branch** の項目で、以下を選択して **Save** をクリックします。
   - Branch: `main` (または `master`)
   - Folder: `/docs`
6. 数分待つと、ページ上部に公開URL（例: `https://username.github.io/repository-name/`）が表示されます。

## 手順 4: 共有

表示されたURLをコピーして、仲間と共有してください。

---

### その他の方法（Netlify Dropを使用する場合）

GitHub Pagesを使わず、手軽にファイルをアップロードしたい場合は、[Netlify Drop](https://app.netlify.com/drop) を使用することもできます。

1. 手順1で生成された `docs` フォルダをPC上で探します。
2. `docs` フォルダごと Netlify Drop の点線枠内にドラッグ＆ドロップします。
3. アップロードが完了するとURLが発行されます。
