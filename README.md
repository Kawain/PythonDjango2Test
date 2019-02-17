# PythonDjango2Test

* sqliteの既存DBファイルを追加したのでDATABASE_ROUTERSを追加
* 既存のDBはmigrationsの管理対象外とするためにclass Meta:に `managed = False` を追加した
* 特に必要はなかったが、勉強のためにアプリを２つにした
* templatesを基本通りアプリ内に置いた
* staticも基本通りアプリ内に置いた
* Class-based 汎用 views で書くようにした（django.views.generic）
* forms.ModelForm を使用した
* CSS は Bootstrap から bulma に変更した
* 必要ないが実験のためにListViewのget_context_dataにModelFormを追加してみた


