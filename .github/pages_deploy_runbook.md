# GitHub Pages デプロイ障害の対応手順

`deploy__site` ワークフローの GitHub Pages デプロイが失敗したときの復旧手順を記録する。
ワークフローの不具合ではなく GitHub 側の設定破損が原因のため、コード修正では直せない。
再発時にこの手順で数分で復旧できるようにする。

## 症状

`deploy__site` ワークフローの `Deploy to GitHub Pages` ステップだけが失敗する。
`Build Site` と `Upload artifact` は成功し、artifact も生成されている。

エラーメッセージは以下のいずれか。

- `Deployment failed, try again later.` (即時失敗)
- `Timeout reached, aborting!` (`Getting Pages deployment status...` を繰り返した末に 10 分でタイムアウト)

## 根本原因

GitHub 側に保存された Pages 設定が壊れていることが原因。
`build_type` は `workflow` なのに、保存された `source.branch` が存在しないブランチ
(このリポジトリでは削除済みの `gh-pages`) を指したままになっている。
この不整合により Pages バックエンドがデプロイを拒否する。

GitHub 側の既知の不具合で、過去のインシデント後に断続的に再発している。

- <https://github.com/actions/deploy-pages/issues/418>
- <https://github.com/orgs/community/discussions/200823>

## 前提

- `gh` (GitHub CLI) が利用でき、`gh auth status` が成功していること
- Pages 設定を更新できる権限（リポジトリ管理者相当）があること（Fine-grained PAT の場合は Pages への write 権限が必要）
- 対象リポジトリが `shunsock/resume` であること（別リポジトリで実施する場合はコマンド内の owner/repo を置き換える）

## 確認方法

Pages 設定に幽霊ブランチが残っていないかを確認する。

```bash
gh api repos/shunsock/resume/pages --jq '{build_type, source, status}'
```

`source.branch` が実在しないブランチ (`gh-pages` など) を指していれば設定破損。
ブランチ一覧は `gh api repos/shunsock/resume/branches --jq '.[].name'` で確認する。

## 復旧手順

Pages 設定を上書きし、幽霊ブランチの参照を実在するブランチ (`main`) に付け替える。
`build_type` は `workflow` のまま維持するので、配信方式は変わらず live サイトへの影響はない。

```bash
gh api -X PUT repos/shunsock/resume/pages \
  -f build_type=workflow \
  -f 'source[branch]=main' \
  -f 'source[path]=/'
```

Settings → Pages の UI から source を切り替えて戻す (Deploy from a branch ↔ GitHub Actions) 操作でも
設定が再初期化され復旧する。ただし本リポジトリは `gh-pages` ブランチが存在しないため、
UI で一時的に branch 配信へ切り替えると live サイトが壊れる。API での上書きを推奨する。

## 検証

デプロイを再実行し、成功することを確認する。

```bash
gh workflow run deploy__site.yaml --ref main
gh run watch "$(gh run list --workflow=deploy__site.yaml --limit 1 --json databaseId --jq '.[0].databaseId')" --exit-status
```

デプロイのステータスと live サイトも合わせて確認する。

```bash
latest=$(gh api "repos/shunsock/resume/deployments?environment=github-pages" --jq '.[0].id')
gh api "repos/shunsock/resume/deployments/${latest}/statuses" --jq '.[0].state'   # success を期待
curl -sS -o /dev/null -w '%{http_code}\n' https://shunsock.com/resume/            # 200 を期待
```
