from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import MemoModelForm
from .models import Category, Memo


class MemoListView(ListView):
    """トップページとカテゴリ検索と文字列検索兼ねる"""

    # ページネーションはここを参考
    # https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
    paginate_by = 20

    def get_queryset(self):
        # object_list を作成してテンプレートに渡す

        # カテゴリ取得 Noneなら""
        self.c = self.request.GET.get("c") or ""
        # 検索文字取得 Noneなら""
        self.q = self.request.GET.get("q") or ""
        # カテゴリ＆文字列検索
        if self.q and self.c:
            return Memo.objects.filter((Q(title__contains=self.q) | Q(detail__contains=self.q)), category__id=self.c).order_by('-id')
        # カテゴリ検索
        elif self.c:
            return Memo.objects.filter(category__id=self.c).order_by('-id')
        # 文字列検索
        elif self.q:
            return Memo.objects.filter(Q(title__contains=self.q) | Q(detail__contains=self.q)).order_by('-id')
        # 全部表示
        else:
            return Memo.objects.order_by('-id').all()

    def get_context_data(self, **kwargs):
        # 他の変数をテンプレートに渡す

        # 親メソッドを呼び
        context = super().get_context_data(**kwargs)
        # ここから追加
        context["home"] = False
        context["c"] = self.c
        context["q"] = self.q
        # タイトル作成
        if self.c and self.q:
            cate = Category.objects.filter(id=self.c).first()
            context["title"] = f"{cate.name} {self.q}"
        elif self.c:
            cate = Category.objects.filter(id=self.c).first()
            context["title"] = cate.name
        elif self.q:
            context["title"] = self.q
        else:
            context["home"] = True
            context["title"] = "トップページ"

        context['category_items'] = Category.objects.order_by('name')

        return context


class MemoDetailView(DetailView):
    """詳細ページ"""
    model = Memo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_items'] = Category.objects.order_by('name')
        return context


class MemoCreateView(CreateView):
    """新規入力画面"""
    model = Memo
    form_class = MemoModelForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "新規入力"
        context['category_items'] = Category.objects.order_by('name')
        return context


class MemoUpdateView(UpdateView):
    """編集画面"""
    model = Memo
    form_class = MemoModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "編集画面"
        context['category_items'] = Category.objects.order_by('name')
        return context


class MemoDeleteView(DeleteView):
    """削除 getで確認 postで削除"""
    model = Memo
    success_url = reverse_lazy('app1:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_items'] = Category.objects.order_by('name')
        return context
