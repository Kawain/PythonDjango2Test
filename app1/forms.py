from django import forms

from .models import Category, Memo


class MemoModelForm(forms.ModelForm):
    """メモのフォーム（新規追加、編集共通）"""

    def __init__(self, *args, **kwargs):
        # https://narito.ninja/blog/detail/52/

        super().__init__(*args, **kwargs)

        # Categoryのqueryset変更（並べ替えただけ）
        self.fields['category'].queryset = Category.objects.order_by('name')

    class Meta:
        model = Memo

        fields = (
            'category',
            'title',
            'detail',
        )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'detail': forms.Textarea(attrs={'class': 'input'}),
        }
