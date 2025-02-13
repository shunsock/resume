## PHPerKaigi 2024 Booth Game 「PHP 8.3秒チャレンジ」の開発

### Summary

- Period: 2024-01 => 2024-03
- Role: 計画者・実装者
- About: PHPerKaigi 2024のブースゲーム「PHP 8.3秒チャレンジ」を開発しました．

### Technologies

- Languages:
    - `PHP`, `TypeScript`, `SQL (MySQL)`
- Framework: `Leaf PHP`, `Pactum JS`, `React`, `Bun`, `Vite`, `Tailwind CSS`
- Infrastructure: `Nginx`, `MySQL`, `Docker`, `AWS (EC2)`

- Technology selection:
    - Common: イベントなので変わり種を入れようと話していました
    - Frontend: 高機能ですぐに開発ができるReactを使用しました．一工夫としてPackage ManagerにBunを使用しました．
    - Backend: PHPのイベントなのでPHP 8.3を使用しました．一工夫としてLeaf PHPを使用しました．
    - Database: PHPと相性の良いMySQLを使用しました．
    - Infrastructure: AWSでの最小構成を考え，EC2 on Dockerを使用しました．

### Story

- Background:
    - PHPerKaigiは，PHPのカンファレンスであり，PHPの最新技術やトレンドを学ぶことができるイベントです．
    - スポンサーには企業ブースという企業専用のブースが割り当てられ，広告や宣伝をすることができます．
- Issue:
    - 前回のイベント(PHP Conference 2023)ではスポンサーブースでPHPに関するクイズを提供しましたが，以下のような問題がありました．
        - 問題自体の難易度調整が難しい．
        - X(Twitter)への反応があまりなかった．
        - ブースに常時エンジニアが在籍する必要がある．
        - １回の体験に時間がかかってしまう．
    - そこで案をチームで出し合い以下のような内容にすることが決まりました．
        - PHPのlatest version 8.3にちなんだ10秒ストップチャレンジゲーム．
        - Result画面でQRを出すことによってTwitterでシェアをしてもらう．
- Development:
    - BackendとInfrastructureの計画を担当しました
    - 私は API Serverの構築，FrontendのInfrastructure層(=Repository層)の実装を担当しました．
- Result:
    - PHP 8.3秒チャレンジを開発することで，PHPerKaigi 2024のブースゲームを実現しました．
    - 3日間に及ぶPHPerKaigi2024本番では、140人以上の方に「PHP8.3秒チャレンジ」にプレイしていただきました。
    - 非常に好評で[Twitterで多くの投稿をもらった](https://twitter.com/search?q=%23prtimes_dev%20until:2024-03-10%20since:2024-03-06&src=typed_query&f=live)他，カンファレンスのフィードバックでもアイディアや実装が評価されました．
- Learn:
    - 今回の開発ではコンセプトを大事にしました．PHP 8.3を目指すという前向きな目標を掲げたことにより，参加しやすい雰囲気を作ることができました．
    - 最小構成での開発を行ったことで，インフラの構築や開発の効率化について学びました．単に簡素にすることと，最小構成にすることは異なることを学びました．
    - チーム開発の重要性を学びました．
        - 今回の開発では，自分ともう一人の開発者で多くの機能を作る必要があったのでコミュニケーションの機会を通常より多く取りました．
        - 事前に決めておいても，実際に開発を進めると変更が必要になることが多かったので，上記の選択は正解でした．

### Reference

- reference:
    - [PR TIMES 開発者ブログ."PHPerKaigi2024のブース企画を担当しました！"](https://developers.prtimes.jp/2024/04/03/phperkaigi2024-booth/)

## PR TIMESの記事データの前処理バッチサーバーの開発

### Summary

- period: 2024-09 => 2024-03
- role: 計画者・実装者
- about: PR TIMESの記事データの前処理バッチサーバーを開発しました．

### Technologies

- languages: `Python`, `SQL (PostgreSQL, BigQuery)`
- framework: `Prefect`
- Infrastructure: `BigQuery`, `Cloud Storage`, `Cloud Compute Engine`, `IAP`

### Story

- Background:
    - PR TIMESの記事データは，プレスリリースのデータを含む膨大なデータ量があります．
    - PR TIMESの記事は公共性が高く，日本語の文法に則っているため，機械学習の学習データとして適していると考えられました．
    - それらの価値はインターン時代に社内で紹介しています ※ PR TIMES(Intern)の項目を参照
- Issue:
    - 一方で，これらを機械学習に用いるためにはデータの前処理が必要でした．
    - PR TIMESのデータはHTML形式であり，HTMLタグや文字参照の除去や形態素解析(Tokenization)が必要でした．
    - これらの処理は自然言語や日本語のテキストデータに関する専門知識を必要とします．
    - 現状では社内でのデータ活用を進めにくいのでDWHを使って前処理済みのデータを配信することになりました．
- Development:
    - アドバイスをもらいながら，私がオペレータとして開発しました
- Result:
    - バッチサーバーを開発することで，PR TIMESの記事データを前処理済みのデータとして取得できるようになりました．
- Learn:
    - この開発では，機能の実装はできたものの悔しい点がいくつかありました．
    - PoCを作らずにいきなり実装してしまったため，後からアーキテクチャの変更が必要になりました．
        - このことから，まず実現可能性を最小構成で確認することの重要性を学びました．
    - プロジェクト管理の重要性を学びました．
        - 今回の開発では，自分がオペレータとして開発を行いましたが，プロジェクト管理を適切行う人がいなかったため，進捗管理が難しかったです．
        - 進捗管理が難しかったため，開発が遅れることがありました．

## PR TIMESの新規機能開発: カテゴリーごとのランキング

### Summary

- period: 2023-09 => 2023-11
- role: 実装者
- about: PR TIMESの新規機能として，カテゴリーごとのランキングを実装しました．

### Technologies

- languages: `PHP`, `JavaScript`, `SQL (PostgreSQL)`, `Opensearch`
- framework: `Smarty (PHP Template)`

### Story

- Background:
    - PR TIMESは，プレスリリースの配信サービスを提供している企業です．
    - 既存の機能として総合的なランキングがありました．
        - ランキングはプレスリリースを配信する団体のモチベーションや広告のきっかけにもつながるので，重要な機能でした．
        - 顧客から良いフィードバックをもらっており人気がありました
- Issue:
    - 既存のランキングは総合的なランキングであり，ニッチな分野が掲載される機会が少ないという問題がありました．
    - カテゴリーごとのランキングを実装することで普段見られないようなプレスリリースにも目が行くようになると考えられました．
- Assignment:
    - 既存のランキングの機能を拡張し，カテゴリーごとのランキングを実装することになりました．
- Technology selection:
    - 本件は関わっていません
- Development:
    - 私ともう一人の開発者で実装しました．
    - 私はFrontend / Backend (Controllerからサービス層)を担当しました．
    - もう一人の開発者はBackend (Repository層) / OpenSearchの設定を担当しました．
    - PHP部分が複雑で理解が難しかったですが，Debug ToolやPHP Stormの機能を使いながら理解を深めました．
- Result:
    - カテゴリーごとのランキングを実装することで，ニッチな分野のプレスリリースにもアクセスがしやすくなりました．
- Learn:
    - Layered Architectureの理解
        - PR TIMESのリファクタリングが進んでいる部分はLayered Architectureに基づいていました．
        - これにより，OpensearchのAPIを意識せずに，ControllerからService層を経由してRepository層にアクセスすることができました．
        - そのおかげで実装が楽になると気づき，学びになりました．
    - 一見謎なコードでも意外に理由があることを学びました．
        - 例えば，Smartyのテンプレートエンジンでコメントアウトしたところバグが起こりました
        - これはコメントアウトをカスタムをしているからですが，昔はシンタックスハイライトが弱かったという背景があることを知りました．

## 検索機能改善PoC作成 (検索機能アルゴリズム開発)

### Summary

- period: 2023-04 => 2023-05 (2023-06 => 2023-09)
- role: PoC開発者 => 技術相談役・技術調査役
- about: PR TIMESの検索機能のPoCを開発・提案し，その後，検索機能のアルゴリズム開発に相談役として携わりました．

### Technologies

- technologies:
    - PoC: `Python`, `TF-IDF`
    - Production: `Opensearch`, `AWS`

### Story

- background:
    - 2021年に開発体制が現体制になりましたが，当初はサービスがいつ止まってもおかしくない状況でした．
    - 当時のElasticSearchは自前で運用していましたが，壊れかけで2022年に移行されました．
    - 2023年になり，ある程度Webサービスとしての安定感が出てきたため，検索機能の改善に取り組むことになりました．
- issue:
    - 2023年当初，PR TIMESの検索機能はOpensearchで運用されていましたが検索としての機能をなしていませんでした．
    - 顧客から「何が出現するかわからないから逆に使っている」というようなフィードバックをもらっていたそうです．
- assignment:
    - 総合職と合同の新卒研修の一貫として，プロダクトの検索機能の改善案を考え，発表することになりました．
    - チームの知識役として総合職のメンバー・開発職のメンバーと協力し，検索機能のアルゴリズムの提案を行いました．
- proposal:
    - 不要な部分の除去
        - 現状では検索対象の記事の本文全てをindexに含めていましたが，記事の後半部分には会社の住所など不要なデータが含まれていることに気づきました．
        - そこで，記事の前半部分のみをindexに含めることを提案しました．
        - また，正規化についても改善できることに気づきました．
        - HTMLをそのまま，indexに含めていたたので形態素解析(Tokenize)に影響があると推察できたからです．
        - そこで，HTMLタグを除去や文字参照の除去といった文字列正規化を提案しました．
    - 必要な部分の追加
        - また，タイトルやサブタイトルもindexに含めることで，検索結果の精度を向上させることができました
    - アルゴリズムの改良
        - 現状は単純なAND/OR検索でしたが，TF-IDFベースScoring Functionを用いる検索アルゴリズムを提案しました．
        - 提案手法のLucine's Practical Scoring FunctionはQueryのTokenごとに重みを計算し，それを元に検索結果をランク付けすることができます．
        - よって重要な単語が含まれている記事が上位に表示されるようになりました．
- PoC:
    - About: 課題そのものは上記の提案で十分でしたが，自分達の案を採用することで改善することを認知してもらうためにdemoを作成しました．
    - background: チームメンバーがプレゼンを作っているタイミングで手が空いたので，チームメンバーに許可をとって開発しました
    - developer: 自分
    - languages: `Python`
    - algorithm: `TF-IDF`, `Lucine's Practical Scoring Function`
    - technology selection:
        - NLPと相性がよく，予めNLP向けの関数が用意されているため，`Python`を選定しました．
        - TF-IDFまではMeCab Pythonやsklearnを用いて実装しましたが，Lucine's Practical Scoring Functionは用意されていないので自前で実装しました．
        - 実装の詳細はReferenceのLinkを参照してください．
    - result：
        - PoCを通して，提案手法の有効性を認知してもらうことができました．その後，提案手法の一部が採用され，検索機能の改善が行われました．
        - また，検索技術・自然言語処理の知識が認められ，技術相談役・技術調査役としてその後の改善に携わることができました．
- Production:
    - about: PoCを通して提案手法の有効性を認知してもらい，その後，提案手法の一部が採用され，検索機能の改善が行われました．
    - developer: 開発チーム
    - role: 技術相談役・技術調査役
    - languages: `PHP`, `TF-IDF`
    - framework: `Opensearch`
    - technology selection:
        - 他の業務と並行して短い期間で開発する必要があったため，既存の技術を用いつつ改善をすることになりました．
        - 日本語形態素解析機がOpenSearchは`kuromoji`のみの対応であるため`MeCab`ではなく`kuromoji`の対応となりました．
        - Lucine's Practical Scoring Functionは実装の時間の関係でTF-IDFのみの採用となりました．
    - result： 検索機能の改善により，検索結果の精度が向上しました．短い期間でしたが，十分な成果をあげることができました．
- Others:
    - これらの開発を通して，検索機能の内部を学びました．その経験を活かし，2024年にはPHPカンファレンス福岡で検索機能のアルゴリズムについてのセッションを行う予定です．
    - [CfP: 作って学ぶ ★ 検索機能](https://fortee.jp/phpcon-fukuoka-2024/proposal/356e0c9c-fbc3-4c88-bb89-0ba3a03672bd)
- Reference:
    - [GitBook."Elastic Search - Definitive Guide"](https://feliperohdee.gitbooks.io/elastic-search-definitive-guide/content/170_Relevance/15_Practical_scoring.html)
    - [Medium."Deconstructing Scoring In Elasticsearch"](https://codeburst.io/deconstructing-scoring-in-elasticsearch-e8544676a24)

## 機械学習を用いたPoCの開発

- description:
    - 2022年には，機械学習を用いたPoCの開発を行いました．
        - 具体的には，Word2Vecを用いた類似度に基づく単語推薦システムをPoCとして開発し，社内に公開しました．
        - この開発を通して，文字コードの知識を深く学びました
        - 特に日本語の新旧字体の処理を行う必要があり，互換表を作成するなどの作業を行っています．
        - [新旧字体の表記ゆれを統一するために互換表を作成した話](https://developers.prtimes.jp/2022/11/18/change_word_form/)
- languages: `Python`, `JavaScript`
- frameworks: `Gensim`, `MeCab`, `FastAPI`, `Next.js`
- algorithms: `Word2Vec`
- infrastructure: `AWS`, `GCP`
- background:
    - PR TIMESの記事データは，プレスリリースのデータを含む膨大なデータ量があります．
    - PR TIMESの記事は公共性が高く，日本語の文法に則っているため，機械学習の学習データとして適していると考えられました．
- issue:
    - 一方でそのデータの価値はあまり理解されていませんでした．
    - そのため，機械学習を用いたPoCの開発を行い，データの価値を認知してもらうことが求められました．
- technology selection:
    - インターン生のPoCであるため特に言語やアルゴリズムに制約はありませんでした
    - ただし，社内のシステムはAWSで運用されているため，AWSを用いた開発を行いました．
    - よって管理のしやすさから以下の方法にしました
        - FrontendとAPI Server, 機械学習環境を分けることでコードを疎結合になるようにしたい
        - Smart UIを避けるため，FrontendとBackendの切り離しをしました．
        - Backendの機械学習推論サーバーは機械学習モデルがPythonであることから，Pythonの軽量FWのFastAPIを選定しました．
        - 機械学習は完全にローカルサーバーで行い，API Serverは推論のみを行うようにしました．
- development:
    - 自分で全て開発を行いました．
    - また，成果物を社内に公開し，フィードバックをもらいながら改善を行いました．(社長からのフィードバックもありました)
- result:
    - 機械学習を用いたPoCの開発を行うことで，PR TIMESの記事データの価値を認知してもらうことができました．
    - インフラストラクチャの構築やデータの前処理など，機械学習の理論には出てこないものの実践で重要なスキルを学ぶことができました．
    - ビジネス側からの意見をもらったことで，技術だけでなくビジネスの視点も学ぶことができました．

