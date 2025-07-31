---
title: Findy Inc.
description: My works at Findy Inc.
prev:
  text: "Open Source Software"
  link: "/works/oss"
next:
  text: "Findy Inc."
  link: "/works/prtimes"
---

# ファインディ株式会社

## 概要

- 会社名: ファインディ株式会社
- 創業: 2016年7月1日
- 従業員数: 275名 (2024年9月時点)
- 所属期間: 2024-08-16 - 現在
- 所属部署: CTO室
- 職種: データエンジニア・プラットフォームエンジニア

## Findy Toolsデータ基盤構築

Findy Toolsのデータ基盤の新規構築に携わりました。設計や実装をメインで行いました。

![System Architecture](/image/works/works__findy_tools_embulk.jpg)

具体的には、AWSからGoogle Cloudデータを移送するシステムをECS、データを加工するシステムをBigQueryとdbtで構築しています。インフラリソースの管理はTerraformをGitHub Actionsで動かすことで管理しています。また、上記システムの監視システムも併せて開発しました。Googleのリソースは、Cloud LoggingとCloud Monitoring、AWSのリソースはCloudWatch, SNS, Chatbotを利用しました。

基盤構築後、Looker Studioを利用したBIの機能追加など運用保守に携わっております。

### 参考資料

- [Findy Toolsのデータ基盤を1ヶ月前倒しで新規構築した話](https://tech.findy.co.jp/entry/findy_tools_data_infrastructure_introduction)
- [ファインディ株式会社におけるEmbulkの導入事例](https://findy-tools.io/products/embulk/367/352)

## データ同期の高速化

[Findy Team+](https://findy-team.io/)のチームにおいてBIは始業後の朝会等で参照されています。このBIはEmbulkによってAWS RDSと同期されたBigQueryのテーブルを参照していました。

しかし、Team+の成長にEmbulkによる同期システムの処理が追いつかなくなってきていました。そこで高速化を行い解決しました。具体的には、Embulkの並列数とEmbulkを起動するECSを並列化しております。

既存のBIに対する同期システムの移行の影響範囲を小さくするために、同期システムとデータセットを別で作成し、インフラストラクチャの構築終了後に参照の切りかえを行いました。これにより、BIを落とすことなく移行できました。

## 記事寄稿

### 技術ブログ

- [Findy Toolsのデータ基盤を1ヶ月前倒しで新規構築した話](https://tech.findy.co.jp/entry/findy_tools_data_infrastructure_introduction)
- [【エンジニアの日常】エンジニア達の自慢の作業環境を大公開 Part6](https://tech.findy.co.jp/entry/2025/03/13/070000)

### 企画「#も読」

「あの人も読んでる」略して「も読」。さまざまな寄稿者が最近気になった情報や話題をシェアする企画です。

- [【#も読】マイナポータルのCSV、読みやすいコード、Pythonの定数（@shunsock）](https://findy-code.io/media/articles/modoku20250325-shunsock)
- [【#も読】JetBrainsのAI活用 / Church Encoding / DuckDBのSDK（@shunsock）](https://findy-code.io/media/articles/modoku20250501-shunsock)

