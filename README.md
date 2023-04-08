# CIST:CaT
CIST:ComfortAble Toolkit(仮称) は、CIST生の学生生活をより便利にするためのアプリケーションです
![mock](https://user-images.githubusercontent.com/41831807/219938781-83d66e09-8fad-45c1-936a-d9281116d446.png)
# このリポジトリについて
ここでは、バックエンドの構築を行います。
フロントエンドの開発は別のレポジトリで行います。

# 構成
![arch](https://user-images.githubusercontent.com/41831807/220086683-affa1c20-f077-4c01-b401-d213fd98dea6.png)


# 推奨開発環境
VScodeの拡張機能である[Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers)を利用すると、快適に開発が行えます。Windowsで導入する場合の概要は以下の通りです。
1. [Visual Studio Code](https://code.visualstudio.com/)のインストール
2. [WSL2](https://www.kagoya.jp/howto/cloud/container/wsl2_docker/)のインストール(Docker Desktopのインストールまで書いてあります)
3. [Docker Desktop](https://www.docker.com/products/docker-desktop/)のインストール
4. [Dev Container拡張](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)をインストール

インストール後にVScodeでこのレポジトリをcloneして開くと、下記のような通知が表示されます。「Reopen in Container」をクリックすると、開発環境が起動します。
![devcontainer-demo](https://user-images.githubusercontent.com/41831807/219937556-43b980e2-caf6-4fa8-8f0b-7fea16138995.png)


# 役割分担
流動的にタスクを配分するため、以下のような方法を採用します。


1. **担当するissueを決める**  
[githubでissuesを確認](https://github.com/ItisNoMatter/cist-cat/issues)し、まだ誰もアサインされていないissueを探しましょう。issue毎についているLabelsを見て判断するのもお勧めです。担当したいissueを見つけたら、assign yourselfをクリックします。
![assign-example](https://user-images.githubusercontent.com/41831807/219937092-98369e9c-5dba-42bc-91bb-7c28c4c4919c.png)

2. **ブランチを切って開発する**  
開発環境に戻って、devlopから「feature/(issue番号)」という名前のブランチを切って作業を始めます。issue番号は、githubでissueタイトルの傍に＃1のように表示されています。

3. **devlopへプルリクエストを送る**  
issueの要件を実装し終えたら、プルリクエストを送りましょう。問題ないと判断されたら、devlopにマージされます。基本的に、この時点でissueはcloseされます。
4. **[1.]に戻る**  
　魅力的なタスクがない場合は、自分で新しくissueを立てても良いです。

# 詰まった時のルール

不具合やわからないことがあり解決できない場合、長時間一人で悩み続けるのは生産性を著しく損なう行為です。**15分調べて解決しなかった場合は必ずQ＆A issueを立てましょう**。

## Q＆A isuue の立て方

1. githubの[issuesページ](https://github.com/ItisNoMatter/cist-cat/issues)を開く
2. New Issuesボタンをクリック
3. Q&A を選択
4. issueテンプレートを埋めて、submitする
5. 返信が来るまで他のタスクを進める

5.の「他のタスク」は、このプロジェクトに関連するものでなくても構いません。時間を有意義に使いましょう。

Q&A issueテンプレートは、[技術系メーリングリストで質問するときのパターン・ランゲージ](https://www.hyuki.com/writing/techask.html)に基づいています。質問の方法に困る場合、こちらを一読するのも良いでしょう。Qiitaの[質問は恥ではないし役に立つ](https://qiita.com/seki_uk/items/4001423b3cd3db0dada7)という記事も参考になります。

# 基本のgitルール
gitを使った開発が初めてのメンバーの参加も想定しています。  
以下は、gitを利用して共同開発を行うときに気を付けるとよいとされているルールです。  
これを守って開発することで、チーム開発における混乱を最小限に留めることができます。
1. **必ずブランチを切る**  
開発作業は、issue毎に必ず新しいブランチを切って行ってください。誤ってdevlopブランチやmasterブランチへコミットしないように気を付けましょう。
2. **こまめにコミットする**  
作業をしたときは、コミットメッセージと共にこまめなコミットを行うのが良いです。コミットメッセージを簡潔にまとめるのが難しい場合、そのコミットは変更が大きすぎる可能性があります（複数のコミットに分けたほうがいいかもしれません）。
3. **定期的にpullをする**  
他の開発メンバーのpushによる変更を取り入れるために、定期的にgit pullをしましょう。特に、devlopブランチのpullは大切です。ブランチを新しく切る前には、devlopブランチのpullを忘れないようにしましょう。

Gitには多くのコマンドが存在するため、必要に応じて詳細を調べてください。また、コマンドを実行する前には必ず、コマンドの意味や効果を理解してから実行してください。

## Gitコマンドの意味とトラブルシューティング
**git clone (リポジトリのURL)**  
Github上のデータを自分の手元にコピーするコマンドです。  
基本的には最初の一回だけこれを使います。  
![GitClone](https://user-images.githubusercontent.com/86462419/222182259-36e46dc7-8120-413b-90d1-c1138d212869.png)

**git branch**  
今いるブランチがどこなのかわかるコマンドです。  
  
**git checkout -b (ブランチ名)**  
新しいブランチを作るときに使うコマンドです。  
新たなブランチが作られ自動的にそのブランチに移動します。  
  
**git checkout (ブランチ名)**  
既存のブランチに移動するときに使うコマンドです。  
  
**ブランチについて少し補足**  
**Q:** ブランチを作ると何が嬉しいのか  
**A:** ブランチを作るとほかのメンバーの作業内容に関係なく自分の作業ができます。自分が作業してないときに勝手にほかのメンバーにファイルを編集されたりしなくなります。また、「変更を加えたけどやっぱりやめたい。でもどこを変えたか覚えてない」というときに変更前の状態に戻すことができます。  
**Q:** ほかのメンバーの編集内容と競合してしまったらどうなるのか  
**A:** 統合するための作業があるので大丈夫です。  
  
**git add .**(スペース1個開けてピリオド)  
![GitAdd](https://user-images.githubusercontent.com/86462419/222197322-8d96ed09-8fc1-4037-942e-78345117cf6e.png)  
自分の作業内容をgitに加えるコマンドです。スペースとピリオドを忘れがちなので注意。 
  
**git commit -m "作業内容をここに書く"**  
![GitCommit](https://user-images.githubusercontent.com/86462419/222197639-b65c85be-2c09-484b-9124-67c48cd607e7.png)  
作業内容を記録するコマンドです。後で巻き戻したくなったときのために何を変更したのかを書き残しておきましょう。  
  
**git push origin (ブランチ名)**  
![GitPush](https://user-images.githubusercontent.com/86462419/222198243-8cc2f386-8ef0-4f8b-bfc6-88916a7be936.png)  
作業内容をクラウド上に反映させるコマンドです。これによりGithub上のコードの内容が更新され、ほかのメンバーもあなたの変更を受け取れます。  
  
**git pull origin develop**  
クラウド上のデータを手元に持ってくるコマンドです。個人的に理解に苦しんだコマンドなので少し詳しめに書きます。
自分が作業を始めてから終わるまでの間にほかのメンバーが作業を終わらせてクラウド上のデータを更新している場合があります。
例えば、自分がデータBを作っている間にほかのメンバーが新しいデータCを追加していたとします。  
![GitPull1](https://user-images.githubusercontent.com/86462419/222356741-1ce49d61-d1c8-4244-8755-a0d3184111c7.png)  
このまま自分がクラウドを更新するとデータCがなくなって困ります。  
そこでこのgit pull origin developコマンドを使います。  
![GitPull2](https://user-images.githubusercontent.com/86462419/222204330-4f6cf75b-9725-431f-80d5-3199c69119df.png)  
するとこのように、手元になかったデータCを手元に持ってくることができます。  
![GitPull3](https://user-images.githubusercontent.com/86462419/222205111-fb14bd84-f8e5-4fda-aa6b-24c39989459b.png)  
それからadd,commit,pushを行うと無事にクラウド上にデータABCが揃います。  
自分が作業している間にほかのメンバーがデータを追加しているかもしれないので定期的にgit pull origin developを使いましょう。  
特に自分がadd,commit,pushを行う前には必ず使いましょう。
また、自分の作業中にほかのメンバーが既存のデータを書き換えている可能性があります。
![GitPull4](https://user-images.githubusercontent.com/86462419/222206751-c1793047-9b5d-443c-b385-3b10a5f2d8f7.png)  
このときもgit pullを使うことで書き換えられたデータを手元に持ってくることができます。  
![GitPull5](https://user-images.githubusercontent.com/86462419/222207242-98a96c43-3e8b-4fdb-b8be-38cc7b28c992.png)  
それからadd,commit,pushを行うと無事にクラウド上に両方のデータが更新された状態で揃います。  
![GitPull6](https://user-images.githubusercontent.com/86462419/222207689-09010fda-dc22-4b18-aac3-6dc99324b8af.png)  
自分が作業している間にほかのメンバーがデータを書き換えているかもしれないので定期的にgit pull origin developを使いましょう。  
特に自分がadd,commit,pushを行う前には必ず使いましょう。  
**Q:** ほかのメンバーと同じファイルを編集していたらどうなる？  
**A:** そのときはGitがコードの被っている部分を洗い出して自分の変更とほかのメンバーの変更のどっちを採択するか聞いてきます。適切なほうのコードを残し、いらないほうは消しましょう。ファイル単位ではなく行単位でどちらをとるか聞いてくるので細かい調整が可能です。 
  
**Pull Request**  
git push origin (ブランチ名)まで行ったら、Githubのリポジトリをブラウザで開いてください。  
すると、Compare & pull requestという緑のボタンが出てきます。これを押しましょう。  
Pull Requestという画面に移行します。メッセージを書く場所があるので何を実装・変更したのか書いてCreate Pull Requestを押しましょう。  
すると、ほかのメンバーに「○○さんがこういう内容でクラウド上のデータを更新しようとしています」という情報がGithub上にあがります。  
ほかのメンバーがこれを許可すると、晴れてクラウド上のデータは更新されます。(これをマージ・mergeといいます)  
  
これらを踏まえて、開発の流れはこのようになります。
![Workflow](https://user-images.githubusercontent.com/86462419/222214244-86cab0c5-36fe-4ada-a48b-13603468138a.png)  
**Q:** 間違えてDevelopブランチで作業してしまった  
**A:** addする前にgit checkout -b ブランチ名で大丈夫です。  
**Q:** 最後にcommitしたときの状態に戻したい  
**A:** git reset --hard HEADというコマンドを使うと戻せます。  
**Q:** 特定のcommitの状態に戻したい  
**A:** git logというコマンドを使うとcommitごとに割り振られた数値が出てきます。これをコミットIDといいます。戻したいcommitのコミットIDをコピーしてgit reset --hard (コミットID)というコマンドを使うと戻せます。  
**Q:** うわ！やらかした！なんかよくわからんけどGitの操作を戻したい！  
**A:** git reflogというコマンドを使うと、行ったGit操作の履歴が出てきます。その履歴一つ一つにHEAD@{数字}という表記がついています。これをコピーしてgit reset --hard HEAD@{数字}を使うと魔法のように戻せます。  
**Q:** addやcommitをしないでリモートとローカルのコードを比較したい  
**A:** git diffというコマンドを使うと、addやcommitをしなくてもコードを比較できます。

### よくあるエラー  
**fatal: not a git repository (or any of the parent directories): .git**  
これはgitの使えない場所でgitコマンドを打つと起こります。  
gitが使える場所とは、「.git」というフォルダの存在しているディレクトリです。  
![GitRepository](https://user-images.githubusercontent.com/86462419/222217620-d743e587-9b31-4885-9489-78a675ee96ae.png)  
このディレクトリには上から2番目に「.git」というフォルダが存在していることがわかります。  
これがgitの正体であり、gitコマンドを受け取っている存在です。  
このエラーが出た場合はcdコマンドで「.git」というフォルダが存在しているディレクトリに移動しましょう。  
![GitArea](https://user-images.githubusercontent.com/86462419/222218455-f0461957-1952-43ae-a0f1-c3b6b11056d9.png)  
  
**error: Your local changes to the following files would be overwritten by checkout:**  
commitする前にブランチを切り替えようとすると起こります。
commitするか、git stashというコマンドを使いましょう。  
一時的に作業を棚上げしてブランチ切り替えが効くようになります。  
戻すときはgit stash applyで戻せます。 

**PullしたらVimに閉じ込められた！**  
Escキーを押してください。その後落ち着いて:q!と入力してEnterキーを押します。  
  
**閉じ込めからは抜けられたけどPullができない**  
対処法がどこかに行きました。すみません。見つかったら追記します。  

思い出し次第追記します。
